import discord
import os
import asyncio
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

load_dotenv() # load all the variables from the env file
bot = discord.Bot(intents=intents)

GUILD_ID = 1278321371469971456

@bot.event
async def on_ready():
    await bot.sync_commands()
    print(f"{bot.user} Ping Pong bot è pronto a fare ping pong! Versione bot: {os.getenv('VERSION')}")
    print(f"Bot connesso come {bot.user}")
    for guild in bot.guilds:
        print(f"{guild.name} (ID: {guild.id})")


#------------------

@bot.slash_command(description="Fai fare ping pong ad un user in vc!", guild_ids=[GUILD_ID])
@discord.default_permissions(move_members=True)
async def ping_pong(ctx: discord.ApplicationContext, user: discord.User, channel1: discord.VoiceChannel, channel2: discord.VoiceChannel, ping_pong_amount: int):
    print(f"Chosen member: {user}")
    #await ctx.respond(f"Goditi il tuo ping pong all'utente {user}")
    guild = ctx.guild
    member = guild.get_member(user.id)
    if member and member.voice and member.voice.channel:
        await ctx.respond(f"{user} è in un canale vocale! Verrà spostato in {channel1.mention} e poi in {channel2.mention} e viceversa per {ping_pong_amount} volte!!")
        for ping_pong in range(ping_pong_amount):
            if member.voice.channel == channel1:
                await member.move_to(channel2)
                print(f'{ping_pong}')
            elif member.voice.channel == channel2:
                await member.move_to(channel1)
                print(f'{ping_pong}')
            else:
                print("There's somethign wrong or user left the vc!")
                break
            await asyncio.sleep(0.5)
    else:
        await ctx.respond(f"{user} non è in nessun canale vocale.")

bot.run(os.getenv('TOKEN')) # run the bot with the token