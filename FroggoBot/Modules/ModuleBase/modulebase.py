class ModuleBase:
    def __init__(self, config):
        self.config = config

    def onMessage(self, message):
        pass

    def onMessageEdit(self, oldMessage, newMessage):
        pass
