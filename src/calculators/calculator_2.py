from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.numpy_handler import NumpyHandler


class Calculator2():
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        print(body)
        input_data = self.__validate_body(body)
        print(input_data)
        result = self.__process_data(input_data)
        print(result)
        return self.__format_response(result)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Ill-formed body.")

        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        numpy_handler = NumpyHandler()
        
        first_process_result = [ (num * 11) ** 0.95 for num in input_data]
        result = numpy_handler.standard_deviation(first_process_result)
        return 1/result

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calc_result, 2)
            }
        }

        