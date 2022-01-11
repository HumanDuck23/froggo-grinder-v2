from FroggoBot.Modules import *
from FroggoBot.Tools import *

import threading
import random
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
                if msg["author"]["id"] == self.config["bot"]["dankID"] and msg["channel_id"] == self.config["bot"]["channelID"]:
                    for module in self.modules.keys():
                        self.modules[module].onMessage(msg)

        # threads
        self.roundThread = None
        self.botGatewayThread = threading.Thread(target=self.bot.gateway.run)
        self.botGatewayThread.start()

    def runRound(self):
        if self.active:
            """
            if self.config["bot"]["lastWorked"] is None or (int(self.config["bot"]["lastWorked"]) + 60 * 60) < time.time():
                self.paused = True
                Messages.sendMessage(self, "pls work")
                self.config["bot"]["lastWorked"] = time.time()
                self.writeConfig()
            """
            commands = self.config["commands"]
            r = []
            for command in commands.keys():
                if commands[command]:
                    r.append(command)

            if random.random() >= 0.8:
                modified = False
                for index, item in enumerate(r):
                    if not modified and random.random() >= 0.6:
                        modified = True
                        tmp = item
                        offset = 0
                        if index == 0:
                            offset = 1
                        else:
                            offset = random.randint(-1, 1)
                        r[index] = r[index + offset]
                        r[index + offset] = tmp

            for command in r:
                while self.paused:
                    pass
                Messages.sendMessage(self, "pls " + command)
                x = commands[command]
                time.sleep(random.randint(x[0], x[1]))

            self.runRound()

    def start(self):
        self.active = True
        self.modules["autobox"].useBox()
        time.sleep(5)
        self.modules["autopizza"].usePizza()
        time.sleep(5)
        self.runRound()

    def stop(self):
        self.active = False

    def pause(self):
        self.paused = True

    def writeConfig(self):
        with open("config.json", "w") as f:
            f.write(json.dumps(self.config, indent=2))
            f.close()
