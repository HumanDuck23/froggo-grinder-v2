from FroggoBot.Modules.ModuleBase import modulebase
from FroggoBot.Tools import Logger, Messages, Buttons
import random
import time
import re


class Work(modulebase.ModuleBase):
    def onMessage(self, message):
        if message["content"].count("You never fail to amaze me"):
            Messages.sendMessage(self.froggo, "pls work")
        else:
            lookFor = {
                "\\*\\*Work for .*\\*\\* - Color Match .*": (self.colorMatch, False),
                "\\*\\*Work for .*\\*\\* - Emoji Match .*": (self.emojiMatch, False),
                "\\*\\*Work for .*\\*\\* - Repeat Order .*": (self.wordOrder, True),
                "\\*\\*Work for .*\\*\\* - Soccer .*": (self.soccer, False),
                "Dunk the ball!": (self.basketball, False)
            }

            for key in lookFor.keys():
                if re.search(key, message["content"]):
                    # Work time!
                    self.froggo.paused = True
                    Logger.info("Working...")
                    work = lookFor[key]
                    time.sleep(5)
                    nMsg = Messages.getMessage(self.froggo, message["id"])
                    buttons = Buttons.parseButtons(nMsg["components"])
                    buttonsToClick = work[0](message["content"], buttons, nMsg["content"])
                    if type(buttonsToClick) == list:
                        for button in buttons:
                            time.sleep(random.randint(1, 3))
                            Buttons.clickButton(self.froggo, button, nMsg)
                    else:
                        time.sleep(random.randint(1, 3))
                        Buttons.clickButton(self.froggo, buttons, nMsg)

                    self.froggo.paused = False
                    Logger.info("Resuming bot round...")

    def colorMatch(self, text, buttons, updatedText):
        lines = text.split("\n")[1:]
        colors = {}
        for line in lines:
            color = re.search(r":([a-zA-Z]+).*: .*", line).group(1)
            word = re.search(r":[a-zA-Z]+.*: `?([a-zA-Z]+)`?", line).group(1)
            colors[word] = color

        searchWord = re.search(r".* `?([a-zA-Z]+)`?", updatedText.split("\n")[0]).group(1)
        for button in buttons:
            if button["label"] == colors[searchWord]:
                return button

    def emojiMatch(self, text, buttons, _=""):
        emoji = text.split("\n")[1].strip()
        for button in buttons:
            if button["emoji"]["name"] == emoji:
                return button

    def wordOrder(self, text, buttons, _=""):
        words = text.split("\n")[1:]
        nButtons = []
        for word in words:
            word = re.search("`(.*)`", word).group(1)
            print(word)
            for button in buttons:
                if button["label"] == word:
                    nButtons.append(button)
                    break

        return nButtons

    def soccer(self, text, buttons, _=""):
        spaceCount = text.split("\n")[2].count(" ")
        if spaceCount == 7:
            return buttons[random.choice([0, 2])]
        elif spaceCount > 7:
            return buttons[random.choice([0, 1])]
        else:
            return buttons[random.choice([1, 2])]

    def basketball(self, text, buttons, _=""):
        spaceCount = text.split("\n")[2].count(" ")
        if spaceCount == 7:
            return buttons[1]
        elif spaceCount > 7:
            return buttons[2]
        else:
            return buttons[0]

