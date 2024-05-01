# How-To-Pull-AWS-S3-Data-Using-Lambda
How to fetch S3 data using AWS Lambda



## Steps to fetch S3 Data Using Lambda
### Step 1
  Login into AWS Console and Create a S3 bucket with default settings
### Step 2
  Go to Lambda and create a lambda function using Author from scratch option and fill function name
  Select Runtime Python 3.x
  Architecture --> x86_64
  Change default execution role --> Select Create a new role with basic Lambda permissions
  No need to change Advanced settings
  Click Create Function Button
### Step 3
    Go To Bucket ---> Properties ---> Create event notification
                      In General Configuration -- Fill Event name and leave it Prefix and Suffix
                      In Event types -- Object creation -- Select All object create events
                      In Destination -- Choose Lambda function
                      In Specify Lambda function -- Choose from your Lambda functions

### Step 4 
  Click on Lambda function that you have created 
### Step 5
  Click on Code tab and remove everything from code snippet and paste LambdaCode.py code into them
### Step 6
  Scroll little bit up you will se function overview
### Step 7
  Click on Layers it will redirect to the layer section
### Step 8
  Click on Add Layer
    Go with AWS layers and from dropdown menu select ### AWSSDKPandas-Python39 and select latest version 
    and click Add Layer button
## Note: - Adding layers to this lambda function because this code is imprting pandas library
### Step 9
  Click Deploy Button to make changes

## To Check the function
  
