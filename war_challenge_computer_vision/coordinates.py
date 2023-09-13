from dataclasses import dataclass

from war_challenge_computer_vision.regions.regions import Region

# Coordinates for a (1153, 649) image
original_res = (1920, 1080)

offset = 37


@dataclass
class Coordinate:
    top_left: tuple[int, int]
    bottom_right: tuple[int, int]
    color_pixel: tuple[int, int]


coordinates_dict: dict[Region, Coordinate] = {
    Region.Brazil: Coordinate(
        top_left=(671,588), bottom_right=(643, 625), color_pixel=(627, 595)
    ),
    Region.Argentina_Uruguay: Coordinate(
        top_left=(616,664), bottom_right=(344, 431), color_pixel=(334, 413)
    ),
    Region.Colombia_Venezuela: Coordinate(
        top_left=(599,523), bottom_right=(334, 391), color_pixel=(324, 373)
    ),
    Region.Peru_Bolivia_Chile: Coordinate(
        top_left=(602,609), bottom_right=(332, 329), color_pixel=(322, 311)
    ),
    Region.Mexico: Coordinate(
        top_left=(476,453), bottom_right=(244, 278), color_pixel=(234, 260)
    ),
    Region.California: Coordinate(
        top_left=(481,373), bottom_right=(246, 221), color_pixel=(236, 203)
    ),
    Region.New_York: Coordinate(
        top_left=(568,405), bottom_right=(308, 242), color_pixel=(298, 224)
    ),
    Region.Labrador: Coordinate(
        top_left=(667, 330), bottom_right=(381, 189), color_pixel=(371, 171)
    ),
    Region.Ottawa: Coordinate(
        top_left=(591,340), bottom_right=(327, 196), color_pixel=(317, 178)
    ),
    Region.Vancouver: Coordinate(
        top_left=(501,307), bottom_right=(261, 174), color_pixel=(251, 156)
    ),
    Region.Mackenzie: Coordinate(
        top_left=(577,267), bottom_right=(317, 143), color_pixel=(307, 125)
    ),
    Region.Alaska: Coordinate(
        top_left=(433,226), bottom_right=(213, 114), color_pixel=(203, 96)
    ),
    Region.Greenland: Coordinate(
        top_left=(767,201), bottom_right=(453, 96), color_pixel=(443, 78)
    ),
    Region.Iceland: Coordinate(
        top_left=(813,275), bottom_right=(486, 149), color_pixel=(476, 131)
    ),
    Region.England: Coordinate(
        top_left=(809,341), bottom_right=(484, 197), color_pixel=(474, 179)
    ),
    Region.Sweden: Coordinate(
        top_left=(909,294), bottom_right=(557, 164), color_pixel=(647, 146)
    ),
    Region.Germany: Coordinate(
        top_left=(867,359), bottom_right=(526, 211), color_pixel=(516, 193)
    ),
    Region.Spain_Portugal_France_Italy: Coordinate(
        top_left=(830,406), bottom_right=(499, 245), color_pixel=(489, 227)
    ),
    Region.Poland_Yugoslavia: Coordinate(
        top_left=(909,387), bottom_right=(557, 231), color_pixel=(647, 213)
    ),
    Region.Moscow: Coordinate(
        top_left=(964,350), bottom_right=(596, 203), color_pixel=(586, 185)
    ),
    Region.Algeria_Nigeria: Coordinate(
        top_left=(820,513), bottom_right=(492, 321), color_pixel=(482, 303)
    ),
    Region.Egypt: Coordinate(
        top_left=(920,490), bottom_right=(564, 302), color_pixel=(554, 284)
    ),
    Region.Congo: Coordinate(
        top_left=(905,597), bottom_right=(554, 383), color_pixel=(544, 365)
    ),
    Region.Sudan: Coordinate(
        top_left=(958,541), bottom_right=(591, 343), color_pixel=(581, 325)
    ),
    Region.Madagascar: Coordinate(
        top_left=(1020,624), bottom_right=(636, 402), color_pixel=(626, 384)
    ),
    Region.South_Africa: Coordinate(
        top_left=(914,662), bottom_right=(560, 429), color_pixel=(550, 411)
    ),
    Region.Middle_East: Coordinate(
        top_left=(1009,440), bottom_right=(629, 269), color_pixel=(619, 251)
    ),
    Region.Aral: Coordinate(
        top_left=(1081,377), bottom_right=(680, 223), color_pixel=(670, 205)
    ),
    Region.Omsk: Coordinate(
        top_left=(1052,334), bottom_right=(659, 193), color_pixel=(649, 175)
    ),
    Region.Dudinka: Coordinate(
        top_left=(1118, 310), bottom_right=(707, 175), color_pixel=(697, 157)
    ),
    Region.Siberia: Coordinate(
        top_left=(1172, 269), bottom_right=(746, 146), color_pixel=(736, 128)
    ),
    Region.Tchita: Coordinate(
        top_left=(1232, 334), bottom_right=(790, 192), color_pixel=(780, 174)
    ),
    Region.Mongolia: Coordinate(
        top_left=(1211, 379), bottom_right=(775, 226), color_pixel=(765, 208)
    ),
    Region.Vladivostok: Coordinate(
        top_left=(217,231), bottom_right=(863, 135), color_pixel=(833, 117)
    ),
    Region.China: Coordinate(
        top_left=(1239, 438), bottom_right=(795, 266), color_pixel=(785, 248)
    ),
    Region.India: Coordinate(
        top_left=(1140, 474), bottom_right=(723, 294), color_pixel=(713, 276)
    ),
    Region.Japan: Coordinate(
        top_left=(1402, 446), bottom_right=(912, 274), color_pixel=(902, 256)
    ),
    Region.Vietnam: Coordinate(
        top_left=(1237,503), bottom_right=(793, 314), color_pixel=(783, 296)
    ),
    Region.Borneo: Coordinate(
        top_left=(1299,599), bottom_right=(838, 384), color_pixel=(828, 366)
    ),
    Region.Sumatra: Coordinate(
        top_left=(1227,613), bottom_right=(786, 395), color_pixel=(776, 377)
    ),
    Region.New_Guinea: Coordinate(
        top_left=(1400,606), bottom_right=(912, 390), color_pixel=(902, 372)
    ),
    Region.Australia: Coordinate(
        top_left=(1338,688), bottom_right=(866, 448), color_pixel=(856, 430)
    ),
}


def get_coordinates():
    coordinates = (
        (territory, coordinate) for (territory, coordinate) in coordinates_dict.items()
    )
    return coordinates
