from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError

client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})     # Initialize client

flow = Flow(source="https://replit.com/@archiemittal12/Python-1#flow.yaml")                    # Load flow
try:
    client.flow.deploy(flow)                                # Deploy to platform
except FlowError as e:
    print(f"Error occurred: {str(e)}")                      # Handle deployment error
