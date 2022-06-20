from Structs.OPCBase import OPCBase


class IOPCItems(OPCBase):

    def Item(self, ItemSpecifier): pass

    def GetOPCItem(self, ServerHandle): pass

    def AddItem(self, ItemID, ClientHandle): pass

    def AddItems(self, Count, ItemIDs, ClientHandles): pass

    def Remove(self, Count, ServerHandles): pass

    def Validate(self, Count, ItemIDs): pass

    def SetActive(self, Count, ServerHandles, ActiveState): pass

    def SetClientHandles(self, Count, ServerHandles, ClientHandles): pass

    def SetDataType(self, Count, ServerHandles, RequestedDataTypes): pass
