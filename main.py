import discord
from discord.ext import commands

intents= discord.Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print("Bot hazır!") # Test

@bot.event
async def on_member_join(member):
    # Bu bölümü istediğiniz mesajın içeriğine göre özelleştirebilirsiniz.

    print(f"{member} server'a katıldı!")
    message = "Sunucuya Hoşgeldiniz!"
    embed = discord.Embed\
    (
        title= message,
        description= "Açıklama",
        colour= discord.Colour.blue()
    )
    embed.set_footer(text="Footer kısmı")
    embed.set_author(name="Author Kısmı")
    embed.add_field(name="Alan 1",value="Alan 1", inline=False)
    embed.add_field(name="Alan 2", value="Alan 2", inline=True)
    embed.add_field(name="Alan 3", value="Alan 3", inline=True)
    await member.send(embed=embed)
    print("mesaj gönderildi.") # Test

token = 'OTI5ODg2MzQ1MTg1MzQ1NTQ3.Ydt2JQ.0n6Ua8aWn8ZhXjoqDbwjRsz3qj8' # Discord Token'ınızı buraya ekleyin.
# (Tokenlar asla paylaşılmaması gereken keylerdir. Yanlış tokenı kullanmayın diye buraya botun eski tokenını koydum örnek olarak. Bu yapıda olanı kullanıcaksanız.)
# (Token'ı yanlışlıkla public bir yerde paylaştıysanız https://discord.com/developers/applications/ kısmından botunuzun token'ını regenerate edebilirsiniz.)
bot.run(token)



