from FroggoBot.Modules.ModuleBase import modulebase
import re


class BalanceCheck(modulebase.ModuleBase):
    def __init__(self, config):
        super().__init__(config)
        self.wallet = -1
        self.bank = -1

    def onMessage(self, message):
        if message["embeds"]:
            for embed in message["embeds"]:
                if embed["description"]:
                    pattern = r"\*\*Wallet\*\*: ⏣ (.*)\n\*\*Bank\*\*: ⏣ (.*) / .* `\(.*\)`"
                    search = re.search(pattern, embed["description"])

                    self.wallet = int(search.group(1).replace(",", ""))
                    self.bank = int(search.group(2).replace(",", ""))

    def getWallet(self):
        return self.wallet

    def getBank(self):
        return self.bank
