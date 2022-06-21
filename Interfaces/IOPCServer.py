from abc import abstractmethod

from Structs.OPCBase import OPCBaseServer


class IOPCServer(OPCBaseServer):
    @abstractmethod
    def GetOPCServers(self, Node="localhost"): pass

    @abstractmethod
    def Connect(self, ProgID, Node='localhost'): pass

    @abstractmethod
    def Disconnect(self): pass

    @abstractmethod
    def CreateBrowser(self): pass

    @abstractmethod
    def GetErrorString(self, ErrorCode): pass

    @abstractmethod
    def QueryAvailableLocaleIDs(self): pass

    @abstractmethod
    def QueryAvailableProperties(self, ItemID): pass

    @abstractmethod
    def GetItemProperties(self):
        """
                not realize
                Return a list of the current data values for the passed ID codes.
                :return:
                """
        pass

    @abstractmethod
    def LookupItemIDs(self):
        """
                no realize
                Return a list of ItemIDs (if available) for each of the passed ID codes. These indicate the ItemID,
                which could be added to an OPCGroup and used for more efficient access to the data
                corresponding to the Item Properties. An error within the error array may indicate that the passed
                Property ID is not defined for this item.
                :return:
                """
        pass

    @abstractmethod
    def BindCallback(self, CallbackClass): pass
