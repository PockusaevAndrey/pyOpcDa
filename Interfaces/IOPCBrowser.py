from Structs.OPCBase import OPCBase


class IOPCBrowser(OPCBase):

    @property
    def Organization(self):
        """
    (Read-only) Returns either OPCHierarchical or OPCFlat.
    """
        return self._object.Organization

    @property
    def Filter(self):
        """
    (Read/Write) The filter that applies to ShowBranches and ShowLeafs methods. This property
    defaults to “” (no filtering). Servers may use this filter to narrow the list of names. Servers are
    recommended to support wildcards such as “*”.
    """
        return self._object.Filter

    @Filter.setter
    def Filter(self, x):
        self._object.Filter = x

    @property
    def DataType(self):
        """
    (Read/Write) The requested data type that applies to ShowLeafs methods. This property defaults to
    VT_EMPTY, which means that any data type is acceptable.
    """
        return self._object.DataType

    @DataType.setter
    def DataType(self, x):
        self._object.DataType = x

    @property
    def AccessRights(self):
        """
    (Read/Write) The requested access rights that apply to the ShowLeafs methods. This property
    defaults to OPCReadable OR’src with OPCWritable (that is, everything). This property applies to
    the filtering, i.e. you only want the leafs with these AccessRights.
    """
        return self._object.AccessRights

    @AccessRights.setter
    def AccessRights(self, x):
        self._object.AccessRights = x

    @property
    def CurrentPosition(self):
        """
    (Read-only) Current position in the tree. This string will be “” (i.e. the "root") initially. It will
    always be “” if Organization is OPCFlat.
    """
        return self._object.CurrentPosition

    @property
    def Count(self):
        """
        (Read-only) Required property for collections. Returns the number of items in the
        collection.
        """
        return self._object.Count

    def Item(self, ItemSpecifier):
        pass

    def __call__(self, ItemSpecifier): pass

    def __iter__(self): pass

    def __next__(self): pass

    def ShowBranches(self): pass

    def ShowLeafs(self, Flat=False): pass

    def MoveUp(self): pass

    def MoveToRoot(self): pass

    def MoveDown(self, Branch): pass

    def MoveTo(self, Branches): pass

    def GetItemID(self, Leaf): pass

    def GetAccessPaths(self, ItemID):
        """
        Returns the strings that are legal AccessPaths for this ItemID. May be Null if there are no
        AccessPaths for this ItemID or the server does not support them.

        :param ItemID: Fully Qualified ItemID
        :type ItemID: str
        :return:
        """
        pass
