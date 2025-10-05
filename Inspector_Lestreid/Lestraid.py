import asyncio
import aiogram
from aiogram import Bot, types, Router, F
from aiogram.types import FSInputFile

BOT_TOKEN = input("Введите токен бота Lestraid: ")
bot1 = Bot(token=BOT_TOKEN)
dp1 = aiogram.Dispatcher()
router1 = Router()


#ЧАСТЬ 1: Начало приключений

@dp1.message(F.text.contains("Привет") | F.text.contains("привет"))
async def first_part(message: types.Message):
    await bot1.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(7.5) #2.5
    await bot1.send_message(text="Доброй ночи! Как видите, нам приходится действовать не по протоколу",
                            chat_id=message.chat.id)

    await bot1.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(5) #2.5
    await bot1.send_message(text="Внезапное исчезновение — это уже слишком даже для Холмса", chat_id=message.chat.id)

    await bot1.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(12.5) #3
    await bot1.send_message(text="Все улики обрывочны. Вот первая из них, оставленная, по-видимому, самим Холмсом ",
                            chat_id=message.chat.id)

    await bot1.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(5.5) #3
    await bot1.send_message(text="Вам стоит поискать подобную у себя дома. Наверняка где-то есть второй её экземпляр:",
                            chat_id=message.chat.id)

    await bot1.send_chat_action(chat_id=message.chat.id, action="upload_photo")
    await asyncio.sleep(6.5) #5
    await bot1.send_photo(chat_id=message.chat.id, photo=FSInputFile(r"decorations\конверт.png"),
                          caption="Он как-то обмолвился, что «истинный свет является лишь тем, кто умеет смотреть в "
                                  "темноту». Изучите это")


#ЧАСТЬ 2: Первая загадка
@dp1.message(F.text.contains("Схема") | F.text.contains("схема"))
async def second_part(message: types.Message):
    await bot1.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(18.5)
    await bot1.send_message(text="Да, коробка со свечами должна быть у вас ", chat_id=message.chat.id)

    await bot1.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(8.5)
    await bot1.send_message(text="Хм... Воссоздать схему... Звучит как одна из его театральных выходок. Но другого "
                                 "выхода у нас нет. Ждем ваше фото для протокола", chat_id=message.chat.id)


#ЧАСТЬ 3: Шифр Свечей
@dp1.message(F.photo)
async def part3(message: types.Message):
    await bot1.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(36.5) #10 секунд
    await bot1.send_message(text="Серебро... В деле упоминался серебряный ларец, но мы его так и не нашли, даже всю "
                                 "его домашнюю библиотеку обыскали",
                            chat_id=message.chat.id)

#ЗАКЛЮЧЕНИЕ: Подарки и поздравления
@dp1.message(F.text.contains("047"))
async def part5(message: types.Message):
    await bot1.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(24.5)
    await bot1.send_message(text="Что ж... Черт возьми. Я обычно не одобряю его методы, но на этот раз... Я снимаю "
                                 "шляпу. И перед Холмсом, и перед вами",
                            chat_id=message.chat.id)

    await bot1.send_chat_action(chat_id=message.chat.id, action="typing")
    await asyncio.sleep(10)
    await bot1.send_message(text="Вы провели расследование блестяще. Поздравляю "
                                 "с Днем Рождения и с успешным раскрытием дела!",
                            chat_id=message.chat.id)


dp1.include_router(router1)


async def main():
    try:
        print('Лестрейд готов!')
        await dp1.start_polling(bot1)
    finally:
        await bot1.session.close()
        print("Сессия бота закрыта")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен пользователем")
