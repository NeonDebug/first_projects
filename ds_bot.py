from discord.ext import commands



bot = commands.Bot(command_prefix='!')

bot.lava_nodes = [
    {
        "host": "lava.link",
        "port": 80,
        "rest_uri": f"http://lava.link:80",
        "identifier": "MAIN",
        'password': 'anything',
        "region": "russia"
    }
]

@bot.event
async def on_ready():
    print ("Bot gatov. ")
    bot.load_extension('dismusic')

bot.run('OToIRkxi2_960')
