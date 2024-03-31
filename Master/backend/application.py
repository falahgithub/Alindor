from flask import Flask, redirect, request, jsonify
from utils.deepgram_api import using_deepgram
from utils.s3 import save_to_s3
from utils.openai_api import using_openai
import json

from flask_cors import CORS


application = Flask(__name__)
CORS(application) 



@application.route('/upload', methods=['POST'])
def upload_file():
    if 'audio_file' not in request.files:
        return redirect(request.url)
    
    audio_file = request.files['audio_file']

    if audio_file.filename == '':
        return redirect(request.url)
    

    if audio_file:

        # Get the audio file size 
        audio_file.seek(0, 2)  
        file_size = audio_file.tell()  
        file_size_GB = file_size / (1024 * 1024 * 1024) 
        audio_file.seek(0, 0)  


        if file_size_GB > 2:
            return jsonify({"failed":"Size Exceeded",
                    "insights": [["Transcription not possible"]],        
                    "conversation":"Size should be less than 2 GB for Deepgram transcription"})



        file_format = audio_file.filename.split(".")[1]    # Get format of file
        file_content = audio_file.read()


        obj_url = save_to_s3(file=file_content, file_format=file_format)
   

        if obj_url == "Unable to Save":                    # exiting if error from aws side
            return jsonify({"failed":"Unable to save file to S3",
                    "insights": [["Unable to save file to S3"]],        
                    "conversation": "Unable to save file to S3"})
             
                
        deepgram_data = using_deepgram(AUDIO_FILE=obj_url)            
        transcripted = json.loads(deepgram_data)

        try:
            data_for_openai = transcripted["results"]["channels"][0]["alternatives"][0]["paragraphs"]["transcript"]
        except:
            data_for_openai = transcripted["Exception"]     # if error from deepgram API
            



        analysis = using_openai(conversation=data_for_openai)


        return jsonify({"success":"File has been received and saved",
                    "insights": analysis,        
                    "conversation": data_for_openai})



if __name__ == '__main__':
    application.run(port=8000, debug=True)