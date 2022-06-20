class IGlobalDataChange:
    def OnGlobalDataChange(self, TransitionID, GroupHandle, NumItems, ClientHandles, ItemValues, Qualities, Timestamps):
        """
        The GlobalDataChange event is an event to facilitate one event handler being implemented to
        receive and process data changes across multiple groups.
        :param TransitionID:    The client specified transaction ID. A non-0 value for this indicates
                                that this call has been generated as a result of an AsyncRefresh. A
                                value of 0 indicates that this call has been generated as a result of
                                normal subscription processing.
        :param GroupHandle:     ClientHandle of the OPCGroup Object the changed data corresponds to.
        :param NumItems:        The number of items returned
        :param ClientHandles:   Array of client item handles for the items
        :param ItemValues:      Array of values
        :param Qualities:       Array of Qualities for each item's value
        :param Timestamps:      Array of UTC TimeStamps for each item's value
        """
        pass
