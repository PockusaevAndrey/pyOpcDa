from abc import abstractmethod, ABCMeta

from Structs.OPCBase import OPCBase


class IOPCItems(OPCBase, metaclass=ABCMeta):
    @abstractmethod
    def Item(self, ItemSpecifier): pass

    @abstractmethod
    def GetOPCItem(self, ServerHandle): pass

    @abstractmethod
    def AddItem(self, ItemID, ClientHandle): pass

    @abstractmethod
    def AddItems(self, Count, ItemIDs, ClientHandles): pass

    @abstractmethod
    def Remove(self, Count, ServerHandles): pass

    @abstractmethod
    def Validate(self, Count, ItemIDs): pass

    @abstractmethod
    def SetActive(self, Count, ServerHandles, ActiveState): pass

    @abstractmethod
    def SetClientHandles(self, Count, ServerHandles, ClientHandles): pass

    @abstractmethod
    def SetDataType(self, Count, ServerHandles, RequestedDataTypes): pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self): pass
