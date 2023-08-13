from dataclasses import dataclass
from enum import Enum


@dataclass
class ContinentData:
    idx = 0

    def __init__(self, qtd_troops: int):
        ContinentData.idx += 1
        self.qtd_troops = qtd_troops
        self.idx = ContinentData.idx


class Continents(Enum):
    AFRICA = ContinentData(3)
    ASIA = ContinentData(7)
    EU = ContinentData(5)
    NA = ContinentData(5)
    OCEANIA = ContinentData(2)
    SA = ContinentData(2)

@dataclass()
class RegionData:
    idx = 0

    def __init__(self, continent: Continents):
        RegionData.idx += 1
        self.continent = continent
        self.idx = RegionData.idx


class Regions(Enum):
    Brazil = RegionData(Continents.SA)
    Argentina_Uruguay = RegionData(Continents.SA)
    Colombia_Venezuela = RegionData(Continents.SA)
    Peru_Bolivia_Chile = RegionData(Continents.SA)

    Mexico = RegionData(Continents.NA)
    California = RegionData(Continents.NA)
    New_York = RegionData(Continents.NA)
    Labrador = RegionData(Continents.NA)
    Ottawa = RegionData(Continents.NA)
    Vancouver = RegionData(Continents.NA)
    Mackenzie = RegionData(Continents.NA)
    Alaska = RegionData(Continents.NA)
    Greenland = RegionData(Continents.NA)

    Iceland = RegionData(Continents.EU)
    England = RegionData(Continents.EU)
    Sweden = RegionData(Continents.EU)
    Germany = RegionData(Continents.EU)
    Spain_Portugal_France_Italy = RegionData(Continents.EU)
    Poland_Yugoslavia = RegionData(Continents.EU)
    Moscow = RegionData(Continents.EU)

    Algeria_Nigeria = RegionData(Continents.AFRICA)
    Egypt = RegionData(Continents.AFRICA)
    Congo = RegionData(Continents.AFRICA)
    Sudan = RegionData(Continents.AFRICA)
    Madagascar = RegionData(Continents.AFRICA)
    South_Africa = RegionData(Continents.AFRICA)

    Middle_East = RegionData(Continents.ASIA)
    Aral = RegionData(Continents.ASIA)
    Omsk = RegionData(Continents.ASIA)
    Dudinka = RegionData(Continents.ASIA)
    Siberia = RegionData(Continents.ASIA)
    Tchita = RegionData(Continents.ASIA)
    Mongolia = RegionData(Continents.ASIA)
    Vladivostok = RegionData(Continents.ASIA)
    China = RegionData(Continents.ASIA)
    India = RegionData(Continents.ASIA)
    Japan = RegionData(Continents.ASIA)
    Vietnam = RegionData(Continents.ASIA)

    Borneo = RegionData(Continents.OCEANIA)
    Sumatra = RegionData(Continents.OCEANIA)
    New_Guinea = RegionData(Continents.OCEANIA)
    Australia = RegionData(Continents.OCEANIA)
