from telethon import TelegramClient, events
import requests
import os
from time import sleep

api_id = 1567951
api_hash = ''
TOKEN=str('')
BOT_url='https://api.telegram.org/bot'+TOKEN
log_users=['']
botii=['ForwardsCoversBot' ,'AnonySenderBot','Stickers','fakemailbot','PrimeAccz_bot']
client = TelegramClient('anon', api_id, api_hash)

def botSend(fileName, tes):
    files = {'document': (fileName, open(fileName, 'rb'))}
    for log_user in log_users:
        r = requests.post(BOT_url+tes+'&chat_id='+log_user, files=files)
        print(r.text)

def dirup(event,sender):
    tes ='/sendDocument?caption=@'+ str(sender.username)+" \n "+str(event.text)+" \n "+str(event.date)
    arr = os.listdir('pic')
    for files in arr:
        path='pic/'+str(files)
        botSend(path,tes)
        os.remove(path)
            
@client.on(events.NewMessage)
async def my_event_handler(event):
    sender = await event.get_sender()
    if event.is_private and sender.username not in botii :
        if event.photo or event.video or event.document or event.audio:
            sender = await event.get_sender()
            await event.download_media(file="pic")
            sleep(2)
            await dirup(event,sender)
        else:
            tes ="@"+ str(sender.username)+"   "+str(event.text)+"   "+str(event.date)
            for log_user in log_users:
                g=requests.post(BOT_url+'/sendmessage' , json={"chat_id":log_user,"text":tes})
                print(g.text)

client.start()
client.run_until_disconnected()
