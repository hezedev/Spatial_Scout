# brain.py
from google import genai
import config
import json
import time
import re

# Initialize the 2025 SDK
client = genai.Client(api_key=config.GEMINI_API_KEY)

def evaluate_job(page_text):
    """Analyzes site text with a smart retry for 429 Rate Limits."""
    MODEL_ID = 'gemini-2.5-flash-lite' 

    prompt = f"""
    You are a Career Agent. Identify job/internship openings matching: {config.PROFILE_SUMMARY}
    Requirements: Must be in {config.LOCATION} and around {config.MAX_HOURS}h/week.
    
    Website Data:
    {page_text[:12000]}
    
    Output ONLY a JSON list: [{{"title": "Role", "score": 1-10, "is_compliant": true, "reason": "..."}}]
    """

    for attempt in range(5):  # It will try 5 times if it hits a limit
        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt,
                config={'response_mime_type': 'application/json'}
            )
            return json.loads(response.text)
            
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg:
                # 2025 logic: Extract wait time from Google's error (e.g., 'retry in 54s')
                wait_time = 65  # Default wait
                match = re.search(r"retry in (\d+\.\d+)s", error_msg)
                if match:
                    wait_time = float(match.group(1)) + 5 # Add a small safety buffer
                
                print(f"🛑 Quota Hit. Hibernating for {wait_time}s before retrying (Attempt {attempt+1}/5)...")
                time.sleep(wait_time)
            else:
                print(f"⚠️ Brain Error: {e}")
                break
    return []