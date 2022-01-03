from FroggoBot.Modules import *

import threading
import discum
import json


class Froggo:
    def __init__(self):
        self.modules = {
            "autobox": autobox.AutoBox(self),
            "autobuy": autobuy.AutoBuy(self),
            "autogift": autogift.AutoGift(self),
            "automoney": automoney.AutoMoney(self),
            "autopizza": autopizza.AutoPizza(self),
            "balancecheck": balancecheck.BalanceCheck(self),
            "beg": beg.Beg(self),
            "crime": crime.Crime(self),
            "dig": dig.Dig(self),
            "fish": fish.Fish(self),
            "highlow": highlow.HighLow(self),
            "hunt": hunt.Hunt(self),
            "postmeme": postmeme.PostMeme(self),
            "scratch": scratch.Scratch(self),
            "search": search.Search(self),
            "snakeeyes": snakeeyes.SnakeEyes(self),
            "work": work.Work(self)
        }

        # load modules from conf
        self.config = json.loads(open("config.json", "r").read())
        for module in self.config["modules"].keys():
            if not self.config["modules"][module]:
                del self.modules[module]

        # discum bot
        self.bot = discum.Client(token=self.config["bot"]["token"], log=False)
        self.active = False
        self.paused = False

        @self.bot.gateway.command
        def a(msg):
            if msg.raw["t"] == "MESSAGE_CREATE":
                msg = msg.parsed.auto()
                for module in self.modules.keys():
                    self.modules[module].onMessage(msg)

        # threads
        self.roundThread = None
        self.botGatewayThread = threading.Thread(target=self.bot.gateway.run)
        self.botGatewayThread.start()
    