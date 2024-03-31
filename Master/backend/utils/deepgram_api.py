import json

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
)



API_KEY = "7e523932953edaa204f571187d4ee8cd638701f7"

def using_deepgram(AUDIO_FILE):
  
  # URL to the audio file
  AUDIO_URL = {"url": AUDIO_FILE}
  
  try:
    deepgram = DeepgramClient(API_KEY)

    options = PrerecordedOptions(
        model="nova-2",
        smart_format=True,
        diarize=True
    )

    # STEP 3: Call the transcribe_url method with the audio payload and options
    response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)
    
    # STEP 4: Return the response
    net_response = response.to_json(indent=4)
    return net_response

  except Exception as e:
    print(e)
    return json.dumps({"Exception": "Error occured from Deepgram API side"})
