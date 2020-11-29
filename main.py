"""
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
        print(f"『EXTENSION』『✓』 EXTENSION '{extension.split('.')[-1]}' LOADED FROM '{extension}'")
    except Exception:
        print(
            f"『FAILED』『×』 {extension.split('.')[-1]} COULD NOT BE LOADED FROM {extension}"
        )
        print(f"『ERROR』")
        print(Exception)

# Run the bot
client.run(token)
