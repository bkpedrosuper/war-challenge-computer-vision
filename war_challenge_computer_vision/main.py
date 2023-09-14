import glob
import os
from functools import partial
from multiprocessing import Pool
from os import cpu_count
from pathlib import Path

from PIL import Image

from war_challenge_computer_vision.coordinates import (
    Coordinate,
    get_coordinates,
    original_res,
)
from war_challenge_computer_vision.read_map import get_game_step, process_territory
from war_challenge_computer_vision.regions.regions import Region, gen_border_matrix


def mapper_process_territory(image: Image.Image, data: tuple[Region, Coordinate]):
    territory = data[0]
    coordinate = data[1]
    return process_territory(image, territory, coordinate)


def mapper_game_step(image: Image.Image):
    game_step = get_game_step(image)
    return game_step, game_step.troops_to_alloc


def get_data_from_path(image_filepath: Path):
    # print(path)
    image = Image.open(image_filepath)
    image = image.resize(original_res)
    return get_data_from_image(image)


def get_data_from_image(image: Image.Image):
    cpu_counts = cpu_count()
    cpu_counts = cpu_counts if cpu_counts else 0
    coordinates = get_coordinates()
    with Pool(max(cpu_counts - 1, 1)) as pool:
        map_state = pool.map(
            partial(mapper_process_territory, image),
            coordinates,
        )
        border_matrix = pool.apply(gen_border_matrix)
        game_step, troops_to_alloc = pool.apply(mapper_game_step, (image,))
        game_step.set_troops_to_alloc(troops_to_alloc if troops_to_alloc else 0)
    return map_state, border_matrix, game_step


def get_data():
    pattern = (
        str(Path(f"{os.path.expanduser('~')}/Pictures/Screenshots/").resolve()) + "/*"
    )
    list_of_files = glob.glob(pattern)
    latest_file = max(list_of_files, key=os.path.getctime)
    path = Path(latest_file)
    return get_data_from_path(path)


if __name__ == "__main__":
    print(*get_data(), sep="\n")
