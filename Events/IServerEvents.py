from abc import abstractmethod, ABCMeta


class IServerShutDownEvent(metaclass=ABCMeta):
    @abstractmethod
    def OnServerShutDown(self, ServerReason):
        """
        The ServerShutDown event is fired when the server is planning on shutting down and wants to tell
        all the active clients to release any resources. The client provides this method so that the server can
        request that the client disconnect from the server. The client should remove all groups and items.

        :param ServerReason:    An optional text string provided by the server indicating the reason
                                for the shutdown.
        :type ServerReason:     str
        """
        pass
