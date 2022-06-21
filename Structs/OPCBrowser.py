from Interfaces.IOPCBrowser import IOPCBrowser
from typing import Tuple


class OPCBrowser(IOPCBrowser):
    """
    The OPCBrowser object is a collection of branch or item names that exist in the server. Browsing
    is optional. If the server does not support browsing, CreateBrowser will not create this object.
    """

    def Item(self, ItemSpecifier):
        """
        Required property for collections. Returns a name indexed by ItemSpecifier. The name will be a
        branch or leaf name, depending on previous calls to ShowBranches or ShowLeafs. Item is the
        default for the OPCBrowser.
        :param ItemSpecifier:   1-based index into the collection
        :type ItemSpecifier:    int
        :rtype:               str
        """
        return self._object.Item(ItemSpecifier)

    def __call__(self, ItemSpecifier):
        """
        Same as Item
        :param ItemSpecifier:   1-based index into the collection
        :type ItemSpecifier:    int
        :return:
        :rtype:                 str
        """

        return self._object.Item(ItemSpecifier)

    def __iter__(self):
        return self._object.__iter__()

    def __next__(self):
        return self._object.__next__()

    def ShowBranches(self):
        """
        Fills the collection with names of the branches at the current browse position.
        """
        self._object.ShowBranches()

    def ShowLeafs(self, Flat=False):
        """
        Fills the collection with the names of the leafs at the current browse position. Default for Flat is
        FALSE.

        :param Flat:    Defines what the collection should contain.
                        The Settings for Flat are:
                        True    --  the collection is filled with all leafs at the current browse position, as
                                    well as all the leafs that are below the current browse position.
                                    Basically we are treated from the current position on down as a flat
                                    name space.
                        False   --  the collection is filled with all leafs at the current browse position
        :type Flat:     bool
        :rtype: None
        """
        self._object.ShowLeafs(Flat)

    def MoveUp(self):
        """
        Move up one level in the tree.
        :rtype: None
        """
        return self._object.MoveUp()

    def MoveToRoot(self):
        """
        Move up to the first level in the tree.
        :rtype: None
        """
        return self._object.MoveToRoot()

    def MoveDown(self, Branch):
        """
        Move down into this branch.
        :type Branch: str
        :rtype: None
        """
        return self._object.MoveDown(Branch)

    def MoveTo(self, Branches):
        """
        Move to an absolute position.

        :param Branches: Branches are an array of branch names from the root to a particular
                         position in the tree.
        :type Branches: Tuple[str]
        """
        return self._object.MoveTo(Branches)

    def GetItemID(self, Leaf):
        """
        Given a name, returns a valid ItemID that can be passed to OPCItems Add method.

        :param Leaf: The name of a BRANCH or LEAF at the current level.
        :type Leaf: str
        :rtype: str
        """
        return self._object.GetItemID(Leaf)
