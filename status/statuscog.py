from redbot.core import commands
from redbot.core import Config
from discord.ext import tasks

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
        
        await self.client.wait_until_ready()
        remind_channel = self.bot.get_channel(772899841679818754)
        await remind_channel.send("Passed")
        
        self.index = 0
        self.serverstatus.start()

    def cog_unload(self):
        self.serverstatus.cancel()

    @tasks.loop(seconds=60.0)
    async def serverstatus(self):
        self.index += 1
