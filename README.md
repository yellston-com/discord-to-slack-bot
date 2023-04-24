# discord-notify

## Overview

This bot allows you to post Discord join/leave notifications to Slack. It's easy to set up - just provide your Discord bot token and Slack webhook URL.

## Setup Instructions

### 1. Get a Discord bot token

1. Log in to the Discord Developer Portal: https://discord.com/developers/applications
2. Create a new application.
3. Go to the "Bot" section and click "Add Bot".
4. Copy the "Token".

### 2. Get a Slack webhook URL

1. Log in to your Slack workspace: https://my.slack.com/apps/manage/custom-integrations
2. Click "Incoming Webhooks".
3. Click "Add New Webhook to Workspace".
4. Select a channel and click "Add Incoming WebHooks integration".
5. Copy the "Webhook URL".

### 3. Clone the repository

```
git clone https://github.com/yellston-com/discord-to-slack-bot.git
cd discord-to-slack-bot
```

### 4. Set environment variables

Create a .env file to set environment variables.

```
DISCORD_TOKEN=Your Discord bot token
SLACK_WEBHOOK_URL=Your Slack webhook URL
```

### 5. Run Docker Compose

```
docker compose up
```

Now the bot will run and Discord join/leave notifications will be posted to Slack.

## Additional Configuration

