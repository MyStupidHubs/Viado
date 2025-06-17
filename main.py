import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_USER_ID = 810160880087597076
TARGET_NICK = "vinicius50355"
REPLACE_NICK = "viadinho50355"

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logado como {client.user}")

@client.event
async def on_member_update(before, after):
    if after.id == TARGET_USER_ID:
        if after.nick == TARGET_NICK:
            try:
                await after.edit(nick=REPLACE_NICK)
                print(f"Nick alterado para {REPLACE_NICK}")
            except Exception as e:
                print(f"Erro ao mudar o nick: {e}")

client.run(TOKEN)
