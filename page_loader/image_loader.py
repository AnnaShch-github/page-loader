from bs4 import BeautifulSoup

with open('/home/anna/python-project-lvl3/tests/fixtures/fixture.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
    
print(soup.find_all('img'))