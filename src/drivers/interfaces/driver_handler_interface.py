from typing import List
from abc import ABC, abstractmethod


class DriverhandlerInterface(ABC):

    @classmethod
    @abstractmethod
    def standard_deviation(self, numbers: List[float]) -> float:
        pass

    @classmethod
    @abstractmethod
    def variance(self, numbers: List[float]) -> float:
        pass
