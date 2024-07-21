#(©)codeflix_bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>Smile</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Anity_managementbots'>○ ᴍʏ ᴜᴘᴅᴀᴛᴇs</a>\n○ Support : <a href='https://t.me/Anity_botsupport'>Anity</a>\n○ Updates : <a href='https://t.me/Smile_ownerbotz'>Updates</a>\n○ Owner : <a href='https://t.me/Beesmileee'>Owner</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/Anity_managementbots/27')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pas
