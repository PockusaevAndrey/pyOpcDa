from abc import abstractmethod, ABCMeta

from Structs.OPCBase import OPCBase


class IOPCGroup(OPCBase, metaclass=ABCMeta):
    @abstractmethod
    def SyncRead(self, Source, NumItems, ServerHandles): pass
    @abstractmethod
    def SyncWrite(self, NumItems, ServerHandles, Values): pass
    @abstractmethod
    def AsyncRead(self, NumItems, ServerHandles, TransactionID):pass
    @abstractmethod
    def AsyncWrite(self, NumItems, ServerHandles, Values, TransactionID): pass
    @abstractmethod
    def AsyncRefresh(self, Source, TransactionID): pass
    @abstractmethod
    def AsyncCancel(self, CancelID): pass
