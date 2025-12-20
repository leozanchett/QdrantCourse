from dotenv import load_dotenv
import os
from qdrant_client import QdrantClient
from qdrant_client.http import models

load_dotenv()

client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"))

print(client.get_collections())