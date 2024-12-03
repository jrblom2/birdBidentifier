from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime
import csv
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Replace with your Azure Storage Account details
STORAGE_ACCOUNT_NAME = "birdidentifierstorage"
STORAGE_ACCOUNT_KEY = ""
CONTAINER_NAME = "birdinformation"


def upload_to_azure(file_path, blob_name):
    try:
        # Create a BlobServiceClient
        connection_string = f"DefaultEndpointsProtocol=https;AccountName={STORAGE_ACCOUNT_NAME};AccountKey={STORAGE_ACCOUNT_KEY};EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )

        # Get the container client
        container_client = blob_service_client.get_container_client(
            CONTAINER_NAME
        )

        # Create the container if it doesn't exist
        if not container_client.exists():
            container_client.create_container()

        # Get the blob client
        blob_client = container_client.get_blob_client(blob_name)

        # Upload the file
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(
            f"File '{file_path}' uploaded to Azure Blob Storage as '{blob_name}'."
        )
    except Exception as ex:
        print(f"An error occurred: {ex}")


# Load and initialize the BirdNET-Analyzer models.
analyzer = Analyzer()

recording = Recording(
    analyzer,
    "./input.mp3",
    lat=42.058362,
    lon=-87.676475,
    date=datetime.now(),
    min_conf=0.25,
)
recording.analyze()

lat = 42.058362
lon = -87.676475
with open("output/detections.csv", "a") as outfile:
    writer = csv.writer(outfile)
    for bird in recording.detections:
        data = [lat, lon, bird["common_name"]]
        writer.writerow(data)

upload_to_azure('output/detections.csv', 'birdInfo.csv')
