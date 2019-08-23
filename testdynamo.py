
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('student')

table.put_item(
    Item={ 'email': ' john@gmail.com',
            'name': ' john',
            'age':23,
            'sex':'male',
            }

)

