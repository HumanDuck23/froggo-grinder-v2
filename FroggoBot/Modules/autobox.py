from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Messages, Scheduler
import re


class AutoBox(modulebase.ModuleBase):
    def __init__(self, froggo):
        super().__init__(froggo)
        self.justRequestedDai = False

    def onMessage(self, message):
        if message["embeds"]:
            for embed in message["embeds"]:
                if list(embed.keys()).count("title") and embed["title"].count("Daily Box") and self.justRequestedDai:
                    owned = int(re.search(r"\*\*Daily Box\*\* \(([0-9]*) owned\)", embed["title"]).group(1))
                    if owned:
                        Messages.sendMessage(self.froggo, "pls use dai")
                        self.froggo.paused = False
                        Scheduler.setTimeout(self.useBox, 600000) # use the next box in 10 mins

    def useBox(self):
        self.froggo.paused = True
        Messages.sendMessage(self.froggo, "pls item dai")