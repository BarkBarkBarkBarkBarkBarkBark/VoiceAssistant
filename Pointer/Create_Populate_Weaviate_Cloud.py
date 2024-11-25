#!/usr/bin/env python
# coding: utf-8
#:)
# In[30]:


import os
import weaviate
import weaviate.classes as wvc
import weaviate.classes.config as wc
from weaviate.auth import AuthApiKey
from dotenv import load_dotenv

load_dotenv()

WEAVIATE_CLUSTER_URL = os.getenv('WEAVIATE_URL')
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_CLUSTER_URL,  # Replace with your Weaviate Cloud URL
        auth_credentials=AuthApiKey(api_key=WEAVIATE_API_KEY),  # Replace with your Weaviate Cloud key
        headers={'X-OpenAI-Api-key': OPENAI_API_KEY}  # Replace with your OpenAI API key
    )

collection = input("Collection Name: ")

client.collections.delete(collection)
print(client.is_connected())

questions = client.collections.create(
    name=collection,

#adatabase_name	keywords	few_shot_examples
    vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(model="text-embedding-3-small"),
    generative_config=wvc.config.Configure.Generative.openai(model="gpt-4o-mini"),
    properties=[
        wc.Property(name= "database_name", data_type=wc.DataType.TEXT),
        wc.Property(name= "keywords", data_type=wc.DataType.TEXT),
        wc.Property(name= "few_shot_examples", data_type=wc.DataType.TEXT),
        #wc.Property(name= "example", data_type=wc.DataType.TEXT, skip_vectorization=True),
        #wc.Property(name= "example", data_type=wc.DataType.TEXT, skip_vectorization=True),
        #wc.Property(name= "example", data_type=wc.DataType.TEXT, skip_vectorization=True),
        #wc.Property(name= "example", data_type=wc.DataType.TEXT, skip_vectorization=True),
        
    ],
)

client.close()


# In[31]:


import os
import csv
import weaviate
from dotenv import load_dotenv
from weaviate.auth import AuthApiKey

load_dotenv()

WEAVIATE_CLUSTER_URL = os.getenv('WEAVIATE_URL')
WEAVIATE_API_KEY = os.getenv('WEAVIATE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_CLUSTER_URL,  # Replace with your Weaviate Cloud URL
        auth_credentials=AuthApiKey(api_key=WEAVIATE_API_KEY),  # Replace with your Weaviate Cloud key
        headers={'X-OpenAI-Api-key': OPENAI_API_KEY}  # Replace with your OpenAI API key
    )


book_collection = client.collections.get(input("Collection Name: "))

f = open(input("File Path: "), "r", encoding="cp1252")
current_book = None
try:
    reader = csv.reader(f)
    # Iterate through each row of data
    for book in reader:
      current_book = book


#adatabase_name	keywords	few_shot_examples


      properties = {
          "database_name": book[0],
          "keywords": book[1],
          "few_shot_examples": book[2],
          #"examples": book[2],
          #"examples": book[2],
          #"examples": book[2],
          #"examples": book[2],
          #"examples": book[2],
          #"examples": book[2],
          #"examples": book[2],
          #"examples": book[2],
          #"examples": book[2],
          #"examples": book[2],
          #"examples": book[2],

          

      }

      uuid = book_collection.data.insert(properties)      

      print(f"{book[0]}: {uuid}", end='\n')
except Exception as e:
  print(f"Exception: {e}.")

f.close()
client.close()


# In[ ]:





# In[ ]:





# In[ ]:




