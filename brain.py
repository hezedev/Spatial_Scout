from google import genai
import config
import json
import time
import re

client = genai.Client(api_key=config.GEMINI_API_KEY)

def evaluate_job(page_text):
    MODEL_ID = 'gemini-2.5-flash-lite'
    prompt = f"""
    You are a Career Agent. Evaluate these text data for roles matching: {config.PROFILE_SUMMARY}
    Requirements: Must be in {config.LOCATION} and around {config.MAX_HOURS}h/week.
    Text: {page_text[:12000]}
    Return ONLY a JSON list: [{{"title": "Role", "score": 1-10, "is_compliant": true, "reason": "..."}}]
    """

    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt,
                config={'response_mime_type': 'application/json'}
            )
            return json.loads(response.text)
        except Exception as e:
            if "429" in str(e):
                wait_time = 65
                match = re.search(r"retry in (\d+\.\d+)s", str(e))
                if match:
                    wait_time = float(match.group(1)) + 5
                print(f"🛑 Quota Hit. Hibernating {wait_time}s (Attempt {attempt+1}/5)...")
                time.sleep(wait_time)
            else:
                print(f"⚠️ Brain Error: {e}")
                break
    return []