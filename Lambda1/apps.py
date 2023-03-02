import json
import boto3
from datetime import datetime
from urllib.request import urlopen

def f(event, context):
    
    with urlopen("https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario") as response:
        body=response.read()
    
    #print(body)
    
    date=datetime.now()
    file="dolar_{}.txt".format(date.strftime("%Y%m%d"))
    
    client = boto3.client('s3')
    client.put_object(Body=body,Bucket='dolar-rawseb',Key=file)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }