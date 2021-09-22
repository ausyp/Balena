# Balena_aws_sms

A Simple Flask app to send SMS notification from grafna using AWS sns.

Set variables in balena dashboard for AWS keys.

> Blockquote

"SMS_AWS_SEC_KEY" and "SMS_AWS_ACCESS_KEY"

Based of : https://sean-bradley.medium.com/create-sms-alert-channel-using-a-custom-webhook-and-aws-sns-27e03d55524b

Docker.Template has some unnecessary stuff in it. Left there for ease of development. Delete if you dont need it.

Docker-compose:

    sms:
    build: ./sms
    restart: always
    hostname: sms
