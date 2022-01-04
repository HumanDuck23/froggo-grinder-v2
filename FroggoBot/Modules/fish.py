from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Buttons, Messages, Logger
import random
import time


class Fish(modulebase.ModuleBase):
    def onMessage(self, message):
        if message["content"].count("Catch the fish!") and message["components"] != []:
            # kraken or legendary fish
            time.sleep(random.randint(1, 2))
            nMsg = Messages.getMessage(self.froggo, message["id"])
            spaces = nMsg["content"].split("\n")[1].count(" ")
            buttons = Buttons.parseButtons(nMsg["components"])
            if spaces == 7:
                Buttons.clickButton(self.froggo, buttons[1], nMsg)
            elif spaces > 7:
                Buttons.clickButton(self.froggo, buttons[2], nMsg)
            else:
                Buttons.clickButton(self.froggo, buttons[0], nMsg)
            Logger.info("Caught kraken/legendary fish.")