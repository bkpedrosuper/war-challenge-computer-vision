from multiprocessing import Pool

from PIL import Image

from war_challenge_computer_vision.coordinates import (
    Coordinate,
    coordinates,
    original_res,
)
from war_challenge_computer_vision.read_map import process_territory
from war_challenge_computer_vision.regions.regions import Region, gen_border_matrix

image = Image.open("images/TelaJogo.png")
image = image.resize(original_res)


def mapper_process_territory(data: tuple[Region, Coordinate]):
    territory = data[0]
    coordinate = data[1]
    return process_territory(image, territory, coordinate)


with Pool() as pool:
    map_state = pool.map(
        mapper_process_territory,
        coordinates,
    )
    border_matrix = pool.apply(gen_border_matrix)

print(map_state)
print(border_matrix)
