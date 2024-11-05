from telethon import TelegramClient, events

# API bilgilerinizi girin
api_id = '28973855'
api_hash = 'f5a97adb2ced0180e1fc2040ea9a0f05'
client = TelegramClient('session_name', api_id, api_hash)

# Kaynak ve hedef kanal kimliklerini girin
source_channel = -1001626824569  # Mesajları alacağınız kanal
target_channel = -1002255662739  # Mesajları ileteceğiniz kanal

@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    # Mesajı hedef kanala iletin
    await client.send_message(target_channel, event.message)

client.start()
client.run_until_disconnected()
