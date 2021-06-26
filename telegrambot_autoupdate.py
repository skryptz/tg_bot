from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

updater = Updater(token='1890564401:AAFu8gyFvFK1McNtxMYLgNqfL7udZg3csvc', use_context=True)
dispatcher = updater.dispatcher
j = updater.job_queue

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

import redis
import os
r = redis.from_url('redis://:pb1c8e17076408b03cb495ee2a730390fc452f41aadd0258a42765edb487215fe@ec2-52-203-110-39.compute-1.amazonaws.com:15789')
# r = redis.from_url(os.environ.get(redis://:pb1c8e17076408b03cb495ee2a730390fc452f41aadd0258a42765edb487215fe@ec2-52-203-110-39.compute-1.amazonaws.com:15789))
db_keys = r.keys(pattern='*') # redis key access

# Guess someone wants to know the time
import datetime
now_time = datetime.datetime.now().time()


## ----- start, wake, sleep function ----- ##

def start(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    r.set(user_name, user_id)

    message = 'Welcome to the bot'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def wake(update, context):
	message = 'Waking'
	context.bot.send_message(chat_id=update.effective_chat.id, text=message)
	updater.start_polling()

wake_handler = CommandHandler('wake', wake)
dispatcher.add_handler(wake_handler)

## Sleep
## updater.idle()
## sleep_handler = CommandHandler('sleep', sleep)
## dispatcher.add_handler(sleep_handler)

## --- Loose Announcement --- ##

def announcements(context: CallbackContext):
	context.bot.send_message(chat_id='-516827311',
		text="""/help for more commands \n ________________ \n PussyCredit \n /Rules\."""+ 
		"\n [Dextools Chart](https://www.dextools.io/app/uniswap/pair-explorer/0x5277c3195801fd4acc92ebfd939024f08cfb697a)",
    	parse_mode='MarkdownV2')


## ---- Commands ---- ##

#def announcement(context: telegram.ext.CallbackContext):
#    message = "Hello, this message will be sent in intervals"
#    
#    # send message to all users
#    for keys in db_keys:
#        id = r.get(keys).decode("UTF-8")
#        context.bot.send_message(chat_id=id, text=message)

# ----- Admins / Mods ----- #
# def get_admins(update, context):
# 	list_admins=str(context.bot.get_chat_administrators(chat_id=update.effective_chat.id))
# 	context.bot.send_message(chat_id=update.effective_chat.id, text="Admins are "+ list_admins)
# 	print(list_admins)

# get_admins_handler = CommandHandler('admins', get_admins)
# dispatcher.add_handler(get_admins_handler)
# ----- Admins / Mods ----- #

# uniswap_v2
def uniswap_link(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="[Uniswap](https://app.uniswap.org/#/swap?outputCurrency=0xf184cdf2f96e21f4907b069ab85fb23f4b65ce7b&use=V2)",
		parse_mode='MarkdownV2')

uniswap_link_handler = CommandHandler('uniswap', uniswap_link)
dispatcher.add_handler(uniswap_link_handler)

# etherscan
def etherscan(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="[Etherscan](https://etherscan.io/token/0xf184cdf2f96e21f4907b069ab85fb23f4b65ce7b)",
		parse_mode='MarkdownV2')

etherscan_handler = CommandHandler('etherscan', etherscan)
dispatcher.add_handler(etherscan_handler)

# contract
def contract(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="0xf184cdf2f96e21f4907b069ab85fb23f4b65ce7b")

contract_handler = CommandHandler('contract', contract)
dispatcher.add_handler(contract_handler)
# coinmarketcap
def cmc(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="[CoinMarketCap](https://coinmarketcap.com/currencies/pussycredit/)",
		parse_mode='MarkdownV2')

cmc_handler = CommandHandler('cmc', cmc)
dispatcher.add_handler(cmc_handler)

# coingecko
def coingecko(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="Coingecko applied for, listing soon!")

cg_handler = CommandHandler('whencg', coingecko)
dispatcher.add_handler(cg_handler)

# chart
def chart(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
    	text="[Dextools Chart](https://www.dextools.io/app/uniswap/pair-explorer/0x5277c3195801fd4acc92ebfd939024f08cfb697a)",
    	parse_mode='MarkdownV2')

chart_handler = CommandHandler('chart', chart)
dispatcher.add_handler(chart_handler)

# website
def website(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text = "[Website](https://www.pussycredit.com)",
		parse_mode='MarkdownV2')

website_handler = CommandHandler('website', website)
dispatcher.add_handler(website_handler)

# twitter
def twitter(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="[Twitter](https://twitter.com/PussyCredit)")

twitter_handler = CommandHandler('twitter', twitter)
dispatcher.add_handler(twitter_handler)

# when moon
def whenmoon(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="when you buy")

moon_handler = CommandHandler('whenmoon', whenmoon)
dispatcher.add_handler(moon_handler)


# when listing
def listing(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Listings are on the way. Stay active in the Telegram for further announcements.")

listing_handler = CommandHandler('whenlisting', listing)
dispatcher.add_handler(listing_handler)

# when lambo
def lambo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Why lambo")

lambo_handler = CommandHandler('whenlambo', lambo)
dispatcher.add_handler(lambo_handler)

# tokenomics
def burn(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="[Burn Address on Etherscan](https://etherscan.io/token/0xf184cdf2f96e21f4907b069ab85fb23f4b65ce7b?a=0x000000000000000000000000000000000000dead)",
    	parse_mode='MarkdownV2')

tokennomics_handler = CommandHandler('burn', burn)
dispatcher.add_handler(tokennomics_handler)

#rules
def rules(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Insert Rules here )")

rules_handler = CommandHandler('rules', rules)
dispatcher.add_handler(rules_handler)

## ----- Commands Help List ----- ##

def list_command(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="Pussy Credit \n 100% Community Owned Token. /Rules for telegram rules and guidelines. /help for more info. \n ________ \n Commands List \n ________ \n 🚀 * /uniswap \n 👌 * /etherscan \n 👀 * /contract \n 🔍 * /chart \n 🔞 * /website \n 🐤 * /twitter \n 💹  * /cmc \n ________  \n * /whencg \n * /whenmoon \n * /whenlisting \n * /burn ")

help_handler = CommandHandler('help', list_command)
dispatcher.add_handler(help_handler)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command. \n Type /help for more info.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

## ----- Job Updater ----- ##

j.run_repeating(announcements, interval=1200, first=10)

updater.start_polling()
updater.idle()

## Set job time
# def time(update, context):
#    context.job_queue.run_repeating(announcement, 5, context=update.message.chat_id)

#def start_schedule(update, context):
#	user = update.message.from_user
#	chat_id = user['id']
#	if chat_id == 1582862035:
#		j.run_repeating(announcement, interval=60, first=10)

## schedule command	
#start_schedule_handler = CommandHandler('start_schedule', start_schedule)
#dispatcher.add_handler(start_schedule_handler)

## ---- Announcement Job ---- ##