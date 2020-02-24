imports requests

url="https://s3.us-south.cloud-object-storage.appdomain.cloud/cloud-object-storage-eda-folders"

r = requests.get(url)
print(r.code)