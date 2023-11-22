from langchain.indexes import VectorstoreIndexCreator
#from langchain.llms import OpenAI
#from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader, TextLoader

import os

key = "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"
os.environ["OPENAI_API_KEY"] = key  # Fix the environment variable name

#llm = OpenAI(openai_api_key=key)  # Pass the API key to the OpenAI instance
#chat_model = ChatOpenAI()

query = "total number of employees"
print("Query:", query)

loader = TextLoader("uni.txt")
print(loader.load())
index = VectorstoreIndexCreator().from_loaders([loader])  # Use `from_loader` instead of `from_loaders`
print(index)
# Query the index and print the response
response = index.query(query)
print("Response:", response)
