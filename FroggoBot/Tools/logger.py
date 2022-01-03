from colorama import init, Fore, Back, Style
init()


class Logger:

    @staticmethod
    def info(text):
        Logger._makeMessage("info", text, Fore.CYAN, "", Style.BRIGHT)

    @staticmethod
    def warn(text):
        Logger._makeMessage("warn", text, Fore.YELLOW, "", Style.BRIGHT)

    @staticmethod
    def error(text):
        Logger._makeMessage("error", text, Fore.RED, "", Style.BRIGHT)

    @staticmethod
    def _makeMessage(prefix, text, fore, back="", style=""):
        print(f"{fore + back + style}[{Fore.LIGHTWHITE_EX + prefix + fore}] {text}")