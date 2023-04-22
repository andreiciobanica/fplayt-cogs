from .statuscog import Status

async def setup(bot):
    bot.add_cog(Status(bot))