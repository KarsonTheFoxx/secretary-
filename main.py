from disnake.ext import commands
from disnake import Activity, ActivityType, Status, Message, Intents


async def main(TOKEN:str):
    intents = Intents.default()
    intents.message_content = True

    bot = commands.InteractionBot(owner_id=1125466185861963857, intents=intents)

    @bot.event
    async def on_ready():
        await bot.wait_until_ready()
        await bot.change_presence(activity=Activity(name="Bread 🍞", type=ActivityType.watching), status=Status.idle)
        print("Ready")  
    
    bot.load_extensions("extensions")

    bot.reload = True
    await bot.start(token=TOKEN)

if __name__ == "__main__":
    from asyncio import run
    token_file = open("token.txt")
    token = token_file.read()
    try:
        run(main=main(TOKEN=token))
    except Exception as error:
        print(error)
        exit()