import pymongo

url = 'mongodb+srv://shaaban1:Anas506-@cluster0.djszvee.mongodb.net/'
client = pymongo.MongoClient(url)

db = client['ShopGPT']