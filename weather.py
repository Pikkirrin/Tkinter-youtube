from tkinter import *
import requests
import json

root = Tk()
root.title("Weather")
root.geometry("400x123")


# Create zipcode lookup function
def ziplookup():
    zip.get()


# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=00774BCD-821C-434C-A24A-CC0B53644FD7

try:
    api_request = requests.get(
        "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=00774BCD-821C-434C-A24A-CC0B53644FD7")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == "Good":
        weather_color = "#0C0"
    elif category == "Moderate":
        weather_color = "#FFFF00"
    elif category == "Unhealthy for sensitive Groups":
        weather_color = "#ff9900"
    elif category == "Unhealthy":
        weather_color = "#FF0000"
    elif category == "Very Unhealthy":
        weather_color = "#990066"
    elif category == "Hazardous":
        weather_color = "#660000"

    root.configure(background=weather_color)
    myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=('Helveltica', 20),
                    background=weather_color)
    myLabel.pack()
except:
    api = "Error..."

zip = Entry(root)
zip.pack(pady=10)

zipButton = Button(root, text="Lookup zipcode", command=ziplookup)
zipButton.pack(pady=10)

root.mainloop()
