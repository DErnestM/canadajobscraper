from bs4 import BeautifulSoup
import html


with open("res.html") as f:
    html = f.read()
    
soup_item = BeautifulSoup(html, "html.parser")

def extract(soup):
    """Receives a bs4 object, looks for the job title, company, location, salary, duties and date published. Cleans the data and appends it to a csv file."""

    try:
        title = soup.find(class_="jobTitle").getText().strip()
    except:
        title = "None"
        
    try:
        company = soup.find(class_="companyName").getText().strip()
    except:
        company = "None"
        
    try:
        location = soup.find(class_="companyLocation").getText().strip()
    except:
        company = "None"
        
    try:
        salary = soup.find(class_="salary-snippet").getText().strip()
    except:
        company = "None"
        
    try:
        duties = soup.find(class_="job-snippet").getText().strip()
    except:
        company = "None"
        
    try:
        published = soup.find(class_="date").get_text().strip()
    except:
        company = "None"

    try:
        with open("results.csv", mode="a") as file:
                job = (f"{title}|{company}|{location}|{salary}|{duties}|{published}").replace("\n", "")
                file.write(f"\n{job}")
    except:
        print(f"Some crap happened")

    #job_title;company_name;location;salary;duties;date_published
    
    # finally:
    #     print("Process finished")

# extract(soup_item)