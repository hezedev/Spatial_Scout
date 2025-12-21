import os

# GitHub Secrets
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

MAX_HOURS = 20
LOCATION = "Austria"

PROFILE_SUMMARY = (
    "Candidate: Master's in AI student with a background in Surveying & Geoinformatics. "
    "Expertise: Machine Learning, Computer Vision (CV), Photogrammetry, Point Clouds. "
    "Equipment: DJI Mavic 2 Pro. Focus: Geospatial AI, Infrastructure Digital Twins. "
    "Constraint: STRICT 20h/week limit for Austria roles. Remote roles are unrestricted."
)

# Standard Geospatial Targets
TARGETS = [
    {"name": "AIT (Students)", "url": "https://jobs.ait.ac.at/jobs?jobProfiles=Studierende"},
    {"name": "TU Wien Jobs", "url": "https://tuwien.bewerberportal.at/Jobs"},
    {"name": "GeoSphere Austria", "url": "https://www.geosphere.at/de/ueber-uns/jobs"},
    {"name": "ESA (Space Agency)", "url": "https://careers.esa.int/"},
    {"name": "UP42 (Remote)", "url": "https://up42.com/careers"},
    {"name": "Globhe (Drone Market)", "url": "https://globhe.com/careers"},
    {"name": "Z_GIS Job Hub", "url": "https://www.plus.ac.at/geoinformatik/jobs/?lang=en"},
    {"name": "EODC (Earth Observation)", "url": "https://eodc.eu/careers/"},
    {"name": "IAEA (UN Careers)", "url": "https://careers.un.org/"}
]

# Dedicated AI Internships
AI_INTERN_TARGETS = [
    {"name": "ISTA (Science Interns)", "url": "https://phd.pages.ist.ac.at/scientific-internships/"},
    {"name": "VRVis (Visual Computing)", "url": "https://www.vrvis.at/jobs/offene-stellen"},
    {"name": "Siemens AI Student", "url": "https://jobs.siemens.com/careers?location=Austria&query=AI%20Student"},
    {"name": "AI Austria", "url": "https://aiaustria.com/jobs"}
]

NEWS_TARGETS = [
    {"name": "TU Wien News", "url": "https://www.tuwien.at/en/mg/geo/news"},
    {"name": "FFG Horizon Europe", "url": "https://www.ffg.at/en/Europe/HorizonEurope"}
]

SIGNAL_KEYWORDS = ["Funding", "Awarded", "Launched", "Grant", "WWTF", "Partnership", "Horizon Europe"]