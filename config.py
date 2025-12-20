import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

MAX_HOURS = 20
LOCATION = "Austria"

PROFILE_SUMMARY = (
    "Candidate: Master's in AI student with a professional background in Surveying & Geoinformatics. "
    "Expertise: Machine Learning, Computer Vision (CV), Deep Learning for Point Clouds. "
    "Equipment: Owns DJI Mavic 2 Pro. Focus: Geospatial AI, Photogrammetry, and Digital Twins. "
    "Constraint: STRICT 20h/week limit for Austria roles. Remote roles are unrestricted."
)

TARGETS = [

    {"name": "AIT (Austrian Institute of Tech)", "url": "https://jobs.ait.ac.at/jobs?jobProfiles=Studierende"},
    {"name": "TU Wien", "url": "https://tuwien.bewerberportal.at/Jobs"},
    {"name": "Z_GIS (Uni Salzburg Job Board)", "url": "https://www.plus.ac.at/geoinformatik/jobs/?lang=en"},
    {"name": "GeoSphere Austria (Geophysics/RS)", "url": "https://www.geosphere.at/de/ueber-uns/jobs"},
    {"name": "EODC (Earth Observation Data Centre)", "url": "https://eodc.eu/careers/"},
    
 
    {"name": "AI Austria (AI Hub)", "url": "https://aiaustria.com/jobs"},
    {"name": "Dronetech Austria", "url": "https://www.dronetech.at/en/company/jobs/"},
    
    {"name": "UP42 (Remote Satellite Data)", "url": "https://up42.com/careers"},
    {"name": "Globhe (Drone Data Market)", "url": "https://globhe.com/careers"},
    {"name": "ESA (European Space Agency)", "url": "https://careers.esa.int/"}
]

NEWS_TARGETS = [
    {"name": "TU Wien News (ICT/AI)", "url": "https://www.tuwien.at/en/mg/geo/news"},
    {"name": "GeoSphere Press (Climate/Geo)", "url": "https://www.geosphere.at/en/news-and-events/news"},
    {"name": "AIT Research Projects", "url": "https://www.ait.ac.at/en/projects"},
    {"name": "FFG Horizon Europe News", "url": "https://www.ffg.at/en/Europe/HorizonEurope"}
]


PROFILE_SUMMARY = (
    "AI Master's student with a background in Surveying and Geoinformatics. "
    "Expertise: Machine Learning, Computer Vision, Photogrammetry. "
    "Assets: Owns and operates a DJI Mavic 2 Pro. "
    "Focus: Spatial Intelligence, Geospatial AI, Infrastructure Digital Twins."
)


TARGETS = [
    {"name": "AIT (Students)", "url": "https://jobs.ait.ac.at/jobs?jobProfiles=Studierende"},
    {"name": "TU Wien Jobs", "url": "https://tuwien.bewerberportal.at/Jobs"},
    {"name": "GeoSphere Austria", "url": "https://www.geosphere.at/de/ueber-uns/jobs"},
    {"name": "ESA (Space Agency)", "url": "https://careers.esa.int/"},
    {"name": "UP42 (Remote)", "url": "https://up42.com/careers"},
    {"name": "Globhe (Drone Market)", "url": "https://globhe.com/careers"},
    {"name": "Z_GIS Job Hub", "url": "https://www.plus.ac.at/geoinformatik/jobs/?lang=en"},
    {"name": "EODC (Earth Observation)", "url": "https://eodc.eu/careers/"},
    {"name": "AI Austria", "url": "https://aiaustria.com/jobs"},
    {"name": "IAEA (UN Careers)", "url": "https://careers.un.org/"}
]


SIGNAL_KEYWORDS = ["Funding", "Awarded", "Launched", "Grant", "WWTF", "Partnership", "Horizon Europe"]