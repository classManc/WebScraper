import requests
import bs4
import argparse

# takes in a path to the director of the document you want to scrape the data into as argument
def get_write_latest(dir_path):

    # send a request to the punch website
    website = requests.get('https://punchng.com/')

    # use the data returned to create BeautifulSoup object and use lxml to parse the data into html pattern
    soup = bs4.BeautifulSoup(website.text, 'lxml')

    # get the first element from the list of elements with a class .entry_title and also a link
    latest_news = soup.select('.entry-title a')[0]

    # get the value of the link and send a request to it
    latest_news_link = requests.get(latest_news['href'])

     # use the data returned to create BeautifulSoup object and use lxml to parse the data into html pattern
    soup = bs4.BeautifulSoup(latest_news_link.text, 'lxml')

    # get the first element from the list of elements with a class .post_title  which is the title of the post
    latest_news_title = soup.select('.post-title')[0]

    # get the first element from the list of elements with a class .post_title  which is the date of the post
    latest_news_date =  soup.select('.post-date')[0]

    # get the first element from the list of elements with a class .post_title  which is the author of the post
    latest_news_author =  soup.select('.post-author')[0]

    # get the first element from the list of elements with a class .post_title  which is the main content of the post
    latest_news_content =  soup.select('.post-content')[0]
   
   # open a file with the path given as argument to the function in write mode
    f = open(dir_path,'w')

    # write the post's title to it
    f.write(latest_news_title.text)

    # write the post's date to it
    f.write(latest_news_date.text)

    # write the post's author to it
    f.write(latest_news_author.text)

    # write the post's content to it
    f.write(latest_news_content.text)

    # close the file
    f.close
    
if __name__ == '__main__':
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Web Scraping Script')

    # Add an argument for the directory path
    parser.add_argument('dir_path', type=str, help='Path to the directory')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the get)_write_latest function with the provided directory path
    get_write_latest(args.dir_path)