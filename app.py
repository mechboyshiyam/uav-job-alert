from flask import Flask, render_template, request, redirect, jsonify
import json
from job_bot.main import run_job_search
from config.settings import SETTINGS_PATH, load_settings, save_settings, load_last_jobs

app = Flask(__name__)

@app.route('/')
def index():
    settings = load_settings()
    last_jobs = load_last_jobs()
    return render_template('index.html', settings=settings, jobs=last_jobs)

@app.route('/save', methods=['POST'])
def save():
    data = request.form.to_dict()
    data['job_titles'] = [j.strip() for j in data['job_titles'].split(',')]
    data['locations'] = [l.strip() for l in data['locations'].split(',')]
    save_settings(data)
    return redirect('/')

@app.route('/run-now')
def run_now():
    run_job_search()
    return redirect('/')

# ✅ Required for Render deployment: bind to the correct port
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

