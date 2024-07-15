
import os
import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from config import X1, SUDO_USER
from ... import *
from SACHINxSPAM.data import OneWord, DEV,


FC = 2

@X1.on_message(cdz(["srandi"])  & (filters.me | filters.user(SUDO_USER)))
async def alt_lol(xspam: Client, message: Message):    
    chat_id = message.chat.id
    RUSH = None
    if message.reply_to_message:
        RUSH = message.reply_to_message.id
    try:
        for word in OneWord:
            await xspam.send_message(chat_id, word, reply_to_message_id=RUSH)
            await asyncio.sleep(1)
    except FloodWait:
        print("Flood !!")
        pass



@X1.on_message(cdz(["randii"])  & (filters.me | filters.user(SUDO_USER)))
async def alt_mkc(xspam: Client, message: Message):    
    chat_id = message.chat.id
    RUSH = None
    if message.reply_to_message:
        RUSH = message.reply_to_message.id
    try:
        for word in OneWord:
            await xspam.send_message(chat_id, word, reply_to_message_id=RUSH)
            await asyncio.sleep(000.1)
    except FloodWait:
        print("Flood !!")
        pass
    
    

@X1.on_message(cdz(["rrandi"])  & (filters.me | filters.user(SUDO_USER)))
async def alt_stop(_, message: Message):    
    reply = await message.reply_text("👻𝚃𝙴𝚁𝙸 𝙼𝙰𝙰 𝙺𝙸 𝙲𝙷𝚄𝚃 ...")
    await reply.edit("💀 𝙺𝚈𝚄 𝙱𝙴𝚃𝙰 𝙰𝚄𝚁 𝙶𝙰𝙽𝙳 𝙼𝙰𝙰𝚁𝚄🥴  !!\n\n👻#𝙵𝙴𝙴𝙻_4𝚂𝚃_𝙳𝙰𝙳𝙳𝚈 💕 !!")
    os.system(f"kill -9 {os.getpid()} && python3 -m SHUKLA")
