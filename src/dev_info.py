# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Dev Info is Completely Optional

def dev_info(client, message):
    keyb = [
        [InlineKeyboardButton("join for updates ", url="https://t.me/disneygrou")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    message.reply_text("""Made with ❤️ in 🇮🇳 by @doreamonfans2.
  

Language: Python3

Bot Framework: Pyrogram Asyncio

Server: heroku

Credits: @doreamonfans1 

Please share the bot if you like it 👍👍""", reply_markup=reply_markup, parse_mode="markdown")
