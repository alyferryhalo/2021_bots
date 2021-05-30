from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import emoji

btn_section_skate = KeyboardButton(emoji.emojize(':ice_skate: Фигурное катание'))
btn_section_volleyball = KeyboardButton(emoji.emojize(':volleyball: Воллейбол'))
btn_section_soccer = KeyboardButton(emoji.emojize(':soccer_ball: Футбол'))
btn_section_bullseye = KeyboardButton(emoji.emojize(':bullseye: Дартс'))

kb_sections = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btn_section_skate).add(
    btn_section_volleyball).add(btn_section_soccer).add(btn_section_bullseye)

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отправить номер ☎️', request_contact=True))
