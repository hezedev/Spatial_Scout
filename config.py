import os

# GitHub Secrets
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Profile Constraints
MAX_HOURS = 20
LOCATION = "Austria"

PROFILE_SUMMARY = (
    "AI Master's student with a background in Surveying and Geoinformatics. "
    "Expertise: Machine Learning, Computer Vision, Photogrammetry. "
    "Assets: Owns and operates a DJI Mavic 2 Pro. "
    "Focus: Spatial Intelligence, Geospatial AI, Infrastructure Digital Twins. "
    "Constraint: STRICT 20h/week limit for Austria roles. Remote roles are unrestricted."
)

# Main Job Search Targets (14 active nodes)
TARGETS = [
    {'name': 'AIT (Students)', 'url': 'https://jobs.ait.ac.at/jobs?jobProfiles=Studierende'}, 
    {'name': 'TU Wien Jobs', 'url': 'https://tuwien.bewerberportal.at/Jobs'}, 
    {'name': 'GeoSphere Austria', 'url': 'https://www.geosphere.at/de/ueber-uns/jobs'}, 
    {'name': 'ESA (Space Agency)', 'url': 'https://careers.esa.int/'}, 
    {'name': 'IAEA (UN Careers)', 'url': 'https://careers.un.org/'}, 
    {'name': 'Z_GIS Job Hub', 'url': 'https://www.plus.ac.at/geoinformatik/jobs/?lang=en'}, 
    {'name': 'EODC (Earth Observation)', 'url': 'https://eodc.eu/careers/'}, 
    {'name': 'AI Austria', 'url': 'https://aiaustria.com/jobs'}, 
    {'name': 'VRVis (Visual Computing)', 'url': 'https://www.vrvis.at/jobs/offene-stellen'}, 
    {'name': 'Joanneum Research', 'url': 'https://www.joanneum.at/karriere/offene-stellen'}, 
    {'name': 'ESRI Austria', 'url': 'https://www.esri.at/de-at/ueber-uns/karriere/offene-stellen'}, 
    {'name': 'UP42 (Remote Geospatial)', 'url': 'https://up42.com/careers'}, 
    {'name': 'Globhe (Drone Market)', 'url': 'https://globhe.com/careers'}, 
    {'name': 'Siemens Austria', 'url': 'https://jobs.siemens.com/careers?location=Austria&query=AI%20Student'}
]

# News & Funding Signal Targets (For identifying project-based hiring)
NEWS_TARGETS = [
    {'name': 'TU Wien News (ICT/AI)', 'url': 'https://www.tuwien.at/en/mg/geo/news'}, 
    {'name': 'GeoSphere Press (Climate/Geo)', 'url': 'https://www.geosphere.at/en/news-and-events/news'}, 
    {'name': 'AIT Research Projects', 'url': 'https://www.ait.ac.at/en/projects'}, 
    {'name': 'FFG Horizon Europe News', 'url': 'https://www.ffg.at/en/Europe/HorizonEurope'}
]

# Specific keywords to look for in News Targets
SIGNAL_KEYWORDS = ['Funding', 'Awarded', 'Launched', 'Grant', 'WWTF', 'Partnership', 'Horizon Europe']