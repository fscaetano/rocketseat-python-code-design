from typing import List
import numpy as np
from .interfaces.driver_handler_interface import DriverhandlerInterface


class NumpyHandler(DriverhandlerInterface):
    def __init__(self) -> None:
        self.__np = np

    def standard_deviation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
