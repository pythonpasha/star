import asyncio
import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot import types
# соня 7709203326
# Инициализация асинхронного бота
TOKEN = '8166482888:AAH6jZFh-W7yLp62kRuaaTlBpRLCcYEf4dY'
bot = AsyncTeleBot(TOKEN)

card1 = 1
card2 = 2
phone1 = 0
phone2 = 1
us1 = '@aaa9281'
us2 = '@prachettttt'
chat1 = 5876670696
chat2 = 5983729162
# Обработчик команды /start
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    print(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/купить_звёзды")
    btn2 = types.KeyboardButton("/посмотреть отзывы")
    markup.add(btn1, btn2)

    await bot.reply_to(
        message,
        "Добро пожаловать! Выберите действие:",
        reply_markup=markup
    )


@bot.message_handler(commands=["купить_звёзды"])
async def send_welcome(message):
    stars = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("13⭐/40р", callback_data="13")
    btn2 = types.InlineKeyboardButton("26⭐/65р", callback_data="26")
    btn3 = types.InlineKeyboardButton("43⭐/90р", callback_data="43")
    btn4 = types.InlineKeyboardButton("100⭐/170р", callback_data="100")
    btn5 = types.InlineKeyboardButton("150⭐/270р", callback_data="150")
    btn6 = types.InlineKeyboardButton("250⭐/425р", callback_data="250")
    stars.add(btn1, btn2, btn3, btn4, btn5, btn6)

    await bot.send_message(
        message.chat.id,
        f'''Приветствую, дорогой покупатель здесь можешь купить звезды
        
оплатить можно на несколько карт:

карта1: {card1} время работы
карта2: {card2} время работы


при оплате звёзды поступают за 15(возможно меньше) минут

если возникли вопросы:

{us1} время работы
{us2} время работы


выбери количество звёзд:
        ''',
        reply_markup=stars
    )




# Обработчик callback-запросов
@bot.callback_query_handler(func=lambda call: True)
async def callback_handler(call):
    if call.data == "13":
        await bot.send_message(
            chat1,
                '@' + call.from_user.username + ' хочет купить звезды: ' +call.data
        )
        await bot.send_message(
            chat2,
                '@' + call.from_user.username + ' хочет купить звезды: ' +call.data
        )
        await bot.send_message(
            call.message.chat.id,
            "ожидайте",
        )

    elif call.data == "26":
        await bot.send_message(
            chat1,
                '@' + call.from_user.username + ' хочет купить звезды: ' +call.data
        )
        await bot.send_message(
            chat2,
                '@' + call.from_user.username + ' хочет купить звезды: ' +call.data
        )
        await bot.send_message(
            call.message.chat.id,
            "ожидайте",
        )

    elif call.data == "43":
        await bot.send_message(
            chat1,
                '@' + call.from_user.username + ' хочет купить звезды: ' +call.data
        )
        await bot.send_message(
            chat2,
                '@' + call.from_user.username + ' хочет купить звезды: ' +call.data
        )
        await bot.send_message(
            call.message.chat.id,
            "ожидайте",
        )

    elif call.data == "100":
        await bot.send_message(
            chat1,
                '@' + call.from_user.username + ' хочет купить звезды: ' +call.data
        )
        await bot.send_message(
            chat2,
                '@' + call.from_user.username + ' хочет купить звезды: ' +call.data
        )
        await bot.send_message(
            call.message.chat.id,
            "ожидайте",
        )

    elif call.data == "150":
        await bot.send_message(
            chat1,
                '@' + call.from_user.username + ' хочет купить звезды: ' +call.data
        )
        await bot.send_message(
            chat2,
                '@' + call.from_user.username + ' хочет купить звезды: ' +call.data
        )
        await bot.send_message(
            call.message.chat.id,
            "ожидайте",
        )

    elif call.data == "250":
        await bot.send_message(
            chat1,
                '@' + call.from_user.username + ' хочет купить звезды:' +call.data
        )
        await bot.send_message(
            chat2,
                '@' + call.from_user.username + ' хочет купить звезды:' +call.data
        )
        await bot.send_message(
            call.message.chat.id,
            "ожидайте",
        )


# Запуск бота
async def main():
    await bot.infinity_polling()


if __name__ == '__main__':
    asyncio.run(main())

