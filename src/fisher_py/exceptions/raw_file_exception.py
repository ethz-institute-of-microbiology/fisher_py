class RawFileException(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class NoSelectedDeviceException(Exception):
    pass


class NoSelectedMsDeviceException(Exception):

    def __init__(self, message: str):
        super().__init__(message)
