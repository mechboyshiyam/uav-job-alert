import requests
from bs4 import BeautifulSoup
import re

def fetch_jobs(settings):
    jobs = []
    for title in settings['job_titles']:
        for loc in settings['locations']:
            query = f"{title} {loc} site:linkedin.com/jobs"
            url = f"https://www.bing.com/search?q={query.replace(' ', '+')}"
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'html.parser')
            links = soup.select('li.b_algo h2 a')
            for link in links:
                href = link['href']
                title_text = link.text.strip()
                possibility = 'Mid'
                if re.search("visa|sponsorship|foreign", title_text, re.I):
                    possibility = 'High'
                elif re.search("locals only|citizen", title_text, re.I):
                    possibility = 'Low'
                jobs.append({
                    'title': title_text,
                    'link': href,
                    'location': loc,
                    'source': 'LinkedIn',
                    'possibility': possibility
                })
    return jobs
