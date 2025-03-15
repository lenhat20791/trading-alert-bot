import json
import requests
import os

def handler(event, context):
    try:
        # Parse the incoming JSON
        body = json.loads(event['body'])
        
        # Get environment variables
        bot_token = os.environ['TELEGRAM_BOT_TOKEN']
        chat_id = os.environ['TELEGRAM_CHAT_ID']
        
        # Format message
        message = f"🔔 Trading Alert!\n\n" \
                 f"Symbol: {body['symbol']}\n" \
                 f"Price: {body['price']}\n" \
                 f"Message: {body['message']}\n" \
                 f"Time: {body['time']}"
        
        # Send to Telegram
        telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        response = requests.post(telegram_url, json={
            'chat_id': chat_id,
            'text': message
        })
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"message": "Alert sent successfully!"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"error": str(e)})
        }