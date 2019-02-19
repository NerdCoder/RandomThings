from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import terminal
from urllib.parse import urlparse, unquote


def download():

    crtl_v = "xclip -selection clipboard -o -t text/html"
    data, _, _ = terminal.execute(crtl_v)
    soup = bs(data, "lxml")

    for link in tqdm(soup.findAll('a', href=True), unit='files'):
        file_link = link.get('href')
        print(file_link)
        file_path = urlparse(file_link).path.split('/')
        file_name = unquote(file_path[-1])
        print(file_name)
        

        cmd = "curl -o \""+ file_name + "\" " + link.get('href')
        terminal.execute(cmd)

if __name__ == "__main__":
    download()

#TODO
"""arg to down specific files"""