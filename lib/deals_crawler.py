from bs4 import BeautifulSoup as bs
from urllib.request import Request
from urllib import request
from lib.email_utility import email_utility
from lib.email_utility import EmailMessage
import smtplib
from collections import deque

class deal_finder:

    def __init__(self, search_term, _email, _email_password):
        self.search_keyword = search_term
        self.email = email_utility(_email, _email_password)
        self.msg = ""
        self.reddit_old_deals = deque(maxlen=20)
        self.reddit_new_deals = deque(maxlen=20)
        self.empty_message = False

    
    def email_format(self, from_email, to_email):
        _msg = EmailMessage()
        _msg["Subject"] = "Good Deals!"
        _msg["To"] = to_email
        _msg["From"] = from_email
        body = ""
        
        for name, link in self.reddit_new_deals:
            if (name, link) not in self.reddit_old_deals:
                body += name + '\n' + link + '\n'
                
        _msg.set_content(body)
        self.msg = _msg
    


    def send_deals(self, from_email, to_email):
        self.email_format(from_email, to_email)
        self.email.send_email(self.msg)
            
    # search reddit hardwareswap for deals!
    def search_reddit(self):
        req = Request("https://www.reddit.com/r/hardwareswap/new/", headers={'User-Agent':'Mozilla/5.0'})
        
        try:
            reddit_hardware = request.urlopen(req)
        except: 
            print("Could not open the website")
            exit()

        hardware_buy_soup = bs(reddit_hardware)

        names = []
        links = []
        for tag_name in hardware_buy_soup.findAll('h3'):
            names.append(tag_name.text)

        for tag_links in hardware_buy_soup.findAll(attrs={'data-click-id': 'body'}):
            links.append("www.reddit.com{}".format(tag_links['href']))
        
    
        for x in range(len(links)):
            if self.search_keyword.lower() in names[x].lower() and (names[x], links[x]) not in self.reddit_old_deals:
                self.reddit_new_deals.append((names[x], links[x]))



