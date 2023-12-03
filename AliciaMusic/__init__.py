from AliciaMusic.core.bot import Alicia
from AliciaMusic.core.dir import dirr
from AliciaMusic.core.git import git
from AliciaMusic.core.userbot import Userbot
from AliciaMusic.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER

dirr()
#git()
dbb()
heroku()
sudo()

app = Alicia()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

aiohttpsession = ClientSession()
