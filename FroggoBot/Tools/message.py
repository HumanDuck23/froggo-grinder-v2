import time
import random
import json


class Messages:

    @staticmethod
    def sendMessage(bot, message, channelID, wpm):
        if len(message) < 6:
            bot.sendMessage(channelID, message)
        else:
            # realistic typing
            bot.typingAction(channelID)
            sleep = len(message) / (wpm + random.randint(-10, 10))
            time.sleep(sleep * 10)
            bot.sendMessage(channelID, message)

    @staticmethod
    def getMessage(bot, channelID, messageID):
        t = bot.getMessage(channelID, messageID).text
        return json.loads(t)[0]
