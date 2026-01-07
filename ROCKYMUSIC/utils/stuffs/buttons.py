# ===========================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @TheSigmaCoder
# ===========================================================

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 
import config

class BUTTONS(object):
    ABUTTON = [
    [
        InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/kriti_supprot"),
        InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/kriti_update")
    ],
    [
        InlineKeyboardButton(text="˹ ❍ᴡηєʀ ˼", user_id=config.OWNER_ID),
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settingsback_helper")
    ]
]

    INFO_BUTTON = [
    [
        InlineKeyboardButton("˹ ʀєᴘσ ˼", callback_data="gib_source"),
        InlineKeyboardButton("˹ ʏᴛ-ᴀᴘɪ ˼", callback_data="bot_info_data"),
        InlineKeyboardButton("˹ ʟᴧηɢᴜᴧɢє ˼", callback_data="LG"),
    ],
    [
        
        InlineKeyboardButton("˹ ᴘʀᴏᴍᴏ ˼", url="https://t.me/badnam_xd?text=𝖧ᴇʏ%20ʙᴀʙʏ%20%20😄%20ɪ%20ᴡᴀɴᴛ%20ᴘᴀɪᴅ%20ᴘʀᴏᴍᴏᴛɪᴏɴ,%20ɢɪᴠᴇ%20ᴍᴇ%20ᴘʀɪᴄᴇ%20ʟɪsᴛ%20😙"),
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settingsback_helper"),
    ]
    ]
    


    INFO_NEW = [
    [
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settings_back_helper"),
        InlineKeyboardButton("• ᴋʀɪᴛɪ ʙᴏᴛs •", url="https://t.me/kriti_update")
    ],
    ]
    
    

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Purvi-V2
# 📢 Telegram channel : t.me/Purvi_Bots
# ===========================================================
