from Interfaces.IOPCItem import IOPCItem


class OPCItem(IOPCItem):
    """
    An OPC Item represents a connection to data sources within the server. Associated with each item
    is a Value, Quality and Time Stamp. The value is in the form of a VARIANT, and the Quality is
    similar to that specified by Fieldbus.
    """
    @property
    def Parent(self):
        """
        Read-only) Returns reference to the parent OPCGroup object.
        """
        return self._object.Parent

    @property
    def ClientHandle(self):
        """
        (Read/Write) A Long value associated with the OPCItem. Its purpose is for the client to quickly
        locate the destination of data. The handle is typically an index, etc. This handle will be returned to
        the client along with data or status changes by OPCGroup events.
        """
        return self._object.ClientHandle

    @ClientHandle.setter
    def ClientHandle(self, value):
        self._object.ClientHandle = value

    @property
    def ServerHandle(self):
        """
        (Read-only) The server assigned handle for the AnOPCItem. The ServerHandle is a Long that
        uniquely identifies this AnOPCItem. The client must supply this handle to some of the methods
        that operate on OPCItem objects (such as OPCItems.Remove).
        """
        return self._object.ServerHandle

    @property
    def AccessPath(self):
        """
        (Read-only) The access path specified by the client on the Add function..
        """
        return self._object.AccessPath

    @property
    def AccessRights(self):
        """
        (Read-only) Returns the access rights of this item.
        """
        return self._object.AccessRights

    @property
    def ItemID(self):
        """
        (Read-only) The unique identifier for this item.
        """
        return self._object.ItemID

    @property
    def IsActive(self):
        """
        (Read/Write) State of the Data Acquisition for this item.
        """
        return self._object.IsActive

    @IsActive.setter
    def IsActive(self, value: bool):
        self._object.IsActive = value

    @property
    def RequestedDataType(self):
        """
        (Read/Write) The data type in which the item's value will be returned. Note that if the requested
        data type was rejected the OPCItem will be invalid(failed), until the RequestedDataType is set to
        a valid value.
        """
        return self._object.RequestedDataType

    @RequestedDataType.setter
    def RequestedDataType(self, value):
        self._object.RequestedDataType = value

    @property
    def Value(self):
        """
        (Read-only) Returns the latest value read from the server. This is the default property of
        AnOPCItem.
        """
        return self._object.Value

    @property
    def Quality(self):
        """
        (Read-only) Returns the latest quality read from the server.
        """
        return self._object.Quality

    @property
    def TimeStamp(self):
        """
        (Read-only) Returns the latest timestamp read from the server.
        """
        return self._object.TimeStamp

    @property
    def CanonicalDataType(self):
        """
        (Read-only) Returns the native data type in the server.
        """
        return self._object.CanonicalDataType

    @property
    def EUType(self):
        """
        (Read-only) Indicate the type of Engineering Units (EU) information (if any) contained in EUInfo.
        """
        return self._object.EUType

    @property
    def EUInfo(self):
        """(Read-only) Variant that contains the Engineering Units information"""
        return self._object.EUInfo

    def Read(self, Source):
        """
        Read makes a blocking call to read this item from the server.
        Read can be called with only a source (either OPCCache or OPCDevice) to refresh the item’s
        value, quality and timestamp properties. If the value, quality and timestamp must be in sync, this
        method’s optional parameters return values that were acquired together.

        :param Source:  The ‘data source’; OPC_DS_CACHE or OPC_DS_DEVICE
        :type Source    int
        :return:        (Value, Quality, TimeStamp)
                        Value       --  Returns the latest value read from the server
                        Quality     --  Returns the latest value read from the server
                        TimeStamp   --  Returns the latest timestamp read from the server.
        :rtype:         (tuple, tuple, tuple)
        """
        return self._object.Read(Source)

    def Write(self, Value):
        """
        Write makes a blocking call to write this value to the server.
        :param Value:   Value to be written to the data source.
        """

        self._object.Write(Value)
