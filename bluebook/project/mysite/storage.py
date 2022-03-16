from storages.backends.s3boto3 import S3Boto3Storage

#정적 파일용
class S3StaticStorage(S3Boto3Storage):
    location = 'static'
    
#미디어 파일용
class S3MediaStorage(S3Boto3Storage):
    location = 'media'