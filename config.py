import os

# GitHub Secrets
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Profile Constraints
MAX_HOURS = 20
LOCATION = "Austria"

PROFILE_SUMMARY = (
    "Candidate: Master's in AI student with a professional background in Surveying & Geoinformatics. "
    "Expertise: Machine Learning, Computer Vision, Photogrammetry, Point Clouds. "
    "Assets: Owns/operates a DJI Mavic 2 Pro. Focus: Geospatial AI, Infrastructure Digital Twins. "
    "Constraint: STRICT 20h/week limit for Austria roles. Remote roles are unrestricted."
)

# Category 1: Main Jobs & Research Hubs
TARGETS = [
    {'name': 'AIT (Students)', 'url': 'https://jobs.ait.ac.at/jobs?jobProfiles=Studierende'},
    {'name': 'TU Wien Jobs', 'url': 'https://tuwien.bewerberportal.at/Jobs'},
    {'name': 'GeoSphere Austria', 'url': 'https://www.geosphere.at/de/ueber-uns/jobs'},
    {'name': 'ESA (Space Agency)', 'url': 'https://careers.esa.int/'},
    {'name': 'IAEA (UN Careers)', 'url': 'https://careers.un.org/'},
    {'name': 'Z_GIS Job Hub', 'url': 'https://www.plus.ac.at/geoinformatik/jobs/?lang=en'},
    {'name': 'EODC (Earth Observation)', 'url': 'https://eodc.eu/careers/'},
    {'name': 'UP42 (Remote Geospatial)', 'url': 'https://up42.com/careers'}
]

# Category 2: AI & Master's Level Tech Internships
AI_INTERN_TARGETS = [
    {'name': 'AIT AI Internships', 'url': 'https://www.ait.ac.at/en/career/students/internships'},
    {'name': 'ISTA (Science Internships)', 'url': 'https://phd.pages.ist.ac.at/scientific-internships/'},
    {'name': 'VRVis (Visual Computing)', 'url': 'https://www.vrvis.at/jobs/offene-stellen'},
    {'name': 'Siemens AI/Software Interns', 'url': 'https://jobs.siemens.com/careers?location=Austria&query=AI%20Student'},
    {'name': 'AI Austria Job Board', 'url': 'https://aiaustria.com/jobs'},
    {'name': 'UNOOSA (Space AI)', 'url': 'https://www.unoosa.org/oosa/en/aboutus/internship.html'},
    {'name': 'Riegl (LiDAR/Photogrammetry)', 'url': 'http://www.riegl.com/about-riegl/careers/'}
]

# News Signals
NEWS_TARGETS = [
    {'name': 'TU Wien News', 'url': 'https://www.tuwien.at/en/mg/geo/news'},
    {'name': 'FFG Horizon Europe', 'url': 'https://www.ffg.at/en/Europe/HorizonEurope'}
]
SIGNAL_KEYWORDS = ['Funding', 'Awarded', 'Grant', 'WWTF', 'Partnership', 'Horizon Europe']