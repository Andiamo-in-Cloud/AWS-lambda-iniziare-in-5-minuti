import json
from datetime import datetime

def lambda_handler(event, context):
    time=datetime.now()
    formatted_time=time.strftime("%H:%M:%S")
    
    return {
        'statusCode': 200,
        'body': formatted_time
    }
