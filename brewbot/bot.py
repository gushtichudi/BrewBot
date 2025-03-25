from .log import Log, Level

import discord
import os

from discord.ext import commands 

class Bot:
    def __init__(self, token, log_descriptor: str | None = "/dev/stdout"):
        self.token = token
        self.bot_prefix = ";"
        self.log_descriptor = log_descriptor
        self.tries = 0

    def change_log_descriptor(self, location):
        self.log_descriptor = location
    
    def verify_token(self) -> bool:
        assure = input(f"Is this token correct? ( {self.token} ) [y/n] ")

        if assure.casefold() == "y":
            return True
        else:
            return False

    def run(self, token_override = ""):
        l = Log(2, self.log_descriptor)
        
        l.log_write(Level.Info, "Starting BrewBot...")

        intents = discord.Intents.default()
        intents.message_content = True

        client = commands.Bot(command_prefix=self.bot_prefix, intents=intents)

        # only few basic commands are hardly coded here
        @client.event
        async def onready(ctx):
            l.log_write(Level.Success, f"Bot started as {ctx.user}!")
            await ctx.send("do you see ts????")

        @client.command() 
        async def sayhi(ctx):
            await ctx.send(f"hi, i am brewy.")

        @client.command()
        async def cat(ctx, arg):
            arg.replace("`", "\\`")

            msg_fmt = f"```\n{arg}\n```"
            await ctx.send(msg_fmt)

        @client.command()
        async def free_mem(ctx):
            ret = os.popen("free -h").read()
            ret.replace("`", "\\`")
            
            msg_fmt = f"```\n{ret}\n```"
            await ctx.send(msg_fmt)

        @client.command()
        async def neofetch(ctx):
            ret = os.popen("fastfetch").read()
            ret.replace("`", "\\`")
            ret.replace("\\x1b", "")
            
            msg_fmt = f"```\n{ret}\n```"
            await ctx.send(msg_fmt)

        try:
            client.run(self.token)
        except Exception as e:
            l.log_write(Level.Error, f"API RETURNED EXCEPTION: {e}")
            l.log_write(Level.Error, f"As the API suggests, it might be becaused of an errorneous token.")
            
            if self.verify_token():
                self.run()
            else:
                l.log_write(Level.Info, "Trying to run with token override...")

                from os import getenv 
                self.run(getenv("BREWBOT_TOKEN"))
                self.tries += 1

            if self.tries > 3:
                l.log_write(Level.Info, "Still doesn't work no matter what...")

                self.run(input("Maybe just try manually putting in your token:- "))
