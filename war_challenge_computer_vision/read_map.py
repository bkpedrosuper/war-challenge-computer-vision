from enum import Enum

import pytesseract
from PIL.Image import Image as ImagePIL
from unidecode import unidecode

from war_challenge_computer_vision.colors.territory_color import get_colour_name
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


possible_colors = (
    "lightseagreen",
    "olivedrab",
    "firebrick",
    "darkslateblue",
    "goldenrod",
    "darkslategray",
)


@timer_func
def process_territory(image: ImagePIL, territory: Region, coordinate: Coordinate):
    top_left = coordinate.top_left
    bottom_right = (top_left[0] + offset, top_left[1] + offset)
    c1, c2 = (top_left[0] + (offset / 2), top_left[1] + 0)
    counter = 0
    max_tries = 30
    while True:
        color = tuple(image.getpixel((c1, c2)))  # type: ignore
        _, nearest_team_color = get_colour_name(tuple(color[:3]))  # type: ignore
        if nearest_team_color in possible_colors or counter > max_tries:
            break
        c2 += 1
        counter += 1

    x1, y1 = top_left
    x2, y2 = bottom_right

    slice_image = image.crop((x1, y1, x2, y2))
    # preprocessor_color = Preprocessor(slice_image.crop((0, 14, 32, 24)))
    # processed_image_color = preprocessor_color.resize((500, 500)).filter_mean().build()
    # color: tuple[int, int, int, int] = tuple(
    #     Counter(list(processed_image_color.getdata())).most_common(1)[0][0]
    # )  # type: ignore
    # print(territory, color)

    preprocessor = Preprocessor(slice_image)
    if nearest_team_color not in "goldenrod":
        processed_image = (
            preprocessor.convert_to_gray()
            .resize((1000, 1000))
            .threshold(140)
            .center_number()
            # .crop()
            # .resize((1000,1000))
            # .filter_mean(10)
            # .threshold(170)
            .dilate_image(10)
            .erode_image(20)
            # .add_border()
            .invert_image()
            .build()
        )
    else:
        processed_image = (
            preprocessor.convert_to_gray()
            .resize((1500, 1500))
            .threshold(185)
            .dilate_image(10)
            .erode_image(20)
            .invert_image()
            .build()
        )

    # processed_image = ImageOps.expand(processed_image, border=10, fill="black")

    counter = 0
    max_counter = 10
    troops_in_territory = 1
    while counter < max_counter:
        troops_in_territory = str(
            pytesseract.image_to_string(
                processed_image,
                lang="eng",
                config="--psm 8 --oem 3 outputbase digits -c tessedit_char_whitelist=0123456789",
            )
        )
        counter += 1
        try:
            troops_in_territory = int(troops_in_territory)
            break
        except ValueError:
            troops_in_territory = 1
        processed_image = Preprocessor(processed_image).erode_image(5).build()

    # print(f"There is {str(troops_in_territory).strip()} in {territory}")
    if is_dev:
        processed_image.save(f"images/map_slices/{territory}_slice_threshold.png")
        slice_image.save(f"images/map_slices/{territory}_slice.png")
        # processed_image_color.save(f"images/map_slices/{territory}_color_slice.png")
    return (territory, int(troops_in_territory), nearest_team_color)
