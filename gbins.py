#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
from rich.console import Console

def main():
    style = Console()
    try:
        binInput = (sys.argv[1].strip().lower())
    except(IndexError):
        print("Error --> please specify a GTFOBin. example: 'gbins.py 7z'")
        exit()

    info = parse(binInput)

    for key in info:
        header = key
        style.print(header, style="bold magenta")
        for desc in info[key]:
            print(info[key][desc])        

def parse(binInput):

   
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }

    raw = requests.get(f'https://gtfobins.github.io/gtfobins/{binInput}/', headers=headers).text

    data = BeautifulSoup(raw, features='html.parser')

    info = {}
    for h2_tag in data.find_all('h2'):
        key = h2_tag.get_text()
        p_tag = h2_tag.find_next('p')
        ul_tag = h2_tag.find_next('ul')

        tags = {'p': p_tag.get_text(), 'ul': ul_tag.get_text()}
        info[key] = tags

    return info

main()