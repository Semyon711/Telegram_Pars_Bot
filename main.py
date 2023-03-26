# создаём бота и функцию эхо
from config import TOKEN
from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')


@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
