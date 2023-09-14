from enum import Enum

import numpy as np
import webcolors
from PIL import Image


class PossibleColors(Enum):
    AZUL = "lightseagreen"
    VERDE = "olivedrab"
    VERMELHO = "firebrick"
    ROXO = "darkslateblue"
    AMERELO = "goldenrod"
    CINZA = "darkslategray"

    @staticmethod
    def get_all_possible_colors():
        return (
            "lightseagreen",
            "olivedrab",
            "firebrick",
            "darkslateblue",
            "goldenrod",
            # "darkslategray",
        )


def closest_colour(requested_colour: tuple[int, int, int]):
    min_colours: dict[int, str] = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


for name in PossibleColors.get_all_possible_colors():
    rgb = webcolors.name_to_rgb(name)
    print(name, rgb)


def closest_colour_own(requested_colour: tuple[int, int, int]):
    min_colours: dict[int, str] = {}
    for name in PossibleColors.get_all_possible_colors():
        r_c, g_c, b_c = webcolors.name_to_rgb(name)
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
    compact = {"indigo": "darkslateblue", "marron": "firebrick"}
    if closest_name in compact.keys():
        closest_name = compact[closest_name]
    return actual_name, closest_name


def get_color(t, image_slice: Image.Image):
    # filter out black and white
    # black (20,20,20)
    # white (250,250,250)
    def filter_pixel(pixel):
        min_black = 100
        max_white = 190
        return not (
            all(map(lambda x: x <= min_black, pixel[:3]))
            or all(map(lambda x: x >= max_white, pixel[:3]))
        )

    pixels = np.array(list(filter(filter_pixel, list(image_slice.getdata()))))
    avg_color: np.ndarray = np.mean(pixels, axis=0)
    return closest_colour_own(tuple(avg_color[:3]))  # type: ignore
