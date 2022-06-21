from typing import Tuple, Union

import pythoncom
import win32com.client
from win32.lib import pywintypes

from Events.IGroupEvents import *
from Interfaces.IOPCGroup import IOPCGroup
from Structs.OPCItems import OPCItems


class OPCGroup(IOPCGroup):
    @property
    def Parent(self):
        """
        (Read-only) Returns reference to the parent OPCServer object
        """
        return self._object.Parent

    @property
    def Name(self):
        """(Read/Write) The name given to this group."""
        return self._object.Name

    @property
    def IsPublic(self):
        """(Read-only) Returns True if this group is a public group, otherwise False."""
        return self._object.IsPublic

    @property
    def IsActive(self):
        """(Read/Write) This property controls the active state of the group. A group that is active acquires
            data. An inactive group typically does not continue data acquisition except as required for
            read/writes"""
        return self._object.IsActive

    @IsActive.setter
    def IsActive(self, value):
        self._object.IsActive = value

    @property
    def IsSubscribed(self):
        """(Read/Write) This property controls asynchronous notifications to the group. A group that is
            subscribed receives data changes from the server."""
        return self._object.IsSubscribed

    @IsSubscribed.setter
    def IsSubscribed(self, value):
        self._object.IsSubscribed = value

    @property
    def ClientHandle(self):
        """(Read/Write) A Long value associated with the group. Its purpose is for the client to quickly locate
            the destination of data. The handle is typically an index, etc. This handle will be returned to the
            client along with data or status."""
        return self._object.ClientHandle

    @ClientHandle.setter
    def ClientHandle(self, value):
        self._object.ClientHandle = value

    @property
    def ServerHandle(self):
        """
        (Read-only) The server assigned handle for the group. The ServerHandle is a Long that uniquely
        identifies this group. The client must supply this handle to some of the methods that operate on
        OPCGroup objects (such as OPCGroups.Remove).
        """
        return self._object.ServerHandle

    @property
    def LocaleID(self):
        """
        (Read/Write) This property identifies the locale, which may be used to localize strings returned
        from the server. This property’s default depends on the value set in the OPCGroups Collection..
        """
        return self._object.LocaleID

    @LocaleID.setter
    def LocaleID(self, value):
        self._object.LocaleID = value

    @property
    def TimeBias(self):
        """(Read/Write). This property provides the information needed to convert the time stamp on the data
        back to the local time of the device."""
        return self._object.TimeBias

    @TimeBias.setter
    def TimeBias(self, value):
        self._object.TimeBias = value

    @property
    def DeadBand(self):
        """
        (Read/Write) A deadband is expressed as percent of full scale (legal values 0 to 100). This
        property’s default depends on the value set in the OPCGroups Collection.
        """
        return self._object.DeadBand

    @DeadBand.setter
    def DeadBand(self, value):
        self._object.DeadBand = value

    @property
    def UpdateRate(self):
        """
        (Read/Write) The fastest rate at which data change events may be fired. A slow process might
        cause data changes to fire at less than this rate, but they will never exceed this rate. Rate is in
        milliseconds. This property’s default depends on the value set in the OPCGroups Collection.
        Assigning a value to this property is a “request” for a new update rate. The server may not support
        that rate, so reading the property may result in a different rate (the server will use the closest rate it
        does support).
        """
        return self._object.UpdateRate

    @UpdateRate.setter
    def UpdateRate(self, value):
        self._object.UpdateRate = value

    @property
    def OPCItems(self):
        """
        A collection of OPCItem objects. This is the default property of the OPCGroup object.
        """
        return OPCItems(self._object.OPCItems)

    def SyncRead(self, Source, NumItems, ServerHandles):
        """
        This function reads the value, quality and timestamp information for one or more items in a group
        :param Source:              The ‘data source’; OPC_DS_CACHE or OPC_DS_DEVICE
        :param NumItems:            The number of items to be read.
        :param ServerHandles:       Array of server item handles for the items to be rea
        :type Source:               int
        :type NumItems:             int,
        :type ServerHandles:        Tuple[int]
        :rtype:                     (Tuple[int], Tuple[int], Tuple[int], Tuple[pywintypes.TimeType])
        :return:                    (Values, Errors, Qualities, TimeStamps)                                    cannot provide a timestamp then the server will provide one.
        """
        try:
            return self._object.SyncRead(Source, NumItems, ServerHandles)
        except pywintypes.com_error as e:
            raise RuntimeError(pythoncom.GetScodeString(e.args[2][5]))

    def SyncWrite(self, NumItems, ServerHandles, Values):
        """
        Writes values to one or more items in a group. The function runs to completion. The values are
        written to the DEVICE. That is, the function should not return until it verifies that the device has
        actually accepted (or rejected) the data.
        :param NumItems: Number of items to be written
        :type NumItems: int
        :param ServerHandles: Array of server item handles for the items to be written
        :type ServerHandles: Tuple[int]
        :param Values: Tuple
        :return: Array of Long’s indicating the success of the individual item writes.
        :rtype: Tuple[int]
        """
        try:
            return self._object.SyncWrite(NumItems, ServerHandles, Values)
        except pywintypes.com_error as e:
            raise RuntimeError(pythoncom.GetScodeString(e.args[2][5]))

    def AsyncRead(self, NumItems, ServerHandles, TransactionID):
        """
        Read one or more items in a group. The results are returned via the AsyncReadComplete event
        associated with the OPCGroup object.
        Reads are from ‘DEVICE’ and are not affected by the ACTIVE state of the group or item.

        :param TransactionID:   The client specified transaction ID. This is included in the
                                ‘completion’ information provided in the Corresponding Event.
        :type TransactionID:    int
        :param NumItems:        The number of items to be read
        :type NumItems:         int
        :param ServerHandles:   Array of server item handles for the items to be read
        :type ServerHandles:    Tuple[int]
        """
        try:
            self._object.AsyncRead(NumItems, ServerHandles, None, TransactionID)
        except pywintypes.com_error as e:
            raise RuntimeError(pythoncom.GetScodeString(e.args[2][5]))

    def AsyncWrite(self, NumItems, ServerHandles, Values, TransactionID):
        """
        Write one or more items in a group. The results are returned via the AsyncWriteComplete event
        associated with the OPCGroup object.
        
        :param NumItems:        The number of items to be written.
        :type NumItems:         int
        :param ServerHandles:   Array of server item handles for the items to be written
        :type ServerHandles:    Tuple[int]
        :param Values:          Array of values.
        :type Values:           tuple
        :param TransactionID:   The client specified transaction ID. This is included in the
                                ‘completion’ information provided in the Corresponding Event.
        :type TransactionID:    int
        """
        try:
            self._object.AsyncWrite(NumItems, ServerHandles, Values, None, TransactionID)
        except pywintypes.com_error as e:
            raise RuntimeError(pythoncom.GetScodeString(e.args[2][5]))

    def AsyncRefresh(self, Source, TransactionID):
        """
        Generate an event for all active items in the group (whether they have changed or not). Inactive
        items are not included in the callback. The results are returned via the DataChange event
        associated with the OPCGroup object, as well as the GlobalDataChange event associated with the
        OPCGroups object.

        :param Source:          The ‘data source’; OPC_DS_CACHE or OPC_DS_DEVICE
        :type Source:           int
        :param TransactionID:   The client specified transaction ID. This is included in the
                                ‘completion’ information provided in the Corresponding Event.
        :type TransactionID:    int
        """
        try:
            self._object.AsyncRefresh(Source, TransactionID)
        except pywintypes.com_error as e:
            raise RuntimeError(pythoncom.GetScodeString(e.args[2][5]))

    def AsyncCancel(self, CancelID):
        """
        Request that the server cancel an outstanding transaction. An AsyncCancelComplete event will
        occur indicating whether or not the cancel succeeded

        :param CancelID:    The Server generated CancelID that was previously returned by the
                            AsyncRead, AsyncWrite or AsyncRefresh method that the client now
                            wants to cancel.
        :type CancelID:     int
        """
        try:
            self._object.AsyncCancel(CancelID)
        except pywintypes.com_error as e:
            raise RuntimeError(pythoncom.GetScodeString(e.args[2][5]))

    def BindCallback(self,
                     CallbackClass: Union[IDataChangeEvent, IAsyncCancelEvent, IAsyncReadEvent, IAsyncWriteEvent]):
        """
        Binds Callback Class to object
        """
        win32com.client.WithEvents(self._object, CallbackClass)
