
import pyrogram
import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery


tutorial1 = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Next ➡️', callback_data='helpmenu'),
                    InlineKeyboardButton('Close', callback_data='close')
                ]
            ]
        )

tutorial1t = "Hello {}. \n Coming Soon Tutorial "

@Client.on_message(filters.command("tutorial"))
async def tutorial1(client, message):
    await client.reply_video(
                    video="https://telegra.ph/file/fe9fcc029fd846457fac7.mp4",
                    reply_markup = tutorial1,
                    caption = tutorial1t.format(update.from_user.mention))
    
