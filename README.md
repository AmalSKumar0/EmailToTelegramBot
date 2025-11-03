# EmailToTelegramBot 🤖📨

A simple Python bot that bridges your email inbox and Telegram: it fetches your unread emails, sends them to your Telegram bot, and uses AI to generate a summary of each email. Sounds fun, right?

## Table of Contents  
1. [About](#about)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Setup & Installation](#setup-installation)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Configuration](#configuration)  
5. [Usage](#usage)  
6. [Folder Structure](#folder-structure)  
7. [Future Improvements](#future-improvements)  
8. [Author](#author)  
9. [License](#license)  

---

## About  
This project helps you stay on top of your inbox by forwarding unread emails to your Telegram bot, summarizing them automatically using AI, and delivering concise insights. Instead of opening multiple emails, you get key points delivered on Telegram.

---

## Features  
- Connects to your email account and fetches unread messages.  
- Forwards email content to your Telegram bot.  
- Uses AI (e.g., GPT-style summarisation) to create brief summaries of each email.  
- Simple setup for fast deployment.

---

## Tech Stack  
- **Language:** Python  
- **Bot Platform:** Telegram Bot API  
- **Email Access:** IMAP (or equivalent)  
- **AI Summarisation:** e.g., OpenAI API (or another large language model)  
- **Dependencies:** Listed in `requirements.txt` (or inside `automation.py`)  

---

## Setup & Installation  
### Prerequisites  
- Python 3.8+ installed  
- A Telegram Bot token (create via BotFather)  
- Email account credentials (with IMAP access enabled)  
- (Optional) Access to an AI summarisation API and its key

### Installation  
```bash  
git clone https://github.com/AmalSKumar0/EmailToTelegramBot.git  
cd EmailToTelegramBot  
pip install -r requirements.txt  
````

### Configuration

1. Open `automation.py` (or the config file).
2. Set the environment variables or constants for:

   * `TELEGRAM_BOT_TOKEN`
   * `TELEGRAM_CHAT_ID`
   * `EMAIL_HOST`, `EMAIL_USER`, `EMAIL_PASSWORD`
   * `AI_API_KEY` (if applicable)
3. Ensure your email account allows IMAP and “less secure apps” if needed.

### Running the Bot

```bash
python automation.py  
```

Once it’s running, the bot will check unread emails periodically (or on demand), send them to Telegram, and post a summary.

---

## Folder Structure

```
EmailToTelegramBot/
├── automation.py       # Main script handling email retrieval + Telegram + summarisation  
├── requirements.txt    # Python dependencies  
└── README.md           # This file  
```

*Adjust folder names if your project has more modules or configuration files.*

---

## Future Improvements

* Add a scheduler or cron job for periodic checks instead of manual run.
* Support for other email protocols and providers (e.g., Gmail, Exchange).
* Add HTML parsing, attachments handling, and richer content summarisation.
* Add interactive Telegram commands (e.g., `/summary last 10`, `/mark-read`, `/delete`).
* Deploy as a Docker container or serverless function for always-on usage.
* Add security: OAuth2 for email accounts, token refresh, encrypted storage of credentials.

---

## Author

**Amal S Kumar**
Full-Stack Developer | AI Enthusiast
[GitHub Profile](https://github.com/AmalSKumar0)

---

## License

MIT License – feel free to use and modify for your needs.

```
