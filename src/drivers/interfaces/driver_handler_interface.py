from typing import List
from abc import ABC, abstractmethod


class DriverhandlerInterface(ABC):

    @abstractmethod
    def standard_deviation(self, numbers: List[float]) -> float:
        pass
