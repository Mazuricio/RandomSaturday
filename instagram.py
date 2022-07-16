#!/usr/bin/env python
# -*- coding: utf-8 -*-
from instabot import Bot
import senhas
def postar_instagram():
   bot = Bot()
   bot.login(username=senhas.username, password=senhas.password)
   foto = 'new_post.jpg'
   legenda = "- twitter.com/SaturdayRandom"
   bot.upload_photo(foto, caption= legenda)