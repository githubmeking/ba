from telethon import TelegramClient, events

# API bilgilerinizi girin
api_id = '28973855'
api_hash = 'f5a97adb2ced0180e1fc2040ea9a0f05'
client = TelegramClient('session_name', api_id, api_hash)

# Kaynak ve hedef kanal kimliklerini veya kullanıcı adlarını girin, -100 önekini ekleyin
source_channel = -1002348222494
target_channel = -1002340433708

@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    await client.send_message(target_channel, event.message)

client.start()
client.run_until_disconnected()
