from pyrogram import Client, filters

# Usando a sessão salva "my_account.session"
app = Client("my_account")

@app.on_message(filters.private)
async def greet(client, message):
    greeting_message = "Olá! Obrigado por entrar em contato. Confira nosso novo produto!"
    await message.reply(greeting_message)

app.run()
