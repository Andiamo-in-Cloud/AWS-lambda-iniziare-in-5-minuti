# Andiamo in Cloud: il canale in Italiano per imparare a sviluppare applicazioni in Cloud
# https://www.youtube.com/@andiamoincloud
# https://www.youtube.com/watch?v=eOzg98EZol8

import json
from datetime import datetime

def lambda_handler(event, context):
    time=datetime.now()
    formatted_time=time.strftime("%H:%M:%S")
    
    return {
        'statusCode': 200,
        'body': formatted_time
    }
