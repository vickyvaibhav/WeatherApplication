import tkinter as tk
import requests
from tkinter import font
from tkinter import *

WIDTH = 700
HEIGHT = 600

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
# weather api key : e3dbc5aed72a94ffaffe320286fe4811


def get_weather(city):
    weather_key = 'e3dbc5aed72a94ffaffe320286fe4811'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key,'q':city, 'units': 'imperial'}
    response = requests.get(url,params=params)
    weather = response.json()
    label['text'] = format_response(weather)

def format_response(weather):
    print(weather)
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        country = weather['sys']['country']
        final_str =  'City: %s \nConditions: %s \nTemperature(F): %s\nCountry: %s' %(name,desc,temp,country)
    except:
        final_str = "Please Enter the Correct City name/Zipcode"
    return final_str

root = tk.Tk()
root.title("Weather Application")
root.maxsize(700,600)
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = PhotoImage(file='2.gif')
background_label = Label(root, image = background_image)
#background_label.background_image = background_image
background_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx = 0.5, rely = 0.12, relwidth = 0.75, relheight = 0.1, anchor = 'n')

lbl = tk.Label(root,text = 'Enter City name or zipcode to get Weather', bg = '#80c1ff', bd = 5,font=('Courier',15))
lbl.place(relx = 0.5, rely = 0.03, relwidth = 0.75, relheight = 0.08, anchor='n')

entry = tk.Entry(frame, font=('Courier',15))
entry.insert(0,"Boston")
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", font=('Courier',10), command = lambda :get_weather(entry.get()))
button.place(relx = 0.70, relwidth = .30, relheight = 1)

lower_frame = tk.Frame(root,bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.27, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame, bg = 'cyan', font=('Courier',15),anchor = 'nw',justify ='left')
label.place(relwidth = 1, relheight = 1)

lbl = tk.Label(root,text = 'Developed By Vaibhav Agrawal', bg = '#80c1ff',fg = '#F2512E', bd = 5,font=('Courier',15))
lbl.place(relx = 0.5, rely = 0.9, relwidth = 0.75, relheight = 0.08, anchor='n')

root.mainloop()