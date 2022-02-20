import urllib.request
from .. import loader, utils
from telethon import types, TelegramClient
import json

import asyncio
import logging

@loader.tds
class ip_checkerMod(loader.Module):
    """just simple ip geolocation checker"""
    strings = {'name': 'ip_check'}


    async def ipcmd(self, message: types.Message):
        """type .ip <here ip adress> to check location."""
        args = utils.get_args_raw(message)
        ip = str(args.split(' ', 2)[0])
        response = urllib.request.urlopen("http://ipwhois.app/json/"+ip)
        ipgeolocation = json.load(response)
        await message.edit( '☘️ country - ' + ipgeolocation["country"] + '\n\n☘️ city - ' + ipgeolocation["city"])
    
    async def remaincmd(self, message: types.Message):
        """type .remain to check remaining requests"""
        response = urllib.request.urlopen("http://ipwhois.app/json/")
        ipgeolocation = json.load(response)
        requests = 10000 - int(ipgeolocation["completed_requests"])
        await message.edit('remaining requests - ' + str(requests))


    

