# Froggo Grinder  
  
---  
![img](https://c.tenor.com/ayqgE7SP1_UAAAAC/hmm.gif)
  
### What is Froggo Grinder?  
Froggo Grinder is a free and open-source [Dank Memer](https://dankmemer.lol) selfbot!  
Froggo is designed to get as much XP as possible, as fast as possible.   
That way you can get all the sweet leveling rewards!  
  
### How does Froggo work?
One of the key features that make Froggo so hard to detect is the more or less complete randomization of basically everything the bot does. The bot types messages at random speeds, it takes a random amount of time to press buttons, it sends the commands in a (kind of) random order (like a human). Very early prototype versions didn't include lots of randomization, and were blacklisted pretty quick. With the randomization in place, the bot has been able to stay undetected for multiple weeks (and counting)!
  
### Will I get banned for using Froggo?  
Technically, any kind of automation of a normal user account is against Discord's TOS ([Support Article](https://support.discord.com/hc/en-us/articles/115002192352-Automated-user-accounts-self-bots-)).  However, they will not actively go looking for userbots / selfbots, so they are unlikely to get banned if they don't stress the API (which Froggo does not). So you are most likely to be fine.  
Being blacklisted from Dank Memer is a different question. I have used this bot to get an account to level 3k+,  
so you'll probably be fine, as it is designed to look like a human.  
  
### Where can I download it?  
To run the bot, all you need to do is download this repo as a zip, extract it and run main.py! You need to have [Python 3](https://www.python.org) installed for it to work
  
### How do I get the most XP?  
Since a recent update Dank Memer gives double XP on weekends. This makes them the perfect opportunity for the bot! Make sure to give it pizza slices and/or daily boxes for the fastest possible grinding. You can also make the account it's running on eat cheese for an extra XP multi. With ~20 cheese eaten, pizzas and daily boxes the bot can get up to 600 levels in around 8-10 hours!  
  
### How do I use the bot?
Using the bot is very simple! When you download the ZIP, one of the two files included is called `config.json`. This file is where you can configure the bot! Here's a simple table to describe values you might want to change:

| Name | Description |
| ----------- | ----------- |
| modules | list of modules, replace `true` with `false` to disable |
| commands | list of commands, replace `true` with `false` to disable |
| token | The auth token for the account [How to get it](https://discordhelp.net/discord-token) |
| channelID | The ID of the channel the bot should use |
| guildID | The ID of the server the bot should use |
| WPM | How fast (words per minute) the bot should type |

Here's a list of the modules you can disable/enable and what they do:

| Name | Description |
| ----------- | ----------- |
| autobox | Automatically uses a daily box every 10 minutes |
| autobuy | Automatically buy an item when you need it (fishingpole, rifle, etc.) |
| autogift | Automatically gift you rare items it obtains (work items, dragon, etc.) |
| automoney | Automatically give you most of the money it earns |
| autopizza | Automatically eats a pizza slice every hour |

---
This project uses Discord-S.C.U.M, an awesome selfbot library for python! <br>  
GitHub: https://github.com/Merubokkusu/Discord-S.C.U.M

Froggo was also inspired by a very cool dank memer automation program that is sadly no longer maintained: [Dank Grinder](https://github.com/V4NSH4J/dankgrinder/) and it's parent [Dank Grinder](https://github.com/dankgrinder/dankgrinder)