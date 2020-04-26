import discord
from discord.ext import commands
from scoreboard import Scores

# client = discord.Client()

bot = commands.Bot(
    command_prefix='<', 
    case_insensitive=True,
    activity=discord.Game('with my code'))
bot.remove_command('help')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def add(ctx, name, point): # adds points
    # if not isinstance(point,int):
        # await ctx.send('Gotta put a number value')
        # return
    board = Scores()
    board.add(name,point)
    await ctx.send('{} got {} points'.format(name,point))

@bot.command()
async def add_player(ctx, name): # adds players
    bord = Scores()
    bord.add_gamer(name)
    await ctx.send('%s added to gamers'%name)

@bot.command()
async def sub(ctx, name, point): # takes points
    board = Scores()
    # if not isinstance(point,int):
        # await ctx.send('Gotta putq a number value')
        # return
    board.sub(name, point)
    await ctx.send('{} lost {} points'.format(name,point))

@bot.command()
async def sub_player(ctx, name):
    board = Scores()
    board.sub_gamer(name)
    await ctx.send('%s removed from gamers'%name)

@bot.command()
async def sb(ctx):
    bord = Scores()
    embed = discord.Embed(title='SCOREBOEARD',color=discord.Color(0))
    for x in range(bord.length()):
        embed.add_field(name=bord.names(x+1),value=bord.points(x+1),inline=True)
    await ctx.send(embed=embed)


bot.run('Njk3NjUxMzQ3MTM4MjgxNDcy.XqOmSA.-9XE8YgCFafjBTOe-rbVuRgA1HI')