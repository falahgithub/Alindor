import boto3, os, io

AWS_ACCESS_KEY_ID = os.getenv("AWS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
S3_BUCKET_NAME = "alindor-audio-bucket"

def save_to_s3(file, file_format):
  try:
  
    # s3 = boto3.client("s3", 
    #                   aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    session = boto3.Session()  
    s3 = session.client("s3")

    with io.BytesIO(file) as file_data:
        s3.upload_fileobj(file_data, S3_BUCKET_NAME, f"newest.{file_format}")


    return f"https://alindor-audio-bucket.s3.amazonaws.com/newest.{file_format}"
  except:
     return "Unable to Save"