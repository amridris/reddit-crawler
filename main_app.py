from lib.deals_crawler import deal_finder
import argparse
import time





if __name__ == '__main__':

    app_parser = argparse.ArgumentParser(description="Program to parse reddit hardware swap section for deals using keyword.")

    app_parser.add_argument('-s', dest ='keyword', help='The keyword to be searched for deals')
    app_parser.add_argument('-e', dest='email', help='Your account email')
    app_parser.add_argument('-p',dest = 'password', help='Your email passwrd')

    previously_sent_deals = []

    args_input = app_parser.parse_args()
    print(args_input.email)
    while True:
        find_deals = deal_finder(args_input.keyword, args_input.email, args_input.password)
        print("Checking Reddit deals ...")
        find_deals.search_reddit()

        if len(find_deals.reddit_new_deals) != 0 and find_deals.reddit_new_deals != find_deals.reddit_old_deals:
            find_deals.send_deals(args_input.email, args_input.email)
            find_deals.reddit_old_deals = find_deals.reddit_old_deals

        print("Sleeping..")
        time.sleep(5)


    



