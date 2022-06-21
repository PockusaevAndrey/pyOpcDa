from abc import ABCMeta, abstractmethod

from Structs.OPCBase import OPCBase


class IOPCGroups(OPCBase, metaclass=ABCMeta):
    @abstractmethod
    def Item(self, ItemSpecifier):
        pass
    @abstractmethod
    def Add(self, Name):
        pass
    @abstractmethod
    def GetOPCGroup(self, ItemSpecifier):
        pass
    @abstractmethod
    def Remove(self, ItemSpecifier):
        pass
    @abstractmethod
    def RemoveAll(self):
        pass
    @abstractmethod
    def ConnectPublicGroup(self, Name):
        pass
    @abstractmethod
    def RemovePublicGroup(self, ItemSpecifier):
        pass
