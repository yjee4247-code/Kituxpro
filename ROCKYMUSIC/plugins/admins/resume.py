# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @MrRockytg
# ===========================================================

from pyrogram import filters
from pyrogram.types import Message

from ROCKYMUSIC import app
from ROCKYMUSIC.core.call import ROCKY
from ROCKYMUSIC.utils.database import is_music_playing, music_on
from ROCKYMUSIC.utils.decorators import AdminRightsCheck
from ROCKYMUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await ROCKY.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
    )

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/MrRockytg
# 🔗 Source link : t.me/Rockyxsupport
# 📢 Telegram channel : t.me/Rockyxupdate
# ===========================================================
