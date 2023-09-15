from dataclasses import dataclass
from enum import Enum
from typing import ClassVar

import easyocr
import numpy as np
import pytesseract
from PIL.Image import Image as ImagePIL
from unidecode import unidecode

from war_challenge_computer_vision.colors.territory_color import (
    PossibleColors,
    get_color,
)
from war_challenge_computer_vision.coordinates import Coordinate, offset
from war_challenge_computer_vision.preprocessing.preprocessing import Preprocessor
from war_challenge_computer_vision.regions.regions import Region
from war_challenge_computer_vision.utils.enviroment import is_dev
from war_challenge_computer_vision.utils.timer import timer_func


class GameStepData:
    def __init__(self, desc_word: str, troops_to_alloc: int | None = None) -> None:
        self.desc_word = desc_word
        self.troops_to_alloc = troops_to_alloc


class GameStep(Enum):
    ALOCACAO = GameStepData("Fortificar")
    ATAQUE = GameStepData("Atacar")
    MOVIMENTACAO = GameStepData("Deslocar")

    @property
    def desc_word(self):
        return self.value.desc_word

    @property
    def troops_to_alloc(self):
        return self.value.troops_to_alloc

    def set_troops_to_alloc(self, troops_to_alloc: int):
        if self != GameStep.ALOCACAO:
            return
        self.value.troops_to_alloc = troops_to_alloc

    @property
    def desc_word_norm(self):
        return unidecode(self.desc_word).lower()

    @staticmethod
    def get_game_step(possible_game_step: str) -> "GameStep":
        possible_game_step = unidecode(possible_game_step).lower()
        for game_step in GameStep:
            if game_step.desc_word_norm in possible_game_step:
                return game_step
        return GameStep.MOVIMENTACAO

    def __str__(self) -> str:
        return self.name.lower()

    def __repr__(self) -> str:
        return str(self)


@timer_func
def get_troops_to_alloc(image: ImagePIL) -> int:
    # 1229, 946
    # 1249, 972
    x1, y1 = 1230, 945
    x2, y2 = (x1 + 20, y1 + 28)
    slice_image = image.crop((x1, y1, x2, y2))
    preprocessor = Preprocessor(slice_image)
    processed_image = (
        preprocessor.convert_to_gray()
        .resize()
        .threshold(140)
        .dilate_image(5)
        .erode_image(10)
        .invert_image()
        .build()
    )
    possible_alloc_troops = pytesseract.image_to_string(
        processed_image,
        lang="por",
        config="--psm 8 --oem 3 outputbase digits -c tessedit_char_whitelist=0123456789",
    )
    if is_dev:
        slice_image.save("images/map_slices/game_alloc_troops_slice.png")
        processed_image.save("images/map_slices/game_alloc_troops_threshold.png")
    try:
        return int(possible_alloc_troops)
    except ValueError:
        return 0


@timer_func
def get_game_step(image: ImagePIL) -> GameStep:
    # 762, 990
    # 1158, 1046
    x1, y1 = 770, 995
    x2, y2 = (x1 + 380, y1 + 45)
    slice_image = image.crop((x1, y1, x2, y2))
    preprocessor = Preprocessor(slice_image)
    processed_image = (
        preprocessor.convert_to_gray()
        .resize((800, 200))
        .threshold(140)
        # .dilate_image(5)
        # .erode_image(10)
        .invert_image()
        .build()
    )
    possible_game_step = pytesseract.image_to_string(
        processed_image,
        lang="por",
        config="--psm 7 --oem 3",
    )
    # print(unidecode(game_step))
    if is_dev:
        processed_image.save("images/map_slices/game_step_slice.png")
    game_step = GameStep.get_game_step(possible_game_step)
    if game_step == GameStep.ALOCACAO:
        troops_to_alloc = get_troops_to_alloc(image)
        game_step.set_troops_to_alloc(troops_to_alloc)
    return game_step


@dataclass
class PreprocessingConfig:
    image_resize = (1500, 1500)
    image_resize_yellow = (2000, 2000)
    threshold = 140
    threshold_yellow = 210
    median_filter_footprint_size = 5
    blur_filter_footprint_size = 5
    dilate_times = 10
    erode_times = 15
    max_counter = 10
    erode_times_each_try = 5
    default_troops_count = 1


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances: ClassVar = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class EasyOCRSingleton(metaclass=SingletonMeta):
    _reader: easyocr.Reader | None = None

    @property
    def reader(self):
        if self._reader is None:
            self._reader = easyocr.Reader(["en", "pt"], gpu=True)
        return self._reader


@timer_func
def process_territory(
    image: ImagePIL,
    territory: Region,
    coordinate: Coordinate,
    config: PreprocessingConfig,
):
    top_left = coordinate.top_left
    bottom_right = (top_left[0] + offset, top_left[1] + offset)
    # c1, c2 = (top_left[0] + (offset / 2), top_left[1] + 0)
    # counter = 0
    # max_tries = 30
    # while True:
    #     color = tuple(image.getpixel((c1, c2)))  # type: ignore
    #     _, nearest_team_color = get_colour_name(tuple(color[:3]))  # type: ignore
    #     if nearest_team_color in PossibleColors.get_all_possible_colors() or counter > max_tries:
    #         break
    #     c2 += 1
    #     counter += 1

    x1, y1 = top_left
    x2, y2 = bottom_right

    image_slice = image.crop((x1, y1, x2, y2))
    nearest_team_color = get_color(territory, image_slice)
    # print(territory, color_aprox, nearest_team_color)
    # preprocessor_color = Preprocessor(slice_image.crop((0, 14, 32, 24)))
    # processed_image_color = preprocessor_color.resize((500, 500)).filter_mean().build()
    # color: tuple[int, int, int, int] = tuple(
    #     Counter(list(processed_image_color.getdata())).most_common(1)[0][0]
    # )  # type: ignore
    # print(territory, color)

    preprocessor = Preprocessor(image_slice)
    if nearest_team_color not in PossibleColors.AMERELO.value:
        processed_image = (
            preprocessor.convert_to_gray()
            .resize(config.image_resize)
            .filter_median(config.median_filter_footprint_size)
            .blur_image(config.blur_filter_footprint_size)
            .threshold(config.threshold)
            # .center_number()
            # .crop()
            # .resize((1000,1000))
            # .filter_mean(10)
            # .threshold(170)
            .dilate_image(config.dilate_times)
            .erode_image(config.erode_times)
            # .add_border()
            .invert_image()
            .build()
        )
    else:
        processed_image = (
            preprocessor.convert_to_gray()
            .resize(config.image_resize_yellow)
            .filter_median(config.median_filter_footprint_size)
            .blur_image(config.blur_filter_footprint_size)
            .threshold(config.threshold_yellow)
            # .center_number()
            .dilate_image(config.dilate_times)
            .erode_image(config.erode_times)
            # .add_border()
            .invert_image()
            .build()
        )

    # processed_image = ImageOps.expand(processed_image, border=10, fill="black")

    counter = 0
    max_counter = config.max_counter
    troops_in_territory = config.default_troops_count
    if is_dev:
        processed_image.save(f"images/map_slices/{territory}_slice_threshold.png")
        image_slice.save(f"images/map_slices/{territory}_slice.png")
    original_processed_image = processed_image.copy()
    while counter < max_counter:
        troops_in_territory = str(
            pytesseract.image_to_string(
                processed_image,
                lang="eng",
                config="--psm 9 --oem 1 -c tessedit_char_whitelist=0123456789iI",
            )
        )
        counter += 1
        try:
            troops_in_territory = troops_in_territory.replace("i", "1").replace(
                "I", "1"
            )
            troops_in_territory = int(troops_in_territory)
            break
        except ValueError:
            troops_in_territory = config.default_troops_count

        processed_image = (
            Preprocessor(processed_image)
            .dilate_image(config.erode_times_each_try)
            .build()
        )

    if counter >= max_counter - 1:
        easy_ocr_singleton = EasyOCRSingleton()
        reader = easy_ocr_singleton.reader
        result = reader.readtext(
            image=np.array(original_processed_image.resize((500, 500))),
            decoder="beamsearch",
            detail=0,
            workers=0,
        )
        troops_in_territory = "".join(result)
        try:
            troops_in_territory = troops_in_territory.replace("i", "1").replace(
                "I", "1"
            )
            troops_in_territory = int(troops_in_territory)
        except ValueError:
            troops_in_territory = 1
        print(f"{territory} {nearest_team_color} {troops_in_territory}")
    return (territory, int(troops_in_territory), nearest_team_color)
