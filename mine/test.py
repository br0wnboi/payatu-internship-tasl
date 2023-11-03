import datetime
import base64
import urllib.request
import zipfile
import os

# Get the current date in DD-MM-YY format
current_date = datetime.datetime.now().strftime('%d-%m-%y')

# Append ".zip" to the date
date_with_extension = current_date + ".zip"

# Encode the string in base64
encoded_date = base64.urlsafe_b64encode(date_with_extension.encode()).decode()

# Append the encoded date to the URL
url = f"https://www.whoisds.com/whois-database/newly-registered-domains/{encoded_date}/nrd"

# Print url
print(url)

# Download the zip file to the current directory
urllib.request.urlretrieve(url)

# Extract the contents of the zip file to a new folder in the current working directory with the name as the current date
# with zipfile.ZipFile(date_with_extension, 'r') as zip_ref:
#    os.mkdir(current_date)
#     zip_ref.extractall(current_date)


