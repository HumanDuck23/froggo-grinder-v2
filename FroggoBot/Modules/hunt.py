from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Buttons, Messages, Logger
import random
import time


class Hunt(modulebase.ModuleBase):
    def onMessage(self, message):
        if message["content"].count("Dodge the Fireball") and message["components"] != []:
            # dragon
            time.sleep(random.randint(1, 2))
            nMsg = Messages.getMessage(self.froggo, message["id"])
            spaces = nMsg["content"].split("\n")[2].count(" ")
            buttons = Buttons.parseButtons(nMsg["components"])
            if spaces == 7:
                Buttons.clickButton(self.froggo, buttons[random.choice([0, 2])], nMsg)
            elif spaces > 7:
                Buttons.clickButton(self.froggo, buttons[random.choice([0, 1])], nMsg)
            else:
                Buttons.clickButton(self.froggo,  buttons[random.choice([1, 2])], nMsg)

            Logger.info("Caught dragon.")
