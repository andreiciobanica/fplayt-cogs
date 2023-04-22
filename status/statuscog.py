from redbot.core import commands
from redbot.core import Config
from discord.ext import tasks, commands

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=253939849348907019)
        default_global = {
            "channelId": 0,
            "messageId": 0,
        }
        default_guild = {
            "channelId": 0,
            "messageId": 0,
        }
        self.config.register_global(**default_global)
        self.config.register_guild(**default_guild)
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1
