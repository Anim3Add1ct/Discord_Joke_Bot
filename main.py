import requests
import discord
import DiscordUtils
import random
import json
from discord.ext import commands

intents = discord.Intents()  # JokeBot only needs intents related to messages.
intents.messages = True  #  JokeBot needs this intent to send messages, this includes embeds.
intents.message_content = True  # JokeBot needs this intent to read messages from the user.

bot = commands.Bot(command_prefix='!', intents=intents)  # Initializes an instance of a bot with '!' as the prefix.
bot.remove_command('help')  # Removes discord.ext's original help command to allow my own help command

@bot.event
async def on_ready():  # Does not interact with users. It just sends a message to show that the bot is running.
    print("==========================")
    print("JokeBot is up and running!")
    print("==========================")


@bot.command()
async def joke(ctx):  # The only other command that JokeBot has, which gets and sends the joke.
    joke_url = "https://official-joke-api.appspot.com/random_joke"  # A constant storing the REST API URL.

    response = requests.get(joke_url)  # Stores the random joke from the API in JSON format
    setup = json.loads(response.text)["setup"]  # Interprets the JSON response and extracts the first part (setup) of the joke.
    punchline = json.loads(response.text)["punchline"]  # Interprets the JSON response and extracts the second part (punchline) of the joke.

    joke = discord.Embed(title=setup, description=punchline, color=0x9999ff)  # Creates an instance of Discord's embed with the setup and punchline. The color of the embed highlights is #9999FF (RGB)
    await ctx.message.channel.send(embed=joke)  # Sends the embed created


@bot.command()
async def help(ctx):  # A command explaining the uses of JokeBot
    title = "**Everything You Need to Know about JokeBot**"
    description = "JokeBot has one single purpose: send jokes when asked."
    help_embed = discord.Embed(title=title, description=description, color=0x9999FF)
    help_embed.add_field(name="How it Works?", value="JokeBot uses a REST API to access a database of jokes compiled by coders around the world. When !joke is sent, it asks the database for a random joke and presents it to the user.", inline=False)  # Adds a field to the embed, which is basically a paragraph break. Inline is set to false to the field appears as a paragraph break.
    help_embed.add_field(name="What Else Can It Do?", value="JokeBot was created for only one purpose, therefore it only has two commands: !joke and !help. !joke is the command that lets JokeBot send you a joke, try it!", inline=False)
    help_embed.add_field(name="More Features", value="If you want to see a bot with more features, check out my other repos. I am planning to create a fully functional music bot at the time of writing this.", inline=False)

    await ctx.message.channel.send(embed=help_embed)


bot.run(BOTTOKEN)  # Runs the bot with the Token obtained from Discord's Developer Portal. The token has been removed prior to uploading to GitHub for security reasons.
