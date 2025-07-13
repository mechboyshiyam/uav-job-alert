import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def write_jobs_to_sheet(jobs):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("config/credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("UAV_Job_Alerts").sheet1  # Change this if your sheet has a different name
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for job in jobs:
        sheet.append_row([
            now,
            job.get('title', 'N/A'),
            job.get('location', 'N/A'),
            job.get('source', 'N/A'),
            job.get('link', 'N/A'),
            job.get('possibility', 'Unknown')
        ])
