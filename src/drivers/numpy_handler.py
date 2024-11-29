from typing import List
import numpy as np

class NumpyHandler:
    def __init__(self) -> None:
        self.__np = np
        
    def standard_deviation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)