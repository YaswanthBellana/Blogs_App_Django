class CustomError(Exception):
    def __init__(self, message, status_code=500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class PageNotFoundError(CustomError):
    def __init__(self, message="Page not found"):
        super().__init__(message, status_code=404)


class ServerError(CustomError):
    def __init__(self, message="Internal server error"):
        super().__init__(message, status_code=500)
