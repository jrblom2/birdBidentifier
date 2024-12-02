from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Replace with your Azure Storage Account details
STORAGE_ACCOUNT_NAME = "birdidentifierstorage"
STORAGE_ACCOUNT_KEY = "RRDrk61WfR7C5zPdfC2Ul37EzXMHegbKWdUs3fhjQowP3En+I2t51kvhNVqH921eF9DgbLQ/hL1Z+AStHwANOg=="
CONTAINER_NAME = "birdinformation"


def upload_to_azure(file_path, blob_name):
    try:
        # Create a BlobServiceClient
        connection_string = f"DefaultEndpointsProtocol=https;AccountName={STORAGE_ACCOUNT_NAME};AccountKey={STORAGE_ACCOUNT_KEY};EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )

        # Get the container client
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # Create the container if it doesn't exist
        if not container_client.exists():
            container_client.create_container()

        # Get the blob client
        blob_client = container_client.get_blob_client(blob_name)

        # Upload the file
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"File '{file_path}' uploaded to Azure Blob Storage as '{blob_name}'.")
    except Exception as ex:
        print(f"An error occurred: {ex}")


# Example usage
# upload_to_azure("local_file.txt", "uploaded_file.txt")
upload_to_azure('test.csv', 'birdInfo.csv')
