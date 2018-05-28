import discord
from discord.ext.commands import Bot
from discord.ext import commands
from UserInfo import user_, password_, client_id_, secret_
import asyncio
import praw
import random


Client = discord.Client()
botCommand = commands.Bot(command_prefix = "!")
reddit = praw.Reddit(
    client_id = client_id_,
    client_secret = secret_,
    password = password_,
    user_agent = "DiscordBot by mitchames",
    username = user_
)


@botCommand.event
async def on_ready() :
    print("Memes inbound")
    print(botCommand.user.name)
    print(botCommand.user.id)

@botCommand.command()
async def meme() :
    sub = reddit.subreddit('dankmemes') # Here is the subreddit you want it to post from
    posts = [post for post in sub.hot(limit=20)]
    random_post_number = random.randint(0, 20)
    random_post = posts[random_post_number]
    await botCommand.say(random_post.url)



botCommand.run("Enter your OAuth2 url here")
