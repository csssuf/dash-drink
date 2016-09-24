import boto3

dynamodb = boto3.resource('dynamodb')
button_table = dynamodb.Table('DrinkButtons')

def main(event, context):
    # Print button info.
    print(button_table.get_item(Key = { 'button_sn' : event["serialNumber"] }))
