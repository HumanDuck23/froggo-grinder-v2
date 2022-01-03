from FroggoBot.Modules import *
from FroggoBot.Tools import *

import threading
import discum
import time
import json


class Froggo:
    def __init__(self):
        # read and parse config
        self.config = json.loads(open("config.json", "r").read())

        self.modules = {
            "autobox": AutoBox(self),
            "autobuy": AutoBuy(self),
            "autogift": AutoGift(self),
            "automoney": AutoMoney(self),
            "autopizza": AutoPizza(self),
            "balancecheck": BalanceCheck(self),
            "beg": Beg(self),
            "crime": Crime(self, self.config["priority"]["crime"]),
            "dig": Dig(self),
            "fish": Fish(self),
            "highlow": HighLow(self),
            "hunt": Hunt(self),
            "postmeme": PostMeme(self),
            "scratch": Scratch(self),
            "search": Search(self, self.config["priority"]["search"]),
            "snakeeyes": SnakeEyes(self),
            "work": Work(self)
        }

        # load modules from conf
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

    def start(self):
        self.active = True
        Messages.sendMessage(self, "pls scratch 1k")

    def stop(self):
        self.active = False

    def pause(self):
        self.paused = True
