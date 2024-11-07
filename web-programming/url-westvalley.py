import webbrowser    # Open the Web Browser
import urllib.request, urllib.parse, urllib.error

def show_contents(url):
    file_handle = urllib.request.urlopen(url)
    for line in file_handle:
        # print(line)
        print(line.decode().strip())

#-------- main program --------
url1 = "http://www.westvalley.edu"
url1a = "https://www.westvalley.edu/classes/schedule/"
url2 = "https://deanza.edu"
#url = "https://www.westvalley.edu/classes/schedule/"
show_contents(url2)

#url = input("\nEnter a URL to retrieve contents (ex. http://westvalley.edu): ")
#show_contents(url)

"""
url = "www.python.org"
"""
url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"

# Launch web browser
input("\nHit enter to launch the web browser.")
webbrowser.open(url)