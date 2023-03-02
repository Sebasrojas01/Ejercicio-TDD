import json
import boto3

from datetime import datetime

def f(event, context):
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('dolar-rawseb')
    
    date=datetime.now()
    file="dolar_{}.txt".format(date.strftime("%Y%m%d"))
    obj = bucket.Object(file)
    
    body = obj.get()['Body'].read()
    print(body)


    archivo = json.loads(body)
    archivo_2 = "fechahora, valor\n"
    
    for i in range(len(archivo)):
        timestamp = int(archivo[i][0]) / 1000
        dt_object = datetime. fromtimestamp(timestamp)
        
        archivo_2 += str(dt_object) + ","
        archivo_2 += archivo[i][1] + "\n" 
        
    print (archivo_2)
    
    
    file="dolar_{}.csv".format(date.strftime("%Y%m%d"))
    client = boto3.client("s3")
    client.put_object(Body = archivo_2, Bucket = 'dolar-finalseb', Key = file)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }