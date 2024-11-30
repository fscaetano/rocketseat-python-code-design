from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverhandlerInterface


class Calculator3():
    def __init__(self, driver_handler: DriverhandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        product = self.__calculate_product(input_data)
        self.__verify_results(variance, product)
        formatted_response = self.__format_response(variance)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Ill-formed body.")

        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return float(variance)  # note: it was returning np.float64

    def __calculate_product(self, numbers: List[float]) -> float:
        product = 1
        for number in numbers:
            product *= number
        return product

    def __verify_results(self, variance: float, product: float) -> None:
        if variance < product:
            raise Exception("Process failed: Variance is less than product.")

    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "Success": True
            }
        }
