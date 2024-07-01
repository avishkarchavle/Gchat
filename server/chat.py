# import vertexai
# from vertexai.preview.generative_models import GenerativeModel

# project_id ='active-tangent-428009-a6'
# location='us-central1'

# vertexai.init(project=project_id,location=location)

# model = GenerativeModel('gemini-pro')
# response = model.generate_content('Aeroplane')

# print(response.text)
import sys
import vertexai
from vertexai.preview.generative_models import GenerativeModel

project_id = 'active-tangent-428009-a6'
location = 'us-central1'

vertexai.init(project=project_id, location=location)

model = GenerativeModel('gemini-pro')
user_input = sys.argv[1]  # Get the input from the command line argument
prompt="Consider yourself as Avishkar, and answer to the query just like you are replying to Avishkars girlfriend Grishma, also remove the special characters from the response"

response = model.generate_content(prompt+user_input)

print(response.text)
