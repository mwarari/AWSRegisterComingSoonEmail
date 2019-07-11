# AWSRegisterComingSoonEmail


This AWS lambda function sends an email to the email in the environment variable RECIPIENT_EMAIL from a coming soon page. 
It uses SES, so the mail must be confirmed before it can be successfully sent. 

The form needs to have an input field 'Email' that will hold the email of the person to be notified when the site is
up and running  

Below are the environment variables to be configured:

RECIPIENT_EMAIL     The recipient of the email
SES_REGION          The region where the lambda expression is running
SITE_NAME           The name of the site