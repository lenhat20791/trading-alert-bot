import json
import requests

TELEGRAM_BOT_TOKEN = '7637023247:AAG_utVTC0rXyfute9xsBdh-IrTUE3432o8'  # Thay bằng token thật
TELEGRAM_CHAT_ID = '7662080576'      # Thay bằng chat ID thật

def handler(event, context):
    # Add CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
    }
    
    # Handle OPTIONS request (preflight)
    if event['httpMethod'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
        
    try:
        # Parse request body
        body = json.loads(event['body'])
        
        # Extract data
        message = body.get('message', 'No message provided')
        symbol = body.get('symbol', 'No symbol provided')
        price = body.get('price', 'No price provided')
        time = body.get('time', 'No time provided')
        
        # Format message
        alert_message = f"🔔 Trading Alert!\n\n" \
                       f"Symbol: {symbol}\n" \
                       f"Price: {price}\n" \
                       f"Time: {time}\n" \
                       f"Message: {message}"
        
        # Send to Telegram
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': alert_message
        }
        
        response = requests.post(telegram_url, json=payload)
        response.raise_for_status()
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': 'Alert sent successfully'})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }