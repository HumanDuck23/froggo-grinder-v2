from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Buttons, Messages
import random
import time




class Search(modulebase.ModuleBase):
    def __init__(self, froggo, priority):
        super().__init__(froggo)
        self.priority = priority

    def onMessage(self, message):
        if message["content"].lower().count("where do you want to search?"):
            btn = Buttons.getButtonWithPriority(self.priority, message)
            for button in btn:
                if Messages.isReplyToMe(self.froggo, message):
                    time.sleep(random.randint(1, 3))
                    Buttons.clickButton(self.froggo, button, message)