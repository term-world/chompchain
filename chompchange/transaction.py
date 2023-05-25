import json

class Transaction:	class Transaction:


    def __init__(self):	    def __init__(self, **kwargs):
        pass	        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def __str__(self):
        return json.dumps(self.__dict__)
