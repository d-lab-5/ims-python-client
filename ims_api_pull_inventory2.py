import json
import boto3
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
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

# Define your API endpoint URL
api_url = f'https://{api_id}.appsync-api.{api_region}.amazonaws.com/graphql'

# Create a transport with the API endpoint URL and API key
transport = RequestsHTTPTransport(url=api_url, headers={'x-api-key': api_key}, use_json=True)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Define your GraphQL queries
queries = {
    "ListFiles": """
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
    """,
    "ListHosts": """
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
}

# Execute the queries and write the results to JSON files
for query_name, query_str in queries.items():
    try:
        # Execute the GraphQL query
        query = gql(query_str)
        result = client.execute(query)

        # Write the results to a JSON file
        with open(f'{query_name.lower()}.json', 'w') as f:
            json.dump(result, f)

    except BotoCoreError as e:
        print(f'Error making GraphQL request: {e}')
