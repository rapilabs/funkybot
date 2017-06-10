import re

from irc3 import event, plugin, rfc
from irc3.utils import IrcString


@plugin
class FunkyBot:
    def __init__(self, bot):
        self.bot = bot

    @event(rfc.PRIVMSG)
    def admin_answer(self, mask, target, data, **kwargs):
        if re.search(r'admin.*\?', data, re.IGNORECASE):
            self.bot.privmsg(
                target,
                '{}: Admin is no substitute for a proper management / back-office interface'.format(IrcString(mask).nick),
            )
