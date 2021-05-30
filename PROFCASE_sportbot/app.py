from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
import keyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    msg_start = "Привет! Я — бот Sport_Club, который поможет тебе сориентироваться! Напиши /help, чтобы узнать, что я умею!"
    await message.reply(msg_start)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg_help = "Мои команды: /start, /help, /news, /timetable, /contact"
    await message.reply(msg_help)

@dp.message_handler(commands=['news'])
async def process_news_command(message: types.Message):
    msg_news = "Заглушка для news"
    await message.reply(msg_news)

@dp.message_handler(commands=['timetable'])
async def process_timetable_command(message: types.Message):
    msg_timetable = "Расписание какой спортивной секции ты хочешь знать? Выбери на клавиатуре, пожалуйста!"
    await message.reply(msg_timetable, reply_markup=kb.kb_sections)

@dp.message_handler(commands=['contact'])
async def process_contact_command(message: types.Message):
    await message.reply("Оставьте свой контакт!", reply_markup=kb.markup_request)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
