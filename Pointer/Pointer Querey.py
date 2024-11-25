#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import libraries

from dotenv import load_dotenv
import weaviate.classes as wvc
import os
load_dotenv()

# Best practice: store your credentials in environment variables
wcd_url = os.environ["WEAVIATE_URL"]
wcd_api_key = os.environ["WEAVIATE_API_KEY"]
openai_api_key = os.environ["OPENAI_API_KEY"]


# Debugging: Print loaded variables
print(f"OpenAI API Key: {'Loaded' if openai_api_key else 'Not Loaded'}")
print(f"Weaviate Endpoint: {'Loaded' if wcd_url else 'Not Loaded'}")
print(f"Weaviate API Key: {'Loaded' if wcd_api_key else 'Not Loaded'}")

import weaviate
from weaviate.classes.init import Auth

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_api_key),
)

print("Weaviate is ready: ", client.is_ready())


# In[41]:





# In[25]:


from pprint import pprint  # Import pprint for a readable output

# Establish the Weaviate client connection
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,                                    # Replace with your Weaviate Cloud URL
    auth_credentials=wvc.init.Auth.api_key(wcd_api_key),    # Replace with your Weaviate Cloud key
    headers={"X-OpenAI-Api-Key": openai_api_key}            # Replace with appropriate header key/value pair for the required API
)

try:
    # Initial query to get the database name
    collection_name = "Pointer"
    questions = client.collections.get(collection_name)

    response = questions.query.near_text(
        query=input("Query: "),
        limit=6
    )

    # Extract the database name from the response properties
    database_name = response.objects[0].properties.get("database_name")
    print(f"Extracted database name: {database_name}")
    
    # Use the extracted database name in a subsequent call and display 5 responses in pretty format
    if database_name:
        next_query_response = client.collections.get(database_name).query.near_text(
            query="Your next query here",  # Replace with the user's next intended query
            limit=5
        )
        
        # Display the properties of each object in a pretty format
        print("Next Query Responses:")
        for i, obj in enumerate(next_query_response.objects[2:5], start=1):
            print(f"\nResponse {i}:")
            pprint(obj.properties)
    else:
        print("Database name not found in the response.")

finally:
    client.close()  # Ensure the client is closed gracefully


# In[ ]:




