from os import error
from bs4 import BeautifulSoup
from datetime import datetime
from random import randint
import time
import requests
from extract import extract
from provinces import provinces

start_time = datetime.now()

# Measuring execution time
def execution_time(start, end):
    duration = end - start
    duration = duration.seconds
    days = divmod(duration, 86400)
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    seconds = divmod(minutes[1], 1)
    print(f"Execution code lasted: {days[0]} days, {hours[0]} hours, {minutes[0]} minutes and {seconds[0]} seconds")


# Making the request

def send_petition(province="canada" , iterations=1):
    pages = [n for n in range(0, (iterations*10) +1, 10) ]
    
    try:
        for page in pages:
            time.sleep(randint(0,2))
            url_endpoint = f"https://ca.indeed.com/jobs?q&l={province}&start={page}"
            req = requests.get(url_endpoint)
    
    
            soup = BeautifulSoup(req.text,'html.parser')
            all_jobs = soup.find_all(class_="slider_container")

            # Add a job line by line
            for job in all_jobs:
                extract(job)
    
    except Exception as e:
        print(f"Failed with code error: {e}")


for province in provinces:
    send_petition(province[0], province[1])


#Measure execution time
finish_time = datetime.now()
execution_time(start_time, finish_time)