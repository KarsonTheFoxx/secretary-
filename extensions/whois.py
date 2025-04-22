from disnake_plugins import Plugin
from disnake.ext import commands
from disnake import Embed, Color, CommandInteraction, User, ChannelType

plugin = Plugin()

@plugin.slash_command(name="whois", description="Get some information about another user")
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.install_types(guild=False, user=True)
@commands.contexts(guild=True, bot_dm=True, private_channel=True)
async def whois_private(inter:CommandInteraction, user:User, ephemeral:bool=True):

    embed = Embed(title=f"{user.display_name}({user.id})", color=Color.random())
    embed.set_image(url=user.avatar.url)
    embed.add_field(name="🕐|Created at", value=f"<t:{int(user.created_at.timestamp())}:R> ({user.created_at.month}/{user.created_at.day}/{user.created_at.year})\n-# mm/dd/yyyy")
    if not inter.channel.type in [ChannelType.private, ChannelType.group]:
        embed.add_field(name="📅|Joined at", value=f"<t:{int(user.joined_at.timestamp())}:R> ({user.joined_at.month}/{user.joined_at.day}/{user.joined_at.year})\n-# mm/dd/yyyy")

    await inter.response.send_message(embed=embed, ephemeral=ephemeral)

setup, teardown = plugin.create_extension_handlers()