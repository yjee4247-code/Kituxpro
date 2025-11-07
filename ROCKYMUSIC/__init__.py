# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @MrRockytg
# ===========================================================

from ROCKYMUSIC.core.bot import ROCKY
from ROCKYMUSIC.core.dir import dirr
from ROCKYMUSIC.core.git import git
from ROCKYMUSIC.core.userbot import Userbot
from ROCKYMUSIC.misc import dbb, heroku
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ROCKY()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/mrrockytg
# 🔗 Source link : t.me/rockyxsupport
# 📢 Telegram channel : t.me/rockyxupdate
# ===========================================================
