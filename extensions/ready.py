# Import required modules

from discord import activity
from discord.ext import commands
from discord import ActivityType, Activity, Status
from json import load

# Load Configuration
with open("config/config.json", "r") as conf:
    config = load(conf)
    prefix = config["prefix"]

# Change as you need. This is the status for the bot
type = ActivityType.playing
name = f"Prefix: {prefix}"
status = Status.online
act = Activity(name=name, type=type)

# Create the class for the extension
class InitListener(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        # Change the bot status to what we mention above
        await self.client.change_presence(activity=act, status=status)
        print("『BOT』『✓』 LOGGED IN AS " + str(self.client.user))
        print(f"『{str(self.client.user)}』『✓』IS ONLINE!")


# Function for discord.py to load this extension
def setup(client):
    client.add_cog(InitListener(client))
