# Create a new csv file with a column of addresses for geocoding
# Save the csv file in the same folder with this python geocoding script
# Type "python google_geocode.py" in terminal to run script and start geocoding!

import requests
import csv

# Google Geocoding API key
api_key = "Placeholder" # Replace with your api key

# Input and output file paths
input_csv = "addresses.csv"
output_csv = "coordinates.csv"

# Open and read csv file with addresses and URL encode the file
# Create output csv file for writing with latitude and longitude as fieldnames
with open(input_csv, "r", encoding="utf-8") as infile, open(output_csv, "w", newline='', encoding="utf-8") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["latitude", "longitude"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through addresses in input csv file
    for row in reader:
        address = row['address'] # Replace 'address' with name of address column
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}%20Richmond%20BC&key={api_key}" # URL is adjusted for Toronto Ontario: '%20Toronto%20ON'. Replace accordingly
        # Make google geocoding api request
        response = requests.get(url)

        # If api request is successful
        if response.status_code == 200:
            geocoded_data = response.json()
            # Extract coordinates from json response
            if geocoded_data['status'] == 'OK':
                location = geocoded_data['results'][0]['geometry']['location']
                row['latitude'] = location['lat']
                row['longitude'] = location['lng']
            # If api reqeusts succeeds but json response includes error or something wrong with geocoding
            else:
                print(f"Geocoding failed for address:{address}. Status json: {geocoded_data['status']}")
                row['latitude'] = None
                row['longitude'] = None
        
        # If api request fails
        else:
            print(f"HTTP geocode request failed for address: {address}. Status code: {response.status_code}")
            row['latitude'] = None
            row['longitude'] = None

        # Write the geocoded coordinates into the output csv file
        writer.writerow(row)
        # Print geocoded address and output coordinates for logging and debugging
        print(f"Address: {address} -> Latitude: {row['latitude']}, Longitude: {row['longitude']}")

print(f"Geocoding completed! Results saved to {output_csv}!")