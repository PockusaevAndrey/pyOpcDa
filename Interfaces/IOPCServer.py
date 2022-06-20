from Structs.OPCBase import OPCBaseServer


class IOPCServer(OPCBaseServer):
    def GetOPCServers(self, Node="localhost"): pass

    def Connect(self, ProgID, Node='localhost'): pass

    def Disconnect(self): pass

    def CreateBrowser(self): pass

    def GetErrorString(self, ErrorCode): pass

    def QueryAvailableLocaleIDs(self): pass

    def QueryAvailableProperties(self, ItemID): pass

    def GetItemProperties(self):
        """
                not realize
                Return a list of the current data values for the passed ID codes.
                :return:
                """
        pass

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

    def BindCallback(self, CallbackClass): pass
