from abc import abstractmethod, ABCMeta

from Structs.OPCBase import OPCBase


class IOPCBrowser(OPCBase, metaclass=ABCMeta):

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

    @abstractmethod
    def Item(self, ItemSpecifier):
        pass

    @abstractmethod
    def __call__(self, ItemSpecifier): pass

    @abstractmethod
    def __iter__(self): pass

    @abstractmethod
    def __next__(self): pass

    @abstractmethod
    def ShowBranches(self): pass

    @abstractmethod
    def ShowLeafs(self, Flat=False): pass

    @abstractmethod
    def MoveUp(self): pass

    @abstractmethod
    def MoveToRoot(self): pass

    @abstractmethod
    def MoveDown(self, Branch): pass

    @abstractmethod
    def MoveTo(self, Branches): pass

    @abstractmethod
    def GetItemID(self, Leaf): pass

    @abstractmethod
    def GetAccessPaths(self, ItemID):
        """
        Returns the strings that are legal AccessPaths for this ItemID. May be Null if there are no
        AccessPaths for this ItemID or the server does not support them.

        :param ItemID: Fully Qualified ItemID
        :type ItemID: str
        :return:
        """
        pass
