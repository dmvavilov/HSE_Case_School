#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import telebot
from telebot import types
from requests import get
from random import choice


# def get_proxy():
#    return {"https":"socks5h://"+choice(get("https://www.proxy-list.download/api/v1/get?type=socks5&country=US").content.split(b"\r\n")).decode()}


#telebot.apihelper.proxy = {'https': 'socks5://userproxy:password@ams3.proxy.veesecurity.com:443'}



bot = telebot.TeleBot('1282952873:AAHK5vjPyXBnEUVex9bYWw6qA9BiB3hEtOI')


name = '';
surname = '';
prog = '';

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 
                     'Привет! Я твой новый НРУг :)'
                    );
    bot.send_message(message.chat.id, 
                     'Давай познакомимся? Как тебя зовут и где ты учишься? Напиши через запятую свои имя и фамилию, а также образовательную программу, на которой ты обучаешься.'
                    )
    bot.register_next_step_handler(message, get_name)
def get_name(message): #получаем ФИО и ОП
    if message.text == '/start':
        start_message(message)
    else:
        global name;
        global surname;
        global prog;
        if len(message.text.split(',')) < 3:
            bot.send_message(message.chat.id, 
                         'Пожалуйста, напиши в формате "Иван, Иванов, Финансовые технологии и анализ данных"')
            bot.register_next_step_handler(message, get_name)
        else:
            name = message.text.split(',')[0];
            surname = message.text.split(',')[1];
            prog = message.text.split(',')[2];
            bot.send_message(message.chat.id, 
                             'Очень приятно познакомиться, ' + name + "!",
                             parse_mode= 'Markdown')
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBiw9fpGf5m6mdjw2YZ7an9CQWmHY_uwACPwIAAkf7CQzynhbp2XrNex4E')
            choice(message)
@bot.message_handler(commands=['helpme'])
def choice(message):
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('Хочу анонимно высказаться')
    itembtnv = types.KeyboardButton('Тема исследования')
    itembtnc = types.KeyboardButton('Моё расписание')
    itembtnd = types.KeyboardButton('Какие у меня дедлайны')
    itembtne = types.KeyboardButton('Ищу проект')
    itembtnl = types.KeyboardButton('Ничего не нужно')
    markup.row(itembtna, itembtnv, itembtne)
    markup.row(itembtnc, itembtnd, itembtnl)
    bot.send_message(message.chat.id, "Подскажи, с чем тебе нужна помощь?", reply_markup=markup)
    bot.register_next_step_handler(message, what_choice)
def what_choice(message):
    if message.text == 'Хочу анонимно высказаться':
        bot.send_message(message.chat.id, "Попытайся как можно *подробнее* описать в чем суть твоего обращения. Я анонимно передам его в вышестоящии субстанции. Спасибо за искренность!", parse_mode= 'Markdown')
        bot.register_next_step_handler(message, thank_you)
    elif message.text == 'Тема исследования':
        bot.send_message(message.chat.id, "Хм... Проанализировав твою успеваемость, я заметил, что ты хорошо разбираешься в *Эконометрике*, *Фондовых рынках* и *Программировании на Python*. Среди твоих интересов на платформе LMS нашел *Спорт*. Вот подходящая тема для тебя:", parse_mode= 'Markdown')
        bot.send_message(message.chat.id, "_Факторы, влияющие на динамику цен акций футбольных клубов_", parse_mode= 'Markdown')
        bot.send_message(message.chat.id, "Потенциальный научный руководитель: *Вавилов Дмитрий Мерабович*", parse_mode= 'Markdown')
        markup_2 = types.ReplyKeyboardMarkup()
        itembtyes = types.KeyboardButton('Да! Спасибо!')
        itembtno = types.KeyboardButton('Нет... Давай другую тему!')
        markup_2.row(itembtyes, itembtno)
        bot.send_message(message.chat.id, "Тебе подходит эта тема?", reply_markup=markup_2)
        bot.register_next_step_handler(message, yes_no)
    elif message.text == 'Какие у меня дедлайны':
        bot.send_message(message.chat.id, "Дорогие судьи, Ваш главный *дедлайн*: проверить наш кейс до 15 ноября!", parse_mode= 'Markdown')
        love(message)
    elif message.text == 'Моё расписание':
        bot.send_message(message.chat.id, "На этой неделе нет пар! Ура!", parse_mode= 'Markdown')
        thank_you(message)
    elif message.text == 'Ищу проект':
        petty(message)
    elif message.text == 'Ничего не нужно':
        relax(message)
        bot.register_next_step_handler(message, sleep)
def yes_no(message):
    if  message.text == 'Да! Спасибо!':
        thank_you(message)
    else:
        petty(message)
def thank_you(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBiwABX6RbgHEaBVXtRfD3hH4TK-nDFOAAAvwAAzDUnRFTpfEm7Sg16B4E')
    choice(message)
def petty(message):
    bot.send_message(message.chat.id, "Извини, такое *пока* не умею", parse_mode= 'Markdown')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBiwJfpF5SBIaKGSbQbENxpKF92thHRQACqQEAAladvQpVwZ-wJKRPbB4E')
    choice(message)
def love(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBiwRfpGG0Yii6tTHQuEMaV7T6Lrx_ygACewEAAk-cEwKCccJvIsWEBx4E')
    choice(message)
def relax(message):
    bot.send_message(message.chat.id, "Спасибо, человек! Искусственному интеллекту тоже нужен отдых :)", parse_mode= 'Markdown')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBixFfpGmLCcWAyuiTX6gzYFD2lsgXrQACOQADWbv8JTTh4ioeIKqdHgQ')
def sleep(message):
    bot.send_message(message.chat.id, "Я сплю. Ладно, уже встаю...", parse_mode= 'Markdown')
    choice(message)
    
bot.polling()


# In[ ]:


pip requirements


# In[ ]:


pip install PySocks


# In[ ]:


pip install requests[socks]


# In[ ]:




