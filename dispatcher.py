from time import sleep
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv, find_dotenv
from handlers import *

import logging, random, time, asyncio, os

# Find .env file
load_dotenv(find_dotenv())

# init
bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode="HTML")
dp = Dispatcher(bot)

""" HEANDLERS """

# -- COMMANDS HANDLER -- #
# /start
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                            sticker=r"CAACAgIAAxkBAAEFg5li8qnCAwn8afnP9H1xPgVgxgEmZgACuAAD9wLID0YLnLTiTgs4KQQ")
    await bot.send_message(message.from_user.id, 'Приветствую тебя, {0.first_name}!'.format(message.from_user),
    reply_markup = markups.main_menu, parse_mode='html')
# -- MESSSAGES HANDLER -- #
@dp.message_handler()
async def bot_message(message: types.Message):
    """ BOT HANDLER """
    # --- LAUGH ---
    for s in msgs.laugh_trigger:
        if message.text.lower().find(s.lower()) != -1:
            await bot.send_sticker(message.from_user.id, f'{random.choice(msgs.green_lizard_laugh)}')
            break
    # ANOTHER MESSAGE ---
    for s in msgs.variable:
        if message.text.lower().find(s.lower()) != -1:
            # logic
            break

    match message.text:
        # --- General --- #
        case "◀️ НАЗАД":
            await bot.send_message(message.from_user.id, '☑️ Главное меню'.format(message.from_user),
        reply_markup = markups.main_menu, parse_mode='html')
        # --- INFO --- #
        case "ℹ️ INFO":
            me = await bot.get_me()
            await bot.send_message(message.from_user.id, f"Я <b><a href='https://t.me/{me.username}'>{me.first_name}</a></b>.\nМой автор - <a href='https://github.com/{me.username}'>{me.username}</a>!".format(bot.get_me()), parse_mode="html")
        case "info":
            me = await bot.get_me()
            await bot.send_message(message.from_user.id, f"Я <b>{me.first_name}</b>.\nМой автор - <a href='https://github.com/{me.username}'>{me.username}</a>!".format(bot.get_me()), parse_mode="html")