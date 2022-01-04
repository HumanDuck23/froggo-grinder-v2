from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Buttons, Logger
import random
import time


class Scratch(modulebase.ModuleBase):
    def onMessage(self, message):
        for embed in message["embeds"]:
            if embed["description"] is not None:
                if embed["description"].lower().count("you can scratch"):
                    buttonList = Buttons.parseButtons(message["components"])
                    l = []
                    for i in range(3):
                        while True:
                            btn = random.choice(buttonList)
                            if l.count(btn) == 0:
                                l.append(btn)
                                break

                    x = 0
                    for button in l:
                        time.sleep(random.randint(1, 2))
                        Buttons.clickButton(self.froggo, button, message)
                        Logger.info("Scratched field #" + str(x))
                        x += 1
