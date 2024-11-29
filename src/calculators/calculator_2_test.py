from typing import Dict
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})
    driver = NumpyHandler()
    calulator2 = Calculator2(driver)
    response = calulator2.calculate(mock_request)
    print("\n", response)

    assert isinstance(response, dict)
    assert response == {'data': {'Calculator': 2, 'result': 0.08}}
