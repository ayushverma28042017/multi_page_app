import cohere 
co = cohere.Client('') # This is your trial API key
response = co.chat( 
  message='<YOUR MESSAGE HERE>',
  prompt_truncation='auto',
  connectors=[{"id": "web-search"}]
) 
print(response)