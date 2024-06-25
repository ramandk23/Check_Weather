from tkinter import *
from tkinter import ttk

import requests

def get_weather_data():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=66f40733770948784546b5a48e731293").json()
    w_label_result.config(text = data["weather"][0]["main"])
    desc_label_result.config(text=data["weather"][0]["description"])
    temprature = int(data["main"]["temp"] - 273.15)
    temprature_label_result.config(text = str(temprature)+"°C")
    pressure_label_result.config(text = data["main"]["pressure"])
    humidity_label_result.config(text = data["main"]["humidity"])

win = Tk()
win.title("How's Weather")
win.config(bg="#2F7AB0")
win.geometry("500x520")

name_label = Label(win, text = "Get Today's Weather", font=("Arial", 30 , "bold"))
name_label.place(x=25, y=50, height=50, width=450)

list_names = ["Singapore", "Johor Bahru", "Kuala Lumpur", "Batam", "Bangkok", "Vietnam", "Delhi","Mumbai","Kochi", "Chennai", "Pune",  "Bhopal","Bhubaneswar","Chandigarh","Faridabad","Ghaziabad","Jamshedpur","Jaipur","Kochi","Lucknow",
"Nagpur","Patna","Raipur","Surat","Visakhapatnam","Agra","Ajmer","Kanpur","Mysore","Srinagar",
]

city_name = StringVar()
country_combo = ttk.Combobox(win, text = "How's Weather Today", font=("Arial", 30 , "bold"), values=list_names, textvariable=city_name)
country_combo.place(x=25, y=110, height=40, width="450")

w_label = Label(win, text = "Weather Climate:", font=("Arial", 17), bg="#2F7AB0", justify=LEFT)
w_label.place(x=25, y=250, height=30, width=210)
w_label_result = Label(win, text = "", font=("Arial", 17), bg="#2F7AB0", justify=LEFT)
w_label_result.place(x=200, y=250, height=30, width=210)

desc_label = Label(win, text = "Description:", font=("Arial", 17), bg="#2F7AB0", justify=LEFT)
desc_label.place(x=25, y=290, height=30, width=210)
desc_label_result = Label(win, text = "", font=("Arial", 17), bg="#2F7AB0", justify=LEFT)
desc_label_result.place(x=200, y=290, height=30, width=210)

temprature_label = Label(win, text = "Temprature:", font=("Arial", 17), bg="#2F7AB0", justify=LEFT)
temprature_label.place(x=25, y=330, height=30, width=210)
temprature_label_result = Label(win, text = "", font=("Arial", 17), bg="#2F7AB0", justify=LEFT)
temprature_label_result.place(x=200, y=330, height=30, width=210)

pressure_label = Label(win, text = "Pressure:", font=("Arial", 17), bg="#2F7AB0", justify=LEFT)
pressure_label.place(x=25, y=370, height=30, width=210)
pressure_label_result = Label(win, text = "", font=("Arial", 17), bg="#2F7AB0", justify=LEFT)
pressure_label_result.place(x=200, y=370, height=30, width=210)

humidity_label = Label(win, text = "Humidity:", font=("Arial", 17), bg="#2F7AB0", justify=LEFT)
humidity_label.place(x=25, y=410, height=30, width=210)
humidity_label_result = Label(win, text = "", font=("Arial", 17), bg="#2F7AB0", justify=LEFT)
humidity_label_result.place(x=200, y=410, height=30, width=210)



check_weather_button = Button(win, text="Get", font=("Arial","30", "bold", "italic"), command=get_weather_data)
check_weather_button.place(x=150, y=170, width=150, height=40)


win.mainloop()