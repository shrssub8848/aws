
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('student')

table.put_item(
    Item={ 'email': ' roy@gmail.com',
            'name': ' roy',
            'age':25,
            'sex':'male',
            }

)

