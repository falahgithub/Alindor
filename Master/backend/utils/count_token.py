import tiktoken

TOKEN_LIMIT = 2000;

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

def using_count_token(conversation):

  tokens = encoding.encode(conversation)
  num_tokens = len(tokens)
  parts = []

  if num_tokens <= TOKEN_LIMIT:
    parts.append(conversation)
  
  else:
    num_parts_conversation = num_tokens // TOKEN_LIMIT

    lines = conversation.splitlines(keepends=True)
    num_lines_per_part = len(lines) // num_parts_conversation


    for i in range(0, len(lines), num_lines_per_part):   
      part = ''.join(lines[i:i+num_lines_per_part])
      parts.append(part)
    
    if len(lines) % num_lines_per_part != 0:                # for remaining lines
      start_index = num_lines_per_part * num_parts_conversation
      parts.append(''.join(lines[start_index:]))
  
  return parts
