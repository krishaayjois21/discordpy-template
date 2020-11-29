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
act = Activity(name=name, type=type)

# Create the class for the extension
class InitListener(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        # Change the bot status to what we mention above
        await self.client.change_presence(activity=act)
        print(f"『{str(self.client.user)}』『✓』LOGGED IN AS " + str(self.client.user))
        print(f"『{str(self.client.user)}』『✓』IS ONLINE!")
        n_guilds = len(self.client.guilds)
        print(f"『{str(self.client.user)}』『✓』IN {n_guilds} GUILD(S)")

# Function for discord.py to load this extension
def setup(client):
    client.add_cog(InitListener(client))
