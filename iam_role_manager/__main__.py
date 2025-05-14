import argparse
import os
import boto3
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Set up argument parser
    parser = argparse.ArgumentParser(description="IAM Role Automation Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--create", action="store_true", help="Create IAM role(s)")
    group.add_argument("--delete", action="store_true", help="Delete IAM role(s)")
    group.add_argument("--update", action="store_true", help="Update existing IAM role(s)")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without making changes to AWS account")
    parser.add_argument("--config", type=str, required=True, help="Path to the config file (YAML or JSON)")
    args = parser.parse_args()

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
    # sts = session.client("sts")
    # identity = sts.get_caller_identity()
    # print(f"Connected to AWS as: {identity['Arn']}")
    
    # Print for now (later will pass these to core logic)
    if args.create:
        mode = "create"
    elif args.delete:
        mode = "delete"
    elif args.update:
        mode = "update"
    else:
        mode = "unknown"
    print(f"Mode: {mode}")
    print(f"Dry run: {args.dry_run}")
    print(f"Config file: {args.config}")

if __name__ == "__main__":
    main()
    

 



























