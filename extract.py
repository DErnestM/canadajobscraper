from bs4 import BeautifulSoup
import html


with open("res.html") as f:
    html = f.read()
    
soup_item = BeautifulSoup(html, "html.parser")

def extract(soup):
    """Receives a bs4 object, looks for the job title, company, location, salary, duties and date published. Cleans the data and appends it to a csv file."""

    no_value = "Null"
    
    title = no_value
    company = no_value
    location = no_value
    salary = no_value
    duties = no_value
    published = no_value

    try:
        title = soup.find(class_="jobTitle").getText().strip()
        company = soup.find(class_="companyName").getText().strip()
        location = soup.find(class_="companyLocation").getText().strip()
        salary = soup.find(class_="salary-snippet").getText().strip()
        duties = soup.find(class_="job-snippet").getText().strip()
        published = soup.find(class_="date").get_text().strip()
    except:
        print("One or more values are missing. But the job was still added.")

    job = (f"{title}|{company}|{location}|{salary}|{duties}|{published}").replace("\n", "")
    
    try:
        with open("results.csv", mode="a") as file:
            file.write(f"\n{job}")
    except:
        print(f"Something really bad happened and one register was skipped.")


# extract(soup_item)
