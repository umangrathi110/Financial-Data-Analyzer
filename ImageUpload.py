import cloudinary.uploader
import os 
from dotenv import load_dotenv

load_dotenv()

cloud_name = os.getenv("CLOUD_NAME")
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")


def uploadImageOnCloud(fileName):
    # Configure Cloudinary credentials
    cloudinary.config( 
        cloud_name = cloud_name, 
        api_key = api_key, 
        api_secret = api_secret
    )
    # Upload a file to Cloudinary
    result = cloudinary.uploader.upload(fileName, folder="poc-graph")
    return result['secure_url']

# this will return all the details of the uploaded image on the cloudinary 
# a = uploadImageOnCloud("csv_graph.png")
# print (a)
