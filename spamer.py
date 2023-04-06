from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import time

api_id = #без ""
api_hash = ''
phone = '+7'
timer = 3 #Время между сообщениями 
msgtosend = """Проверка спамера""" #Сообщение для отправки 
commtosend = """/next""" #Если в бота, то комманда 
#юзер нейм для отправки 
username1 = "@AnonRuBot" 
# username2 = ""
# username3 = ""
# username4 = ""
# username5 = ""
# username6 = ""

client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Введите код доступа: '))
chats = []
last_date = None
chunk_size = 10
groups=[]
result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash = 0
            ))
chats.extend(result.chats)
for chat in chats:
    try:
        groups.append(chat)
    except:
        continue
while True:
    try:
        msg = client.send_message(username1, msgtosend)
        msg = client.send_message(username1, commtosend)
        # msg1 = client.send_message(username2, msgtosend)
        # msg2 = client.send_message(username3, msgtosend)
        # msg3 = client.send_message(username4, msgtosend)
        # msg4 = client.send_message(username5, msgtosend)
        # msg5 = client.send_message(username6, msgtosend)
        print("Сообщение отправленно, некст через " + str(timer) + " секунды")
        time.sleep(timer)
    except:
        continue