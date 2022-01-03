from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Buttons


class Search(modulebase.ModuleBase):
    def __init__(self, froggo, priority):
        super().__init__(froggo)
        self.priority = priority

    def onMessage(self, message):
        if message["content"].lower().count("where do you want to search?"):
            btn = Buttons.getButtonWithPriority(self.priority, message)
