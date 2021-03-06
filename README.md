<div align="center"><img src="https://github.com/siruidops/selfbot/raw/main/.tmp/text.gif"/>

![License](https://img.shields.io/badge/license-GPL-blue) ![Status](https://img.shields.io/badge/state-success-cyan) ![Language](https://img.shields.io/badge/language-Python-purple)
</div>

# Telegram MTPeoto Robot: Fun

## Dependencies
```
python v3.x
pip
```

## Install requirements:
``` bash
$ sudo pip3 install -r requirements.txt
```

## Sample config
You can get Telegram API key with https://my.telegram.org/apps <br/>
for more information: https://docs.pyrogram.org/intro/setup

``` json
{
    "app_name": "my_account",

    "api_id": 7539745,
    "api_hash": "3021e68df9a7200135725c6331369a22",

    "user_id": 1144212423,
    "google_lang": "en",
    "google_num": 5,

    "is_unavailable_default": false,
    "message_unavailable": "Hello my friend,\njavad is not available, Whenever he is online, I will send him your message.\n\nSource: https://github.com/siruidops/selfbot",

    "channel_chat_id": -1004712264177
}
```

## Guide
``` text
!on                             Turn on unavailable message.
!off                            Turn off unavailable message.
!dollar                         Show Dollar price (in Iranian Rials).
!bitcoin                        Show Bitcoin price (in US dollars and Iranian rials).
!spam_number [number]           Spamming numbers in order from 0 to numbers.
!spam_text [number] [text]      Spam a text to number.
!exec [command]                 Execute a command and show the standard ouput.
!exec_py [code]                 Execute Python code and show the standard output.
!google [subject]               Search for a subject in Google and show the URLs.
!moon                           A cool animation with moon emojis(🌖🌗🌘🌑🌒🌓🌔🌕🌕).
```

## Usage
``` bash
$ python3 main.py
```

## Docker
``` bash
$ sudo docker build -t selfbot .
$ sudo docker run -rm selfbot
```

## License
This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details

## Preview
[![Preview](https://img.youtube.com/vi/q-gaVYZasbg/maxresdefault.jpg)](https://youtu.be/q-gaVYZasbg)
