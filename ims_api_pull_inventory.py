import json
import boto3
import requests
from botocore.exceptions import BotoCoreError

# Function to get config data
def get_config():
    with open('api_config.json', 'r') as f:
        return json.load(f)

# Get the config data
config = get_config()

# Define your GraphQL API details
api_id = config['api_id']
api_region = config['region']
api_key = config['api_key']

# Define your GraphQL query
query = """
query ListFiles {
  listFiles {
    nextToken
    items {
      extension
      filename
      id
      md5
    }
  }
}

"""

# Define your API endpoint URL
api_url = f'https://{api_id}.appsync-api.{api_region}.amazonaws.com/graphql'

try:
    # Make the GraphQL request
    response = requests.post(
        api_url,
        headers={'x-api-key': api_key, 'Content-Type': 'application/json'},
        json={'query': query}
    )

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()

        # Write the results to a JSON file
        with open('files.json', 'w') as f:
            json.dump(results, f)
    else:
        print(f'Error making GraphQL request: {response.content}')

except BotoCoreError as e:
    print(f'Error making GraphQL request: {e}')

# Define your GraphQL query
query = """
query ListHosts {
  listHosts {
    nextToken
    items {
      id
      hostname
      updatedAt
      createdAt
    }
  }
}
"""

# Define your API endpoint URL
api_url = f'https://{api_id}.appsync-api.{api_region}.amazonaws.com/graphql'

try:
    # Make the GraphQL request
    response = requests.post(
        api_url,
        headers={'x-api-key': api_key, 'Content-Type': 'application/json'},
        json={'query': query}
    )

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()

        # Write the results to a JSON file
        with open('hosts.json', 'w') as f:
            json.dump(results, f)
    else:
        print(f'Error making GraphQL request: {response.content}')

except BotoCoreError as e:
    print(f'Error making GraphQL request: {e}')
