import discord
from discord.ext import commands
import chardet
import os
import random
from random import shuffle, choice

class SbbFun:
    """SBB-Fun-shaped commands!"""

    def __init__(self, bot):
        self.bot = bot

    def guess_encoding(self, trivia_list):
        with open(trivia_list, "rb") as f:
            try:
                return chardet.detect(f.read())["encoding"]
            except:
                return "ISO-8859-1"

    @commands.command(pass_context=True)
    async def insult(self, ctx, user : discord.Member=None):
        """Insulta utente"""

        #Your code will go here
        if user != None:
            msg = ""
            if user.id == self.bot.user.id:
                msg = "Credi che il sommo Lider mi abbia fatto scemo? BHUAHAHAHAHAHA!!! "
                user = ctx.message.author

            #Loads a random insult from database
            ifile = 'data/sbb/insults.txt'
            encoding = self.guess_encoding(ifile)
            lines = open(ifile, "r", encoding=encoding).read().splitlines()
            line =random.choice(lines)
            await self.bot.say(msg + user.mention + line)
        else:
            await self.bot.say("Devi scegliere qualcuno cujò!")


    @commands.command()
    async def punch(self, user : discord.Member):
        """Colpisci un utente con il Pugno di Lato"""

        #Your code will go here
        await self.bot.say("PUGNODILAATOOOOOOOOO! E " + user.mention + " e' fuori! ლ(ಠ益ಠლ)")


    @commands.command(pass_context=True)
    async def ribalta(self, ctx, user : discord.Member=None):
        """Ribalta un utente"""
        if user != None:
            msg = ""
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = "Cujo, fai ridere solo Pinkpig. Che ne dici di *quisst*:\n\n"
            char = "abcdefghijklmnopqrstuvwxyz"
            tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
            table = str.maketrans(char, tran)
            name = user.display_name.translate(table)
            char = char.upper()
            tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z"
            table = str.maketrans(char, tran)
            name = name.translate(table)
            await self.bot.say(msg + "(╯ °□° ）╯︵ " + name[::-1])
        else:
            await self.bot.say("Devi scegliere qualcuno tund!")

def setup(bot):
    bot.add_cog(SbbFun(bot))
