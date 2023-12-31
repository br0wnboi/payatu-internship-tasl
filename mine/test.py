import datetime
import base64
import urllib.request
import zipfile
import os
import datetime

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
yesterday_date = yesterday.strftime('%Y-%m-%d') 
print(yesterday_date)

# Append ".zip" to the date
yesterday_date_with_extension = yesterday_date + ".zip"

# Encode the string in base64
encoded_date = base64.b64encode(yesterday_date_with_extension.encode()).decode()

print(encoded_date)

# Append the encoded date to the URL
url = f"https://www.whoisds.com/whois-database/newly-registered-domains/{encoded_date}/nrd"

# Print url
print(url)

# Download the zip file to the current directory
urllib.request.urlretrieve(url)

# Save the response the from the URL and wait until it is downloaded
response = urllib.request.urlopen(url)

# Extract the contents of the zip file to a new folder in the current working directory with the name as the current date
# with zipfile.ZipFile(yesterday_date_with_extension, 'r') as zip_ref:
#    os.mkdir(yesterday_date)
#   zip_ref.extractall()


