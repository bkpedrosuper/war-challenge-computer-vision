import pytesseract
import webcolors
from PIL import Image

from war_challenge_computer_vision.coordinates import coordinates
from war_challenge_computer_vision.preprocessing.preprocessing import Preprocessor

image = Image.open("images/TelaDoJogo.png")


def closest_colour(requested_colour: tuple[int, int, int]):
    min_colours: dict[int, str] = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour: tuple[int, int, int]):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


for territory, coordinate in coordinates.items():
    top_left = coordinate.top_left
    bottom_right = coordinate.bottom_right
    c1, c2 = coordinate.color_pixel
    color: tuple[int, int, int, int] = tuple(image.getpixel((c1, c2)))

    team_color, nearest_team_color = get_colour_name(color[:3])
    print(f"{territory} Team Color {team_color} {nearest_team_color}")

    x1, y1 = top_left
    x2, y2 = bottom_right

    slice_image = image.crop((x1, y1, x2, y2))

    preprocessor = Preprocessor(slice_image)

    processed_image = (
        preprocessor.convert_to_gray()
        .resize()
        .otsu_threshold(150)
        .dilate_image(5)
        .erode_image(5)
        .dilate_image(5)
        .erode_image(5)
        .dilate_image(5)
        .erode_image(15)
        .dilate_image(2)
        .invert_image()
        .build()
    )

    troops_in_territory = pytesseract.image_to_string(
        processed_image,
        lang="eng",
        config="--psm 8 --oem 3 outputbase digits -c tessedit_char_whitelist=0123456789",
    )

    print(f"There is {str(troops_in_territory).strip()} in {territory}")

    processed_image.save(f"images/{territory}_slice_threshold.png")
    slice_image.save(f"images/{territory}_slice.png")
