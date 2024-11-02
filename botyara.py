import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7696658425:AAFUmZxrEOskasUXn0XG-ZGrc9EurAXPvP0")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет. Я бот")


@dp.message(Command('delete_all'))
async def cmd_delete_all(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text='Да', callback_data='yes')
    builder.button(text='Hет', callback_data='no')
    await message.answer("Вы уверены что хотите очистить историю диалога?", reply_markup=builder.as_markup())
    # вот тут надо сделать действие которое зависит от callback_data


# вот тута надо проверить наличие айди в бд. если он там есть то продолжаем. если нету надо спросить метаданные и добавить их в бд вместе с айди

slovar_of_messages = {}
@dp.message()
async def any_message(message: types.Message):
    print(message.text)
    await message.answer('черт лысый понял меня?')
    if message.from_user.id in slovar_of_messages:
        slovar_of_messages[message.from_user.id].append(message.text)
    else:
        slovar_of_messages[message.from_user.id] = [message.text]
    print(slovar_of_messages)


    if message.text == 'кефтеме':
        await message.answer('kefteme')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
