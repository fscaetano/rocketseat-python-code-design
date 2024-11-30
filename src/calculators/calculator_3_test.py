from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverhandlerInterface
from pprint import pprint


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 1


class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 1000


def test_calculate_with_variance_error():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as ex_info:
        calculator_3.calculate(mock_request)

    assert str(ex_info.value) == "Process failed: Variance is less than product."


def test_calculate():
    mock_request = MockRequest(body={"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())

    response = calculator_3.calculate(mock_request)

    print()
    print(response)

    assert response == {
        'data': {'Calculator': 3, 'Success': True, 'value': 1000}}
