import json
import os
import requests
from http.server import BaseHTTPRequestHandler

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
            'text': message,
            'parse_mode': 'HTML'
        })
        
        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'success', 'message': 'Alert sent'})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'status': 'error', 'message': str(e)})
        }
