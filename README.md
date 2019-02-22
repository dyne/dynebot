<h1 align="center">
  <br>
    <a href="http://t.me/dyne_bot">
      <img src="https://www.dyne.org/wp-content/uploads/2011/09/moebius-band.png" width="150" alt="Dyne.org Telegram Bot">
    </a>
  <br>
  Dyne.org Telegram Bot
  <br>
</h1>

| This bot is intended for helping automating small tecious task of the dyne overall interaction |
:---:
| [![Dyne.org](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%9D%A4%20by-Dyne.org-blue.svg)](https://dyne.org) |

I love this bot, is some handful project mainly to not forget to fill my timesheet, please join it [here](http://t.me/dyne_bot)

<details>
 <summary><strong>:triangular_flag_on_post: Table of Contents</strong> (click to expand)</summary>

* [Install](#floppy_disk-install)
* [Usage](#video_game-usage)
* [Configuration](#wrench-configuration)
* [Acknowledgements](#heart_eyes-acknowledgements)
* [Links](#globe_with_meridians-links)
* [Contributing](#busts_in_silhouette-contributing)
* [License](#briefcase-license)
</details>

***
## :floppy_disk: Install
```pip install -e .```

This should install all the needed dependencies.

A running redis server is also needed. Configuration of the redis url is described below.

***
## :video_game: Usage

To start using the bot just run it and leave it running

```bash
python main.py
```


***
## :wrench: Configuration

All the configuration should be available under an .ini file.
By default the configuration file is [config.ini](config.ini)

### User defined config.ini
Define a environment variable **DYNEBOT_CONFIGFILE** with the absolute path of the file like:

```bash
export DYNEBOT_CONFIGFILE=/srv/some/secure/place/production.ini
```

You are **encouraged to do this** and edit the config file with your real data.


### Variables

| name | description | values | 
| --- | --- | --- |
| **TOKEN** | the token from your telegram channel, I own the real one ask me | `string` |
| **REDIS_HOST** | server host of redis | `string` |
| **REDIS_PORT** | server port of redis | `int` |
| **REDIS_DB** | redis database | `int` |



***
## :heart_eyes: Acknowledgements

Copyright :copyright: 2019 by [Dyne.org](https://www.dyne.org) foundation, Amsterdam

Designed, written and maintained by Puria Nafisi Azizi.


***
## :globe_with_meridians: Links

http://t.me/dyne_bot

https://dyne.org/


***
## :busts_in_silhouette: Contributing

Please first take a look at the [Dyne.org - Contributor License Agreement](CONTRIBUTING.md) then

1.  :twisted_rightwards_arrows: [FORK IT](https://github.com/puria/README/fork)
2.  Create your feature branch `git checkout -b feature/branch`
3.  Commit your changes `git commit -am 'Add some fooBar'`
4.  Push to the branch `git push origin feature/branch`
5.  Create a new Pull Request
6.  :pray: Thank you


***
## :briefcase: License

    Dyne.org Telegram Bot
    Copyright (c) 2019 Dyne.org foundation, Amsterdam
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.