from dataclasses import dataclass
from enum import Enum


@dataclass
class ContinentData:
    idx = 0

    def __init__(self, qtd_troops: int):
        ContinentData.idx += 1
        self.qtd_troops = qtd_troops
        self.idx = ContinentData.idx


class Continent(Enum):
    AFRICA = ContinentData(3)
    ASIA = ContinentData(7)
    EU = ContinentData(5)
    NA = ContinentData(5)
    OCEANIA = ContinentData(2)
    SA = ContinentData(2)

@dataclass()
class RegionData:
    idx = 0

    def __init__(self, continent: Continent):
        RegionData.idx += 1
        self.continent = continent
        self.idx = RegionData.idx


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
