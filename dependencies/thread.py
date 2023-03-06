from threading import Thread as PyThread


class Thread:
    """
    Custom Thread class in order to make it possible to
    return the result of the executed finction after the thread being joined
    """

    def __init__(self, function, *args):
        self.result = []
        self.thread = PyThread(target=self.__function_helper__,
                               args=(function, *args))

    def __function_helper__(self, function, args):
        self.result = function(args)

    def start(self):
        self.thread.start()

    def join(self):
        self.thread.join()
        return self.result
