# Serverless Reference Architecture: Real-time Stream Processing
README Languages:  [DE](README/README-DE.md) | [ES](README/README-ES.md) | [FR](README/README-FR.md) | [IT](README/README-IT.md) | [JP](README/README-JP.md) | [KR](README/README-KR.md) |
[PT](README/README-PT.md) | [RU](README/README-RU.md) |
[CN](README/README-CN.md) | [TW](README/README-TW.md)

You can use [AWS Lambda](http://aws.amazon.com/lambda/) and Amazon Kinesis to process real-time streaming data for application activity tracking, transaction order processing, click stream analysis, data cleansing, metrics generation, log filtering, indexing, social media analysis, and IoT device data telemetry and metering. The architecture described in this [diagram](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf) can be created with an AWS CloudFormation template.

[The template](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda_stream_processing.template)
does the following:

-   Creates a Kinesis Stream

-   Creates a DynamoDB table named &lt;stackname&gt;-EventData

-   Creates Lambda Function 1 (&lt;stackname&gt;-DDBEventProcessor)
    which receives records from Kinesis and writes records to the
    DynamoDB table

-   Creates an IAM Role and Policy to allow the event processing Lambda
    function read from the Kinesis Stream and write to the DynamoDB table

-   Creates an IAM user with permission to put events in the Kinesis stream
    together with credentials for the user to use in an API client

## Instructions

Step 1 -  Create an AWS CloudFormation stack with [the
template](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-stream-processing.template). The AWS CloudFormation template completely automates the building, deployment, and configuration of all the components of the application.

Step 2 - Once the AWS CloudFormation stack has successfully been created you can do select the Outputs tab and see the AWS parameters needed in the demo Twitter client in the steps below.

Step 3 - To run the example application you need to update the code with AWS and Twitter information. Open twitter2kinesis.py in a text editor.

Step 4 - To access the Twitter API you need to get [access tokens](https://dev.twitter.com/oauth/overview/application-owner-access-tokens). Make sure you have these available and enter the information in the following parameters:

The Twitter API parameters
```
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
```

Step 5 - Enter the values for the AWS credentials and Amazon Kinesis stream name. This is the information from the Outputs tab of the CloudFormation template you got in step 2:

AWS parameters - from the Outputs tab of the CloudFormation template
```
access_key = ""
secret_access_key = ""
region = ""
stream_name = ""
```

Step 6 - Finally, before running the example code, you need [Python](https://www.python.org/) installed together with the Python modules boto3 and TwitterAPI. If you don't have the modules already, install them using [pip](http://pip.readthedocs.org/en/stable/installing/):

```
pip install boto3 TwitterAPI
```

## Test

Step 1 - Run the twitter2kinesis.py Python application from the command line to start sending tweets into the Kinesis stream.

```
python twitter2kinesis.py
```

Step 2 - In the Amazon DynamoDB management console, select the table named &lt;stackname&gt;-EventData and explore the records.

## Cleanup

To remove all created resources, delete the AWS CloudFormation stack.
