# Import libraries
import os
import requests
import pandas as pd
import urllib3
import certifi


# Get Data function
def get_data (url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    output = 0
    filename = url.split('/')[-1]

    try:
        # Check filename doesn't exist
        if os.path.exists(filename):
            print('Error: File exists, skipping download.')
            output = 'FileExists'
        else:
            # Download URL to data
            req = http.request('GET', url)
            data = req.data

            # Write to file locally
            f = open(filename, 'wb')
            f.write(data)
            f.close()

            print('Success: Downloaded data to: "' + filename + '"')
            output = 'FileDownloaded'   
    except Exception as error:
        print('Exception details: ' + repr(error))
        output = 'NoUrl'
    return (output)

# Remove Data function
def remove_data (url):
  filename = url.split('/')[-1]
  if os.path.exists(filename):
      os.remove(filename)
      print('Success: "' + filename + '" deleted.')
      output = 'FileDeleted'
  else:
      print('Error: File does not exist.')
      output = 'NoFile'
  return (output)

# Run the following code if the file is run at the command line
if __name__ == "__main__":
  option = int(input("Enter an option [0 = Get Data, 1 = Remove Data]: "))
  if option == 0:
    url = input("Enter a url: ")
    get_data(url)
  elif option == 1:
    local_file = input("Enter a url: ")
    remove_data(local_file)
  else:
    print("Invalid option.")