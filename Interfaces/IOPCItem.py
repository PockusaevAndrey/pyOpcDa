from abc import abstractmethod, ABCMeta

from Structs.OPCBase import OPCBase


class IOPCItem(OPCBase, metaclass=ABCMeta):
    @abstractmethod
    def Read(self, Source): pass
    @abstractmethod
    def Write(self, Value): pass
