from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Messages, Logger


class AutoBuy(modulebase.ModuleBase):
    def onMessage(self, message):
        items = {
            "You don't have a fishing pole": "fishing",
            "You don't have a hunting rifle": "rifle",
            "oi you need to buy a laptop": "laptop",
            "You don't have a shovel": "shovel"
        }
        for e in items.keys():
            if message["content"].count(e) and Messages.isReplyToMe(self.froggo, message):
                Messages.sendMessage("pls buy " + items[e])
                Logger.info("Bought " + items[e] + ".")
