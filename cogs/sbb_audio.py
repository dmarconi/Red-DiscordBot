import discord
from discord.ext import commands
import asyncio
import logging

try:
    if not discord.opus.is_loaded():
        discord.opus.load_opus('libopus-0.dll')
except OSError:  # Incorrect bitness
    opus = False
except:  # Missing opus
    opus = None
else:
    opus = True

class SbbAudio:
    """SBB-Audio-shaped commands!"""

    def __init__(self, bot):
        self.bot = bot
        logging.basicConfig(level=logging.DEBUG)

    @commands.command()
    async def sbbplay(self, sbb_audio_choice):
        """Plays an MP3 from SBB archive: fatality"""

        logging.debug('Watch out!')  # will print a message to the console
        if sbb_audio_choice == None:
            await self.bot.say("Testa di cazzo scegli una clip audio!!!")
def setup(bot):
    bot.add_cog(SbbAudio(bot))
