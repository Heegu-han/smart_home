import boto3
import datetime

s3=boto3.resource('s3')
nowDatetime=datetime.datetime.now().strftime('%Y_%m_%d')
fileName=datetime.datetime.now().strftime('%H_%M_%S')
data=open('1.mp4','rb')
s3.Bucket('smarthome-2021').put_object(Key='cctv/'+nowDatetime+'/' +fileName+'.mp4',Body=data,ACL='public-read')
