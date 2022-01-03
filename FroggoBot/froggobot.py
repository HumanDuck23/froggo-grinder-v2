from FroggoBot.Modules import *

import json


class Froggo:
    def __init__(self):
        self.modules = {
            "autobox": autobox,
            "autobuy": autobuy,
            "autogift": autogift,
            "automoney": automoney,
            "autopizza": autopizza,
            "balancecheck": balancecheck.BalanceCheck(self),
            "beg": beg,
            "crime": crime,
            "dig": dig,
            "fish": fish,
            "highlow": highlow,
            "hunt": hunt,
            "postmeme": postmeme,
            "scratch": scratch,
            "search": search,
            "snakeeyes": snakeeyes,
            "work": work
        }

        # load modules from conf
        self.config = json.loads(open("config.json", "r").read())
        for module in self.config["modules"].keys():
            if not self.config["modules"][module]:
                del self.modules[module]