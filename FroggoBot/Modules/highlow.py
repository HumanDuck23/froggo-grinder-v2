from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Buttons, Logger
import random
import time
import re


class HighLow(modulebase.ModuleBase):
    def onMessage(self, message):
        for embed in message["embeds"]:
            if list(embed.keys()).count("description"):
                if embed["description"].count("a secret number"):
                    hint = int(re.search(r"I just chose a secret number between 1 and 100\.\nIs the secret number \*higher\* or \*lower\* than \*\*([0-9]+)\*\*\.", embed["description"]).group(1))
                    buttons = Buttons.parseButtons(message["components"])
                    if hint:
                        if hint <= 45:
                            time.sleep(random.randint(1, 2))
                            Buttons.clickButton(self.froggo, buttons[2], message)
                            Logger.info("Pressed " + buttons[2]["label"] + ".")
                        elif hint >= 55:
                            time.sleep(random.randint(1, 2))
                            Buttons.clickButton(self.froggo, buttons[0], message)
                            Logger.info("Pressed " + buttons[0]["label"] + ".")
                        else:
                            time.sleep(random.randint(1, 2))
                            btn = random.choice(buttons)
                            Buttons.clickButton(self.froggo, btn, message)
                            Logger.info("Pressed " + btn["label"] + ".")
                    else:
                        time.sleep(random.randint(1, 2))
                        btn = random.choice(buttons)
                        Buttons.clickButton(self.froggo, btn, message)
                        Logger.info("Pressed " + btn["label"] + ".")
