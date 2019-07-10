'''
    This function sends an email to the owner of the website when a user visits a site and puts in their email to be
    notified when the site is up.
    NOTE: The recipient email must be registered, since it makes use of SES.

    This function uses the following environment variables.
        RECIPIENT_EMAIL     The email to receive the email.
        SITE_NAME           The site's name
        AWS_REGION          The AWS region to sue.

'''

import os
import boto3
from botocore.exceptions import ClientError


def register_email(event, context):
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = os.environ['RECIPIENT_EMAIL']

    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = os.environ['RECIPIENT_EMAIL']

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    # CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = os.environ['AWS_REGION']

    # The subject line for the email.
    SUBJECT = "Coming Soon Email Registration from " + os.environ['SITE_NAME']

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = 'New Email From {}\r\nA new user wants to be notified when {} website becomes available.'.format(event['Email'], os.environ['SITE_NAME'])

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>New Email From {}</h1>
      <p>A new user wants to be notified when {} website becomes available.</a>.</p>
    </body>
    </html>
                """.format(event['Email'], os.environ['SITE_NAME'])

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Send error to log if something goes wrong.
    except ClientError as e:
        return e.response['Error']['Message']
    else:
        return "Email sent! Message ID:" + response['MessageId']