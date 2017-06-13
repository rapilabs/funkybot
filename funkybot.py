import re

from irc3 import event, plugin, rfc
from irc3.utils import IrcString


def slugify(input_str):
    return input_str.lower().replace('_', '-')


@plugin
class FunkyBot:
    def __init__(self, bot):
        self.bot = bot

    @event(rfc.PRIVMSG)
    def admin_answer(self, mask, target, data, **kwargs):
        if data.startswith('FunkyBot:'):
            message = re.sub(r'^FunkyBot: *', '', data)

            doc_match = re.search(r'^doc +(\w+)', message)
            if doc_match:
                if re.search(r'^[A-Z_]+$', doc_match[1]):
                    self.bot.privmsg(
                        target,
                        'https://docs.djangoproject.com/en/stable/ref/settings/#{}'.format(slugify(doc_match[1])),
                    )

            elif re.search(r'admin.*\?', message, re.IGNORECASE):
                self.bot.privmsg(
                    target,
                    '{}: Admin is no substitute for a proper management / back-office interface'.format(IrcString(mask).nick),
                )
