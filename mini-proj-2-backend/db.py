from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from local_config import MONGODB_CLUSTER, MONGODB_USER, MONGODB_PASSWORD, APP_NAME

try:
    uri = f"mongodb+srv://saimonish2005:Monish2005@pre-developmentstructur.lygl6.mongodb.net/?retryWrites=true&w=majority&appName=Pre-DevelopmentStructure"
    client = MongoClient(uri, server_api=ServerApi('1'))
    
    # Test the connection
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
    
    # Get or create database
    db = client['Diary']
    
    # Get or create collection
    pages_collection = db['Daily Notes']
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    client = None
    db = None
    pages_collection = None