import json
import os
from datetime import datetime
from job_bot.scraper import search_jobs
from job_bot.storage import save_jobs, load_previous_jobs
from job_bot.sheets_writer import write_jobs_to_sheet
from config.settings import load_settings, save_last_jobs

def run_job_search():
    settings = load_settings()
    job_titles = settings.get('job_titles', [])
    locations = settings.get('locations', [])
    date_posted = settings.get('date_posted', 'Any')

    print(f"🔍 Searching jobs for: {job_titles} in {locations} (Posted: {date_posted})")

    all_results = []

    for job_title in job_titles:
        for location in locations:
            results = search_jobs(job_title, location, date_posted)
            all_results.extend(results)

    print(f"✅ Found {len(all_results)} jobs")

    previous_jobs = load_previous_jobs()
    new_jobs = [job for job in all_results if job['id'] not in previous_jobs]

    print(f"🆕 New jobs: {len(new_jobs)}")

    if new_jobs:
        write_jobs_to_sheet(new_jobs)
        save_jobs(new_jobs)
        save_last_jobs(new_jobs)
    else:
        print("📭 No new jobs to add.")
