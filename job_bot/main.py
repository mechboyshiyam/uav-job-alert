import json
import os
from job_bot.search import fetch_jobs
from job_bot.mailer import send_email
from config.settings import load_settings, save_last_jobs

CACHE_FILE = "job_cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return []

def save_cache(jobs):
    with open(CACHE_FILE, "w") as f:
        json.dump(jobs, f, indent=2)

def filter_new_jobs(jobs, cache):
    return [job for job in jobs if job not in cache]

def run_job_search():
    settings = load_settings()
    all_jobs = fetch_jobs(settings)
    cache = load_cache()
    new_jobs = filter_new_jobs(all_jobs, cache)
    if new_jobs:
        send_email(new_jobs, settings)
        save_cache(cache + new_jobs)
        save_last_jobs(new_jobs)
