from dataclasses import dataclass

from war_challenge_computer_vision.regions.regions import Region

# Coordinates for a (1153, 649) image
original_res = (1920, 1080)

offset = 28


@dataclass
class Coordinate:
    top_left: tuple[int, int]
    bottom_right: tuple[int, int]
    color_pixel: tuple[int, int]


coordinates_dict: dict[Region, Coordinate] = {
    Region.Brazil: Coordinate(
        top_left=(668, 593), bottom_right=(643, 625), color_pixel=(627, 595)
    ),
    Region.Argentina_Uruguay: Coordinate(
        top_left=(613, 672), bottom_right=(344, 431), color_pixel=(334, 413)
    ),
    Region.Colombia_Venezuela: Coordinate(
        top_left=(597, 527), bottom_right=(334, 391), color_pixel=(324, 373)
    ),
    Region.Peru_Bolivia_Chile: Coordinate(
        top_left=(599, 615), bottom_right=(332, 329), color_pixel=(322, 311)
    ),
    Region.Mexico: Coordinate(
        top_left=(473, 456), bottom_right=(244, 278), color_pixel=(234, 260)
    ),
    Region.California: Coordinate(
        top_left=(477, 375), bottom_right=(246, 221), color_pixel=(236, 203)
    ),
    Region.New_York: Coordinate(
        top_left=(562, 404), bottom_right=(308, 242), color_pixel=(298, 224)
    ),
    Region.Labrador: Coordinate(
        top_left=(664, 330), bottom_right=(381, 189), color_pixel=(371, 171)
    ),
    Region.Ottawa: Coordinate(
        top_left=(588, 340), bottom_right=(327, 196), color_pixel=(317, 178)
    ),
    Region.Vancouver: Coordinate(
        top_left=(498, 308), bottom_right=(261, 174), color_pixel=(251, 156)
    ),
    Region.Mackenzie: Coordinate(
        top_left=(575, 264), bottom_right=(317, 143), color_pixel=(307, 125)
    ),
    Region.Alaska: Coordinate(
        top_left=(430, 224), bottom_right=(213, 114), color_pixel=(203, 96)
    ),
    Region.Greenland: Coordinate(
        top_left=(765, 198), bottom_right=(453, 96), color_pixel=(443, 78)
    ),
    Region.Iceland: Coordinate(
        top_left=(810, 273), bottom_right=(486, 149), color_pixel=(476, 131)
    ),
    Region.England: Coordinate(
        top_left=(807, 341), bottom_right=(484, 197), color_pixel=(474, 179)
    ),
    Region.Sweden: Coordinate(
        top_left=(908, 295), bottom_right=(557, 164), color_pixel=(647, 146)
    ),
    Region.Germany: Coordinate(
        top_left=(866, 362), bottom_right=(526, 211), color_pixel=(516, 193)
    ),
    Region.Spain_Portugal_France_Italy: Coordinate(
        top_left=(828, 409), bottom_right=(499, 245), color_pixel=(489, 227)
    ),
    Region.Poland_Yugoslavia: Coordinate(
        top_left=(909, 389), bottom_right=(557, 231), color_pixel=(647, 213)
    ),
    Region.Moscow: Coordinate(
        top_left=(962, 350), bottom_right=(596, 203), color_pixel=(586, 185)
    ),
    Region.Algeria_Nigeria: Coordinate(
        top_left=(818, 516), bottom_right=(492, 321), color_pixel=(482, 303)
    ),
    Region.Egypt: Coordinate(
        top_left=(918, 489), bottom_right=(564, 302), color_pixel=(554, 284)
    ),
    Region.Congo: Coordinate(
        top_left=(904, 604), bottom_right=(554, 383), color_pixel=(544, 365)
    ),
    Region.Sudan: Coordinate(
        top_left=(957, 548), bottom_right=(591, 343), color_pixel=(581, 325)
    ),
    Region.Madagascar: Coordinate(
        top_left=(1019, 632), bottom_right=(636, 402), color_pixel=(626, 384)
    ),
    Region.South_Africa: Coordinate(
        top_left=(912, 670), bottom_right=(560, 429), color_pixel=(550, 411)
    ),
    Region.Middle_East: Coordinate(
        top_left=(1009, 444), bottom_right=(629, 269), color_pixel=(619, 251)
    ),
    Region.Aral: Coordinate(
        top_left=(1080, 378), bottom_right=(680, 223), color_pixel=(670, 205)
    ),
    Region.Omsk: Coordinate(
        top_left=(1051, 335), bottom_right=(659, 193), color_pixel=(649, 175)
    ),
    Region.Dudinka: Coordinate(
        top_left=(1118, 310), bottom_right=(707, 175), color_pixel=(697, 157)
    ),
    Region.Siberia: Coordinate(
        top_left=(1172, 269), bottom_right=(746, 146), color_pixel=(736, 128)
    ),
    Region.Tchita: Coordinate(
        top_left=(1233, 335), bottom_right=(790, 192), color_pixel=(780, 174)
    ),
    Region.Mongolia: Coordinate(
        top_left=(1212, 382), bottom_right=(775, 226), color_pixel=(765, 208)
    ),
    Region.Vladivostok: Coordinate(
        top_left=(1335, 254), bottom_right=(863, 135), color_pixel=(833, 117)
    ),
    Region.China: Coordinate(
        top_left=(1239, 439), bottom_right=(795, 266), color_pixel=(785, 248)
    ),
    Region.India: Coordinate(
        top_left=(1140, 478), bottom_right=(723, 294), color_pixel=(713, 276)
    ),
    Region.Japan: Coordinate(
        top_left=(1402, 449), bottom_right=(912, 274), color_pixel=(902, 256)
    ),
    Region.Vietnam: Coordinate(
        top_left=(1238, 507), bottom_right=(793, 314), color_pixel=(783, 296)
    ),
    Region.Borneo: Coordinate(
        top_left=(1301, 606), bottom_right=(838, 384), color_pixel=(828, 366)
    ),
    Region.Sumatra: Coordinate(
        top_left=(1228, 621), bottom_right=(786, 395), color_pixel=(776, 377)
    ),
    Region.New_Guinea: Coordinate(
        top_left=(1403, 614), bottom_right=(912, 390), color_pixel=(902, 372)
    ),
    Region.Australia: Coordinate(
        top_left=(1339, 696), bottom_right=(866, 448), color_pixel=(856, 430)
    ),
}


def get_coordinates():
    coordinates = (
        (territory, coordinate) for (territory, coordinate) in coordinates_dict.items()
    )
    return coordinates
