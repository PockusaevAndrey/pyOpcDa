import win32com.client
import win32com.server.util
from typing import Tuple
from Structs.OPCBrowser import OPCBrowser
from Structs.OPCGroups import OPCGroups
from Interfaces.IOPCServer import IOPCServer
from Events.IServerEvents import IServerShutDownEvent
import pywintypes

pywintypes.datetime = pywintypes.TimeType


class OPCServer(IOPCServer):
    """
    A client creates the OPCServer Automation object. The client then 'connects' it to an OPC Data
    Access Custom Interface (see the 'Connect' method). The OPCServer object can now be used to
    obtain general information about an OPC server and to create and manipulate the collection of
    OPCGroup objects.
    """

    @property
    def StartTime(self):
        """
        (Read-only) Returns the time the server started running. This is the start time of the server that the
        client has specified to connect to. Multiple Clients connecting to the same server can be assured
        that each client will read the same value from the server for this property.
        """
        return self._object.StartTime

    @property
    def CurrentTime(self):
        """
        (Read-only) Returns the current time from the server. When you access this property, you will get
        the value that the automation server has obtained from the custom server via the GetStatus ()
        interface.
        """
        return self._object.CurrentTime

    @property
    def LastUpdateTime(self):
        """
            (Read-only) Returns the last update time from the server. When you access this property, you will
            get the value that the automation server has obtained from the custom server via the GetStatus()
            interface.
            """
        return self._object.LastUpdateTime

    @property
    def MajorVersion(self):
        """
        (Read-only) Returns the major part of the server version number (e.g. the “1” in version 1.32).
        When you access this property, you will get the value that the automation server has obtained from
        the custom server via the GetStatus() interface
        """
        return self._object.MajorVersion

    @property
    def MinorVersion(self):
        """
        (Read-only) Returns the minor part of the server version number (e.g. the “32” in version 1.32).
        When you access this property, you will get the value that the automation server has obtained from
        the custom server via the GetStatus () interface.
        """
        return self._object.MinorVersion

    @property
    def BuildNumber(self):
        """
        (Read-only) Returns the build number of the server. When you access this property, you will get
        the value that the automation server has obtained from the custom server via the GetStatus ()
        interface.
        """
        return self._object.BuildNumber

    @property
    def VendorInfo(self):
        """
    (Read-only) Returns the vendor information string for the server. When you access this property,
    you will get the value that the automation server has obtained from the custom server via the
    GetStatus () interface.
    """
        return self._object.VendorInfo

    @property
    def ServerState(self):
        """
    (Read-only) Returns the server’s state, which will be one of the OPCServerState values

    OPC_STATUS_RUNNING  --  The server is running normally. This is the usual state for a server
    OPC_STATUS_FAILED   --  A vendor specific fatal error has occurred within the server. The
                            server is no longer functioning. The recovery procedure from this
                            situation is vendor specific. An error code of E_FAIL should
                            generally be returned from any other server method.
    OPC_STATUS_NOCONFIG --  The server is running but has no configuration information loaded
                            and thus cannot function normally. Note this state implies that the
                            server needs configuration information in order to function.
                            Servers which do not require configuration information should
                            not return this state.
    OPC_STATUS_SUSPENDED -- The server has been temporarily suspended via some vendor
                            specific method and is not getting or sending data. Note that Quality will be returned as
                            OPC_QUALITY_OUT_OF_SERVICE.
    OPC_STATUS_TEST      -- The server is in Test Mode. The outputs are disconnected from
                            the real hardware but the server will otherwise behave normally.
                            Inputs may be real or may be simulated depending on the vendor
                            implementation. Quality will generally be returned normally
    """
        return self._object.ServerState

    @property
    def LocaleID(self):
        """
    (Read/Write) This property identifies the locale, which may be used to localize strings returned
    from the server. . This LocaleID will be used by the GetErrorString method on this interface
    """
        return self._object.LocaleID

    @LocaleID.setter
    def LocaleID(self, x):
        self._object.LocaleID = x

    @property
    def BandWidth(self):
        """
    (Read-only) This is server specific. The suggested use is the server’s bandwidth as a percentage of
    available bandwidth. This value will be hFFFFFFFF when the server cannot calculate a
    bandwidth. When you access this property, you will get the value that the automation server has
    obtained from the custom server via the GetStatus () interface.
    """
        return self._object.BandWidth

    @property
    def OPCGroups(self):
        """
    (Read only) A collection of OPCGroup objects. This is the default property of the OPCServer
    object.
    """
        return OPCGroups(self._object.OPCGroups)

    @property
    def PublicGroupNames(self):
        """
    (Read-only) Returns the names of this server’s Public Groups. These names can be used in
    ConnectPublicGroup. The names are returned as an array of strings.
    """
        return self._object.PublicGroupNames

    @property
    def ServerName(self):
        """
    (Read-only) Returns the server name of the server that the client connected to via Connect().
    """
        return self._object.ServerName

    @property
    def ServerNode(self):
        """
    (Read-only) Returns the node name of the server that the client connected to via Connect(). When
    you access this property, you will get the value that the automation server has cached locally.
    """
        return self._object.ServerNode

    @property
    def ClientName(self):
        """
    (Read/Write) This property allows the client to optionally register a client name with the server.
    This is included primarily for debugging purposes. The recommended behavior is that the client
    set his Node name and EXE name here.
    """
        return self._object.ClientName

    @ClientName.setter
    def ClientName(self, x):
        self._object.ClientName = x

    def GetOPCServers(self, Node="localhost"):
        """
        :param Node:    The Node name provides the mechanism to specify the remote node where you want the
                        automation server to give you the list of all the registered OPC servers.
        :type Node:     str
        :rtype:         Tuple[str]
        :return:        Returns the names (ProgID’s) of the registered OPC Servers. Use one of these ProgIDs in the
                        Connect method. The names are returned as an array of strings
        """
        return self._object.GetOPCServers(Node)

    def Connect(self, ProgID, Node='localhost'):
        """
        Must be called to establish connection to an OPC Data Access Server (that implements the
        custom interface).

        :param ProgID:  The ProgID is a string that uniquely identifies the registered real OPC Data Access
                        Server (that implements the custom interface).
        :type ProgID:   str
        :param Node:    The Node name can specify another computer to connect using DCOM.
        :type Node: str
        :rtype: None
        """
        self._object.Connect(ProgID, Node)

    def Disconnect(self):
        """
        Disconnects from the OPC server.
        :rtype: None
        """
        self._object.Disconnect()

    def CreateBrowser(self):
        """
        Creates an OPCBrowser object
        """
        return OPCBrowser(self._object.CreateBrowser())

    def GetErrorString(self, ErrorCode):
        """
        Converts an error number to a readable string. The server will return the string in the Locale that is
        specified in the server level LocaleID property. Refer to the properties of the OPC Server for
        setting and getting the LocaleID property.

        :param ErrorCode:   Server specific error code that the client application had returned from an interface
                            function from the server, and for which the client application is requesting the server’s
                            textual representation.
        :type ErrorCode:    int
        :rtype:             str
        """
        return self._object.GetErrorString(ErrorCode)

    def QueryAvailableLocaleIDs(self):
        """
        :rtype:     Tuple[int]
        :return:    Return the available LocaleIDs for this server/client session. The LocaleIDs are returned as an
                    array of longs.
        """
        return self._object.QueryAvailableLocaleIDs()

    def QueryAvailableProperties(self, ItemID):
        """
        Return a list of ID codes and Descriptions for the available properties for this ItemID. This list
        may differ for different ItemIDs. This list is expected to be relatively stable for a particular
        ItemID. That is, it could be affected from time to time by changes to the underlying system’s
        configuration.

        :param ItemID:  The ItemID for which the caller wants to know the
                        available properties
        :type ItemID:   str

        :rtype:         (int, Tuple[int], Tuple[str], Tuple[int])
        :return:        (Count, PropertyIDs, Descriptions, DataTypes)
                        Count           --  The number of properties returned
                        PropertyIDs     --  DWORD ids for the returned properties. These IDs can
                                            be passed to GetItemProperties or LookupItemIDs
                        Descriptions    --  A brief vendor supplied text Description of each
                                            Property. NOTE LocalID does not apply to Descriptions
        """
        return self._object.QueryAvailableProperties(ItemID)

    def BindCallback(self, CallbackClass):
        """
        Binds Callback Class to object
        :type CallbackClass: IServerShutDownEvent
        """
        win32com.client.WithEvents(self._object, CallbackClass)


def connect(serverName, host='localhost') -> OPCServer:
    OPC_CLASS = 'Matrikon.OPC.Automation;Graybox.OPC.DAWrapper;HSCOPC.Automation;RSI.OPCAutomation;OPC.Automation'

    server = None
    for cls in OPC_CLASS.split(";"):
        try:
            server = OPCServer(win32com.client.gencache.EnsureDispatch(cls, 1))
            server.Connect(serverName, host)
            break

        except:
            pass

    return server
