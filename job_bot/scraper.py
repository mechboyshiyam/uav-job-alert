import requests
from bs4 import BeautifulSoup
import hashlib
from datetime import datetime

def create_job_id(title, company, location, link):
    return hashlib.md5(f"{title}-{company}-{location}-{link}".encode()).hexdigest()

def search_jobs(job_title, location, date_filter="Any"):
    job_title_query = job_title.replace(" ", "+")
    location_query = location.replace(" ", "+")

    base_url = f"https://www.indeed.com/jobs?q={job_title_query}&l={location_query}"

    if date_filter.lower() == "today":
        base_url += "&fromage=1"  # posted today

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Error fetching jobs for {job_title} in {location}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    job_cards = soup.select(".job_seen_beacon")

    jobs = []

    for card in job_cards:
        title_tag = card.select_one("h2.jobTitle span")
        company_tag = card.select_one(".companyName")
        location_tag = card.select_one(".companyLocation")
        link_tag = card.find("a", href=True)

        if not (title_tag and company_tag and link_tag):
            continue

        title = title_tag.text.strip()
        company = company_tag.text.strip()
        loc = location_tag.text.strip() if location_tag else location
        link = "https://www.indeed.com" + link_tag['href']
        posted = card.select_one(".date")
        posted_text = posted.text.strip() if posted else "N/A"

        job_id = create_job_id(title, company, loc, link)

        jobs.append({
            "id": job_id,
            "title": title,
            "company": company,
            "location": loc,
            "link": link,
            "posted": posted_text,
            "source": "Indeed",
            "possibility": "Mid"
        })

    return jobs
