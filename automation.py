import imaplib
import email
from email.header import decode_header
import re
from openai import OpenAI
import requests
from gtts import gTTS
import pygame
import time
import os

def speak_gtts(text):
    filename = "email.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Wait until music finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # more reliable than time.sleep

    # Add slight delay before deleting
    time.sleep(0.5)

    # Unload and quit pygame before deleting the file
    pygame.mixer.music.unload()
    pygame.mixer.quit()

    # Now it's safe to delete
    os.remove(filename)





TELEGRAM_BOT_TOKEN = ""
TELEGRAM_CHAT_ID = ""
client = OpenAI(
    api_key="",
    base_url="https://api.groq.com/openai/v1"
)  
EMAIL = ""
PASSWORD = ""






def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.status_code == 200



def is_email_spam(subject, body, sender):
    prompt = f"""
You're an email filtering assistant. Here's an email:

From: {sender}
Subject: {subject}
Body: {body[:600]}

Question: Is this a spam, ad, promotional offer,linked in,pinterest or junk email that I can ignore?
Reply only with: Yes or No.
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )

    return response.choices[0].message.content.strip().lower()

def summerise_email(subject, body):
    prompt = f"""
You're an email summarizing assistant. Here's an email:
Subject: {subject}
Body: {body[:600]}

Question: summarizing this email in just 20 words.
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    return response.choices[0].message.content.strip()



# Connect to Gmail
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)
mail.select("inbox")

# Search for unread emails
status, messages = mail.search(None, '(UNSEEN)')
email_ids = messages[0].split()

print(f"\n📬 Found {len(email_ids)} unread emails.\n")


def clean(text):
    return re.sub(r"\s+", " ", text).strip()

for eid in email_ids:
    _, msg_data = mail.fetch(eid, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            raw_subject = msg["Subject"]
            if raw_subject is None:
               subject = "(No Subject)"
            else:
               subject, encoding = decode_header(raw_subject)[0]
               if isinstance(subject, bytes):
                   subject = subject.decode(encoding or "utf-8", errors="ignore")
            subject = clean(subject)
            from_ = msg.get("From")

            # Extract body
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        body = part.get_payload(decode=True).decode(errors="ignore")
                        break
            else:
                body = msg.get_payload(decode=True).decode(errors="ignore")
            is_spam = is_email_spam(subject, body, from_)

            if is_spam == "yes":
               print("❌ Spam detected — skipping.\n")
               continue
            else:
                 print("✅ Not spam — processing...\n")
                    # You can now call another function to summarize or send to Telegram


            # Only if it's not spam
            analysis = summerise_email(subject, body)
            telegram_message = f"""📩 *Important Email Detected!*

*From:* `{from_}`
*Subject:* `{subject}`

*AI Summary:*
{analysis}
"""
            sent = send_to_telegram(telegram_message)
            if sent:
               print("🚀 Message sent to Telegram!\n")
            else:
               print("⚠️ Failed to send Telegram message\n")

            speak_gtts(summerise_email(subject, body))
            break
mail.logout()