from customtkinter import *
import requests

#Initialisation
set_appearance_mode("dark")
set_default_color_theme("green")

WINDOW = CTk()
WINDOW.geometry("300x500")
WINDOW.title("Weather App")

ktemp = 0
ctemp = 0
ftemp = 0

fktemp = 0
fctemp = 0
fftemp = 0

speed = 0
gust = 0

coord = 0

city = ""
weather = ""


#Code
def get_data():
    with open("api.txt", "r") as f:
        API_KEY = f.read()
    city = cityentry.get()
    try:
        if any(i.isdigit() for i in city): #Some numbers give a result. Ensures only strings can be entered
            print("ahhh")
            raise
        url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_KEY}&q={city}"

        response = requests.get(url)
        response = response.json()

        ktemp = round(response["list"][1]["main"]["temp"], 1)
        ctemp = round(ktemp - 273.15, 1)
        ftemp = round((ctemp * 9/5) + 32, 1)

        fktemp = round(response["list"][1]["main"]["feels_like"], 1)
        fctemp = round(ktemp - 273.15, 1)
        fftemp = round((ctemp * 9/5) + 32, 1)

        speed = response["list"][1]["wind"]["speed"]
        gust = response["list"][1]["wind"]["gust"]

        coord = response["city"]["coord"]["lat"]

        weather = response["list"][1]["weather"][0]["description"]
        print(weather)

        ktemplabel = CTkLabel(master=frame, text=f"K: {ktemp}K")
        ktemplabel.place(x=22,y=170)
        ctemplabel = CTkLabel(master=frame, text=f"C: {ctemp}°c")
        ctemplabel.place(x=22,y=190)
        ftemplabel = CTkLabel(master=frame, text=f"F: {ftemp}°F" )
        ftemplabel.place(x=22,y=210)
        fktemplabel = CTkLabel(master=frame, text=f"K: {fktemp}K")
        fktemplabel.place(x=142,y=170)
        fctemplabel = CTkLabel(master=frame, text=f"C: {fctemp}°c")
        fctemplabel.place(x=142,y=190)
        fftemplabel = CTkLabel(master=frame, text=f"F: {fftemp}°F" )
        fftemplabel.place(x=142,y=210)
        speedlabel = CTkLabel(master=frame, text=f"Speed: {speed} m/s")
        speedlabel.place(x=22,y=270)
        gustlabel = CTkLabel(master=frame, text=f"Gust: {gust} m/s" )
        gustlabel.place(x=22,y=290)
        weatherlabel = CTkLabel(master=frame, text=f"The weather in {city} is \n{weather} " )
        weatherlabel.place(x=40,y=340)
    except:
        errorlabel = CTkLabel(master=frame, text=f"An error occured,\n please enter a valid location", fg_color="red")
        errorlabel.place(x=40,y=400)


frame = CTkFrame(master=WINDOW)
frame.pack(pady=20, padx=30, fill="both", expand=True)

title = CTkLabel(master=frame, text="Weather Info")
title.pack(pady=10)

cityentry = CTkEntry(frame, placeholder_text="Enter city name:")
cityentry.pack(pady=10)

searchbutton = CTkButton(frame, text="Search", command=get_data)
searchbutton.pack(pady=5)

templabel = CTkLabel(master=frame, text=f"Temperature:")
templabel.place(x=20,y=150)

ktemplabel = CTkLabel(master=frame, text=f"K: {ktemp}K")
ktemplabel.place(x=22,y=170)


ctemplabel = CTkLabel(master=frame, text=f"C: {ctemp}°c")
ctemplabel.place(x=22,y=190)

ftemplabel = CTkLabel(master=frame, text=f"F: {ftemp}°F" )
ftemplabel.place(x=22,y=210)


ftemplabel = CTkLabel(master=frame, text=f"Feels Like:")
ftemplabel.place(x=140,y=150)

fktemplabel = CTkLabel(master=frame, text=f"K: {fktemp}K")
fktemplabel.place(x=142,y=170)

fctemplabel = CTkLabel(master=frame, text=f"C: {fctemp}°c")
fctemplabel.place(x=142,y=190)

fftemplabel = CTkLabel(master=frame, text=f"F: {fftemp}°F" )
fftemplabel.place(x=142,y=210)

templabel = CTkLabel(master=frame, text=f"Temperature:")
templabel.place(x=20,y=150)



windlabel = CTkLabel(master=frame, text=f"Wind:")
windlabel.place(x=20,y=250)

speedlabel = CTkLabel(master=frame, text=f"Speed: {speed} m/s")
speedlabel.place(x=22,y=270)

gustlabel = CTkLabel(master=frame, text=f"Gust: {gust} m/s" )
gustlabel.place(x=22,y=290)


WINDOW.mainloop()





#print(response)
