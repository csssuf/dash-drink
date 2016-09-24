# dash-drink

Ever wanted to drop a drink using a Dash IoT button? Now you can!

## Requirements
* Must have DynamoDB tables named DrinkButtons (for button -> user/drink
  mappings) and DrinkUsers (for user -> Webdrink API key mappings) created.
* Must have the AWS CLI installed and configured, and a Lambda function called
  Drink created in order to use the provided Makefile to upload code.

## Setup
```bash
# Create virtualenv and install dependencies
virtualenv --python=python2 .venv
source .venv/bin/activate
pip install -r requirements.txt

# Build and push code
make

# Or, to just build the code
make zip
```
