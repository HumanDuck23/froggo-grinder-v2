from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Messages, Scheduler, Logger
import re


class AutoPizza(modulebase.ModuleBase):
    def __init__(self, froggo):
        super().__init__(froggo)
        self.justRequestedPizza = False

    def onMessage(self, message):
        if message["embeds"]:
            for embed in message["embeds"]:
                if list(embed.keys()).count("title") and embed["title"].count("Pizza Slice") and self.justRequestedPizza:
                    owned = int(re.search(r"\*\*Pizza Slice\*\* \(([0-9]*) owned\)", embed["title"]).group(1))
                    if owned:
                        Messages.sendMessage(self.froggo, "pls use pizza")
                        self.froggo.paused = False
                        Scheduler.setTimeout(self.usePizza, 3.6e+6)  # use the next pizza in 1h
                        Logger.info("Used pizza, using again in 1 hour.")

    def usePizza(self):
        self.froggo.paused = True
        Messages.sendMessage(self.froggo, "pls item pizza")
