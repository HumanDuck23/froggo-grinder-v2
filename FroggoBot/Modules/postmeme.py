from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Buttons, Logger
import random
import time


class PostMeme(modulebase.ModuleBase):
    def onMessage(self, message):
        for embed in message["embeds"]:
            if list(embed.keys()).count("description"):
                if embed["description"].lower().count("pick a meme"):
                    time.sleep(random.randint(1, 2))
                    btn = random.choice((Buttons.parseButtons(message["components"])))
                    Buttons.clickButton(self.froggo, btn, message)
                    Logger.info("Posted a meme: " + btn["label"] + ".")
