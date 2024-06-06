import sys, requests
from bs4 import BeautifulSoup
#keep serching get in inside links until reach_philosophi

def get_response(url):
    return requests.get(url)
    pass

def get_title(soup):
    return soup.find('h1').text

def get_next_link(soup):
    content = soup.find('div', {'class':'mw-content-ltr mw-parser-output'})
    if not content:
        print('Dead End')
        exit(0);
    
    paragraphs = content.findAll('p')
    for parag in paragraphs :
        a = parag.find('a')
        if a and a.get('title'):
            break
    if not a :
        print('Dead end')
        exit(0)

    header = a.text;
    href = a.get('href')
    return { header : href}

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        exit(1)
    url = 'https://en.wikipedia.org/wiki/'
    visited_links = []
    root = sys.argv[1]
    while(1):
        data = get_response((url + root))
        soup = BeautifulSoup(data.content, 'html.parser')
        title = get_title(soup)
        next_title = get_next_link(soup)
        visited_links.append(root)
        root = list(next_title.values())[0][1 + len('wiki/'):]
        print(title)
        if (title == 'Philosophy'):
            print('road to Philosophy ' + str(len(visited_links)) )
            del soup
            break; 
        if (root in visited_links):
            print('Infinit Loop')
            break
    
        

    