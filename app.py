from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from datetime import datetime

app = FastAPI()

# Mount static files (CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Replace with your OpenWeather API key + location
OPENWEATHER_API = "YOUR_API_KEY"
CITY = "Johannesburg"
LAT, LON = -26.2041, 28.0473  # Example coords


def check_internet():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/dashboard")
def dashboard():
    weather_data = {}
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API}&units=metric"
        r = requests.get(url)
        w = r.json()
        weather_data = {
            "temp": w["main"]["temp"],
            "humidity": w["main"]["humidity"],
            "wind_speed": w["wind"]["speed"],
            "sunrise": datetime.fromtimestamp(w["sys"]["sunrise"]).strftime("%H:%M"),
            "sunset": datetime.fromtimestamp(w["sys"]["sunset"]).strftime("%H:%M"),
            "condition": w["weather"][0]["main"]
        }
    except:
        weather_data = {"error": "Weather fetch failed"}

    return {
        "internet": check_internet(),
        "weather": weather_data,
        "time": datetime.now().strftime("%H:%M"),
        "date": datetime.now().strftime("%A, %d %B"),
        "calendar": [
            {"time": "12:00", "event": "Team Meeting"},
            {"time": "14:30", "event": "Code Review"},
        ]
    }
