from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="Radar 360 API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "ok", "service": "Radar 360 API"}

@app.get("/api/aircraft")
async def aircraft():
    params = {
        "lamin": 53.35,
        "lomin": 18.60,
        "lamax": 54.95,
        "lomax": 20.20
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.get(
            "https://opensky-network.org/api/states/all",
            params=params
        )
        response.raise_for_status()
        data = response.json()

    planes = []
    for s in data.get("states") or []:
        if s[5] is None or s[6] is None:
            continue
        planes.append({
            "icao24": s[0],
            "callsign": (s[1] or "").strip(),
            "originCountry": s[2],
            "longitude": s[5],
            "latitude": s[6],
            "baroAltitude": s[7],
            "onGround": s[8],
            "velocity": s[9],
            "trueTrack": s[10],
            "verticalRate": s[11]
        })

    return {
        "time": data.get("time"),
        "count": len(planes),
        "aircraft": planes,
        "source": "OpenSky Network"
    }
