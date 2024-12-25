# AutoPurgeBot

AutoPurgeBot is a Telegram bot designed to automatically delete system messages like joins, leaves, pins, video chat updates, and more in groups and channels. It helps to keep your chats clean and clutter-free.

---

## Features

- Deletes system messages such as:
  - Member joins and leaves
  - Chat title or photo changes
  - Pinned messages
  - Video chat updates (scheduled, started, ended, participants invited)
  - Auto-delete timer updates
  - Forum topic events (created, closed, reopened, edited)
  - Supergroup migrations
- Handles multiple groups and channels simultaneously.

---

## Requirements

- Python 3.10 or later
- Telegram Bot API Token (Create a bot using [BotFather](https://t.me/BotFather))

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AutoPurgeBot.git
   cd AutoPurgeBot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your bot token:
   - Create a `.env` file in the project directory.
   - Add your bot token:
     ```env
     BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
     ```

---

## Usage

1. Run the bot:
   ```bash
   python main.py
   ```

2. Add the bot to your Telegram group or channel.

3. Make the bot an **admin** with the following permissions:
   - Delete messages

The bot will automatically detect and delete system messages.

---

## Configuration

- The bot requires no additional configuration for basic functionality.
- To customize its behavior, modify the `main.py` file.

---

## File Structure

```
AutoPurgeBot/
├── main.py            # Main bot script
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── .env               # Bot token (not included by default)
```

---

## Known Issues

- The bot must have delete permissions in the group or channel.
- Some events may not trigger in older versions of the Telegram Bot API. Ensure you're using the latest version of `python-telegram-bot`.

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add a new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or support, feel free to contact [@YourUsername](https://t.me/YourUsername).
