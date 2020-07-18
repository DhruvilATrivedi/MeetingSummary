import boto3
import time
import urllib.request as ur
import json


AWS_ACCESS_KEY_ID = 'AKIA4KRDLQZDBRHHME55'
AWS_SECRET_ACCESS_KEY = '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'

job_name = 'first_job6'
job_uri = 'https://project21test.s3.ap-south-1.amazonaws.com/recorded2.wav'

transcribe = boto3.client('transcribe', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY,region_name='ap-south-1')
transcribe.start_transcription_job(TranscriptionJobName=job_name, Media={'MediaFileUri': job_uri}, MediaFormat='wav', LanguageCode='en-US')
while True:
    status = transcribe.get_medical_transcription_job(
    MedicalTranscriptionJobName = job_name
)
#    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(2)
print(status)

if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
    response = ur.urlopen(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])
    data = json.loads(response.read())
    text = data['results']['transcripts'][0]['transcript']
    print(text)
    