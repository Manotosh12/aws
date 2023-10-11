import boto3
import pprint

# Create an boto client for Amazon Rekognition
client = boto3.client(
    "rekognition",
    aws_access_key_id="AKIAZXQBV75LK44EBXFN",
    aws_secret_access_key="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",
    region_name="ap-south-1"
)


response = client.detect_labels(
    Image={

        'S3Object': {
            'Bucket': 'humpi',
            'Name': 'zoo.jpg'
        }
    }
)

#print the json response
pprint.pprint(response)