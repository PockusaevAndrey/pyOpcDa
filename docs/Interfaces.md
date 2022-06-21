# Interfaces package

## Submodules

## Interfaces.IOPCBase module


### _class_ Interfaces.IOPCBase.IOPCBase()
Bases: `object`

## Interfaces.IOPCBrowser module


### _class_ Interfaces.IOPCBrowser.IOPCBrowser(comObject)
Bases: [`OPCBase`](Structs.md#Structs.OPCBase.OPCBase)


#### _property_ AccessRights()
(Read/Write) The requested access rights that apply to the ShowLeafs methods. This property
defaults to OPCReadable OR’src with OPCWritable (that is, everything). This property applies to
the filtering, i.e. you only want the leafs with these AccessRights.


#### _property_ Count()
(Read-only) Required property for collections. Returns the number of items in the
collection.


#### _property_ CurrentPosition()
(Read-only) Current position in the tree. This string will be “” (i.e. the “root”) initially. It will
always be “” if Organization is OPCFlat.


#### _property_ DataType()
(Read/Write) The requested data type that applies to ShowLeafs methods. This property defaults to
VT_EMPTY, which means that any data type is acceptable.


#### _property_ Filter()
(Read/Write) The filter that applies to ShowBranches and ShowLeafs methods. This property
defaults to “” (no filtering). Servers may use this filter to narrow the list of names. Servers are
recommended to support wildcards such as “\*”.


#### GetAccessPaths(ItemID)
Returns the strings that are legal AccessPaths for this ItemID. May be Null if there are no
AccessPaths for this ItemID or the server does not support them.


* **Parameters**

    **ItemID** (*str*) – Fully Qualified ItemID



* **Returns**

    


#### GetItemID(Leaf)

#### Item(ItemSpecifier)

#### MoveDown(Branch)

#### MoveTo(Branches)

#### MoveToRoot()

#### MoveUp()

#### _property_ Organization()
(Read-only) Returns either OPCHierarchical or OPCFlat.


#### ShowBranches()

#### ShowLeafs(Flat=False)
## Interfaces.IOPCGroup module


### _class_ Interfaces.IOPCGroup.IOPCGroup(comObject)
Bases: [`OPCBase`](Structs.md#Structs.OPCBase.OPCBase)


#### AsyncCancel(CancelID)

#### AsyncRead(NumItems, ServerHandles, TransactionID)

#### AsyncRefresh(Source, TransactionID)

#### AsyncWrite(NumItems, ServerHandles, Values, TransactionID)

#### SyncRead(Source, NumItems, ServerHandles)

#### SyncWrite(NumItems, ServerHandles, Values)
## Interfaces.IOPCGroups module


### _class_ Interfaces.IOPCGroups.IOPCGroups(comObject)
Bases: [`OPCBase`](Structs.md#Structs.OPCBase.OPCBase)


#### Add(Name)

#### ConnectPublicGroup(Name)

#### GetOPCGroup(ItemSpecifier)

#### Item(ItemSpecifier)

#### Remove(ItemSpecifier)

#### RemoveAll()

#### RemovePublicGroup(ItemSpecifier)
## Interfaces.IOPCItem module


### _class_ Interfaces.IOPCItem.IOPCItem(comObject)
Bases: [`OPCBase`](Structs.md#Structs.OPCBase.OPCBase)


#### Read(Source)

#### Write(Value)
## Interfaces.IOPCItems module


### _class_ Interfaces.IOPCItems.IOPCItems(comObject)
Bases: [`OPCBase`](Structs.md#Structs.OPCBase.OPCBase)


#### AddItem(ItemID, ClientHandle)

#### AddItems(Count, ItemIDs, ClientHandles)

#### GetOPCItem(ServerHandle)

#### Item(ItemSpecifier)

#### Remove(Count, ServerHandles)

#### SetActive(Count, ServerHandles, ActiveState)

#### SetClientHandles(Count, ServerHandles, ClientHandles)

#### SetDataType(Count, ServerHandles, RequestedDataTypes)

#### Validate(Count, ItemIDs)
## Interfaces.IOPCServer module


### _class_ Interfaces.IOPCServer.IOPCServer(comObject)
Bases: [`OPCBaseServer`](Structs.md#Structs.OPCBase.OPCBaseServer)


#### BindCallback(CallbackClass)

#### Connect(ProgID, Node='localhost')

#### CreateBrowser()

#### Disconnect()

#### GetErrorString(ErrorCode)

#### GetItemProperties()
not realize
Return a list of the current data values for the passed ID codes.
:return:


#### GetOPCServers(Node='localhost')

#### LookupItemIDs()
no realize
Return a list of ItemIDs (if available) for each of the passed ID codes. These indicate the ItemID,
which could be added to an OPCGroup and used for more efficient access to the data
corresponding to the Item Properties. An error within the error array may indicate that the passed
Property ID is not defined for this item.
:return:


#### QueryAvailableLocaleIDs()

#### QueryAvailableProperties(ItemID)
## Module contents
