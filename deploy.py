from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError

client = MiraClient(config={"API_KEY": "sb-709187d8f2d899030c54b3e8ac95e262"})     # Initialize client

flow = Flow(source="https://replit.com/@archiemittal12/Python-1#flow.yaml")                    # Load flow
try:
    client.flow.deploy(flow)                                # Deploy to platform
except FlowError as e:
    print(f"Error occurred: {str(e)}")                      # Handle deployment error
