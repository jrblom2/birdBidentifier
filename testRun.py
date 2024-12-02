from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime
import csv

# Load and initialize the BirdNET-Analyzer models.
analyzer = Analyzer()

recording = Recording(
    analyzer,
    "./birdNETSample.mp3",
    lat=42.058362,
    lon=-87.676475,
    date=datetime.now(),
    min_conf=0.25,
)
recording.analyze()

lat = 42.058362
lon = -87.676475
with open("output/" + "detections.csv", "a") as outfile:
    writer = csv.writer(outfile)
    for bird in recording.detections:
        data = [lat, lon, bird["common_name"]]
        writer.writerow(data)
