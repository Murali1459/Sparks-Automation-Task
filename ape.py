import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "http://thesparksfoundation.sg/"
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options,service=s)
driver.get(url)
# driver.maximize_window()

def print_bold(p):
    print(f"\033[1m{p}\033[0m")

def check_page(*sleep_time,**arg):
    for Wait_time,element,by_method in zip(sleep_time,arg.keys(),arg.values()):
        element = element.replace("_", " ")
        x = (by_method,element)
        try:
            WebDriverWait(driver,Wait_time).until(EC.presence_of_element_located(x)).click()
        except NoSuchElementException:
            return False
        time.sleep(2)
    return True


# TEST CASE 1:ABOUT US -> GUIDING PRINCIPLES
if check_page(4,2,About_Us=By.LINK_TEXT,Guiding_Principles=By.LINK_TEXT):
    print_bold("\nSuccessfully visited the Guiding Principles page of About Us.\n")
else:
    print_bold("About us / Guiding Principles page does not exist.\n")


    
# TEST CASE 2:HOME LINK
if check_page(4,2,Join_Us=By.LINK_TEXT,Internship_Positions=By.LINK_TEXT):
    print_bold('Successfully visited the Internship Positions page of Join Us.\n')
else:
    print_bold("Join Us / Internship Positions page does not exist.\n")


# TEST CASE 3:POLICIES AND CODE -> POLICIES
if check_page(4,2,Policies_and_Code=By.LINK_TEXT,Policies=By.LINK_TEXT):
    print_bold('Successfully visited the Policies page of Policies and Code.\n')
else:
    print_bold("Policies and Code / Policies page does not exist.\n")

# TEST CASE 4:PROGRAMS -> WORKSHOPS
if check_page(4,2,Programs=By.LINK_TEXT,Workshops=By.LINK_TEXT):
    print_bold('Successfully visited the the Workshops page of Programs.\n')
else:
    print_bold("Programs / Workshops page does not exist.\n")

# TEST CASE 5:LINK -> AI IN EDUCATION
if check_page(4,2,LINKS=By.LINK_TEXT,AI_in_Education=By.LINK_TEXT):
    print_bold('Successfully visited the AI in Education page of LINKS.\n')
else:
    print_bold("LINKS / AI in Education does not exist.\n")

    
# TEST CASE 6:JOIN US -> INTERNSHIP POSITIONS
if check_page(4,2,Join_Us=By.LINK_TEXT,Internship_Positions=By.LINK_TEXT):
    print_bold('Successfully visited the Internship Positions page of Join Us.\n')
else:
    print_bold("Join Us / Internship Positions page does not exist.\n")

# TEST CASE 7:SCROLL TO TOP BUTTON
if check_page(4,2,toTopHover=By.ID):
    print_bold('Scroll to top button is functioning properly.\n')
else:
    print_bold("Scroll to top button does not function properly.\n")
    
        
# TEST CASE 8:RESUME WRITING
if check_page(4,2,Resume_Writing=By.LINK_TEXT):
    print_bold('Successfully visited the Resume Writing page.\n')
else:
    print_bold('Resume Writing page does not exist.\n')

# TEST CASE 9:CONTACT US
if check_page(4,2,Contact_Us=By.LINK_TEXT):
    print_bold('Successfully visited the Contact Us page.\n')
else:
    print_bold("Contact us page does not exist.\n")

# TEST CASE 10: STUDENT SCHOLARSHIP PROGRAM
if check_page(4,2,Student_Scholarship_Program=By.LINK_TEXT):
    print_bold('Successfully visited the Student Scholarship Program page.\n')
else:
    print_bold('Student Scholarship Program page does not exist.\n')
    
time.sleep(3)

driver.close()