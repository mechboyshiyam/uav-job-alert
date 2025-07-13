import json
import os

SETTINGS_PATH = "config/settings.json"
LAST_JOBS_PATH = "config/last_jobs.json"

def load_settings():
    if os.path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH, "r") as f:
            return json.load(f)
    return {
        "job_titles": ["UAV Systems Engineer"],
        "locations": ["UAE", "Qatar"],
        "email": "your-email@gmail.com",
        "password": "your-app-password",
        "receiver": "mechboyshiyam@gmail.com",
        "time": "12:00"
    }

def save_settings(settings):
    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=2)

def save_last_jobs(jobs):
    with open(LAST_JOBS_PATH, "w") as f:
        json.dump(jobs, f, indent=2)

def load_last_jobs():
    if os.path.exists(LAST_JOBS_PATH):
        with open(LAST_JOBS_PATH, "r") as f:
            return json.load(f)
    return []
