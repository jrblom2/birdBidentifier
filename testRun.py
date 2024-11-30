from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime
import json

# Load and initialize the BirdNET-Analyzer models.
analyzer = Analyzer()

recording = Recording(
    analyzer,
    "./input.mp3",
    lat=35.4244,
    lon=-120.7463,
    date=datetime.now(),
    min_conf=0.25,
)
recording.analyze()

data = {
    "lat": recording.lat,
    "lon": recording.lon,
    "date": recording.date.strftime("%m/%d/%Y, %H:%M:%S"),
    "detections": recording.detections,
}
with open("output/" + str(recording.date) + ".json", "w") as outfile:
    json.dump(data, outfile)
