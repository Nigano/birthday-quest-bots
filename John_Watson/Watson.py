import asyncio
from aiogram import Bot, types, Dispatcher, Router, F


BOT_TOKEN = input("Введите токен бота Watson: ")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

# ЧАСТЬ 1: Начало приключений
#-4812049115 -4812049115
@dp.message(F.text.contains("Привет") | F.text.contains("привет"))
async def part1(message: types.Message):

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(2.5) #2.5
    await message.reply("Рад видеть вас здесь, Мис! Спасибо, что присоединились к нам")

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(14) #3
    await bot.send_message(text="Пропал не только он. Исчез уникальный артефакт — источник редкого сияния, который он "
                                "хранил", chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(6.5) #2.5
    await bot.send_message(text="Холмс называл его «Блеск»", chat_id=message.chat.id)


#ЧАСТЬ 2: Первая загадка
@dp.message(F.text.contains("Схем") | F.text.contains("схем"))
async def part2(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(2.5)
    await bot.send_message(text="Что вы обнаружили? Неужели там есть скрытое послание? Потрясающе! Это схема! Похоже "
                                "на чертеж. Лестрейд, у нас же есть опись вещей, связанных с этим делом! Среди них "
                                "значатся свечи: 10 малых и 3 больших.", chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(20)
    await bot.send_message(text="Холмс явно хотел, чтобы вы воссоздали этот чертеж с их помощью",
                           chat_id=message.chat.id)

#ЧАСТЬ 3: Шифр Свечей
@dp.message(F.photo)
async def part3(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(2.5)
    await bot.send_message(text="Браво! Фотография получена. Вы воссоздали схему в точности! Позвольте мне свериться "
                                "с его записями... ",
                           chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(7)
    await bot.send_message(text="Так, так, так... Гениально!!!", chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(2)
    await bot.send_message(text="Лестрейд, вы понимаете? Это не просто "
                                "схема! Три большие свечи — это точки отсчета. Форма, которую образуют малые...  ",
                           chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(8.5)
    await bot.send_message(text="Да это же... Это похоже на первые буквы латинского слова «Lumen» — «Свет»! Или...",
                           chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(6.5)
    await bot.send_message(text="Боже! Это же символ, который Холмс использовал для обозначения кода «S-I-L-V-E-R»! "
                                "Серебро, 047-й элемент! Он вел нас к серебру", chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(19.5)
    await bot.send_message(text="Библиотеку... Книги! Разумеется! Он говорил: «Самая надежная сокровищница — это "
                                "книжная полка,"
                                " ибо никто не ищет сокровищ в словах»",
                           chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(9)
    await bot.send_message(text="У него была одна особая книга, толстый том. Он "
                                "всегда держал его на видном месте. Но мы не нашли в ней ничего примечательного. ",
                           chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(11.5)
    await bot.send_message(text="Мисс, вам нужно найти эту книгу. Она должна быть у вас. Холмс, должно быть, "
                                "предусмотрел и это. Это ключевая улика. Осмотрите и опишите её. На что она похожа?",
                           chat_id=message.chat.id)

#ЧАСТЬ 4: Загадочная книга
@dp.message(F.text.contains("Сейф") | F.text.contains("сейф") | F.text.contains("замок") | F.text.contains("Замок"))
async def part4(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(2.5)
    await bot.send_message(text="Так вот оно что! Это не книга, это сейф! У нас есть код?",
                           chat_id=message.chat.id)

#ЗАКЛЮЧЕНИЕ: Подарки и поздравления
@dp.message(F.text.contains("047"))
async def part5(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(2.5)
    await bot.send_message(text="Невероятно! Вы раскрыли дело! Вы нашли «Запертый Блеск»! Это же великолепные "
                                "украшения... Так вот что охранял "
                                "Холмс! Это был не пропавший артефакт, а ваш подарок! Всё это он устроил "
                                "лично для вас! Он предвидел, что только вы сможете дойти до конца!",
                           chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(17)
    await bot.send_message(text="Лестрейд, вы понимаете? Не было никакого преступления! Было гениально спланированное "
                                "поздравление!",
                           chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(23)
    await bot.send_message(text="И от меня самые теплые поздравления! И, кажется, Холмс оставил для вас финальную "
                                "записку внутри. Он хотел, чтобы вы прочли ее именно в этот момент",
                           chat_id=message.chat.id)

    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(11.5)
    await bot.send_message(text="Счастья вам и, как говаривал Шерлок, помните: \n«Жизнь — это цепь загадок, а истинное сокровище — "
                                "умение их разгадывать»",
                           chat_id=message.chat.id)


dp.include_router(router)


async def main():
    try:
        print('Ватсон готов!')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        print("Сессия бота закрыта")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен пользователем")
