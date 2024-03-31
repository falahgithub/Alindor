from openai import OpenAI
from utils.count_token import using_count_token
import json



client = OpenAI(
  api_key="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"
  )

def using_openai(conversation):
 
  output = []
  parts = using_count_token(conversation=conversation)
 

  for part in parts:
    try:
      completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          response_format={ "type": "json_object" },
          messages=[
          {
          "role": "system",
          "content": 
          "You have to do analysis of all speakers ( based on each of their       statements, not entire conversation) during conversation. Thus each turn of each speaker will result in one analysis. \
          Use the following step-by-step instructions to respond to user inputs. \
          step 1: Analyze the text and identify each statement of the speakers.\
          step 2: Give a psychological insight in short about that particular speaker in context of that statement. your output should be like speaker code, followed with colon, followed by your insight. \
          step 3: The output of step 2 should be rephrased so that it become concise. You can use any trick to shorten output. Also omit name of orator (like speaker 0 or 1, etc). Then Output should be appended to a list. \
          step 4: Reiterate step 1, 2 and 3 till you come to the end.\
          step 5: Send output to the user. Your ouput must be in json format. Output should contain the key named 'result' and the value as the list you made in step2" 
          },

    
          {"role": "user", "content": part},
        ]
      )

      new = json.loads(completion.choices[0].message.content)
      output.append(new["result"])

    except:
      output.append(["Error occured from openAI API side"])
      return output
    
  
  return output

  