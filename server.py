from secrets import choice
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import random

updater = Updater("API_KEY",
                use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello Friend, you have proved you are so loyal by reaching me\
        use /help to see what i can tell you !")

def help(update: Update, context: CallbackContext):
    update.message.reply_text(""" Here you go:
    /name : Enter your name please  
    /missed 
    /bye""")

def name(update: Update, context):
    list= ["can you tell me your name my friend ?","What is your name?" ,"can you share with me your name ?","i wonder who is this friend searching for me ?"]
    if len(context.args) == 0 :
        update.message.reply_text(random.choice(list))
    else :
        welcomes = ["hi","hello","hellohaaa !" , "welcome "]
        update.message.reply_text(f"{random.choice(welcomes)} {' '.join(context.args)}")

  
 
def missed(update: Update, context: CallbackContext):
    my_list = ["you too dude" ,"Maybe we don't really know each other but you are really missed !","thanks for your efforts to reach me , you are missed"]
    update.message.reply_text(random.choice(my_list))
  
def bye(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Bye Friend it was really nice talking to an old Friend!")
  

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry But what is '%s' ?? " % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

    

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('name', name,pass_args=True))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('bye', bye))
updater.dispatcher.add_handler(CommandHandler('missed', missed))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
