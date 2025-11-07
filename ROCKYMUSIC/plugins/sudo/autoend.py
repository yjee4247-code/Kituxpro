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
from ROCKYMUSIC.misc import SUDOERS
from ROCKYMUSIC.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/autoend [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴇɴᴀʙʟᴇᴅ.\n\nᴀssɪsᴛᴀɴᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀғᴛᴇʀ ғᴇᴡ ᴍɪɴs ᴡʜᴇɴ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴅɪsᴀʙʟᴇᴅ.")
    else:
        await message.reply_text(usage)

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/MrRockytg
# 🔗 Source link : t.me/Rockyxsupport
# 📢 Telegram channel : t.me/Rockyxupdate
# ===========================================================
