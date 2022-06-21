# Events package

## Submodules

## Events.IGroupEvents module


### _class_ Events.IGroupEvents.IAllEvents()
Bases: `IAsyncReadEvent`, `IAsyncCancelEvent`, `IAsyncWriteEvent`, `IDataChangeEvent`


### _class_ Events.IGroupEvents.IAsyncCancelEvent()
Bases: `object`


#### OnAsyncCancelComplete(TransactionID)

* **Parameters**

    **TransactionID** – The client specified transaction ID. This is included in the
    ‘completion’ information provided in the Corresponding Event



### _class_ Events.IGroupEvents.IAsyncReadEvent()
Bases: `object`


#### OnAsyncReadComplete(TransactionID, NumItems, ClientHandles, ItemValues, Qualities, TimeStamps, Errors)
This event fires when an AsyncRead is completed.


* **Parameters**

    
    * **TransactionID** – The client specified transaction ID


    * **NumItems** – The number of items returned


    * **ClientHandles** – Array of client item handles for the items


    * **ItemValues** – Array of values.


    * **Qualities** – Array of Qualities for each item’s value


    * **TimeStamps** – Array of UTC TimeStamps for each item’s value. If the device cannot
    provide a timestamp then the server will provide one.


    * **Errors** – Array of Long’s indicating the success of the individual item reads.
    This indicates whether the read succeeded in obtaining a defined
    value, quality and timestamp. NOTE any FAILED error code
    indicates that the corresponding Value, Quality and Time stamp are UNDEFINED.



### _class_ Events.IGroupEvents.IAsyncWriteEvent()
Bases: `object`


#### OnAsyncWriteComplete(TransactionID, NumItems, ClientHandles, Errors)
This event fires when an AsyncWrite is completed
:param TransactionID:   The client specified transaction ID.
:param NumItems:        The number of items returned
:param ClientHandles:   Array of client item handles for the items
:param Errors:          Array of Long’s indicating the success of the individual item writes.


### _class_ Events.IGroupEvents.IDataChangeEvent()
Bases: `object`


#### OnDataChange(TransactionID, NumItems, ClientHandles, ItemValues, Qualities, TimeStamps)
The DataChange event is fired when a value or the quality of a value for an item within the group
has changed. Note the event will not fire faster than the update rate of the group. Therefore, item
values will be held by the server and buffered until the current time + update rate is greater than
the time of the previous update (event fired).
This is also affected by active states for both Group and Items. Only items that are active, and
whose group is active will be sent to the client in an event
:param TransactionID:       The client specified transaction ID. A non-0 value for this indicates

> that this call has been generated as a result of an AsyncRefresh. A
> value of 0 indicates that this call has been generated as a result of
> normal subscription processing.


* **Parameters**

    
    * **NumItems** – The number of items returned


    * **ClientHandles** – Array of client item handles for the items


    * **ItemValues** – Array of values


    * **Qualities** – Array of Qualities for each item’s value.


    * **TimeStamps** – Array of UTC TimeStamps for each item’s value. If the device cannot
    provide a timestamp then the server will provide one


## Events.IGroupsEvents module


### _class_ Events.IGroupsEvents.IGlobalDataChange()
Bases: `object`


#### OnGlobalDataChange(TransitionID, GroupHandle, NumItems, ClientHandles, ItemValues, Qualities, Timestamps)
The GlobalDataChange event is an event to facilitate one event handler being implemented to
receive and process data changes across multiple groups.
:param TransitionID:    The client specified transaction ID. A non-0 value for this indicates

> that this call has been generated as a result of an AsyncRefresh. A
> value of 0 indicates that this call has been generated as a result of
> normal subscription processing.


* **Parameters**

    
    * **GroupHandle** – ClientHandle of the OPCGroup Object the changed data corresponds to.


    * **NumItems** – The number of items returned


    * **ClientHandles** – Array of client item handles for the items


    * **ItemValues** – Array of values


    * **Qualities** – Array of Qualities for each item’s value


    * **Timestamps** – Array of UTC TimeStamps for each item’s value


## Events.IServerEvents module


### _class_ Events.IServerEvents.IServerShutDownEvent()
Bases: `object`


#### OnServerShutDown(ServerReason)
The ServerShutDown event is fired when the server is planning on shutting down and wants to tell
all the active clients to release any resources. The client provides this method so that the server can
request that the client disconnect from the server. The client should remove all groups and items.


* **Parameters**

    **ServerReason** (*str*) – An optional text string provided by the server indicating the reason
    for the shutdown.


## Module contents
