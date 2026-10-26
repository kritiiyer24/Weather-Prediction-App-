import requests 
from flask import Flask, render_template, request 
app=Flask(__name__)
API_KEY="28ea75a6263b44079f9f9c1693387023"
@app.route("/",methods=["GET","POST"])
def home(): 
    weather=None
    error=None
    if request.method=="POST":
        city=request.form.get("city","").strip()
        if not city: 
            error="Please enter a city name"
        else: 
            url="http://api.openweathermap.org/data/2.5/weather"
            params={ 
                "q":city,
                "appid":API_KEY,
                "units":"metric"
            }
            try: 
                response=requests.get(url,params=params,timeout=10)
                if response.status_code==200: 
                    data=response.json()
                    weather={ 
                        "city":data["name"],
                        "temperature":data["main"]["temp"], 
                        "humidity":data["main"]["humidity"],
                        "description":data["weather"][0]["description"]
                    }
                else: 
                    error= "City does not exist"
            except requests.RequestException: 
                error="Unable to connect to weather api"
    return render_template("index.html",weather=weather,error=error)
    
if __name__=="__main__": 
    app.run(debug=True)