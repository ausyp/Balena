#Copyright 2020 Sean Bradley https://sbcode.net/grafana/ MIT License
from flask import Flask, request
import boto3

APP = Flask(__name__)

CLIENT = boto3.client(
    "sns",
    aws_access_key_id="$SMS_AWS_ACCESS_KEY",
    aws_secret_access_key="$SMS_AWS_SEC_KEY",
    region_name="us-east-1"
)


@APP.route('/sendsms', methods=['POST'])
def sendsms():
    number = "+" + request.args.get('number')
    print(number)
    message = request.json["message"]
    print(message)

    response = CLIENT.publish(
        PhoneNumber=number,
        Message=message,
        MessageAttributes={
            'AWS.SNS.SMS.SenderID':
            {
                'DataType': 'String',
                'StringValue': 'Grafana'
            }
        }
    )
    return response


APP.run(host='', port= '80')
