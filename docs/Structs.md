# Structs package

## Submodules

## Structs.OPCBase module


### _class_ Structs.OPCBase.OPCBase(comObject)
Bases: [`IOPCBase`](Interfaces.md#Interfaces.IOPCBase.IOPCBase)


#### _property_ Parent()

#### \__init__(comObject)

### _class_ Structs.OPCBase.OPCBaseServer(comObject)
Bases: [`IOPCBase`](Interfaces.md#Interfaces.IOPCBase.IOPCBase)


#### \__init__(comObject)
## Structs.OPCBrowser module


### _class_ Structs.OPCBrowser.OPCBrowser(comObject)
Bases: [`IOPCBrowser`](Interfaces.md#Interfaces.IOPCBrowser.IOPCBrowser)

The OPCBrowser object is a collection of branch or item names that exist in the server. Browsing
is optional. If the server does not support browsing, CreateBrowser will not create this object.


#### GetItemID(Leaf)
Given a name, returns a valid ItemID that can be passed to OPCItems Add method.


* **Parameters**

    **Leaf** (*str*) – The name of a BRANCH or LEAF at the current level.



* **Return type**

    str



#### Item(ItemSpecifier)
Required property for collections. Returns a name indexed by ItemSpecifier. The name will be a
branch or leaf name, depending on previous calls to ShowBranches or ShowLeafs. Item is the
default for the OPCBrowser.
:param ItemSpecifier:   1-based index into the collection
:type ItemSpecifier:    int
:rtype:               str


#### MoveDown(Branch)
Move down into this branch.
:type Branch: str
:rtype: None


#### MoveTo(Branches)
Move to an absolute position.


* **Parameters**

    **Branches** (*Tuple**[**str**]*) – Branches are an array of branch names from the root to a particular
    position in the tree.



#### MoveToRoot()
Move up to the first level in the tree.
:rtype: None


#### MoveUp()
Move up one level in the tree.
:rtype: None


#### ShowBranches()
Fills the collection with names of the branches at the current browse position.


#### ShowLeafs(Flat=False)
Fills the collection with the names of the leafs at the current browse position. Default for Flat is
FALSE.


* **Parameters**

    **Flat** (*bool*) – Defines what the collection should contain.
    The Settings for Flat are:
    True    –  the collection is filled with all leafs at the current browse position, as

    > well as all the leafs that are below the current browse position.
    > Basically we are treated from the current position on down as a flat
    > name space.

    False   –  the collection is filled with all leafs at the current browse position




* **Return type**

    None


## Structs.OPCGroup module


### _class_ Structs.OPCGroup.OPCGroup(comObject)
Bases: [`IOPCGroup`](Interfaces.md#Interfaces.IOPCGroup.IOPCGroup)


#### AsyncCancel(CancelID)
Request that the server cancel an outstanding transaction. An AsyncCancelComplete event will
occur indicating whether or not the cancel succeeded


* **Parameters**

    **CancelID** (*int*) – The Server generated CancelID that was previously returned by the
    AsyncRead, AsyncWrite or AsyncRefresh method that the client now
    wants to cancel.



#### AsyncRead(NumItems, ServerHandles, TransactionID)
Read one or more items in a group. The results are returned via the AsyncReadComplete event
associated with the OPCGroup object.
Reads are from ‘DEVICE’ and are not affected by the ACTIVE state of the group or item.


* **Parameters**

    
    * **TransactionID** (*int*) – The client specified transaction ID. This is included in the
    ‘completion’ information provided in the Corresponding Event.


    * **NumItems** (*int*) – The number of items to be read


    * **ServerHandles** (*Tuple**[**int**]*) – Array of server item handles for the items to be read



#### AsyncRefresh(Source, TransactionID)
Generate an event for all active items in the group (whether they have changed or not). Inactive
items are not included in the callback. The results are returned via the DataChange event
associated with the OPCGroup object, as well as the GlobalDataChange event associated with the
OPCGroups object.


* **Parameters**

    
    * **Source** (*int*) – The ‘data source’; OPC_DS_CACHE or OPC_DS_DEVICE


    * **TransactionID** (*int*) – The client specified transaction ID. This is included in the
    ‘completion’ information provided in the Corresponding Event.



#### AsyncWrite(NumItems, ServerHandles, Values, TransactionID)
Write one or more items in a group. The results are returned via the AsyncWriteComplete event
associated with the OPCGroup object.


* **Parameters**

    
    * **NumItems** (*int*) – The number of items to be written.


    * **ServerHandles** (*Tuple**[**int**]*) – Array of server item handles for the items to be written


    * **Values** (*tuple*) – Array of values.


    * **TransactionID** (*int*) – The client specified transaction ID. This is included in the
    ‘completion’ information provided in the Corresponding Event.



#### BindCallback(CallbackClass)
Binds Callback Class to object


#### _property_ ClientHandle()
(Read/Write) A Long value associated with the group. Its purpose is for the client to quickly locate
the destination of data. The handle is typically an index, etc. This handle will be returned to the
client along with data or status.


#### _property_ DeadBand()
(Read/Write) A deadband is expressed as percent of full scale (legal values 0 to 100). This
property’s default depends on the value set in the OPCGroups Collection.


#### _property_ IsActive()
(Read/Write) This property controls the active state of the group. A group that is active acquires
data. An inactive group typically does not continue data acquisition except as required for
read/writes


#### _property_ IsPublic()
(Read-only) Returns True if this group is a public group, otherwise False.


#### _property_ IsSubscribed()
(Read/Write) This property controls asynchronous notifications to the group. A group that is
subscribed receives data changes from the server.


#### _property_ LocaleID()
(Read/Write) This property identifies the locale, which may be used to localize strings returned
from the server. This property’s default depends on the value set in the OPCGroups Collection..


#### _property_ Name()
(Read/Write) The name given to this group.


#### _property_ OPCItems()
A collection of OPCItem objects. This is the default property of the OPCGroup object.


#### _property_ Parent()
(Read-only) Returns reference to the parent OPCServer object


#### _property_ ServerHandle()
(Read-only) The server assigned handle for the group. The ServerHandle is a Long that uniquely
identifies this group. The client must supply this handle to some of the methods that operate on
OPCGroup objects (such as OPCGroups.Remove).


#### SyncRead(Source, NumItems, ServerHandles)
This function reads the value, quality and timestamp information for one or more items in a group
:param Source:              The ‘data source’; OPC_DS_CACHE or OPC_DS_DEVICE
:param NumItems:            The number of items to be read.
:param ServerHandles:       Array of server item handles for the items to be rea
:type Source:               int
:type NumItems:             int,
:type ServerHandles:        Tuple[int]
:rtype:                     (Tuple[int], Tuple[int], Tuple[int], Tuple[pywintypes.TimeType])
:return:                    (Values, Errors, Qualities, TimeStamps)                                    cannot provide a timestamp then the server will provide one.


#### SyncWrite(NumItems, ServerHandles, Values)
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


#### _property_ TimeBias()
(Read/Write). This property provides the information needed to convert the time stamp on the data
back to the local time of the device.


#### _property_ UpdateRate()
(Read/Write) The fastest rate at which data change events may be fired. A slow process might
cause data changes to fire at less than this rate, but they will never exceed this rate. Rate is in
milliseconds. This property’s default depends on the value set in the OPCGroups Collection.
Assigning a value to this property is a “request” for a new update rate. The server may not support
that rate, so reading the property may result in a different rate (the server will use the closest rate it
does support).

## Structs.OPCGroups module


### _class_ Structs.OPCGroups.OPCGroups(comObject)
Bases: [`IOPCGroups`](Interfaces.md#Interfaces.IOPCGroups.IOPCGroups)

OPCGroups is a collection of OPCGroup objects, and the methods that create, remove, and
manage them.
This object also has properties for OPCGroup defaults. When OPCGroups are added, the
DefaultGroupXXXX properties set its initial state. The defaults can be changed to add
OPCGroups with different initial states. Changing the defaults does not affect groups that have
already been created. Once an OPCGroup is added, its properties can be modified. This reduces
the number of parameters required to call the Add method.


#### Add(Name)
Creates a new OPCGroup object and adds it to the collection. The properties of this new group are
determined by the current defaults in the OPCServer object. After a group is added, its properties
can also be modified.
:param Name:    Name of the group. The name must be unique among the other

> groups created by this client. If no name is provided, The server-
> generated name will also be unique relative to any existing groups.


#### BindCallback(CallbackClass)
Binds Callback Class to object
:type CallbackClass:


#### ConnectPublicGroup(Name)
Public Groups are pre-existing groups in a server. These groups can be connected rather than
added..
Refer to Appendix A - OPC Automation Error Handling for information on OPC Automation
errors and Exceptions.
:param Name: Name of group to be connected.
:type Name: str


#### _property_ Count()

#### _property_ DefaultGroupDeadband()
(Read/Write) This property provides the default deadband for OPCGroups created using
Groups.Add. A deadband is expressed as percent of full scale (legal values 0 to 100).


#### _property_ DefaultGroupIsActive()
(Read/Write) This property provides the default active state for OPCGroups created using
Groups.Add.


#### _property_ DefaultGroupLocaleID()
> (Read/Write) This property provides the default locale for OPCGroups created using

Groups.Add.


#### _property_ DefaultGroupTimeBias()

#### _property_ DefaultGroupUpdateRate()
(Read/Write) This property provides the default update rate (in milliseconds) for OPCGroups
created using Groups.Add. This property defaults to 1000 milliseconds (1 second).


#### GetOPCGroup(ItemSpecifier)
Returns an OPCGroup by ItemSpecifier.
:param ItemSpecifier:   ItemSpecifier is either the OPCGroup’s ServerHandle, or the name of

> an OPCGroup. Use Item to reference by index.


#### Item(ItemSpecifier)

* **Returns**

    Returns an OPCGroup by ItemSpecifier. ItemSpecifier is the name or 1-based index into the


collection. Use GetOPCGroup to reference by ServerHandle.
Item is the default method for OPCGroups.


#### _property_ Parent()
(Read-only) Returns reference to the parent OPCServer object


#### Remove(ItemSpecifier)
Removes an OPCGroup by Key.
:param ItemSpecifier:   ItemSpecifier is either the OPCGroup’s ServerHandle, or the name of

> an OPCGroup. Use Item to reference by index.


#### RemoveAll()
Removes all current OPCGroup and OPCItem objects to prepare for server shutdown


#### RemovePublicGroup(ItemSpecifier)
Removes the OPCGroup specified by ItemSpecifier.
:param ItemSpecifier:   The ServerHandle returned by ConnectPublicGroup, or the name of a

> Public OPCGroup.

## Structs.OPCItem module


### _class_ Structs.OPCItem.OPCItem(comObject)
Bases: [`IOPCItem`](Interfaces.md#Interfaces.IOPCItem.IOPCItem)

An OPC Item represents a connection to data sources within the server. Associated with each item
is a Value, Quality and Time Stamp. The value is in the form of a VARIANT, and the Quality is
similar to that specified by Fieldbus.


#### _property_ AccessPath()
(Read-only) The access path specified by the client on the Add function..


#### _property_ AccessRights()
(Read-only) Returns the access rights of this item.


#### _property_ CanonicalDataType()
(Read-only) Returns the native data type in the server.


#### _property_ ClientHandle()
(Read/Write) A Long value associated with the OPCItem. Its purpose is for the client to quickly
locate the destination of data. The handle is typically an index, etc. This handle will be returned to
the client along with data or status changes by OPCGroup events.


#### _property_ EUInfo()
(Read-only) Variant that contains the Engineering Units information


#### _property_ EUType()
(Read-only) Indicate the type of Engineering Units (EU) information (if any) contained in EUInfo.


#### _property_ IsActive()
(Read/Write) State of the Data Acquisition for this item.


#### _property_ ItemID()
(Read-only) The unique identifier for this item.


#### _property_ Parent()
Read-only) Returns reference to the parent OPCGroup object.


#### _property_ Quality()
(Read-only) Returns the latest quality read from the server.


#### Read(Source)
Read makes a blocking call to read this item from the server.
Read can be called with only a source (either OPCCache or OPCDevice) to refresh the item’s
value, quality and timestamp properties. If the value, quality and timestamp must be in sync, this
method’s optional parameters return values that were acquired together.


* **Parameters**

    **Source** – The ‘data source’; OPC_DS_CACHE or OPC_DS_DEVICE


:type Source    int
:return:        (Value, Quality, TimeStamp)

> Value       –  Returns the latest value read from the server
> Quality     –  Returns the latest value read from the server
> TimeStamp   –  Returns the latest timestamp read from the server.


* **Return type**

    (tuple, tuple, tuple)



#### _property_ RequestedDataType()
(Read/Write) The data type in which the item’s value will be returned. Note that if the requested
data type was rejected the OPCItem will be invalid(failed), until the RequestedDataType is set to
a valid value.


#### _property_ ServerHandle()
(Read-only) The server assigned handle for the AnOPCItem. The ServerHandle is a Long that
uniquely identifies this AnOPCItem. The client must supply this handle to some of the methods
that operate on OPCItem objects (such as OPCItems.Remove).


#### _property_ TimeStamp()
(Read-only) Returns the latest timestamp read from the server.


#### _property_ Value()
(Read-only) Returns the latest value read from the server. This is the default property of
AnOPCItem.


#### Write(Value)
Write makes a blocking call to write this value to the server.
:param Value:   Value to be written to the data source.

## Structs.OPCItems module


### _class_ Structs.OPCItems.OPCItems(comObject)
Bases: [`IOPCItems`](Interfaces.md#Interfaces.IOPCItems.IOPCItems)

This object also has properties for OPCItem defaults. When an OPCItem is added, the
DefaultXXXX properties set its initial state. The defaults can be changed to add OPCItems with
different initial states. Of course, once an OPCItem is added, its properties can be modified. This
reduces the number of parameters required to call the Add method.


#### AddItem(ItemID, ClientHandle)
Creates a new OPCItem object and adds it to the collection. The properties of this new OPCItem
are determined by the current defaults in the OPCItems collection object. After an OPCItem is
added, its properties can also be modified.


* **Parameters**

    
    * **ItemID** (*str*) – Fully Qualified ItemID


    * **ClientHandle** (*int*) – Client handle that will be returned with the



#### AddItems(Count, ItemIDs, ClientHandles)
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

> ServerHandles   –  Array of server item handles for the items processed
> Errors          –  Array of Long’s indicating the success of the individual items

> > operation.


* **Return type**

    (Tuple[int], Tuple[int])



#### _property_ Count()
(Read-only) Required property for collections
:rtype: int


#### _property_ DefaultAccessPath()
(Read/Write) The default AccessPath that will be used in calls to Add. This property defaults to
“”
:rtype: str


#### _property_ DefaultIsActive()
(Read/Write) The default active state that will be used in calls to Add. This property defaults to
True.
:rtype: bool


#### _property_ DefaultRequestedDataType()
(Read/Write) The requested data type that will be used in calls to Add. This property defaults to
VT_EMPTY (which means the server sends data in the server canonical data type).
:rtype: int


#### GetOPCItem(ServerHandle)
Returns an OPCItem by ServerHandle returned by Add. Use the Item property to reference by
index.
:param ServerHandle:    ServerHandle is the OPCItem’s ServerHandle

> Use Item to reference by index.


#### Item(ItemSpecifier)
Required property for collections


* **Parameters**

    **ItemSpecifier** (*int*) – Returns an OPCItem by ItemSpecifier. ItemSpecifier is the 1-based
    index into the collection



#### _property_ Parent()
(Read-only) Returns reference to the parent OPCGroup object.


#### Remove(Count, ServerHandles)
Removes an OPCItem


* **Parameters**

    
    * **Count** (*int*) – The number of items to be removed


    * **ServerHandles** (*Tuple**[**int**]*) – Array of server item handles for the items processed



* **Returns**

    Errors – Array of Long’s indicating the success of the individual items
    operation.



* **Return type**

    Tuple[int]



#### SetActive(Count, ServerHandles, ActiveState)
Allows Activation and deactivation of individual OPCItem’s in the OPCItems Collection


* **Parameters**

    
    * **Count** (*int*) – The number of items to be affected


    * **ServerHandles** (*Tuple**[**int**]*) – Array of server item handles for the items processed


    * **ActiveState** – TRUE if items are to be activated. FALSE if items are to be
    deactivated.



* **Returns**

    Errors – Array of Long’s indicating the success of the individual items
    operation.



* **Return type**

    Tuple[int]



#### SetClientHandles(Count, ServerHandles, ClientHandles)
Changes the client handles or one or more Items in a Group.


* **Parameters**

    
    * **Count** (*int*) – The number of items to be affected


    * **ServerHandles** (*Tuple**[**int**]*) – Array of server item handles for the items processed


    * **ClientHandles** (*Tuple**[**int**]*) – Array of new Client item handles to be stored. The Client
    handles do not need to be unique.



* **Returns**

    Errors – Array of Long’s indicating the success of the individual items
    operation.



* **Return type**

    Tuple[int]



#### SetDataType(Count, ServerHandles, RequestedDataTypes)
Changes the requested data type for one or more Items


* **Parameters**

    
    * **Count** (*int*) – The number of items to be affected


    * **ServerHandles** (*Tuple**[**int**]*) – Array of server item handles for the items processed


    * **RequestedDataTypes** (*Tuple**[**int**]*) – Array of new Requested DataTypes to be stored.



* **Returns**

    Errors – Array of Long’s indicating the success of the individual items
    operation.



* **Return type**

    Tuple[int]



#### Validate(Count, ItemIDs)
Determines if one or more OPCItems could be successfully created via the Add method (but does
not add them).


* **Parameters**

    
    * **Count** (*int*) – The number of items to be affected


    * **ItemIDs** (*Tuple**[**str**]*) – Array of Fully Qualified ItemID’s



* **Returns**

    Errors – Array of Long’s indicating the success of the individual items
    operation.



* **Return type**

    Tuple[int]


## Structs.OPCServer module


### _class_ Structs.OPCServer.OPCServer(comObject)
Bases: [`IOPCServer`](Interfaces.md#Interfaces.IOPCServer.IOPCServer)

A client creates the OPCServer Automation object. The client then ‘connects’ it to an OPC Data
Access Custom Interface (see the ‘Connect’ method). The OPCServer object can now be used to
obtain general information about an OPC server and to create and manipulate the collection of
OPCGroup objects.


#### _property_ BandWidth()
(Read-only) This is server specific. The suggested use is the server’s bandwidth as a percentage of
available bandwidth. This value will be hFFFFFFFF when the server cannot calculate a
bandwidth. When you access this property, you will get the value that the automation server has
obtained from the custom server via the GetStatus () interface.


#### BindCallback(CallbackClass)
Binds Callback Class to object
:type CallbackClass: IServerShutDownEvent


#### _property_ BuildNumber()
(Read-only) Returns the build number of the server. When you access this property, you will get
the value that the automation server has obtained from the custom server via the GetStatus ()
interface.


#### _property_ ClientName()
(Read/Write) This property allows the client to optionally register a client name with the server.
This is included primarily for debugging purposes. The recommended behavior is that the client
set his Node name and EXE name here.


#### Connect(ProgID, Node='localhost')
Must be called to establish connection to an OPC Data Access Server (that implements the
custom interface).


* **Parameters**

    
    * **ProgID** (*str*) – The ProgID is a string that uniquely identifies the registered real OPC Data Access
    Server (that implements the custom interface).


    * **Node** (*str*) – The Node name can specify another computer to connect using DCOM.



* **Return type**

    None



#### CreateBrowser()
Creates an OPCBrowser object


#### _property_ CurrentTime()
(Read-only) Returns the current time from the server. When you access this property, you will get
the value that the automation server has obtained from the custom server via the GetStatus ()
interface.


#### Disconnect()
Disconnects from the OPC server.
:rtype: None


#### GetErrorString(ErrorCode)
Converts an error number to a readable string. The server will return the string in the Locale that is
specified in the server level LocaleID property. Refer to the properties of the OPC Server for
setting and getting the LocaleID property.


* **Parameters**

    **ErrorCode** (*int*) – Server specific error code that the client application had returned from an interface
    function from the server, and for which the client application is requesting the server’s
    textual representation.



* **Return type**

    str



#### GetOPCServers(Node='localhost')

* **Parameters**

    **Node** (*str*) – The Node name provides the mechanism to specify the remote node where you want the
    automation server to give you the list of all the registered OPC servers.



* **Return type**

    Tuple[str]



* **Returns**

    Returns the names (ProgID’s) of the registered OPC Servers. Use one of these ProgIDs in the
    Connect method. The names are returned as an array of strings



#### _property_ LastUpdateTime()
(Read-only) Returns the last update time from the server. When you access this property, you will
get the value that the automation server has obtained from the custom server via the GetStatus()
interface.


#### _property_ LocaleID()
(Read/Write) This property identifies the locale, which may be used to localize strings returned
from the server. . This LocaleID will be used by the GetErrorString method on this interface


#### _property_ MajorVersion()
(Read-only) Returns the major part of the server version number (e.g. the “1” in version 1.32).
When you access this property, you will get the value that the automation server has obtained from
the custom server via the GetStatus() interface


#### _property_ MinorVersion()
(Read-only) Returns the minor part of the server version number (e.g. the “32” in version 1.32).
When you access this property, you will get the value that the automation server has obtained from
the custom server via the GetStatus () interface.


#### _property_ OPCGroups()
(Read only) A collection of OPCGroup objects. This is the default property of the OPCServer
object.


#### _property_ PublicGroupNames()
(Read-only) Returns the names of this server’s Public Groups. These names can be used in
ConnectPublicGroup. The names are returned as an array of strings.


#### QueryAvailableLocaleIDs()

* **Return type**

    Tuple[int]



* **Returns**

    Return the available LocaleIDs for this server/client session. The LocaleIDs are returned as an
    array of longs.



#### QueryAvailableProperties(ItemID)
Return a list of ID codes and Descriptions for the available properties for this ItemID. This list
may differ for different ItemIDs. This list is expected to be relatively stable for a particular
ItemID. That is, it could be affected from time to time by changes to the underlying system’s
configuration.


* **Parameters**

    **ItemID** (*str*) – The ItemID for which the caller wants to know the
    available properties



* **Return type**

    (int, Tuple[int], Tuple[str], Tuple[int])



* **Returns**

    (Count, PropertyIDs, Descriptions, DataTypes)
    Count           –  The number of properties returned
    PropertyIDs     –  DWORD ids for the returned properties. These IDs can

    > be passed to GetItemProperties or LookupItemIDs

    Descriptions    –  A brief vendor supplied text Description of each

        Property. NOTE LocalID does not apply to Descriptions




#### _property_ ServerName()
(Read-only) Returns the server name of the server that the client connected to via Connect().


#### _property_ ServerNode()
(Read-only) Returns the node name of the server that the client connected to via Connect(). When
you access this property, you will get the value that the automation server has cached locally.


#### _property_ ServerState()
(Read-only) Returns the server’s state, which will be one of the OPCServerState values

OPC_STATUS_RUNNING  –  The server is running normally. This is the usual state for a server
OPC_STATUS_FAILED   –  A vendor specific fatal error has occurred within the server. The

> server is no longer functioning. The recovery procedure from this
> situation is vendor specific. An error code of E_FAIL should
> generally be returned from any other server method.

OPC_STATUS_NOCONFIG –  The server is running but has no configuration information loaded

    and thus cannot function normally. Note this state implies that the
    server needs configuration information in order to function.
    Servers which do not require configuration information should
    not return this state.

OPC_STATUS_SUSPENDED – The server has been temporarily suspended via some vendor

    specific method and is not getting or sending data. Note that Quality will be returned as
    OPC_QUALITY_OUT_OF_SERVICE.

OPC_STATUS_TEST      – The server is in Test Mode. The outputs are disconnected from

    the real hardware but the server will otherwise behave normally.
    Inputs may be real or may be simulated depending on the vendor
    implementation. Quality will generally be returned normally


#### _property_ StartTime()
(Read-only) Returns the time the server started running. This is the start time of the server that the
client has specified to connect to. Multiple Clients connecting to the same server can be assured
that each client will read the same value from the server for this property.


#### _property_ VendorInfo()
(Read-only) Returns the vendor information string for the server. When you access this property,
you will get the value that the automation server has obtained from the custom server via the
GetStatus () interface.


### Structs.OPCServer.connect(serverName, host='localhost')

* **Return type**

    `OPCServer`


## Module contents
