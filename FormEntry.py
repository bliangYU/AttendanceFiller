import requests
from bs4 import BeautifulSoup

form_url = 'https://docs.google.com/forms/d/15XKq6Fzp5xM-j3lJBQ7eWmkTgpZCCUoIGjbjNAY_5cM/formResponse'

response = requests.get(form_url)

soup = BeautifulSoup(response.text, 'html.parser')

email_input = soup.find('input', class_='Mh5jwe JqSWld yqQS1')

data = {
    'entry.1475566174': 'bliang@nyc.yearup.org',
    'entry.1684129569': 'Bill',
    'entry.157508738': 'Liang',
}

response = requests.post(form_url, data=data)

if response.status_code == 200:
    print("Form submitted successfully.")
else:
    print("Failed to submit the form.")
