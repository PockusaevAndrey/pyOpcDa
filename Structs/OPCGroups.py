from typing import Union
import win32com.client
from Events.IGroupsEvents import *
from Interfaces.IOPCGroups import IOPCGroups
from Structs.OPCGroup import OPCGroup


class OPCGroups(IOPCGroups):
    """
    OPCGroups is a collection of OPCGroup objects, and the methods that create, remove, and
    manage them.
    This object also has properties for OPCGroup defaults. When OPCGroups are added, the
    DefaultGroupXXXX properties set its initial state. The defaults can be changed to add
    OPCGroups with different initial states. Changing the defaults does not affect groups that have
    already been created. Once an OPCGroup is added, its properties can be modified. This reduces
    the number of parameters required to call the Add method.
    """

    @property
    def Parent(self):
        """(Read-only) Returns reference to the parent OPCServer object"""
        return self._object.Parent

    @property
    def DefaultGroupIsActive(self):
        """
        (Read/Write) This property provides the default active state for OPCGroups created using
        Groups.Add.
        """
        return self._object.DefaultGroupIsActive

    @DefaultGroupIsActive.setter
    def DefaultGroupIsActive(self, value):
        self._object.DefaultGroupIsActive = value

    @property
    def DefaultGroupUpdateRate(self):
        """
        (Read/Write) This property provides the default update rate (in milliseconds) for OPCGroups
        created using Groups.Add. This property defaults to 1000 milliseconds (1 second).
        """
        return self._object.DefaultGroupUpdateRate

    @DefaultGroupUpdateRate.setter
    def DefaultGroupUpdateRate(self, value):
        self._object.DefaultGroupUpdateRate = value

    @property
    def DefaultGroupDeadband(self):
        """
        (Read/Write) This property provides the default deadband for OPCGroups created using
        Groups.Add. A deadband is expressed as percent of full scale (legal values 0 to 100).
        """
        return self._object.DefaultGroupDeadband

    @DefaultGroupDeadband.setter
    def DefaultGroupDeadband(self, value):
        self._object._DefaultGroupDeadband = value

    @property
    def DefaultGroupLocaleID(self):
        """
        (Read/Write) This property provides the default locale for OPCGroups created using
    Groups.Add.
        """
        return self._object.DefaultGroupLocaleID

    @DefaultGroupLocaleID.setter
    def DefaultGroupLocaleID(self, value):
        self._object.DefaultGroupLocaleID = value

    @property
    def DefaultGroupTimeBias(self):
        return self._object.DefaultGroupTimeBias

    @DefaultGroupTimeBias.setter
    def DefaultGroupTimeBias(self, value):
        self._object.DefaultGroupTimeBias = value

    @property
    def Count(self):
        return self._object.Count

    def Item(self, ItemSpecifier):
        """
        :type ItemSpecifier:    int
        :return: Returns an OPCGroup by ItemSpecifier. ItemSpecifier is the name or 1-based index into the
        collection. Use GetOPCGroup to reference by ServerHandle.
        Item is the default method for OPCGroups.
        """
        return OPCGroup(self._object.Item(ItemSpecifier))

    def Add(self, Name):
        """
        Creates a new OPCGroup object and adds it to the collection. The properties of this new group are
        determined by the current defaults in the OPCServer object. After a group is added, its properties
        can also be modified.
        :param Name:    Name of the group. The name must be unique among the other
                        groups created by this client. If no name is provided, The server-
                        generated name will also be unique relative to any existing groups.
        :type Name: str
        """
        return OPCGroup(self._object.Add(Name))

    def GetOPCGroup(self, ItemSpecifier):
        """
        Returns an OPCGroup by ItemSpecifier.
        :param ItemSpecifier:   ItemSpecifier is either the OPCGroup’s ServerHandle, or the name of
                                an OPCGroup. Use Item to reference by index.
        :type ItemSpecifier:    Union[str, int]
        """
        return OPCGroup(self._object.GetOPCGroup(ItemSpecifier))

    def Remove(self, ItemSpecifier):
        """
        Removes an OPCGroup by Key.
        :param ItemSpecifier:   ItemSpecifier is either the OPCGroup’s ServerHandle, or the name of
                                an OPCGroup. Use Item to reference by index.
        :type ItemSpecifier:    Union[str, int]
        """
        self._object.Remove(ItemSpecifier)

    def RemoveAll(self):
        """
        Removes all current OPCGroup and OPCItem objects to prepare for server shutdown
        """
        self._object.RemoveAll()

    def ConnectPublicGroup(self, Name):
        """
        Public Groups are pre-existing groups in a server. These groups can be connected rather than
        added..
        Refer to Appendix A - OPC Automation Error Handling for information on OPC Automation
        errors and Exceptions.
        :param Name: Name of group to be connected.
        :type Name: str
        """
        return OPCGroup(self._object.ConnectPublicGroup(Name))

    def RemovePublicGroup(self, ItemSpecifier):
        """
        Removes the OPCGroup specified by ItemSpecifier.
        :param ItemSpecifier:   The ServerHandle returned by ConnectPublicGroup, or the name of a
                                Public OPCGroup.
        :type ItemSpecifier:    Union[str, int]
        """

    def BindCallback(self, CallbackClass: IGlobalDataChange):
        """
        Binds Callback Class to object
        :type CallbackClass:
        """
        win32com.client.WithEvents(self._object, CallbackClass)
