import telebot
import config
from telebot import types
from requests import get
from string import Template
bot=telebot.TeleBot(config.token)
user_dict=[]
class user:
 def _init_(self, city):
    self.city = city
    keys = ['user', 'fullname']
    for key in keys:
        self.key = None

        
@bot.message_handler(commands=['start'])
def menu(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Купить валюту")
        item2=types.KeyboardButton("Помощь")
        item3=types.KeyboardButton("Гарантия/Отзывы")
        markup.add(item1, item2, item3)
        msg=bot.send_message(message.chat.id,' Приветствую в магазине Silaev Store!\n Здесь ты можешь быстро и надежно купить монеты и аккаунты для твоей любимой игры.\n Не забудь ввести ПРОМОКОД при заказе) ',reply_markup=markup)
        bot.register_next_step_handler(msg, game_step)
    

def game_step(message):
    if  (message.text)=="Купить валюту":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("NBA 2K22")
        item2=types.KeyboardButton("NBA 2K21")
        item3=types.KeyboardButton("NBA Live Mobile")
        item4=types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4)
        msg=bot.send_message(message.chat.id,'Выбери игру',reply_markup=markup)
        bot.register_next_step_handler(msg, platform_step)

    elif(message.text)=="Гарантия/Отзывы":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Назад")
        markup.add(item1)
        msg=bot.send_message(message.chat.id,'@silaev_reviews',reply_markup=markup)
        bot.register_next_step_handler(msg, platform_step)

    elif(message.text)=="Помощь":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Назад")
        markup.add(item1)
        msg=bot.send_message(message.chat.id,'Коротко, в одном сообщении, напиши о своей проблеме и админ вскоре свяжется с тобой',reply_markup=markup)
        bot.register_next_step_handler(msg, pomoch)

def pomoch(message):
       user.pomoch=message.text

       if(message.text)=="Назад":
           msg=bot.send_message(message.chat.id,'Нажми кнопку "Назад" еще раз, чтобы подтвердить')
           bot.register_next_step_handler(msg,menu)
       else:
           markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
           item1=types.KeyboardButton("Главное меню")
           markup.add(item1)
           msg=bot.send_message(message.chat.id,getRegData2(user,message.from_user.first_name, 'Ваша заявка о проблеме была отправлена админу, он скоро свяжется с Вами:'),parse_mode="Markdown",reply_markup=markup)
           bot.send_message(config.owner, getRegData2(user, 'Сообщение о проблеме от пользователя: ',message.from_user.username),parse_mode="Markdown")
           bot.register_next_step_handler(msg,menu)
        
	

def platform_step(message):
    user.game=message.text
    
    if(message.text)=="NBA 2K22":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("PC")
        item2=types.KeyboardButton("PS4/5")
        item3=types.KeyboardButton("Xbox")
        item4=types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4)
        msg=bot.send_message(message.chat.id,'Выбери платформу',reply_markup=markup)
        bot.register_next_step_handler(msg, currency_step)


    elif(message.text)=="NBA 2K21":
     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
     item1=types.KeyboardButton("💻PC")
     item2=types.KeyboardButton("Назад")
     markup.add(item1,item2)
     msg=bot.send_message(message.chat.id,'Выбери платформу',reply_markup=markup)
     bot.register_next_step_handler(msg, currency_step)


    elif(message.text)=="NBA Live Mobile":
     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
     item1=types.KeyboardButton("IOS")
     item2=types.KeyboardButton("Android")
     item3=types.KeyboardButton("Назад")
     markup.add(item1, item2, item3)
     msg=bot.send_message(message.chat.id,'Выбери платформу',reply_markup=markup)
     bot.register_next_step_handler(msg, currency_step)


    elif(message.text)=="Назад":
     msg=bot.send_message(message.chat.id,'Нажми кнопку "Назад" еще раз, чтобы подтвердить')
     bot.register_next_step_handler(msg,menu)


def currency_step(message):
    user.platform=message.text
    
    if(message.text)=="IOS":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Coins")
        item2=types.KeyboardButton("Аккаунты")
        item3=types.KeyboardButton("Назад")
        markup.add(item1, item2,item3)
        msg=bot.send_message(message.chat.id,'Выбери валюту',reply_markup=markup)
        bot.register_next_step_handler(msg, ammount_step)

    elif(message.text)=="Назад":
        msg=bot.send_message(message.chat.id,'Нажми кнопку "Назад" еще раз, чтобы подтвердить')
        bot.register_next_step_handler(msg,menu)

    elif(message.text)=="Android":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Coins")
        item2=types.KeyboardButton("Аккаунты")
        item3=types.KeyboardButton("Назад")
        markup.add(item1, item2,item3)
        msg=bot.send_message(message.chat.id,'Выбери валюту',reply_markup=markup)
        bot.register_next_step_handler(msg, ammount_step)


    elif(message.text)=="💻PC":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("💵VC")
        item2=types.KeyboardButton("Назад")
        markup.add(item1,item2)
        msg=bot.send_message(message.chat.id,'Выбери валюту',reply_markup=markup)
        bot.register_next_step_handler(msg, ammount_step)

    elif(message.text)=="PC":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("MT")
        item2=types.KeyboardButton("VC")
        item3=types.KeyboardButton("аккаунты")
        item4=types.KeyboardButton("Назад")
        markup.add(item1, item2,item3,item4)
        msg=bot.send_message(message.chat.id,'Выбери валюту',reply_markup=markup)
        bot.register_next_step_handler(msg, ammount_step)

    elif(message.text)=="Xbox":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("MT")
        item2=types.KeyboardButton("⭐️VC")
        item3=types.KeyboardButton("Аккаунты")
        item4=types.KeyboardButton("Назад")
        markup.add(item1, item2,item3,item4)
        msg=bot.send_message(message.chat.id,'Выбери валюту',reply_markup=markup)
        bot.register_next_step_handler(msg, ammount_step)


    elif(message.text)=="PS4/5":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("MT")
        item2=types.KeyboardButton("⚡VC")
        item3=types.KeyboardButton("Аккаунты")
        item4=types.KeyboardButton("Назад")
        markup.add(item1, item2,item3,item4)
        msg=bot.send_message(message.chat.id,'Выбери валюту',reply_markup=markup)
        bot.register_next_step_handler(msg, ammount_step)     


def ammount_step(message):
    user.currency=message.text

    if(message.text)=="Coins":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("1.000.000-550 руб")
        item2=types.KeyboardButton("1.500.000-825 руб")
        item3=types.KeyboardButton("2.000.000-1100 руб")
        item4=types.KeyboardButton("3.000.000-1500 руб")
        item5=types.KeyboardButton("4.000.000-2000 руб")
        item5=types.KeyboardButton("5.000.000-2500 руб")
        item6=types.KeyboardButton("Назад")
        markup.add(item1, item2,item3,item4,item5,item6)
        msg=bot.send_message(message.chat.id,'Выбери количество:\n 1.000 000 - 550 руб\n 1.500 000 - 825 руб\n 2.000 000 - 1100 руб\n 3.000 000 - 1500 руб\n 4.000 000 - 2000 руб\n 5.000 000 - 2500 руб',reply_markup=markup)
        bot.register_next_step_handler(msg, instr)
        


    elif(message.text)=="аккаунты":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Аккаунт - 3500 руб")
        item2=types.KeyboardButton("Назад")
        markup.add(item1, item2)
        msg=bot.send_photo(message.chat.id,'https://ibb.co/yF21fHp','В наличии:',reply_markup=markup)
        bot.register_next_step_handler(msg, instr)


    elif(message.text)=="⚡VC":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        item1=types.KeyboardButton("200.000 - 2800 руб")
        item2=types.KeyboardButton("300.000 - 4200 руб")
        item3=types.KeyboardButton("400.000 - 5600 руб")
        item4=types.KeyboardButton("500.000 - 6500 руб")
        item5=types.KeyboardButton("Назад")
        markup.add(item1, item2,item3,item4,item5)
        msg=bot.send_message(message.chat.id,'Выбери количество:\n 200.000 - 2800 руб\n 300.000 - 4200 руб\n 400.000 - 5600 руб\n 500.000 - 6500 руб',reply_markup=markup)
        bot.register_next_step_handler(msg, instr)


    elif(message.text)=="💵VC":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("200.000 - 1100 руб")
        item2=types.KeyboardButton("300.000 - 1650 руб")
        item3=types.KeyboardButton("400.000 - 2200 руб")
        item4=types.KeyboardButton("500.000 - 2500 руб")
        item5=types.KeyboardButton("Назад")
        markup.add(item1, item2,item3,item4,item5)
        msg=bot.send_message(message.chat.id,'Выбери количество:\n 200.000 - 1100 руб\n 300.000 - 1650 руб\n 400.000 - 2200 руб\n 500.000 - 2500 руб',reply_markup=markup)
        bot.register_next_step_handler(msg, instr)

    elif(message.text)=="VC":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("100.000 - 1200 руб")
        item2=types.KeyboardButton("200.000 - 2200 руб")
        item3=types.KeyboardButton("300.000 - 4400 руб")
        item4=types.KeyboardButton("400.000 - 5000 руб")
        item5=types.KeyboardButton("500.000 - 6500 руб")
        item6=types.KeyboardButton("Назад")
        markup.add(item1, item2,item3,item4,item5,item6)
        msg=bot.send_message(message.chat.id,'Выбери количество:\n 100.000 - 1200 руб\n 200.000 - 2200 руб\n 300.000 - 4400 руб\n 400.000 - 5000 руб\n 500.000 - 6500 руб',reply_markup=markup)
        bot.register_next_step_handler(msg, instr)
        
    elif(message.text)=="MT" or(message.text)== "⭐️VC" or (message.text)=="Аккаунты":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        item1=types.KeyboardButton("Хорошо")
        markup.add(item1)
        msg=bot.send_message(message.chat.id,'В ближайшее время с вами свяжется администратор и подскажет курс/цену',reply_markup=markup)
        bot.register_next_step_handler(msg, MTorAcc)

    elif(message.text)=="Назад":
        msg=bot.send_message(message.chat.id,'Нажми кнопку "Назад" еще раз, чтобы подтвердить')
        bot.register_next_step_handler(msg,menu)



def instr(message):
    user.ammount=message.text
    user.ammount_ammount=user.ammount[0:9]
    user.ammount_price=user.ammount[10:14]

#NBA PS4/PS5-------------------------------------------------------------------------------------------------------------------------------------------------------
    if(message.text)=="200.000 - 2800 руб" or (message.text)=="300.000 - 4200 руб" or (message.text)=="400.000 - 5600 руб" or (message.text)=="500.000 - 6500 руб":
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1=types.KeyboardButton("Я ознакомился")
            markup.add(item1)
            msg=bot.send_message(message.chat.id,'''
1.Вы переводите деньги на один из моих кошельков (QIWI, карта Тинькофф, Карта Сбербанк, оплата мобильной связи)
2.Отправляете данные для входа в аккаунт PSN (логин и пароль)
3.Ожидаете в течении часа пока с Вами свяжется Администратор, подтвердит заказ и оплату''',reply_markup=markup)
            bot.register_next_step_handler(msg, promo)
        


    elif(message.text)=="Назад":
        msg=bot.send_message(message.chat.id,'Нажми кнопку "Назад" еще раз, чтобы подтвердить')
        bot.register_next_step_handler(msg,menu)


#NBA PC 2021-------------------------------------------------------------------------------------------------------------------------------------------------------
    elif(message.text)=="200.000 - 1100 руб" or (message.text)=="300.000 - 1650 руб" or (message.text)=="400.000 - 2200 руб" or (message.text)=="500.000 - 2500 руб":
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1=types.KeyboardButton("Я ознакомился")
            markup.add(item1)
            msg=bot.send_message(message.chat.id,'''
1.Вы переводите деньги на один из моих кошельков (QIWI, карта Тинькофф, Карта Сбербанк, оплата мобильной связи)\n
2.Отправляете данные для входа в аккаунт (логин и пароль)\n
3.Ожидаете в течении часа пока с Вами свяжется Администратор, подтвердит заказ и оплату\n
ВАЖНО: вы должны отключить стим гард, он мешает накрутке\n
Как отключить стим гард?\n1. Заходим в настройки аккаунта \n
2. Нажимаем « Об аккаунте»\n
3. Удаляем аутентификатор с телефона \n
4. После этого выбираем отключить стим гард, далее вам приходит подтверждение на почту, готово ✅''',reply_markup=markup)
            
            bot.register_next_step_handler(msg, promo)


#PC NBA 2022-------------------------------------------------------------------------------------------------------------------------------------------------------

    elif(message.text)=="100.000 - 1200 руб" or (message.text)=="200.000 - 2200 руб" or (message.text)=="300.000 - 4400 руб" or (message.text)=="500.000 - 5000 руб" or (message.text)=="700.000 - 6500 руб":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1=types.KeyboardButton("Я ознакомился")
        markup.add(item1)
        msg=bot.send_message(message.chat.id,'1.Вы переводите деньги на один из моих кошельков (QIWI, карта Тинькофф, Карта Сбербанк, оплата мобильной связи)\n 2.Отправляете данные для входа в аккаунт (логин и пароль)\n 3.Ожидаете в течении часа пока с Вами свяжется Администратор, подтвердит заказ и оплату\n ВАЖНО: вы должны отключить стим гард, он мешает накрутке\n Как отключить стим гард?\n1. Заходим в настройки аккаунта \n 2. Нажимаем « Об аккаунте»\n 3. Удаляем аутентификатор с телефона \n 4. После этого выбираем отключить стим гард, далее вам приходит подтверждение на почту, готово ✅\n ВНИМАНИЕ: Если вы играете в Epic Games, то там нет гарда и отключать ничего не надо!',reply_markup=markup)
        bot.register_next_step_handler(msg, promo)



#NBA Mobile IOS Android--------------------------------------------------------------------------------------------------------------------------------------------
    elif(message.text)=="1.000.000-550 руб" or (message.text)== "1.500.000-825 руб" or (message.text)== "2.000.000-1100 руб" or (message.text)== "3.000.000-1500 руб" or (message.text)== "4.000.000-2000 руб" or (message.text)== "5.000.000-2500 руб":
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1=types.KeyboardButton("Я ознакомился")
            markup.add(item1)
            msg=bot.send_message(message.chat.id,'Покупка происходит следующим образом:\n 1.Вы переводите деньги на один из моих кошельков (QIWI, карта Тинькофф, Карта Сбербанк, оплата мобильной связи)\n 2.Отправляете данные для входа в аккаунт фейсбука или гугл плей (логин и пароль)\n 3.Ожидаете в течении часа пока с Вами свяжется Администратор, подтвердит заказ и оплату\n ВАЖНО: Нельзя заходить на аккаунт во время накрутки, т.к при заходе в игру с 2-ух девайсов вылетает игра',reply_markup=markup)
            bot.register_next_step_handler(msg, promo)

#NBA 2K22 Account----------------------------------------------------------------------------------------------------------------------------------------------------

    elif(message.text)=="Аккаунт - 3500 руб":
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1=types.KeyboardButton("Я ознакомился")
            markup.add(item1)
            msg=bot.send_message(message.chat.id,'Покупка происходит следующим образом:\n 1.Вы переводите деньги на один из моих кошельков (QIWI, карта Тинькофф, Карта Сбербанк, оплата мобильной связи)\n 2.Ожидаете в течении часа пока с Вами свяжется Администратор, подтвердит заказ и оплату.',reply_markup=markup)
            bot.register_next_step_handler(msg, promo)






def promo(message):
    msg=bot.send_message(message.chat.id,'Введи промокод (если у тебя есть)')
    bot.register_next_step_handler(msg, process_send_step)

def process_send_step(message):
    user.promo=message.text
    if(message.text.lower())=="old" or (message.text.lower())=="black":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Подтвердить")
        item2=types.KeyboardButton("Назад")
        markup.add(item1,item2)
        bot.send_message(config.owner, getRegData5(user, 'Предварительная Заявка от пользователя ',message.from_user.username),parse_mode="Markdown")
        msg=bot.send_message(message.chat.id,getRegData5(user,message.from_user.first_name, 'Ваш заказ:'),parse_mode="Markdown",reply_markup=markup)
        bot.register_next_step_handler(msg, pay)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Подтвердить")
        item2=types.KeyboardButton("Назад")
        markup.add(item1,item2)
        msg=bot.send_message(message.chat.id,getRegData1(user,message.from_user.first_name, 'Ваш заказ:'),parse_mode="Markdown",reply_markup=markup)
        bot.register_next_step_handler(msg, pay)

    if(message.text)=="Назад":
        msg=bot.send_message(message.chat.id,'Нажми кнопку "Назад" еще раз, чтобы подтвердить')
        bot.register_next_step_handler(msg,menu)

def pay(message):
    if(message.text)=="Подтвердить":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1=types.KeyboardButton("✅Оплатил")
        item2=types.KeyboardButton("Назад")
        markup.add(item1,item2)
        msg=bot.send_message(message.chat.id,'Оплати выбранную тобой сумму по следующим реквизитам и нажми "Оплатил"\n QIWI +79114553016\n Моб.связь +79114553016 МТС\n Тинькофф 4377723760491047\n Сбербанк 4276200734240794',reply_markup=markup)
        bot.register_next_step_handler(msg, login)

    elif(message.text)=="Назад":
        msg=bot.send_message(message.chat.id,'Нажми кнопку "Назад" еще раз, чтобы подтвердить')
        bot.register_next_step_handler(msg,menu)


def login(message):
    paystatus=message.text
    if(message.text)=="Назад":
        msg=bot.send_message(message.chat.id,'Нажми кнопку "Назад" еще раз, чтобы подтвердить',reply_markup=markup)
        bot.register_next_step_handler(msg,menu)

    elif(user.currency)=="аккаунты":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Отправить заявку")
        markup.add(item1)
        msg=bot.send_message(message.chat.id,'Отлично!',reply_markup=markup)
        bot.register_next_step_handler(msg,confirm_step2)
                                       
    
    
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Назад")
        markup.add(item1)
        msg=bot.send_message(message.chat.id,'Введи свой логин',reply_markup=markup)
        bot.register_next_step_handler(msg, password)


def password(message):
    user.login=message.text
    

    if(message.text)=="Назад":
        msg=bot.send_message(message.chat.id,'Нажми кнопку "Назад" еще раз, чтобы подтвердить')
        bot.register_next_step_handler(msg,menu)
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Назад")
        markup.add(item1)
        msg=bot.send_message(message.chat.id,'Введи свой пароль',reply_markup=markup)
        bot.register_next_step_handler(msg, confirm_step)


def MTorAcc(message):
    bot.send_message(config.owner, getRegData3(user, 'Заявка от пользователя ',message.from_user.username),parse_mode="Markdown")
    msg=bot.send_message(message.chat.id,getRegData3(user, message.from_user.first_name,'Ваш заказ принят, ожидайте подтверждение выполнения от администратора, он напишет Вам в ЛС.  Если вы сделали заказ, а с вами не связались в течение часа, то сообщите  сюда @silaevstore'),parse_mode="Markdown")
    bot.register_next_step_handler(msg,menu)

#Confirm for all----------------------------------------------------------------------------------------------------------------------------------------------------
def confirm_step(message):
    if(message.text)=="Назад":
        msg=bot.send_message(message.chat.id,'Нажми кнопку "Назад" еще раз, чтобы подтвердить')
        bot.register_next_step_handler(msg,menu)
    else:
        user.password=message.text
        bot.send_message(config.owner, getRegData(user, 'Заявка от пользователя ',message.from_user.username),parse_mode="Markdown")
        msg=bot.send_message(message.chat.id,getRegData6(user, message.from_user.first_name,'Ваш заказ принят, ожидайте подтверждение выполнения от админа, он напишет Вам в ЛС'),parse_mode="Markdown")
        bot.register_next_step_handler(msg,menu)

#Comfirm for account NBA 2K22---------------------------------------------------------------------------------------------------------------------------------------

        
def confirm_step2(message):
    bot.send_message(config.owner, getRegData5(user, 'Заявка от пользователя ',message.from_user.username),parse_mode="Markdown")
    msg=bot.send_message(message.chat.id,getRegData5(user, message.from_user.first_name,'Ваш заказ принят, ожидайте подтверждение выполнения от админа, он напишет Вам в ЛС'),parse_mode="Markdown")
    bot.register_next_step_handler(msg,menu)

#If user chose MT------------------------------------------------------------------------------------------------------------------------------------------------------
def getRegData3(user,title,name):
    t = Template('$title *$name*\n\n Игра: *$usergame*\n Платформа: *$platform*\n Валюта: *$currency*')
    return t.substitute({'title':title,'name': name,'usergame':user.game,'platform':user.platform,'currency':user.currency})


#If user pressed help button-------------------------------------------------------------------------------------------------------------------------------------------
def getRegData2(user,title,name):
    t = Template('$title *$name*\n Проблема: *$pomoch*')
    return t.substitute({'title':title,'name': name,'pomoch':user.pomoch})

#IF promocod is not correct or not used
def getRegData1(user,title,name):
        t = Template('$title *$name*\n Игра: *$usergame*\n Платформа: *$platform*\n Товар: *$currency*\n Колличество: *$ammount*\n Цена: *$ammount_price*')
        return t.substitute({'title':title,'name': name,'usergame':user.game,'platform':user.platform,'currency':user.currency, 'ammount':(user.ammount_ammount), 'ammount_price':(user.ammount_price) })


#If correct promocod is used---------------------------------------------------------------------------------------------------------------------------------------------------
def getRegData5(user,title,name):
        t = Template('$title *$name*\n Игра: *$usergame*\n Платформа: *$platform*\n Товар: *$currency*\n Колличество: *$ammount*\n К оплате: *$ammount_price*\n Промокод: *$promo*' )
        return t.substitute({'title':title,'name': name,'usergame':user.game,'platform':user.platform,'currency':user.currency, 'ammount':(user.ammount_ammount), 'ammount_price':int(user.ammount_price)*0.9, 'promo': user.promo})

#total last order notification for admin-----------------------------------------------------------------------------------------------------------------------------------------
def getRegData(user,title,name):
        t = Template('$title *$name*\n Игра: *$usergame*\n Платформа: *$platform*\n Товар: *$currency*\n Колличество: *$ammount*\n Логин: *$login*\n Пароль: *$password*\n Промокод: *$promo*')
        return t.substitute({'title':title,'name': name,'usergame':user.game,'platform':user.platform,'currency':user.currency, 'ammount':user.ammount, 'login':user.login, 'password':user.password, 'promo': user.promo})

#total last order notification for user--------------------------------------------------------------------------------------------------------------------------------
def getRegData6(user,title,name):
        t = Template('$title *$name*\n Игра: *$usergame*\n Платформа: *$platform*\n Товар: *$currency*\n Колличество: *$ammount*\n Логин: *$login*\n Промокод: *$promo*')
        return t.substitute({'title':title,'name': name,'usergame':user.game,'platform':user.platform,'currency':user.currency, 'ammount':user.ammount[0:8],'login':user.login,'promo': user.promo})

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()


bot.infinity_polling()

        
