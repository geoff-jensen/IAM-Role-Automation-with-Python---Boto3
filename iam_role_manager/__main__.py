import os
import boto3
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get AWS credentials and region
    aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_region = os.getenv('AWS_DEFAULT_REGION', 'us-west-2')
    
    # Check that keys are loaded
    if not aws_access_key or not aws_secret_key:
        print("AWS credentials are not set in the environment variables.")
        return
    
    # Initialize a session using the provided credentials
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=aws_region
    )

    # Test: print identity to verify credentials
    sts = session.client("sts")
    identity = sts.get_caller_identity()
    print(f"Connected to AWS as: {identity['Arn']}")

if __name__ == "__main__":
    main()
    

 



























