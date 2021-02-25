#!/usr/bin/python3

"""

 * (https://github.com/siruidops/selfbot).
 * Copyright (c) 2021 uidops.

 * This program is free software: you can redistribute it and/or modify  
 * it under the terms of the GNU General Public License as published by  
 * the Free Software Foundation, version 3.
 *
 * This program is distributed in the hope that it will be useful, but 
 * WITHOUT ANY WARRANTY; without even the implied warranty of 
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License 
 * along with this program. If not, see <http://www.gnu.org/licenses/>.

"""

import locale
import requests

from json import load as json_load
from random import choice
from subprocess import check_output, CalledProcessError
from googlesearch import search
from pyrogram import Client, filters
from string import ascii_lowercase, ascii_uppercase, digits
from time import ctime
from bs4 import BeautifulSoup

o = open("config.json", "rb")
config = json_load(o)
o.close()

app = Client(config['app_name'], config['api_id'], config['api_hash'])

def random_string(length):
    total = ascii_lowercase + ascii_uppercase + digits
    return "".join(choice(total) for i in range(length))

def currency_format(number):
    number = str(number)
    length = len(number)
    
    p = int(length/3)
    q = length-(p*3)

    g = ""
    g += number[0:q] + ","
    
    _temp = number[q:]
    n = 0
    for i in _temp:
        g += i
        if n == 2:
            g+= ","
            n = 0
            continue
        n += 1

    if g[-1] == ",":
        g = g[:-1]
    if g[0] == ",":
        g = g[1:]
    
    return g

def get_dollar_price():
    url = "https://www.tgju.org/profile/price_dollar_rl"

    r = requests.get(url)
    bs = BeautifulSoup(r.text, "html.parser")
    a = bs.find("tbody")
    a = a.find_all("tr")[0]
    a = a.find_all("td")[1].text

    return (float(a.replace(",", "")), currency_format(int(a.replace(",", "")))+" ﷼")

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"

    r = requests.get(url)
    a = r.json()
    a = a['bpi']['USD']['rate_float']
    b = get_dollar_price()[0]
    irr = currency_format(int(a*b))
    usd = a

    return (str(usd)+" $", str(irr)+" ﷼")

@app.on_message(filters.text)
def my_handler(client, message):
    global config

    if message.from_user != None:
        if message.from_user.id == config['user_id']:
            if message.text.split(" ")[0] == "!on":
                config['is_unavailable_default'] = True

            elif message.text.split(" ")[0] == "!off":
                config['is_unavailable_default'] = False
            
            elif message.text.split(" ")[0] == "!dollar":
                app.edit_message_text(message.chat.id, message.message_id,
                                    "Dollar: {0}".format(get_dollar_price()[1]))
            
            elif message.text.split(" ")[0] == "!bitcoin":
                answer = get_bitcoin_price()
                app.edit_message_text(message.chat.id, message.message_id,
                                    "Bitcoin (USD): {0}\nBitcoin (IRR): {1}".format(answer[0], answer[1]))
            
            elif message.text.split(" ")[0] == "!spam_number":
                app.delete_messages(message.chat.id, message.message_id)
                for i in range(0, int(message.text.split(" ")[1]) + 1):
                    app.send_message(message.chat.id, str(i))
            
            elif message.text.split(" ")[0] == "!spam_text":
                app.delete_messages(message.chat.id, message.message_id)
                for i in range(0, int(message.text.split(" ")[1]) + 1):
                    app.send_message(message.chat.id,
                                    " ".join(message.text.split(" ")[2:]))

            elif message.text.split(" ")[0] == "!exec":
                o = check_output(" ".join(message.text.split(" ")[1:]),
                                            shell=True)
                app.edit_message_text(message.chat.id, message.message_id,
                                    o.decode())
            
            elif message.text.split(" ")[0] == "!exec_py":
                file_random_name = "/tmp/"+random_string(16)+".py"
                
                _ = open(file_random_name, "w")
                _.write(" ".join(message.text.split(" ")[1:]))
                _.close()

                try:
                    com = check_output("python3 {}".format(file_random_name),
                                                shell=True)
                except CalledProcessError:
                    app.edit_message_text(message.chat.id, message.message_id,
                                    "Error.")
                    return

                app.edit_message_text(message.chat.id, message.message_id,
                                    com.decode())

            elif message.text.split(" ")[0] == "!google":
                data = ""
                num = 0
                for i in search(" ".join(message.text.split(" ")[1:]),
                                            num=config['google_num'],
                                            lang=config['google_lang']):
                    if num >= config['google_num']:
                        break

                    data += str(i) + "\n"
                    num += 1

                app.edit_message_text(message.chat.id, message.message_id, data)

            elif message.text.split(" ")[0] == "!moon":
                n = 0

                while n <= 2:
                    app.edit_message_text(message.chat.id, message.message_id,
                                        "🌖🌗🌘🌑🌒🌓🌔🌕🌕")
                    app.edit_message_text(message.chat.id, message.message_id,
                                        "🌗🌘🌑🌒🌓🌔🌕🌕🌖")
                    app.edit_message_text(message.chat.id, message.message_id,
                                        "🌘🌑🌒🌓🌔🌕🌕🌖🌗")
                    app.edit_message_text(message.chat.id, message.message_id,
                                        "🌑🌒🌓🌔🌕🌕🌖🌗🌘")
                    app.edit_message_text(message.chat.id, message.message_id,
                                        "🌒🌓🌔🌕🌕🌖🌗🌘🌑")
                    app.edit_message_text(message.chat.id, message.message_id,
                                        "🌓🌔🌕🌕🌖🌗🌘🌑🌒")
                    app.edit_message_text(message.chat.id, message.message_id,
                                        "🌔🌕🌕🌖🌗🌘🌑🌒🌓")
                    app.edit_message_text(message.chat.id, message.message_id,
                                        "🌕🌕🌖🌗🌘🌑🌒🌓🌔")
                    app.edit_message_text(message.chat.id, message.message_id,
                                        "🌕🌖🌗🌘🌑🌒🌓🌔🌕")
                    
                    n += 1

        if config['is_unavailable_default']:
            if message.chat.id > 0 and message.from_user.id != config['user_id']:
                app.send_message(message.chat.id, config['message_unavailable'],
                                    reply_to_message_id=message.message_id)
                
                app.send_message(config['channel_chat_id'], "From: {0}\nUsername: {1}\nDate: {2}\nMessage: {3}".format(
                                    str(message.from_user.first_name) + " " + str(message.from_user.last_name),
                                    str(message.from_user.username),
                                    ctime(message.date),
                                    str(message.text)
                ))

            elif "@sys_call".upper() in message.text.upper() and message.chat.id < 0:
                app.send_message(message.chat.id, config['message_unavailable'],
                                    reply_to_message_id=message.message_id)

                app.send_message(config['channel_chat_id'], "From: {0}\nUsername: {1}\nGroup: {2}\nDate: {3}\nMessage: {4}".format(
                                    str(message.from_user.first_name) + " " + str(message.from_user.last_name),
                                    str(message.from_user.username),
                                    str(message.chat.title),
                                    ctime(message.date),
                                    str(message.text)
                ))
            
            elif message.reply_to_message != None:
                if message.reply_to_message.from_user.id == config['user_id'] and message.chat.id < 0:
                    app.send_message(message.chat.id, config['message_unavailable'],
                                        reply_to_message_id=message.message_id)
                    
                    app.send_message(config['channel_chat_id'], "From: {0}\nUsername: {1}\nGroup: {2}\nDate: {3}\nMessage: {4}".format(
                                        str(message.from_user.first_name) + " " + str(message.from_user.last_name),
                                        str(message.from_user.username),
                                        str(message.chat.title),
                                        ctime(message.date),
                                        str(message.text)
                    ))

            else:
                pass

app.run()