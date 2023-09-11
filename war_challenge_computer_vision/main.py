from multiprocessing import Pool
from os import cpu_count
from pathlib import Path

from PIL import Image

from war_challenge_computer_vision.coordinates import (
    Coordinate,
    coordinates,
    original_res,
)
from war_challenge_computer_vision.read_map import get_game_step, process_territory
from war_challenge_computer_vision.regions.regions import Region, gen_border_matrix

image = Image.open(Path(__file__).parent.parent / "images/TelaJogo4.png")
image = image.resize(original_res)


def mapper_process_territory(data: tuple[Region, Coordinate]):
    territory = data[0]
    coordinate = data[1]
    return process_territory(image, territory, coordinate)


def mapper_game_step():
    game_step = get_game_step(image)
    return game_step, game_step.troops_to_alloc


def get_data():
    cpu_counts = cpu_count()
    cpu_counts = cpu_counts if cpu_counts else 0
    with Pool(max(cpu_counts - 2, 1)) as pool:
        map_state = pool.map(
            mapper_process_territory,
            coordinates,
        )
        border_matrix = pool.apply(gen_border_matrix)
        game_step, troops_to_alloc = pool.apply(mapper_game_step)
        game_step.set_troops_to_alloc(troops_to_alloc if troops_to_alloc else 0)
    return map_state, border_matrix, game_step


if __name__ == "__main__":
    print(*get_data(), sep="\n")
