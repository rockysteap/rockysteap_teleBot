### rockysteap_teleBot

    Libs used: telebot (pyTelegramBotAPI) and aiogram
    
    Bot 1 -> main.py (telebot, webbrowser):
        - handle text and commands from telegram
        - create and handle telegram buttons
        - handle content (upload image to user telegram)

    Bot 2 -> bot_w_db.py (telebot, sqlite3):
        - create user query and save data to db

    Bot 3 -> weather.py (telebot, requests, json):
        - get weather status by city using openweathermap api

    Bot 4 -> converter.py (telebot):
        - euro zone currency converter
            https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html

    Bot 5 -> aio_main.py (aiogram, asyncio)
        - create keyboards (inline and reply button sets)
        - create handlers (commands and text)
        - handle user registration with state machine
        - create correct polling loop
