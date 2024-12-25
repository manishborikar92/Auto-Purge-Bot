from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    await update.message.reply_text(
        "I'm AutoPurgeBot! I delete all system messages like joins, leaves, video chat updates, and more."
    )

async def delete_system_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Detect and delete all types of system messages."""
    message = update.message
    if message:
        if (
            message.new_chat_members or  # New members joined
            message.left_chat_member or  # Members left
            message.new_chat_title or  # Chat title changed
            message.new_chat_photo or  # Chat photo changed
            message.delete_chat_photo or  # Chat photo deleted
            message.pinned_message or  # Message pinned
            message.migrate_to_chat_id or  # Group migrated to supergroup
            message.migrate_from_chat_id or  # Supergroup migrated from group
            message.message_auto_delete_timer_changed or  # Auto-delete timer updated
            message.video_chat_scheduled or  # Video chat scheduled
            message.video_chat_started or  # Video chat started
            message.video_chat_ended or  # Video chat ended
            message.video_chat_participants_invited or  # Participants invited to video chat
            message.forum_topic_created or  # Forum topic created
            message.forum_topic_closed or  # Forum topic closed
            message.forum_topic_reopened or  # Forum topic reopened
            message.forum_topic_edited  # Forum topic edited
        ):
            try:
                await message.delete()
                print(f"Deleted system message: {message.message_id}")
            except Exception as e:
                print(f"Failed to delete message: {e}")

if __name__ == "__main__":
    application = ApplicationBuilder().token(f"{BOT_TOKEN}").build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.ALL, delete_system_messages))

    # Start the bot
    print("Bot is running...")
    application.run_polling()
