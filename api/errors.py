class NoSuchContainerError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg
        print("No Container")
        exit()


class ServerErrorError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg

class BadParameterError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg
        print("Bad Parameter")
        exit()
