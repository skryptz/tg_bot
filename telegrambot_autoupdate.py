from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

updater = Updater(token='1783032632:AAFwfGu2SU464Fx43j6kbfuhn41DQglwUQo', use_context=True)
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

    message = 'Welcome to Pussy Credit. Type /help for more info.'
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

# def announcements(context: CallbackContext):
# 	context.bot.send_message(chat_id='-516827311',
# 		text="""/help for more commands \n ________________ \n PussyCredit \n /Rules\."""+ 
# 		"\n [Dextools Chart](https://www.dextools.io/app/uniswap/pair-explorer/0x5277c3195801fd4acc92ebfd939024f08cfb697a)",
#     	parse_mode='MarkdownV2')


## ---- Commands ---- ##

def announcements(context: CallbackContext):   
   # send message to all users
   for keys in db_keys:
       id = r.get(keys).decode("UTF-8")
       context.bot.send_message(chat_id=id, text="""Pussy Credit Info Bot \n \n /help for more commands \n \n /Rules"""+"\n [Dextools Chart](https://www.dextools.io/app/uniswap/pair-explorer/0x5277c3195801fd4acc92ebfd939024f08cfb697a)", parse_mode='MarkdownV2')

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
		text="[ https://app\.uniswap\.org/\#/swap?outputCurrency\=0xA9d945559f6E799c3A4f4aa08DB9674f54DB3E80\&use\=V2](https://app.uniswap.org/#/swap?outputCurrency=0xf184cdf2f96e21f4907b069ab85fb23f4b65ce7b&use=V2)",
		parse_mode='MarkdownV2')

uniswap_link_handler = CommandHandler('uniswap', uniswap_link)
dispatcher.add_handler(uniswap_link_handler)

# etherscan
def etherscan(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="[https://etherscan\.io/token/0xA9d945559f6E799c3A4f4aa08DB9674f54DB3E80](https://etherscan.io/token/0xA9d945559f6E799c3A4f4aa08DB9674f54DB3E80)",
		parse_mode='MarkdownV2')

etherscan_handler = CommandHandler('etherscan', etherscan)
dispatcher.add_handler(etherscan_handler)

# contract
def contract(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="0xA9d945559f6E799c3A4f4aa08DB9674f54DB3E80")

contract_handler = CommandHandler('contract', contract)
dispatcher.add_handler(contract_handler)
# coinmarketcap
def cmc(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="[https://coinmarketcap\.com/currencies/pussycredit/](https://coinmarketcap.com/currencies/pussycredit/)",
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
    	text="[www\.dextools\.io/app/uniswap/pair\-explorer/0x9a2fd1e2ac0ce181e409858068b00a9e5e665da8](https://www.dextools.io/app/uniswap/pair-explorer/0x9a2fd1e2ac0ce181e409858068b00a9e5e665da8)",
    	parse_mode='MarkdownV2')

chart_handler = CommandHandler('chart', chart)
dispatcher.add_handler(chart_handler)

# website
def website(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text = "[http://pussycredit\.xyz/index\.html](http://pussycredit.xyz/index.html)",
		parse_mode='MarkdownV2')

website_handler = CommandHandler('website', website)
dispatcher.add_handler(website_handler)

# twitter
def twitter(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="[https://twitter\.com/PussyCredit](https://twitter.com/PussyCredit)")

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
    context.bot.send_message(chat_id=update.effective_chat.id, text="[https://etherscan\.io/token/0xA9d945559f6E799c3A4f4aa08DB9674f54DB3E80?a\=0x000000000000000000000000000000000000dead](https://etherscan.io/token/0xA9d945559f6E799c3A4f4aa08DB9674f54DB3E80?a=0x000000000000000000000000000000000000dead)",
    	parse_mode='MarkdownV2')

tokennomics_handler = CommandHandler('burn', burn)
dispatcher.add_handler(tokennomics_handler)

# Detailed list of rules
def rules_detailed(update, context):
 	context.bot.send_message(chat_id=update.effective_chat.id, text="""\nPUSSC Rules: \n \nTo Our PussyCredit Community\, \n \n The main goal of this group is to support the PussyCredit community to provide room for discussion and education\. Members of this community that resist to follow the rules below might be permanently banned from the group\. \n • Respect all members in the chat\. Any form of threats\, bullying or harassing members and\/or admins will not be tolerated\. \n • No vulgarity\. \n • No text bombing\. Do not spam messages\. If you want to make a statement\, then do this with one message\. You are allowed to post the same message after a certain amount of time\. \n • The moderators have all rights to ban any individual who spreads negativity in comments related to PussyCredit\. Please note\, this does not mean we cannot be open to constructive criticism and\/or feedback\. \n • Always try to help the moderator by abiding any rules or requests being made for the benefit of the forum\. Keep in mind that everything we do is for your benefit as well\. \n • Spamming\, solicitations\, or advertisement is not allowed\. Links unrelated to PussyCredit will be deleted and you will receive a first warning\.  \n • It is not allowed to post photos or content that contain violence\, fear\, hate or questionable content that might make people feel uncomfortable\. \n • We are always open to tough\/honest questions and we will try to answer as resolute as possible\. But if you intentionally start creating FUD\, rumors without facts or drama will not be tolerated\.  \n \n PUSSC is a community memecoin\, and you are all welcome to share with other members any information they request\, if that information has been released as accurate information\. We are all here to help each other grow this community\, and at the same time\, have fun doing it\. \n \n NOTE \: The moderators and developers of PussyCredit will NEVER ask a member for confidential information like passwords or recovery phrases\. Keep it safe everyone\! If you ever experience this in our chat\, please notify us so we can get the person involving banned\. \n \n \n Penalty system \: \n While trying to maintain our community and helping each other we also provide second chances to people that misbehave\. We know that sometimes we forget these things and therefore we have one more important rule \: \n • Disobeying one of the rules written above will result as followed \: \n We will warn you two times\. When you get warned for the third time you will be banned\. \n /help for more info\.""", parse_mode='MarkdownV2')

rules_detailed_handler = CommandHandler('rules_detailed', rules_detailed)
dispatcher.add_handler(rules_detailed_handler)

# summary of rules
def rules(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="""\n PUSSC Rules\:\n \n To Our PussyCredit Community\, \n \n  The main goal of this group is to support the PussyCredit community to provide room for discussion and education\. Members of this community that resist to follow the rules below might be permanently banned from the group\. \n  \n • Respect all members in chat 🤝 🤝\n • No text bombing\, no spamming 📝 💣 🚫 \n • The moderators have all rights to ban any individual that spreads negativity related to Pussycredit 🚫 \n • Always try to help a moderator by abiding any rules or requests ✅ 📝 ✅ \n • Solicitations\, spamming\, or advertisement are not allowed ❌ \n • Photos containing violence\, fear\, hate\, or questionable content is not allowed 📷 🔫 🗡 🚫 \n • No vulgarity\. 👿\n • Do not FUD or create rumors without facts\. We are always open to tough questions and will answer them as resolute as possible\. 👨‍🚀 \n  \n  While trying to maintain our community and helping each other we also provide second chances to people that misbehave\. We have one more important rule\: \n  \n • Disobeying one of the rules written above will result as followed\: \n \n We will warn you two times\. When you get warned for the third time you will be banned\.  ⚠️⚠️⚠️ \= 🚫 \n \n /rules\_detailed for more info\.\n \n \n This is a Community meme coin\, and everyone should feel comfortable and welcomed here\. The main purpose of this community is to support $PUSSC """, parse_mode='MarkdownV2')

rules_handler = CommandHandler('rules', rules)
dispatcher.add_handler(rules_handler)

## ----- Commands Help List ----- ##

def list_command(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id,
		text="Pussy Credit \n 100% Community Owned Token. \n /Rules for telegram rules and guidelines. /help for more info. \n ________ \n Commands List \n ________ \n 🚀 * /uniswap \n 👌 * /etherscan \n 👀 * /contract \n 🔍 * /chart \n 🔞 * /website \n 🐤 * /twitter \n 💹  * /cmc \n ________  \n * /whencg \n * /whenmoon \n * /whenlisting \n * /burn ")

help_handler = CommandHandler('help', list_command)
dispatcher.add_handler(help_handler)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command. \n Type /help for more info.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

## ----- Job Updater ----- ##

j.run_repeating(announcements, interval=600, first=10)

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