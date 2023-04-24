import json
import os
from datetime import datetime

import discord
import requests
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()

client = discord.Client(intents=intents)


def send_slack_webhook_event(webhook_url: str, event_type: str, username: str, vcname: str, user_icon_url: str):
    content = f"User {event_type} a voice channel on Discord"
    color = "#36a64f" if event_type == "joined" else "#a63636" # join or left

    attachments = [
        {
            "fallback": f"User {event_type} a voice channel",
            "color": color,
            "author_name": username,
            "author_icon": user_icon_url,
            "fields": [
                {
                    "title": "Voice Channel",
                    "value": vcname,
                    "short": False
                }
            ],
            "footer": "Discord App",
            "footer_icon": "https://cdn.icon-icons.com/icons2/2108/PNG/512/discord_icon_130958.png",
            "ts": int(datetime.now().timestamp()),
            # "thumb_url": user_icon_url
        }
    ]
    payload = {
        "text": content,
        "attachments": attachments
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        print("Message sent to Slack successfully")
    else:
        print(f"Failed to send message to Slack. Status code: {response.status_code}, Response: {response.text}")


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        webhook_url = os.getenv("SLACK_WEBHOOK_URL")
        if webhook_url is None:
            print("No webhook URL provided. Please set SLACK_WEBHOOK_URL environment variable")
            return

        username = member.display_name
        user_icon_url = member.display_avatar.url
        if before.channel is None:
            event_type = "joined"
            vcname = after.channel.name
            send_slack_webhook_event(webhook_url, event_type, username, vcname, user_icon_url)
        elif after.channel is None:
            event_type = "left"
            vcname = before.channel.name
            send_slack_webhook_event(webhook_url, event_type, username, vcname, user_icon_url)
        else:
            pass # User switched channels

discord_token = os.getenv("DISCORD_TOKEN")
if discord_token is None:
    print("No Discord token provided. Please set DISCORD_TOKEN environment variable")
    exit(1)
client.run(discord_token)
