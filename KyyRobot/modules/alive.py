import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from KyyRobot.events import register
from KyyRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/0270aa22d8c6ce8ad491e.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Nasty.** \n\n"
  TEXT += "✘ **I'm Working Properly** \n\n"
  TEXT += f"✘ **My Master : [Mr.Shelby](https://t.me/Lost_Kiddo)** \n\n"
  TEXT += f"✘ **Library Version :** `{telever}` \n\n"
  TEXT += f"✘ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"✘ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Iam Working Now🔥 **"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/AngelxRobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/angelsupports")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
