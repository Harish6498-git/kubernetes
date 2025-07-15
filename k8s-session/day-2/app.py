# gold_notify.py

import requests
import boto3
import os

goldapi_key = os.environ.get('GOLDAPI_KEY')
sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')

headers = {'x-access-token': goldapi_key, 'Content-Type': 'application/json'}

try:
    response = requests.get("https://www.goldapi.io/api/XAU/USD", headers=headers)
    response.raise_for_status()
    data = response.json()
    price = data.get('price', 'N/A')

    message = f"Today's gold price is: ${price}"
    print(message)

    sns = boto3.client('sns', region_name='us-east-2')
    sns.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject="Daily Gold Rate"
    )
    print("SNS Notification sent successfully.")

except Exception as e:
    print(f"Error occurred: {e}")
