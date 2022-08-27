from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

""" HERE IS MARKUPS """

# back button
back_btn = KeyboardButton('◀️ BACK')

# --- Main menu ---
games_btn = KeyboardButton('MENU')
info_btn = KeyboardButton('ℹ️ INFO')
main_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(games_btn, info_btn)
