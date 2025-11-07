# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @Mrrockytg
# ===========================================================

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("» ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴍᴏɴɢᴏ ᴅᴀᴛᴀʙᴀsᴇ...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("» ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴍᴏɴɢᴏ ᴅᴀᴛᴀʙᴀsᴇ.")
except:
    LOGGER(__name__).error("» ꜰᴀɪʟᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ʏᴏᴜʀ ᴍᴏɴɢᴏ ᴅᴀᴛᴀʙᴀsᴇ.")
    exit()

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/Mrrockytg
# 🔗 Source link : t.me/rockyxsupport
# 📢 Telegram channel : t.me/rockyxUpdate
# ===========================================================
