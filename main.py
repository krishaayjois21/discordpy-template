"""
discord.py template
Date: 18/11/2020
Author: Krishaay Jois
Github: https://github.com/krishaayjois21/discordpy-template

Note: Before running the bot enter configuration details in config/config.json

LICENSE:
MIT License

Copyright (c) 2020 Krishaay Jois

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Import required modules
from json import load

from discord import client
from discord.ext import commands


# Load configuration data from config/config.json

with open("config/config.json", "r") as conf:
    config = load(conf)
    prefix = config["prefix"]
    token = config["token"]
    extensions = config["extensions"]


# Create a bot instance with the prefix from the configuration
client = commands.Bot(command_prefix=prefix)


# Load all the extensions mentioned in
for extension in extensions:
    try:
        client.load_extension(extension)
        print(f"『LOADED』『✓』 {extension.split('.')[-1]} LOADED FROM {extension}")
    except Exception:
        print(
            f"『FAILED』『×』 {extension.split('.')[-1]} COULD NOT BE LOADED FROM {extension}"
        )
        print(f"『ERROR』")
        print(Exception)

# Run the bot
client.run(token)