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
from flask import Flask

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create a simple Flask app to satisfy Render's port requirements
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    # Ignore messages from groups, supergroups, and channels
    chat_type = update.message.chat.type
    if chat_type in ["group", "supergroup", "channel"]:
        return
    await update.message.reply_text(
        "I'm AutoPurgeBot! I delete all system messages like joins, leaves, video chat updates, and more."
    )

async def delete_system_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Detect and delete all types of system messages."""
    message = update.message
    if message:
        if (
            message.new_chat_members or
            message.left_chat_member or
            message.new_chat_title or
            message.new_chat_photo or
            message.delete_chat_photo or
            message.pinned_message or
            message.migrate_to_chat_id or
            message.migrate_from_chat_id or
            message.message_auto_delete_timer_changed or
            message.video_chat_scheduled or
            message.video_chat_started or
            message.video_chat_ended or
            message.video_chat_participants_invited or
            message.forum_topic_created or
            message.forum_topic_closed or
            message.forum_topic_reopened or
            message.forum_topic_edited
        ):
            try:
                await message.delete()
                print(f"Deleted system message: {message.message_id}")
            except Exception as e:
                print(f"Failed to delete message: {e}")

if __name__ == "__main__":
    # Create the bot application
    application = ApplicationBuilder().token(BOT_TOKEN).concurrent_updates(True).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.ALL, delete_system_messages))

    # Start the bot in polling mode
    print("Bot is running...")

    # Run Flask app alongside the bot polling
    from threading import Thread
    def run_flask():
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))  # Port setup for Render

    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    application.run_polling()  # Polling for updates
