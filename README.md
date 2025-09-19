# Google Geocoding API Pipeline

A simple Python script that uses the Google Geocoding API to geocode addresses into latitude and longitude for GIS workflows. Outputs geocoded addresses into a CSV file.

## Getting Started
Console commands assume that you are using a powershell terminal on windows or VSCode.
Set up a Python virtual environment. "myenv" is the random name given to the virtual environment in this example. Change it to a name of your choice.
```
python -m venv myenv
```
Activate Python virtual environment
```
myenv/scripts/activate
```
Install dependancies
```
 pip install -r requirements.txt
 ```
or create requirements.txt file
```
pip freeze > requirements.txt
```
Run the code
```
python google_geocode.py
```
Deactivate virtual environment
```
deactivate
```