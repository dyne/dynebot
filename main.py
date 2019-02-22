import datetime
import logging

from emoji import emojize
from redis import Redis
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from config import BaseConfig

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)
config = BaseConfig()


def get_db():
    host = config.get('REDIS_HOST')
    port = config.get('REDIS_PORT')
    db = config.get('REDIS_DB')
    return Redis(host=host, port=port, db=db)


def save(k, v):
    r = get_db()
    return r.hmset(k, v)


def hours_button(bot, update):
    query = update.callback_query
    save(str(datetime.date.today()), {'hours': query.data, 'user': update.effective_user.username})
    text = emojize(":tada: COOL! *Thank you for your hard work!* Your %sh are safely recorded" % query.data,
                   use_aliases=True)
    bot.edit_message_text(text=text, chat_id=query.message.chat_id,
                          message_id=query.message.message_id, parse_mode=ParseMode.MARKDOWN)


def ask_for_hours(bot, job):
    update = job.context
    columns = 4
    button_list = [InlineKeyboardButton("%sh" % __, callback_data=__) for __ in range(1, 13)]
    menu = [button_list[i:i + columns] for i in range(0, len(button_list), columns)]
    reply_markup = InlineKeyboardMarkup(menu)
    text = emojize("How many hours :clock10: did you work today?", use_aliases=True)
    bot.send_message(chat_id=update.message.chat_id, text=text, reply_markup=reply_markup)


def timesheet(bot, update, job_queue):
    job_queue.run_daily(ask_for_hours, datetime.time(hour=config.getint("HOUR"), minute=config.getint("MINUTE")), days=(0, 1, 2, 3, 4, 5), context=update)


def help_handler(update, context):
    update.message.reply_text('To start inserting your hours everyday, run */timesheet*', parse_mode=ParseMode.MARKDOWN)


def error(update, context):
    log.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(config.get('TOKEN'))
    updater.dispatcher.add_handler(CommandHandler('timesheet', timesheet, pass_job_queue=True))
    updater.dispatcher.add_handler(CallbackQueryHandler(hours_button))
    updater.dispatcher.add_handler(CommandHandler("help", help_handler))
    updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
