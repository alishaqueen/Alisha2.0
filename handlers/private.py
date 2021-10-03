# ❰ǫᴜᴇᴇɴ✘ᴀʟɪsʜᴀ❱
# ❰ǫᴜᴇᴇɴ✘ᴀʟɪsʜᴀ❱

import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text="**❰ǫᴜᴇᴇɴ✘ᴀʟɪsʜᴀ❱  sᴜᴘᴇʀ ғᴀsᴛ ᴍᴜsɪᴄ\nᴘʟᴀʏᴇʀ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [Aʙʜɪᴍᴀɴʏᴜ Sɪɴɢʜ Rᴀɴᴀᴡᴀᴛ](t.me/Venom_Hai_Hum)  ...**".format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**❰ǫᴜᴇᴇɴ✘ᴀʟɪsʜᴀ❱  sᴜᴘᴇʀ ғᴀsᴛ\nʜɪɢʜ ǫᴜᴀʟɪᴛʏ » ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ\nʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [Aʙʜɪᴍᴀɴʏᴜ Sɪɴɢʜ Rᴀɴᴀᴡᴀᴛ](t.me/Venom_Hai_Hum) ...**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 💥", url=f"https://t.me/Shayri_Music_Lovers"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**❰ǫᴜᴇᴇɴ✘ᴀʟɪsʜᴀ❱  sᴜᴘᴇʀ ғᴀsᴛ\nʜɪɢʜ ǫᴜᴀʟɪᴛʏ » ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ\nʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [Aʙʜɪᴍᴀɴʏᴜ Sɪɴɢʜ Rᴀɴᴀᴡᴀᴛ](t.me/Venom_Hai_Hum) ...**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ʜᴇʀᴇ »» ғᴏʀ ᴍᴏʀᴇ 💞", url=f"https://t.me/Shayri_Music_Lovers"
                    )
                ]
            ]
        ),
    )
