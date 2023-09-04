from enum import Enum

import pytesseract
from PIL.Image import Image as ImagePIL
from unidecode import unidecode

from war_challenge_computer_vision.colors.territory_color import get_colour_name
from war_challenge_computer_vision.coordinates import Coordinate
from war_challenge_computer_vision.preprocessing.preprocessing import Preprocessor
from war_challenge_computer_vision.regions.regions import Region
from war_challenge_computer_vision.utils.enviroment import is_dev
from war_challenge_computer_vision.utils.timer import timer_func


class GameStep(Enum):
    ALOCACAO = "Fortificar"
    ATAQUE = "Atacar"
    MOVIMENTACAO = "Deslocar"

    @property
    def desc_word(self):
        return self.value
    
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
    return GameStep.get_game_step(possible_game_step)


@timer_func
def process_territory(image: ImagePIL, territory: Region, coordinate: Coordinate):
    top_left = coordinate.top_left
    bottom_right = (top_left[0] + 32, top_left[1] + 32)
    c1, c2 = (top_left[0] + 16, top_left[1] + 2)

    color: tuple[int, int, int, int] = tuple(image.getpixel((c1, c2)))  # type: ignore

    _, nearest_team_color = get_colour_name(color[:3])
    # print(f"{territory} Team Color {team_color} {nearest_team_color}")

    x1, y1 = top_left
    x2, y2 = bottom_right

    slice_image = image.crop((x1, y1, x2, y2))

    preprocessor = Preprocessor(slice_image)

    processed_image = (
        preprocessor.convert_to_gray()
        .resize()
        .threshold(185)
        .dilate_image(5)
        .erode_image(10)
        .invert_image()
        .build()
    )

    troops_in_territory = pytesseract.image_to_string(
        processed_image,
        lang="eng",
        config="--psm 8 --oem 3 outputbase digits -c tessedit_char_whitelist=0123456789",
    )

    # print(f"There is {str(troops_in_territory).strip()} in {territory}")
    if is_dev:
        processed_image.save(f"images/map_slices/{territory}_slice_threshold.png")
        slice_image.save(f"images/map_slices/{territory}_slice.png")

    return (territory, int(troops_in_territory), nearest_team_color)
