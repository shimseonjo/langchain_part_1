import meilisearch
import os
from dotenv import load_dotenv
load_dotenv()

client = meilisearch.Client(url=os.getenv('MEILISEARCH_URL'), api_key=os.getenv('MEILISEARCH_API_KEY'))


def stock_search(query):
    return client.index('nasdaq').search(query)
