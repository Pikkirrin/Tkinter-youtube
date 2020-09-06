from tkinter import *
import requests
import json

root = Tk()
root.title("Weather")
root.geometry("400x30")
root.configure(background="green")

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=00774BCD-821C-434C-A24A-CC0B53644FD7

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=00774BCD-821C-434C-A24A-CC0B53644FD7")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality =api[0]['AQI']
    category = api[0]['Category']['Name']
except:
    api = "Error..."

myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=('Helveltica', 20), background="green")
myLabel.pack()

root.mainloop()
