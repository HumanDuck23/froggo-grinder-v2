import time
import random
import json

import FroggoBot.froggobot


class Messages:

    @staticmethod
    def sendMessage(froggo, message):
        if len(message) < 6:
            froggo.bot.sendMessage(froggo.config["bot"]["channelID"], message)
        else:
            # realistic typing
            froggo.bot.typingAction(froggo.config["bot"]["channelID"])
            sleep = len(message) / (int(froggo.config["bot"]["WPM"]) + random.randint(-10, 10))
            time.sleep(sleep * 10)
            froggo.bot.sendMessage(froggo.config["bot"]["channelID"], message)

    @staticmethod
    def getMessage(froggo, messageID):
        t = froggo.bot.getMessage(froggo.config["bot"]["channelID"], messageID).text
        return json.loads(t)[0]

    @staticmethod
    def isReplyToMe(froggo, message):
        try:
            return message["referenced_message"]["author"]["id"] == froggo.bot.gateway.session.user["id"]
        except KeyError:
            return -1
