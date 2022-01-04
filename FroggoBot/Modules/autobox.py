import time

from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Messages, Scheduler, Logger
import re


class AutoBox(modulebase.ModuleBase):
    def __init__(self, froggo):
        super().__init__(froggo)
        self.justRequestedDai = False

    def onMessage(self, message):
        if message["embeds"]:
            for embed in message["embeds"]:
                if list(embed.keys()).count("title") and embed["title"].count("Daily Box") and self.justRequestedDai:
                    self.justRequestedDai = False
                    owned = int(re.search(r"\*\*Daily Box\*\* \(([0-9]*) owned\)", embed["title"]).group(1))
                    print(owned)
                    if owned:
                        time.sleep(2)
                        Messages.sendMessage(self.froggo, "pls use dai")
                        self.froggo.paused = False
                        Scheduler.setTimeout(self.useBox, 600000) # use the next box in 10 mins
                        Logger.info("Used daily box, using again in 10 minutes.")
                    else:
                        self.froggo.paused = False

    def useBox(self):
        self.froggo.paused = True
        self.justRequestedDai = True
        Messages.sendMessage(self.froggo, "pls item dai")