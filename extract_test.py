from os import error
from bs4 import BeautifulSoup
import html


with open("res.html") as f:
    html = f.read()
    
soup_item = BeautifulSoup(html, "html.parser")

def extract(soup):
    """Receives a bs4 object, looks for the job title, company, location, salary, duties and date published. Cleans the data and appends it to a csv file."""

    values = ["jobTitle", "companyName", "companyLocation", "salary-snippet", "job-snippet", "date"]

    # if isinstance(soup.find(class_="jobTitle").getText().strip(), str):
    #     title = soup.find(class_="jobTitle").getText().strip()
    # else:
    #     title = "None"

    try:
        title = soup.find(class_="jobTitle").getText().strip()
    except:
        title = "None"
    print(title)

    # title = soup.find(class_="jobTitle").getText().strip() if soup.find(class_="jobTitle").getText().strip() != error else "None"

    # company = soup.find(class_="companyName").getText().strip() if soup.find(class_="companyName").getText().strip() != error else "None"

    # location = soup.find(class_="companyLocation").getText().strip() if soup.find(class_="companyLocation").getText().strip() != error else "None"

    # salary = soup.find(class_="salary-snippet").getText().strip() if soup.find(class_="salary-snippet").getText().strip() != error else "None"
    
    # duties = soup.find(class_="job-snippet").getText().strip() if soup.find(class_="job-snippet").getText().strip()    != error else "None"
    
    # published = soup.find(class_="date").get_text().strip() if soup.find(class_="date").get_text().strip() != error else "None"


    # try:
    #     with open("results.csv", mode="a") as file:
    #             job = (f"{title}|{company}|{location}|{salary}|{duties}|{published}").replace("\n", "")
    #             file.write(f"\n{job}")
    # except:
    #     global errors
    #     errors =+ 1
    #     print(f"Amount of Errors: {errors}")

    #job_title;company_name;location;salary;duties;date_published
    
    # finally:
    #     print("Process finished")

extract(soup_item)