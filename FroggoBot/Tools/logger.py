from colorama import init, Fore, Back, Style
init()


class Logger:

    @staticmethod
    def info(self, text):
        self._makeMessage("info", text, Fore.CYAN, "", Style.BRIGHT)

    @staticmethod
    def warn(self, text):
        self._makeMessage("warn", text, Fore.YELLOW, "", Style.BRIGHT)

    @staticmethod
    def error(self, text):
        self._makeMessage("error", text, Fore.RED, "", Style.BRIGHT)

    @staticmethod
    def _makeMessage(self, prefix, text, fore, back="", style=""):
        print(f"{fore + back + style}[{Fore.LIGHTWHITE_EX + prefix + fore}] {text}")