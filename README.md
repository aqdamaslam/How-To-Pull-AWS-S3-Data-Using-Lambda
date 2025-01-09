# How-To-Pull-AWS-S3-Data-Using-Lambda
How to fetch S3 data (.csv) using AWS Lambda

To pull data from an AWS S3 bucket using AWS Lambda, follow these steps. This guide assumes you are familiar with AWS services like Lambda, IAM, and S3.

### Step 1: Set Up an S3 Bucket

1. **Create an S3 Bucket:**
   - Go to the AWS Management Console.
   - Navigate to **S3** from the Services menu.
   - Click on **Create bucket** and follow the instructions to create a new S3 bucket.
   - Upload the data you want to access via Lambda into this S3 bucket.

### Step 2: Create an IAM Role for Lambda

1. **Create an IAM Role with S3 Access:**
   - Navigate to **IAM** from the AWS Management Console.
   - Go to **Roles** > **Create Role**.
   - Choose **Lambda** as the trusted entity.
   - Attach the `AmazonS3ReadOnlyAccess` policy (or a custom policy that grants read access to the specific S3 bucket).
   - Provide a role name, such as `LambdaS3Role`, and create the role.

### Step 3: Create the Lambda Function

1. **Go to AWS Lambda:**
   - In the AWS Management Console, navigate to **Lambda** and click on **Create function**.
   - Choose **Author from scratch**.
   - Enter a function name, such as `PullS3DataFunction`.
   - Select **Python 3.x** (or Node.js, if you prefer JavaScript) as the runtime (AWS SDK for Python (Boto3) will be used for S3).
   - Under **Permissions**, choose **Use an existing role**, and select the IAM role you created in Step 2 (`LambdaS3Role`).

2. **Write the Lambda Function Code:**
   - In the **Function code** section, write the code to pull data from your S3 bucket.
   - For example, using Python (Boto3):

### Step 4: Configure Lambda Trigger (Optional)

- If you want to automatically trigger the Lambda function based on an event, like when a new object is added to your S3 bucket, you can configure an **S3 Event Trigger**:
  - Go to the **S3 bucket** in the AWS Management Console.
  - Navigate to the **Properties** tab of the bucket and scroll to the **Event notifications** section.
  - Click **Create Event Notification**, select **All object create events** or another event type, and set the Lambda function as the destination.
  - Ensure the Lambda function has the required permissions to read from the S3 bucket.

### Step 5: Test the Lambda Function

1. **Test Lambda in the Console:**
   - In the Lambda Management Console, navigate to your Lambda function.
   - Click on the **Test** tab to configure a test event.
   - You can leave the default test event or configure it to match your S3 event payload (if triggered by an event).
   - Click **Test** to invoke the Lambda function.

2. **Check Logs in CloudWatch:**
   - After testing, go to **CloudWatch Logs** to check the logs.
   - You should see the content of the file you pulled from S3 in the log output.

### Step 6: Monitor and Debug

- Monitor your Lambda function for any errors or performance issues.
- You can adjust logging levels to capture more detailed output if needed.
- Set up CloudWatch metrics and alarms to monitor the success/failure of the Lambda function.

---

### Explanation of the Lambda Function Code:

- **Boto3 Client Initialization**: We use the `boto3` library to interact with AWS services like S3. The `s3 = boto3.client('s3')` line initializes the S3 client to interact with S3.
  
- **Getting the File**: The `s3.get_object()` function fetches the file from the specified S3 bucket and file name. The response contains metadata and the file content.

- **Error Handling**: The try-except block ensures that if an error occurs while fetching the file (e.g., incorrect bucket or file name), it’s caught, and an error message is logged.

- **Reading the File Content**: The file content is read using `response['Body'].read()`. In this example, the content is decoded as a UTF-8 string, but you can handle binary data depending on your use case.

### Step 7: Check Output
It will redirect to the cloudwatch log click on latest log you will get data below 

![image](https://github.com/aqdamaslam/How-To-Pull-AWS-S3-Data-Using-Lambda/assets/56361347/e5eb7cd6-f828-4d56-867d-7724ba4f815e)

---

By following these steps, you can set up an AWS Lambda function to pull data from an S3 bucket, which can be triggered manually or by S3 events.
