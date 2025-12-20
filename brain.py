from google import genai
import config
import json
import time

client = genai.Client(api_key=config.GEMINI_API_KEY)

def evaluate_job(page_text):
    prompt = f"""
    Analyze this text for Internship/Working Student roles matching: {config.PROFILE_SUMMARY}
    Requirements: Must be in {config.LOCATION} and around {config.MAX_HOURS}h/week.
    Text: {page_text[:12000]}
    Return ONLY a JSON list: [{{"title": "Role", "score": 1-10, "is_compliant": true, "reason": "..."}}]
    """
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite',
            contents=prompt,
            config={'response_mime_type': 'application/json'}
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Brain error: {e}")
        return []