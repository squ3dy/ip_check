import urllib.request
from .. import loader, utils
from telethon import types, TelegramClient
import json

import asyncio
import logging

@loader.tds
class ip_checkerMod(loader.Module):
    """ip check module"""

    async def ipcmd(self, message: types.Message):
        """type .ip <here ip adress> to check location."""
        args = utils.get_args_raw(message)
        ip = str(args.split(' ', 2)[0])
        response = urllib.request.urlopen("http://ipwhois.app/json/"+ip)
        ipgeolocation = json.load(response)
        await message.client.send_message(message.to_id, 'country - ' + ipgeolocation["country"] + '\ncity - ' + ipgeolocation["city"])
    
    async def remaincmd(self, message: types.Message):
        """type .remain to check remaining requests"""
        response = urllib.request.urlopen("http://ipwhois.app/json/")
        ipgeolocation = json.load(response)
        requests = 10000 - int(ipgeolocation["completed_requests"])
        await message.client.send_message(message.to_id, 'remaining requests - ' + str(requests))


    

