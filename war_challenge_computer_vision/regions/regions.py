from enum import Enum

import numpy as np


class ContinentData:
    idx = 0

    def __init__(self, qtd_troops: int):
        self.qtd_troops = qtd_troops
        self.idx = ContinentData.idx
        ContinentData.idx += 1


class Continent(Enum):
    AFRICA = ContinentData(3)
    ASIA = ContinentData(7)
    EU = ContinentData(5)
    NA = ContinentData(5)
    OCEANIA = ContinentData(2)
    SA = ContinentData(2)

    @property
    def idx(self):
        return self.value.idx

    @property
    def qtd_troops(self):
        return self.value.qtd_troops


class RegionData:
    idx = 0

    def __init__(self, continent: Continent):
        self.continent = continent
        self.idx = RegionData.idx
        self.borders: list[Region] = []
        RegionData.idx += 1

    def set_borders(self, borders: list["Region"]):
        self.borders = borders


class Region(Enum):
    Brazil = RegionData(Continent.SA)
    Argentina_Uruguay = RegionData(Continent.SA)
    Colombia_Venezuela = RegionData(Continent.SA)
    Peru_Bolivia_Chile = RegionData(Continent.SA)

    Mexico = RegionData(Continent.NA)
    California = RegionData(Continent.NA)
    New_York = RegionData(Continent.NA)
    Labrador = RegionData(Continent.NA)
    Ottawa = RegionData(Continent.NA)
    Vancouver = RegionData(Continent.NA)
    Mackenzie = RegionData(Continent.NA)
    Alaska = RegionData(Continent.NA)
    Greenland = RegionData(Continent.NA)

    Iceland = RegionData(Continent.EU)
    England = RegionData(Continent.EU)
    Sweden = RegionData(Continent.EU)
    Germany = RegionData(Continent.EU)
    Spain_Portugal_France_Italy = RegionData(Continent.EU)
    Poland_Yugoslavia = RegionData(Continent.EU)
    Moscow = RegionData(Continent.EU)

    Algeria_Nigeria = RegionData(Continent.AFRICA)
    Egypt = RegionData(Continent.AFRICA)
    Congo = RegionData(Continent.AFRICA)
    Sudan = RegionData(Continent.AFRICA)
    Madagascar = RegionData(Continent.AFRICA)
    South_Africa = RegionData(Continent.AFRICA)

    Middle_East = RegionData(Continent.ASIA)
    Aral = RegionData(Continent.ASIA)
    Omsk = RegionData(Continent.ASIA)
    Dudinka = RegionData(Continent.ASIA)
    Siberia = RegionData(Continent.ASIA)
    Tchita = RegionData(Continent.ASIA)
    Mongolia = RegionData(Continent.ASIA)
    Vladivostok = RegionData(Continent.ASIA)
    China = RegionData(Continent.ASIA)
    India = RegionData(Continent.ASIA)
    Japan = RegionData(Continent.ASIA)
    Vietnam = RegionData(Continent.ASIA)

    Borneo = RegionData(Continent.OCEANIA)
    Sumatra = RegionData(Continent.OCEANIA)
    New_Guinea = RegionData(Continent.OCEANIA)
    Australia = RegionData(Continent.OCEANIA)

    def set_borders(self, borders: list["Region"]):
        self.value.set_borders(borders)
        self.foreigner_borders = len(
            set(
                filter(
                    lambda border: border.continent.idx != self.continent.idx, borders
                )
            )
        )

    @property
    def idx(self):
        return self.value.idx

    @property
    def continent(self):
        return self.value.continent

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


Region.Brazil.set_borders(
    [
        Region.Argentina_Uruguay,
        Region.Peru_Bolivia_Chile,
        Region.Colombia_Venezuela,
        Region.Algeria_Nigeria,
    ]
)
Region.Argentina_Uruguay.set_borders(
    [
        Region.Argentina_Uruguay,
        Region.Peru_Bolivia_Chile,
    ]
)
Region.Peru_Bolivia_Chile.set_borders(
    [
        Region.Brazil,
        Region.Peru_Bolivia_Chile,
        Region.Argentina_Uruguay,
    ]
)
Region.Colombia_Venezuela.set_borders(
    [
        Region.Mexico,
        Region.Brazil,
        Region.Peru_Bolivia_Chile,
    ]
)

Region.Mexico.set_borders(
    [Region.California, Region.New_York, Region.Colombia_Venezuela]
)

Region.California.set_borders(
    [
        Region.New_York,
        Region.Mexico,
        Region.Vancouver,
        Region.Ottawa,
    ]
)

Region.New_York.set_borders(
    [
        Region.California,
        Region.Mexico,
        Region.Ottawa,
        Region.Labrador,
    ]
)

Region.Labrador.set_borders(
    [
        Region.Ottawa,
        Region.New_York,
        Region.Greenland,
    ]
)

Region.Ottawa.set_borders(
    [
        Region.New_York,
        Region.California,
        Region.Labrador,
        Region.Vancouver,
        Region.Mackenzie,
    ]
)
Region.Vancouver.set_borders(
    [
        Region.California,
        Region.Ottawa,
        Region.Mackenzie,
        Region.Alaska,
    ]
)
Region.Mackenzie.set_borders(
    [
        Region.Vancouver,
        Region.Alaska,
        Region.Greenland,
        Region.Ottawa,
    ]
)
Region.Alaska.set_borders(
    [
        Region.Vladivostok,
        Region.Mackenzie,
        Region.Vancouver,
    ]
)
Region.Greenland.set_borders(
    [
        Region.Mackenzie,
        Region.Labrador,
    ]
)
Region.Iceland.set_borders(
    [
        Region.Greenland,
        Region.England,
    ]
)
Region.England.set_borders(
    [
        Region.Spain_Portugal_France_Italy,
        Region.Germany,
        Region.Sweden,
    ]
)
Region.Sweden.set_borders(
    [
        Region.Germany,
        Region.Moscow,
    ]
)
Region.Germany.set_borders(
    [
        Region.England,
        Region.Spain_Portugal_France_Italy,
        Region.Poland_Yugoslavia,
        Region.Sweden,
    ]
)
Region.Spain_Portugal_France_Italy.set_borders(
    [
        Region.England,
        Region.Germany,
        Region.Algeria_Nigeria,
        Region.Egypt,
    ]
)
Region.Poland_Yugoslavia.set_borders(
    [
        Region.Middle_East,
        Region.Germany,
        Region.Moscow,
        Region.Egypt,
    ]
)
Region.Moscow.set_borders(
    [
        Region.Sweden,
        Region.Poland_Yugoslavia,
        Region.Aral,
        Region.Omsk,
    ]
)
Region.Algeria_Nigeria.set_borders(
    [
        Region.Brazil,
        Region.Egypt,
        Region.Spain_Portugal_France_Italy,
        Region.Congo,
        Region.Sudan,
    ]
)
Region.Egypt.set_borders(
    [
        Region.Sudan,
        Region.Algeria_Nigeria,
        Region.Spain_Portugal_France_Italy,
        Region.Poland_Yugoslavia,
        Region.Middle_East,
    ]
)
Region.Congo.set_borders(
    [
        Region.Madagascar,
        Region.Congo,
        Region.Algeria_Nigeria,
        Region.Egypt,
    ]
)
Region.Sudan.set_borders(
    [
        Region.Egypt,
        Region.Algeria_Nigeria,
        Region.Congo,
        Region.South_Africa,
        Region.Madagascar,
    ]
)
Region.Madagascar.set_borders(
    [
        Region.Sudan,
        Region.South_Africa,
    ]
)
Region.South_Africa.set_borders(
    [
        Region.Madagascar,
        Region.Congo,
        Region.Sudan,
    ]
)
Region.Middle_East.set_borders(
    [
        Region.Egypt,
        Region.India,
        Region.Aral,
    ]
)
Region.Aral.set_borders(
    [
        Region.Omsk,
        Region.Middle_East,
        Region.India,
        Region.China,
        Region.Moscow,
    ]
)
Region.Omsk.set_borders(
    [
        Region.Aral,
        Region.Dudinka,
        Region.Mongolia,
        Region.Moscow,
        Region.China,
    ]
)
Region.Dudinka.set_borders(
    [
        Region.Omsk,
        Region.Siberia,
        Region.Tchita,
        Region.Mongolia,
    ]
)
Region.Siberia.set_borders(
    [
        Region.Dudinka,
        Region.Vladivostok,
        Region.Tchita,
    ]
)
Region.Tchita.set_borders(
    [
        Region.Siberia,
        Region.Dudinka,
        Region.Mongolia,
        Region.China,
        Region.Vladivostok,
    ]
)
Region.Mongolia.set_borders(
    [
        Region.Dudinka,
        Region.Omsk,
        Region.China,
        Region.Tchita,
    ]
)
Region.Vladivostok.set_borders(
    [
        Region.Siberia,
        Region.Tchita,
        Region.Alaska,
        Region.China,
    ]
)
Region.China.set_borders(
    [
        Region.Mongolia,
        Region.Tchita,
        Region.Vladivostok,
        Region.Vietnam,
        Region.India,
        Region.Aral,
        Region.Omsk,
    ]
)
Region.India.set_borders(
    [
        Region.Middle_East,
        Region.Aral,
        Region.Vietnam,
        Region.Sumatra,
        Region.China,
    ]
)
Region.Japan.set_borders(
    [
        Region.Vladivostok,
        Region.China,
    ]
)
Region.Vietnam.set_borders(
    [
        Region.China,
        Region.India,
        Region.Borneo,
    ]
)
Region.Borneo.set_borders(
    [
        Region.New_Guinea,
        Region.Australia,
        Region.Vietnam,
    ]
)
Region.Sumatra.set_borders(
    [
        Region.Australia,
        Region.India,
    ]
)
Region.New_Guinea.set_borders(
    [
        Region.Borneo,
        Region.Australia,
    ]
)
Region.Australia.set_borders(
    [
        Region.Borneo,
        Region.Sumatra,
        Region.New_Guinea,
    ]
)


def gen_border_matrix():
    border_matriz = np.array(
        [
            [
                True if country1 in country2.value.borders else False
                for country2 in Region
                if country2 != country1
            ]
            for country1 in Region
        ]
    )
    return border_matriz


# print(np.testing.assert_array_almost_equal(border_matriz, border_matriz_dumb))
