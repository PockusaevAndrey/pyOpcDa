from abc import ABCMeta, abstractmethod


class IDataChangeEvent(metaclass=ABCMeta):

    @abstractmethod
    def OnDataChange(self, TransactionID, NumItems, ClientHandles, ItemValues, Qualities, TimeStamps):
        """
        The DataChange event is fired when a value or the quality of a value for an item within the group
        has changed. Note the event will not fire faster than the update rate of the group. Therefore, item
        values will be held by the server and buffered until the current time + update rate is greater than
        the time of the previous update (event fired).
        This is also affected by active states for both Group and Items. Only items that are active, and
        whose group is active will be sent to the client in an event
        :param TransactionID:       The client specified transaction ID. A non-0 value for this indicates
                                    that this call has been generated as a result of an AsyncRefresh. A
                                    value of 0 indicates that this call has been generated as a result of
                                    normal subscription processing.
        :param NumItems:            The number of items returned
        :param ClientHandles:       Array of client item handles for the items
        :param ItemValues:          Array of values
        :param Qualities:           Array of Qualities for each item's value.
        :param TimeStamps:          Array of UTC TimeStamps for each item's value. If the device cannot
                                    provide a timestamp then the server will provide one
        """
        pass


class IAsyncReadEvent(metaclass=ABCMeta):
    @abstractmethod
    def OnAsyncReadComplete(self, TransactionID, NumItems, ClientHandles, ItemValues, Qualities, TimeStamps,
                            Errors):
        """
        This event fires when an AsyncRead is completed.

        :param TransactionID:   The client specified transaction ID
        :param NumItems:        The number of items returned
        :param ClientHandles:   Array of client item handles for the items
        :param ItemValues:      Array of values.
        :param Qualities:       Array of Qualities for each item's value
        :param TimeStamps:      Array of UTC TimeStamps for each item's value. If the device cannot
                                provide a timestamp then the server will provide one.
        :param Errors:          Array of Long’s indicating the success of the individual item reads.
                                This indicates whether the read succeeded in obtaining a defined
                                value, quality and timestamp. NOTE any FAILED error code
                                indicates that the corresponding Value, Quality and Time stamp are UNDEFINED.
        """
        pass


class IAsyncWriteEvent(metaclass=ABCMeta):
    @abstractmethod
    def OnAsyncWriteComplete(self, TransactionID, NumItems, ClientHandles, Errors):
        """
        This event fires when an AsyncWrite is completed
        :param TransactionID:   The client specified transaction ID.
        :param NumItems:        The number of items returned
        :param ClientHandles:   Array of client item handles for the items
        :param Errors:          Array of Long’s indicating the success of the individual item writes.
        """
        pass


class IAsyncCancelEvent(metaclass=ABCMeta):
    @abstractmethod
    def OnAsyncCancelComplete(self, TransactionID):
        """

        :param TransactionID:   The client specified transaction ID. This is included in the
                                ‘completion’ information provided in the Corresponding Event
        """
        pass


class IAllEvents(IAsyncReadEvent, IAsyncCancelEvent, IAsyncWriteEvent, IDataChangeEvent, metaclass=ABCMeta): pass
