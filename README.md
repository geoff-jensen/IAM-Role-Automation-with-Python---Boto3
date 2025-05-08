#  IAM Role Automation with Python & Boto3

This project automates the creation and configuration of AWS IAM roles using Python and the Boto3 SDK. It's designed to streamline cloud access management workflows by programmatically defining, creating, and attaching policies to IAM roles via a structured configuration file.

## 🔧 Features

- Create IAM roles from a JSON or YAML config file  
- Automatically attach managed policies to new roles  
- Log successes, failures, and role ARNs for traceability  
- Modular Python structure for easy extension  
- Command-line runnable: `python main.py`  