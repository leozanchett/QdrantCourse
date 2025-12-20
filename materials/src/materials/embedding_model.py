from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embed_model = AzureOpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=1536,
)