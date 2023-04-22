from redbot.core import commands
from redbot.core import Config

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
        self.tasker.start()
        
        @tasks.loop(seconds=10)
        async def tasker(self):
            if self.config.channelId() != 0 and self.config.messageId() != 0:
                print("in task")
    
        @tasker.before_loop
        async def before_tasker(self):
            print("before wait")
            await self.bot.wait_until_red_ready()
            print("before wait 2")      
