# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start⚡️","help📚","login🔑","DC"],
                ["Subscribe ❤️","ping📡","status📊","maintainers😎"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start⚡️","help📚","DC"],
                ["Subscribe ❤️","ping📡","status📊","maintainers😎"]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.command("start") | filters.regex('start⚡️')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__𝐒𝐨𝐫𝐫𝐲 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐁𝐚𝐧𝐧𝐝 𝐁𝐚𝐛𝐲 😘. 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐡𝐞 𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/c260745e4b43fbfa7f12f.jpg",
                caption="<i>𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐔𝐬𝐞 𝐦𝐞 🔐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>𝐒𝐨𝐦𝐭𝐡𝐢𝐧𝐠 𝐖𝐞𝐧𝐭 𝐖𝐫𝐨𝐧 𝐁𝐚𝐛𝐲</i> <b> <a href='https://t.me/WD_Topic_Group'>𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐁𝐚𝐛𝐲 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 </a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://telegra.ph/file/443745f375ee353092b5c.jpg",
        caption =f'🥰 𝐇𝐢 𝐁𝐚𝐛𝐲 {m.from_user.mention(style="md")}!,\nI am Telegram File to Link Generator Bot with Channel support.\nSend me pom pom file and get a direct download link and streamable link.!',
        reply_markup=buttonz)


@StreamBot.on_message((filters.command("help") | filters.regex('help📚')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>𝐒𝐨𝐫𝐫𝐲 𝐁𝐚𝐛𝐲 😘, 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐁𝐚𝐧𝐧𝐝 FROM USING ᴍᴇ. 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐡𝐞 𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭</i>",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://graph.org/file/24d43cd3d9de74fd7740b.jpg ",
                Caption="**𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩 𝐓𝐨 𝐔𝐬𝐞 𝐦𝐞 ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🦋 𝐉𝐨𝐢𝐧 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__𝐒𝐨𝐦𝐭𝐡𝐢𝐧𝐠 𝐖𝐞𝐧𝐭 𝐖𝐫𝐨𝐧 𝐁𝐚𝐛𝐲. Cᴏɴᴛᴀᴄᴛ ᴍᴇ__ [Support](https://t.me/WD_Topic_Group).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b> Send me pom pom file or video i will give you ban Result and download link.</b>\n
<b> I also support Channels, add me to you Channel and send any media files and see miracle✨ also send /list to know all commands""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💁‍♂️ 𝐎𝐰𝐧𝐞𝐫", url="https://t.me/WD_Contact_Bot")],
                [InlineKeyboardButton("💥 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞", url="https://youtube.com/shorts/EkZU0P_L-9s?feature=share")]
            ]
        )
    )
