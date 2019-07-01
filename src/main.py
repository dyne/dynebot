import datetime
import logging

from emoji import emojize
from sqlalchemy.exc import IntegrityError
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from environs import Env

from src.model import DBSession, Base, engine
from src.model.entry import Entry

env = Env()
env.read_env()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)
Base.metadata.create_all(bind=engine)


def save(hours, user, date):
    e = Entry(hours=hours, user=user, date=date)
    try:
        DBSession.add(e)
        DBSession.commit()
    except IntegrityError:
        DBSession.rollback()


def hours_button(bot, update):
    query = update.callback_query
    save(hours=query.data, user=update.effective_user.username, date=datetime.date.today())
    text = emojize(":tada: COOL! *Thank you for your hard work!* Your %sh are safely recorded" % query.data,
                   use_aliases=True)
    bot.edit_message_text(text=text, chat_id=query.message.chat_id,
                          message_id=query.message.message_id, parse_mode=ParseMode.MARKDOWN)


def ask_for_hours(bot, job):
    update = job.context
    columns = 4
    button_list = [InlineKeyboardButton("%sh" % __, callback_data=__) for __ in range(0, 12)]
    menu = [button_list[i:i + columns] for i in range(0, len(button_list), columns)]
    reply_markup = InlineKeyboardMarkup(menu)
    text = emojize("How many hours :clock10: did you work today?", use_aliases=True)
    bot.send_message(chat_id=update.message.chat_id, text=text, reply_markup=reply_markup)


def timesheet(bot, update, job_queue):
    time = datetime.time(hour=env.int("HOUR"), minute=env.int("MINUTE"))
    job_queue.run_daily(ask_for_hours,
                        time,
                        days=(0, 1, 2, 3, 4, 5),
                        context=update)


def recap_handler(bot, update):
    month = update.message.text.split()[1:2]
    month = int(month[0]) if len(month) else datetime.date.today().month
    result = Entry.recap(update.effective_user.username, int(month))
    update.message.reply_text(str(result))


def help_handler(bot, update):
    update.message.reply_text("""To start inserting your hours everyday, run */timesheet*.
    To see the recap run */recap*""", parse_mode=ParseMode.MARKDOWN)


def error(update, context):
    log.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(env('TOKEN'))
    updater.dispatcher.add_handler(CommandHandler('timesheet', timesheet, pass_job_queue=True))
    updater.dispatcher.add_handler(CallbackQueryHandler(hours_button))
    updater.dispatcher.add_handler(CommandHandler("help", help_handler))
    updater.dispatcher.add_handler(CommandHandler("recap", recap_handler))
    updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
