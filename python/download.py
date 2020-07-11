#pull a csv
import requests

download_url = "URLofCSV"
target_csv_path = "CSFfileName.csv"

response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")
