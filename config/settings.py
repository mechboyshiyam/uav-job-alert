import json
import os

SETTINGS_PATH = "config/settings.json"
LAST_JOBS_PATH = "config/last_jobs.json"

def load_settings():
    if os.path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH, "r") as f:
            return json.load(f)
    return {
        "job_titles": ["UAV Systems Engineer, UAV Flight Operations Engineer"],
        "locations": ["UAE", "Qatar", "Singapore", "Kuwait"],
        "spreadsheet_id": "1kLjsFQCupM0aP-Ww_NDUaedCF1ZW8VKtRenDzlduDi4"
    }

def save_settings(settings):
    allowed_keys = ["job_titles", "locations", "spreadsheet_id"]
    clean_settings = {k: settings[k] for k in allowed_keys if k in settings}
    with open(SETTINGS_PATH, "w") as f:
        json.dump(clean_settings, f, indent=2)

def save_last_jobs(jobs):
    with open(LAST_JOBS_PATH, "w") as f:
        json.dump(jobs, f, indent=2)

def load_last_jobs():
    if os.path.exists(LAST_JOBS_PATH):
        with open(LAST_JOBS_PATH, "r") as f:
            return json.load(f)
    return []
