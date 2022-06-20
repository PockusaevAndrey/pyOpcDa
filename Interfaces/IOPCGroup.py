from Structs.OPCBase import OPCBase


class IOPCGroup(OPCBase):

    def SyncRead(self, Source, NumItems, ServerHandles): pass

    def SyncWrite(self, NumItems, ServerHandles, Values): pass

    def AsyncRead(self, NumItems, ServerHandles, TransactionID):pass

    def AsyncWrite(self, NumItems, ServerHandles, Values, TransactionID): pass

    def AsyncRefresh(self, Source, TransactionID): pass

    def AsyncCancel(self, CancelID): pass
