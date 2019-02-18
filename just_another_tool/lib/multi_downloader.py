from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import terminal
from urllib.parse import urlparse, unquote


def download():

    crtl_v = "xclip -selection clipboard -o -t text/html"
    data, _, _ = terminal.execute(crtl_v)
    soup = bs(data, "lxml")

    for link in tqdm(soup.findAll('a'), unit='files'):
        file_link = link.get('href')
        file_path = urlparse(file_link).path.split('/')
        file_name = unquote(file_path[-1])

        cmd = "curl -o \""+ file_name + "\" " + link.get('href')
        terminal.execute(cmd)

if __name__ == "__main__":
        download()