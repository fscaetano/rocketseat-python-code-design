from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={ "number": 1 })
    calulator1 = Calculator1()
    response = calulator1.calculate(mock_request)
    print("\nteste 0:", response)
    
    # response format
    assert "data" in response    
    assert "Calculator" in response["data"]
    assert "result" in response["data"]
    
    # respose correction
    assert response["data"]["Calculator"] == 1
    assert response["data"]["result"] == 14.25


def test_calculate_with_body_error():
    mock_request = MockRequest(body={ "n": 1 })
    calulator1 = Calculator1()
    
    with raises(Exception) as ex_info:
        response = calulator1.calculate(mock_request)
        
    assert str(ex_info.value) == "Ill-formed body."
    