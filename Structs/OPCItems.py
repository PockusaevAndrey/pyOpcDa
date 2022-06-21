from typing import Tuple

from Interfaces.IOPCItems import IOPCItems
from Structs.OPCItem import OPCItem


class OPCItems(IOPCItems):
    """
    This object also has properties for OPCItem defaults. When an OPCItem is added, the
    DefaultXXXX properties set its initial state. The defaults can be changed to add OPCItems with
    different initial states. Of course, once an OPCItem is added, its properties can be modified. This
    reduces the number of parameters required to call the Add method.
    """

    @property
    def Parent(self):
        """
        (Read-only) Returns reference to the parent OPCGroup object.
        """
        return self._object.Parent

    @property
    def DefaultRequestedDataType(self):
        """
        (Read/Write) The requested data type that will be used in calls to Add. This property defaults to
        VT_EMPTY (which means the server sends data in the server canonical data type).
        :rtype: int
        """
        return self._object.DefaultRequestedDataType

    @DefaultRequestedDataType.setter
    def DefaultRequestedDataType(self, value: int):
        self._object.DefaultRequestedDataType = value

    @property
    def DefaultAccessPath(self):
        """
        (Read/Write) The default AccessPath that will be used in calls to Add. This property defaults to
        “”
        :rtype: str
        """
        return self._object.DefaultAccessPath

    @DefaultAccessPath.setter
    def DefaultAccessPath(self, value: str):
        self._object.DefaultAccessPath = value

    @property
    def DefaultIsActive(self):
        """
        (Read/Write) The default active state that will be used in calls to Add. This property defaults to
        True.
        :rtype: bool
        """
        return self._object.DefaultIsActive

    @DefaultIsActive.setter
    def DefaultIsActive(self, value: bool):
        self._object.DefaultIsActive = value

    @property
    def Count(self):
        """
        (Read-only) Required property for collections
        :rtype: int
        """
        return self._object.Count

    def Item(self, ItemSpecifier):
        """
        Required property for collections

        :param ItemSpecifier:   Returns an OPCItem by ItemSpecifier. ItemSpecifier is the 1-based
                                index into the collection
        :type ItemSpecifier:    int
        """
        return OPCItem(self._object.Item(ItemSpecifier))

    def GetOPCItem(self, ServerHandle):
        """
        Returns an OPCItem by ServerHandle returned by Add. Use the Item property to reference by
        index.
        :param ServerHandle:    ServerHandle is the OPCItem’s ServerHandle
                                Use Item to reference by index.
        :type ServerHandle:     int
        """

        return OPCItem(self._object.GetOPCItem(ServerHandle))

    def AddItem(self, ItemID, ClientHandle):
        """
        Creates a new OPCItem object and adds it to the collection. The properties of this new OPCItem
        are determined by the current defaults in the OPCItems collection object. After an OPCItem is
        added, its properties can also be modified.

        :param ItemID:          Fully Qualified ItemID
        :type ItemID:           str
        :param ClientHandle:    Client handle that will be returned with the
        :type ClientHandle:     int
        """
        OPCItem(self._object.AddItem(ItemID, ClientHandle))

    def AddItems(self, Count, ItemIDs, ClientHandles):
        """
        Creates OPCItem objects and adds them to the collection. The properties of each new OPCItem
        are determined by the current defaults in the OPCItems collection object. After an OPCItem is
        added, its properties can also be modified
        :param Count:           The number of items to be affected
        :type Count:            int
        :param ItemIDs:         Array of Fully Qualified ItemID’s
        :type ItemIDs:          Tuple[str]
        :param ClientHandles:   Array of client item handles for the items processed
        :type ClientHandles:    Tuple[int]
        :return:                (ServerHandles, Errors)
                                ServerHandles   --  Array of server item handles for the items processed
                                Errors          --  Array of Long’s indicating the success of the individual items
                                                    operation.
        :rtype: (Tuple[int], Tuple[int])
        """
        return self._object.AddItems(Count, ItemIDs, ClientHandles)

    def Remove(self, Count, ServerHandles):
        """
        Removes an OPCItem

        :param Count:           The number of items to be removed
        :type Count:            int
        :param ServerHandles:   Array of server item handles for the items processed
        :type ServerHandles:    Tuple[int]
        :return:                Errors -- Array of Long’s indicating the success of the individual items
                                operation.
        :rtype:                 Tuple[int]
        """

        return self._object.Remove(Count, ServerHandles)

    def Validate(self, Count, ItemIDs):
        """
        Determines if one or more OPCItems could be successfully created via the Add method (but does
        not add them).

        :param Count:       The number of items to be affected
        :type Count:        int
        :param ItemIDs:     Array of Fully Qualified ItemID’s
        :type ItemIDs:      Tuple[str]

        :return:            Errors -- Array of Long’s indicating the success of the individual items
                            operation.
        :rtype:             Tuple[int]
        """

        return self._object.Validate(Count, ItemIDs)

    def SetActive(self, Count, ServerHandles, ActiveState):
        """
        Allows Activation and deactivation of individual OPCItem’s in the OPCItems Collection

        :param Count:               The number of items to be affected
        :type Count:                int
        :param ServerHandles:       Array of server item handles for the items processed
        :type ServerHandles:        Tuple[int]
        :param ActiveState:         TRUE if items are to be activated. FALSE if items are to be
                                    deactivated.
        :return:                    Errors -- Array of Long’s indicating the success of the individual items
                                    operation.
        :rtype:                     Tuple[int]
        """
        return self._object.SetActive(Count, ServerHandles, ActiveState)

    def SetClientHandles(self, Count, ServerHandles, ClientHandles):
        """
        Changes the client handles or one or more Items in a Group.

        :param Count:           The number of items to be affected
        :type Count:            int
        :param ServerHandles:   Array of server item handles for the items processed
        :type ServerHandles:    Tuple[int]
        :param ClientHandles:   Array of new Client item handles to be stored. The Client
                                handles do not need to be unique.
        :type ClientHandles:    Tuple[int]

        :return:                Errors -- Array of Long’s indicating the success of the individual items
                                operation.
        :rtype:                 Tuple[int]
        """

        return self._object.SetClientHandles(Count, ServerHandles, ClientHandles)

    def SetDataType(self, Count, ServerHandles, RequestedDataTypes):
        """
        Changes the requested data type for one or more Items

        :param Count:               The number of items to be affected
        :type Count:                int
        :param ServerHandles:       Array of server item handles for the items processed
        :type ServerHandles:        Tuple[int]
        :param RequestedDataTypes:  Array of new Requested DataTypes to be stored.
        :type RequestedDataTypes:   Tuple[int]
        :return:                    Errors -- Array of Long’s indicating the success of the individual items
                                    operation.
        :rtype:                     Tuple[int]
        """
        return self._object.SetDataType(Count, ServerHandles, RequestedDataTypes)

    def __iter__(self):
        return self._object.__iter__()

    def __next__(self):
        return self._object.__next__()
