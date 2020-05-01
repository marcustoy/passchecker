# PassChecker

This simple python application is a convenient script written based on the concept presented under the "Searching by Range" API section under haveibeenpawned (https://haveibeenpwned.com/API/v/#SearchingPwnedPasswordsByRange). This application takes in a password from the user, and instead of sending the whole password text to the haveibeenpawned online database to find matches, the application only sends the first 5 character of the SHA-1 hash to get a list of potential matches which will be subsequently matched against locally. This process adds an additional layer of security by not exposing the full password to any outside parties. 


This application was inspired by the work from haveibeenpawned by Troy Hunt (https://haveibeenpwned.com).

## Installation
1. Ensure Python 3 is installed in your machine.
2. Run `python3 -m venv venv` to create a virtual environment. 
3. Activate the environment by running: `source venv/bin/activate` (Linux/MacOS); `venv/Scripts/activate.bin` (Windows)
4. Install dependencies by running `pip3 install -r requirements.txt`
5. Start application by running `python3 app.py`

