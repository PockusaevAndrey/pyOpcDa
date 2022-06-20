from Structs.OPCBase import OPCBase


class IOPCGroups(OPCBase):

    def Item(self, ItemSpecifier):
        pass

    def Add(self, Name):
        pass

    def GetOPCGroup(self, ItemSpecifier):
        pass

    def Remove(self, ItemSpecifier):
        pass

    def RemoveAll(self):
        pass

    def ConnectPublicGroup(self, Name):
        pass

    def RemovePublicGroup(self, ItemSpecifier):
        pass
