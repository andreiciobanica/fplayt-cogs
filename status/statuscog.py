from redbot.core import commands
from redbot.core import Config
from discord.ext import tasks
from datetime import date, datetime, time
from babel.dates import format_datetime, get_timezone
import discord
import requests

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=253939849348907019)
        default_global = {
            "channelId": 0,
            "messageId": 0,
        }
        self.config.register_global(**default_global)
        self.index = 0
        self.serverstatus.start()

    def cog_unload(self):
        self.serverstatus.cancel()

    @tasks.loop(seconds=60.0)
    async def serverstatus(self):
        channelId = await self.config.channelId()
        messageId = await self.config.messageId()
        if channelId == 0 and messageId == 0:
            serverDetailsJson = requests.get('http://'+ "185.30.165.128:30120" +'/info.json').json()
            print(serverDetailsJson)
            playerNumber = ""
            serverStatus = ""
            serverUptime = ""
            if hasattr(serverDetailsJson, "vars"):
                serverDetailsJson = serverDetailsJson.vars
                playersJson = requests.get('http://'+ "185.30.165.128:30120" +'/players.json').json()
                serverStatus = "```✅ Online```"
                serverUptime = "```" + getattr(serverDetailsJson, 'Uptime', "0m") + "```"
                playerNumber = "```" + len(playersJson) + "/" + getattr(serverDetailsJson, 'sv_maxClients', "1024") + "```"
            else:
                serverStatus = "```❌ Offline```"
                serverUptime = "```0m```"
                playerNumber = "```0/1024```"
            status_channel = self.bot.get_channel(772899841679818753)
            embed=discord.Embed(color=0xe3ee34, url="https://cdn.discordapp.com/attachments/1001319323161346220/1099451162765307984/logofpt.png")
            embed.set_author(name="FPlayT Community | Status", icon_url="https://cdn.discordapp.com/attachments/1001319323161346220/1099451162765307984/logofpt.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1001319323161346220/1099451162765307984/logofpt.png")
            embed.add_field(name="Server name", value="```FPlayT Advanced Roleplay```", inline=False)
            embed.add_field(name="Server DNS", value="```server.fplayt.ro```", inline=False)
            embed.add_field(name="Status", value=serverStatus, inline=True)
            embed.add_field(name="Jucători online", value=playerNumber, inline=True)
            embed.add_field(name="Server uptime", value=serverUptime, inline=True)
            dateNow = datetime.now()
            text = "FPlayT Community • " + str(format_datetime(dateNow, "dd.MM.yyyy HH:mm:ss", tzinfo=get_timezone('Europe/Bucharest'), locale='ro_RO'))
            embed.set_footer(text=text)
            status_message = await status_channel.send(embed=embed)
            await self.config.channelId.set(772899841679818753)
            await self.config.messageId.set(status_message.id)
        else:
            status_channel = self.bot.get_channel(772899841679818753)
            embed=discord.Embed(color=0xe3ee34, url="https://cdn.discordapp.com/attachments/1001319323161346220/1099451162765307984/logofpt.png")
            embed.set_author(name="FPlayT Community | Status", icon_url="https://cdn.discordapp.com/attachments/1001319323161346220/1099451162765307984/logofpt.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1001319323161346220/1099451162765307984/logofpt.png")
            embed.add_field(name="Server name", value="```FPlayT Advanced Roleplay```", inline=False)
            embed.add_field(name="Server DNS", value="```server.fplayt.ro```", inline=False)
            embed.add_field(name="Status", value="```✅ Online```", inline=True)
            embed.add_field(name="Jucători online", value="```921/1024```", inline=True)
            embed.add_field(name="Server uptime", value="```3h 10m```", inline=True)
            dateNow = datetime.now()
            text = "FPlayT Community • " + str(format_datetime(dateNow, "dd.MM.yyyy HH:mm:ss", tzinfo=get_timezone('Europe/Bucharest'), locale='ro_RO'))
            embed.set_footer(text=text)
            status_message = await status_channel.send(embed=embed)
            await self.config.channelId.set(772899841679818753)
            await self.config.messageId.set(status_message.id)
        
    @serverstatus.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()
