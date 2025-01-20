import os
import eel

# Initialize the Eel app with the "Frontend" folder
eel.init("Frontend")

# Path to Google Chrome (Adjust if Chrome is in a custom location)
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Command to open Chrome in app mode with a specific URL
url = "http://localhost:8000/index.html"
os.system(f'"{chrome_path}" --app="{url}"')

# Start the Eel app
eel.start('index.html', mode=None, host='localhost', block=True)


