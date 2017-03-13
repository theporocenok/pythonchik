#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, vkontakte, config

vk = vkontakte.API(token=str(config.vk_token))
while True:
    try:
        vk.get("account.setOnline",v='5.62')
        time.sleep(600)
    except:
        time.sleep(5)
        continue
