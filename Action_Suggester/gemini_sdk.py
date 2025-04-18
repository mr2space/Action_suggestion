import google.generativeai as genai

from .constants import actions

import json
import re
import os


prompt_prefix_text = "tell me the tone and intent of the message "
prompt_suffix_text = " the result prompt should be in json format with structure {status:int, tone:String, intent:String, suggested_actions:list(list(Action_key:string, suggested_text:string))}," + f" in case of successful status set it to 0 but if it fails than make it 1, the only allowed actions are '{json.dumps(actions)}' no extra content"


def extract_json_from_text(text):
    cleaned = re.sub(r"```json\s*|\s*```", "", text.strip())
    try:
        json_data = json.loads(cleaned)
        return json_data
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

def generate_random_text():
    genai.configure(api_key=os.environ.get("API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content("Explain quantum computing in simple terms.")
    return response.text

def tone_and_intent_analyzer(text):
    genai.configure(api_key=os.environ.get("API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt_prefix_text + text + prompt_suffix_text)
    data = extract_json_from_text(response.text)
    data["original_query"]  = text
    return data