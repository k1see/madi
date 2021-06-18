import telebot
from telebot import types
import requests
TOKEN = '1700542513:AAGtNzRTCw65JZoUKEkg1jVhf_Uvtu_0ry4'

WEATHER_TOKEN = "e6e951b131596e6a187d51ea54fd9732"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help', 'weather', 'film', 'find', 'profile', 'calc'])
def start_bot(message):
    if message.text.lower() == '/start':
        keyboard = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Шутеичка',callback_data= 'joke')
        google = types.InlineKeyboardButton("го в гугл", url="https://google.ru")
        keyboard.add(btn)
        keyboard.add(google)
        bot.send_message(message.chat.id,
                        'всем привет!\n Я новый бот',
                        reply_markup=keyboard)
    

    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'здраствуй!')
        bot.send_message(message.chat.id, 'вот список команд')
        bot.send_message(message.chat.id, '/help')
        bot.send_message(message.chat.id, '/weather')
        bot.send_message(message.chat.id, '/film')
        bot.send_message(message.chat.id, '/find')
        bot.send_message(message.chat.id, '/profile')
        bot.send_message(message.chat.id, '/calc')
        
    elif message.text.lower() == '/weather':
        bot.send_message(message.chat.id, 'Вы в разделе погоды')
        bot.send_message(message.chat.id, "введите названия города")
        bot.register_next_step_handler(message,weather_menu)
        
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id, 'вы в разделе помощь')
    
    elif message.text.lower() == '/film':
        bot.send_message(message.chat.id, 'какой жанр вы хотите посмотреть')
        
    elif message.text.lower() == '/find':
        bot.send_message(message.chat.id, 'вы хотите найти')
        
    elif message.text.lower() == '/profile':
        bot.send_message(message.chat.id, 'вы хотите заполнить профиль?')
        bot.send_message(message.chat.id, ' свое имя:')
        bot.register_next_step_handler(message, enter_name)
        
    elif message.text.lower() == '/calc':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('плюс')
        btn2 = types.KeyboardButton('минус')
        btn3 = types.KeyboardButton('делить')
        btn4 = types.KeyboardButton('умножить')
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        bot.send_message(message.chat.id,
                         'выберите действие:',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, calculate_choose)
def calculate_choose(message):
    if message.text.lower() == 'плюс':
        bot.send_message(message.chat.id, "что вы хотите сложить?")
        bot.send_message(message.chat.id, "введите два числа через пробел")
        bot.register_next_step_handler(message, calculate_result_plus)
    elif message.text.lower() == 'минус':
        bot.send_message(message.chat.id, "что вы хотите вычеслить?")
        bot.send_message(message.chat.id, "введите два числа через пробел")
        bot.register_next_step_handler(message, calculate_result_minus)
    elif message.text.lower() == 'делить':
        bot.send_message(message.chat.id, "что вы хотите разделить")
        bot.send_message(message.chat.id, "введите два числа через пробел")
        bot.register_next_step_handler(message, calculate_result_divide)
    elif message.text.lower() == 'умножить':
        bot.send_message(message.chat.id, "что вы хотите умножить?")
        bot.send_message(message.chat.id, "введите два числа через пробел")
        bot.register_next_step_handler(message, calculate_result_multiply)
def calculate_result_plus(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f"результат {num1 + num2}")
def calculate_result_minus(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f"результат {num1 - num2}")
def calculate_result_divide(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f"результат {num1 / num2}")
def calculate_result_multiply(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f"результат {num1 * num2}")

@bot.message_handler(content_type=['text'])
def enter_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"твое имя {name}")
    bot.send_message(message.chat.id, f"какой у тебя возраст?")
    bot.register_next_step_handler(message, enter_age)
@bot.message_handler(content_type=['text'])
def enter_age(message):
    vozrast = message.text
    bot.send_message(message.chat.id, f"тебе {vozrast} лет")
    bot.send_message(message.chat.id, f"какой у тебя номер телефона?")
    bot.register_next_step_handler(message, enter_number)
@bot.message_handler(content_type=['text'])
def enter_number(message):
    nomer = message.text
    bot.send_message(message.chat.id, f"твой номер телефона: {nomer}")
    bot.send_message(message.chat.id, f"где вы живете")
    bot.register_next_step_handler(message, enter_place)
@bot.message_handler(content_type=['text'])
def enter_place(message):
    zhizn = message.text
    bot.send_message(message.chat.id, f"вы живете в {zhizn}")
    bot.send_message(message.chat.id, f"какой у вас любимый фильм?")
    bot.register_next_step_handler(message, enter_film)
@bot.message_handler(content_type=['text'])
def enter_film(message):
    kino = message.text
    bot.send_message(message.chat.id, f"ваш любимый фильм {kino}")
    bot.send_message(message.chat.id, f"вы создали свой профиль")
    
    
@bot.callback_query_handler(func=lambda x: x.data == "joke")
def joke_fn(message):
    bot.send_message(message.from_user.id, "Колобок повесился!")
    
    
def weather_menu(message):
    city = message.text
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}"
    r = requests.get(API_URL)
    w = r.json()
    bot.send_message(message.chat.id, f"В городе: {w["name"]}")
    bot.send_message(message.chat.id, f"температура: {w["main"]["temp"]-273.15}")               
    print(r.text)


bot.polling()