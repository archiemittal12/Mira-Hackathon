from mira_sdk import MiraClient, Flow
import os

# Load environment variables from .env file


my_secret = os.environ['API_KEY']

# Initialize the client
client = MiraClient(config={"API_KEY": my_secret})

flow = Flow(source="flow.yaml")

input_dict = {"topic": "Hard Life", "style": "Lil Wayne"}

response = client.flow.test(flow, input_dict)

print(response)