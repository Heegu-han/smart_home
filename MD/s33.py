import boto3
import datetime

def s3_upload(filename):
    s3 = boto3.resource('s3')
#     nowDatetime=datetime.datetime.now().strftime('%Y_%m_%d')
#     fileName=datetime.datetime.now().strftime('%H_%M_%S')
    folder_name, file_name = filename.split(' ')
    data = open(filename + '.mp4','rb')
    s3.Bucket('smarthome-2021').put_object(Key='cctv/'+folder_name+'/' +file_name+'.mp4', Body=data, ACL='public-read')
