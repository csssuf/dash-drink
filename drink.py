import boto3
import json
import requests

DRINK_API_BASE="https://webdrink.csh.rit.edu/api/index.php?request=%s&api_key=%s"

dynamodb = boto3.resource('dynamodb')
button_table = dynamodb.Table('DrinkButtons')
api_key_table = dynamodb.Table('DrinkUsers')

def drink_api_call(path, api_key, post=False, postdata=None):
    _req_call = requests.post if post else requests.get
    req = _req_call(
        DRINK_API_BASE % (path, api_key),
        data=(postdata if post else None)
    )
    return req.text

def main(event, context):
    button_item = button_table.get_item(Key = { 'button_sn' : event["serialNumber"] })
    if "Item" not in button_item:
        raise Exception("Button not provisioned for drinks.")
    button_item = button_item["Item"]

    api_key_item = api_key_table.get_item(Key = { 'username' :
        button_item["username"]})
    if "Item" not in api_key_item:
        raise Exception("User requires drink API key.")
    api_key_item = api_key_item["Item"]

    drink_user_info = json.loads(drink_api_call(
        'users/info/',
        api_key_item["api_key"]
    ))
    if not drink_user_info["status"]:
        raise Exception("Couldn't get user's iButton.")

    drink_drop_results = json.loads(drink_api_call(
        'drops/drop',
        api_key_item["api_key"],
        True,
        {
            'ibutton': drink_user_info["data"]["ibutton"],
            'machine_id': button_item["machine_id"],
            'slot_num': button_item["slot_num"],
            'delay': 0
        }
    ))
    if not drink_drop_results["status"]:
        raise Exception("Couldn't drop drink.")
