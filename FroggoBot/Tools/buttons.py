import random
import re

import FroggoBot.froggobot


class Buttons:

    @staticmethod
    def getButtonWithPriority(priority, message):
        buttonList = Buttons.parseButtons(message["components"])

        highestIndex = -1
        highestEl = None
        for button in buttonList:
            if priority.count(button["label"].lower()):
                index = priority.index(button["label"].lower())
                if highestIndex == -1:
                    highestIndex = index
                    highestEl = button
                elif index < highestIndex:
                    highestIndex = index
                    highestEl = button

        if highestIndex == -1:
            return [random.choice(buttonList)]

        return [highestEl]

    @staticmethod
    def parseButtons(buttonList):
        l = []

        def mini(c):
            for component in c:
                if component["type"] == 1:
                    mini(component["components"])
                elif component["type"] == 2:
                    l.append(component)

        mini(buttonList)

        return l

    @staticmethod
    def clickButton(froggo, btn, message):
        return froggo.bot.click(froggo.config["bot"]["dankID"], froggo.config["bot"]["channelID"], message["id"], message["flags"], froggo.config["bot"]["guildID"], data={"component_type": 2, "custom_id": btn["custom_id"]})
