"""
Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License"). You may not use 
this file except in compliance with the License. A copy of the License is 
located at

http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an 
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or 
implied. See the License for the specific language governing permissions and 
limitations under the License. 
"""

# Python script for reading from Twitter Streaming API and inserting tweets into an Amazon Kinesis Stream

import boto3
import json

from TwitterAPI import TwitterAPI

# Twitter OAuth Tokens
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""

# AWS Credentials
access_key = ""
secret_access_key = ""

# AWS Region and Kinesis Stream Name
region = ""
stream_name = ""

# Setting up Twitter and Kinesis objects
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
kinesis = boto3.client('kinesis', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)

r = api.request('statuses/filter', {'track': 'yolo'})

# Writes new tweets into Kinesis
for item in r:
    if 'text' in item:
         kinesis.put_record(StreamName=stream_name, Data=json.dumps(item), PartitionKey=item['user']['screen_name'])
         print item['text']
