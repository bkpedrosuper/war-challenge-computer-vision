import pytesseract
from PIL.Image import Image as ImagePIL
from war_challenge_computer_vision.colors.territory_color import get_colour_name

from war_challenge_computer_vision.coordinates import Coordinate
from war_challenge_computer_vision.preprocessing.preprocessing import Preprocessor
from war_challenge_computer_vision.regions.regions import Region
from war_challenge_computer_vision.utils.timer import timer_func
from war_challenge_computer_vision.utils.enviroment import is_dev


@timer_func
def process_territory(image: ImagePIL, territory: Region, coordinate: Coordinate):
    top_left = coordinate.top_left
    bottom_right = (top_left[0] + 32, top_left[1] + 32)
    c1, c2 = (top_left[0] + 16, top_left[1] + 2)

    color: tuple[int, int, int, int] = tuple(image.getpixel((c1, c2)))

    team_color, nearest_team_color = get_colour_name(color[:3])
    # print(f"{territory} Team Color {team_color} {nearest_team_color}")

    x1, y1 = top_left
    x2, y2 = bottom_right

    slice_image = image.crop((x1, y1, x2, y2))

    preprocessor = Preprocessor(slice_image)

    processed_image = (
        preprocessor.convert_to_gray()
        .resize()
        .threshold(150)
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
