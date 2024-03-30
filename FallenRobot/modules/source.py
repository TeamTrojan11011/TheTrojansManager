from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as o
from telethon import __version__ as s

from FallenRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, pbot


@pbot.on_message(filters.command(["repo", "source"]))
async def repo(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**Hᴇʏ {message.from_user.mention},

ɪ ᴀᴍ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

**➢ Mʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ :** [♘Tʀᴏᴊᴀɴs♞](https://t.me/About_Alexander)**
**➢ Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{y()}`
**➢ Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ :** `{o}` 
**➢ Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{s}` 
**➢ Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{z}`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID),
                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ",
                        url="https://t.me/TeamTrojans",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
