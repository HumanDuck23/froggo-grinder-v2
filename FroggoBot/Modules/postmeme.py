from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Buttons
import random
import time

class PostMeme(modulebase.ModuleBase):
    def onMessage(self, message):
        for embed in message["embeds"]:
            if embed["description"] is not None:
                if embed["description"].lower().count("pick a meme"):
                    time.sleep(random.randint(1, 2))
                    Buttons.clickButton(self.froggo, random.choice((Buttons.parseButtons(message["components"]))), message)
