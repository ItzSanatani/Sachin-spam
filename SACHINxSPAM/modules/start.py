# ©️ @SACHIN_OWNER || @V_VIP_OWNER
from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_OP = [
    [
        Button.url("🍁 sᴀᴄʜɪɴ", "https://t.me/V_VIP_OWNER"),
        Button.url("ᴜsᴇʀʙᴏᴛ 🕸️", "https://t.me/SANATANI_X_ROBOT")
    ],
    [
        Button.inline("🥀 ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs 🥀", data="help_back")
    ],
    [
        Button.url("✨ ᴜᴘᴅᴀᴛᴇ", "https://t.me/All_SANATANI_BOT"),
        Button.url("sᴜᴘᴘᴏʀᴛ ❄️", "https://t.me/+cW07X2RM_IBmYTI1")
    ],
    [
        Button.url("🌸 ᴊᴏɪɴ ғᴏʀ sᴜᴅᴏ 🌸", "https://t.me/+cW07X2RM_IBmYTI1")
    ],
]

@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        KEX = await event.client.get_me()
        bot_name = KEX.first_name
        bot_id = KEX.id
        TEXT = f"**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**\n**❍ 𝗛𝗘𝗬 ‣ [{event.sender.first_name}]**\n**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**\n**❍ 𝗜 𝗔𝗠 ‣ [{bot_name}](tg://user?id={bot_id})​**\n**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**\n**● ɪ ᴀᴍ ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟ sᴘᴀᴍ ʙᴏᴛ ●**\n**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**\n**● ᴍᴏᴅᴇ ʙʏ » [❖ | 4ˢᵗ ꭙ ғɪɢʜᴛᴇʀ | ❖](https://t.me/+cW07X2RM_IBmYTI1)**\n**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**"
        await event.client.send_file(
                    event.chat_id,  
                    "https://telegra.ph/file/ede961a5c4eefd97cd380.mp4",
                    caption=TEXT, 
                    buttons=START_OP
                )
