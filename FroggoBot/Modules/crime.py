from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Buttons, Messages


class Crime(modulebase.ModuleBase):
    def __init__(self, froggo, priority):
        super().__init__(froggo)
        self.priority = priority

    def onMessage(self, message):
        if message["content"].lower().count("what crime do you want to commit?"):
            btn = Buttons.getButtonWithPriority(self.priority, message)
            if Messages.isReplyToMe(self.froggo.bot, message):
                print("REEE")