class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422


try:
    print("try block")
    raise HttpUnprocessableEntityError("raise exception")
except Exception as exception:
    print("except block")
    print(exception.name)
    print(exception.message)
    print(exception.status_code)
    
