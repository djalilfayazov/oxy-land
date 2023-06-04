from aiogram import *
from time import *

from config import Settings
from db import DB


# -------------------------------------------------- #


conf = Settings()
db = DB()


bot = Bot(conf.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# -------------------------------------------------- #


@dp.message_handler(commands=['start'])
async def welcome(msg: types.Message):
    user = msg.from_user
    chat = msg.chat

    if chat.id < 0:
        await msg.answer('Adios)')

    else:
        if db.check_user(user.id) == False:
            await msg.reply('Hello!')
            db.add_user(user)

        else:
            await msg.reply('Good day!')



@dp.message_handler(commands=['profile'])
async def show_profile(msg: types.Message):
    user = msg.from_user
    chat = msg.chat

    if chat.id < 0:
        await msg.answer('Adios)')

    else:
        rank = db.get_data(user.id, 'rank')
        caption = conf.get_msg('profile').format(
            user.first_name, conf.ranks.get(rank)[0],
            conf.ranks.get(rank)[1], user.id,
            db.get_data(user.id, 'balance'),
            db.get_data(user.id, 'added'),
        )

        with open(f'ranks/{rank}.jpg', 'rb') as photo:
            await msg.answer_photo(
                photo=photo,
                caption=caption
            )


@dp.message_handler(commands=['ranks'])
async def all_ranks(msg: types.Message):
    user = msg.from_user
    chat = msg.chat

    if chat.id < 0:
        await msg.answer('Adios)')

    else:
        await msg.answer(
            '<b>Список всех рангов на сервере:</b>'
        )

        sleep(0.5)

        for i in conf.ranks.items():
            rank = i[0]
            caption = f'Ранг <b>{i[1][0].title()}</b> [уровень {i[1][1]}/7]'

            with open(f'ranks/{rank}.jpg', 'rb') as photo:
                await msg.answer_photo(
                    photo=photo,
                    caption=caption
                )
                sleep(0.2)


# -------------------------------------------------- #


if __name__ == '__main__':
    executor.start_polling(
        dp, skip_updates=True
    )

