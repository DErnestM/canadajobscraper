from bs4 import BeautifulSoup
from datetime import datetime
import pprint
from random import randint
import time
import requests
from extract import extract

start_time = datetime.now()
pp = pprint.PrettyPrinter(indent=4)
errors = 0


# time.sleep(randint(0,3))


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

req = requests.get("https://ca.indeed.com/jobs?q&l=Nunavut")
print(req)

# extra="&start=10"
# nunavut
# yukon

# https://ca.indeed.com/jobs?q&l=nunavut&vjk=46fa1267e9814cca
# https://ca.indeed.com/jobs?q&l=yukon&vjk=b07763eb5d6eac27
# https://ca.indeed.com/jobs?q&l=Northwest%20Territories&vjk=a37cb391f72032ec
# https://ca.indeed.com/jobs?q&l=Prince%20Edward%20Island&vjk=ccc4ad82169822dc
# https://ca.indeed.com/jobs?q&l=Newfoundland%20and%20Labrador&vjk=d33559c870742adc
# https://ca.indeed.com/jobs?q&l=New%20Brunswick&vjk=4bd75a5407200f63
# https://ca.indeed.com/jobs?q&l=Nova%20Scotia&vjk=1f9823b6bcbe2f92
# https://ca.indeed.com/jobs?q&l=Saskatchewan&vjk=d9f7ebfce2a5e788
# https://ca.indeed.com/jobs?q&l=Manitoba&vjk=a6737b4d8cb01814
# https://ca.indeed.com/jobs?q&l=Alberta&vjk=70793eef3b5f0f31
# https://ca.indeed.com/jobs?q&l=British%20Columbia&vjk=509b0f86a7848a99
# https://ca.indeed.com/jobs?q&l=Quebec&vjk=1311a4ca30ab6bcb
# https://ca.indeed.com/jobs?q&l=ontario&vjk=2c6a2816eba8321b












soup = BeautifulSoup(req.text,'html.parser')
# print(soup.original_encoding)
all_jobs = soup.find_all(class_="slider_container")
# print(all_jobs)

for job in all_jobs:
    extract(job)



#Measure execution time
finish_time = datetime.now()
execution_time(start_time, finish_time)