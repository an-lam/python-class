import webbrowser    # Open the Web Browser
import urllib.request, urllib.parse, urllib.error

def show_contents(url):
    file_handle = urllib.request.urlopen(url)
    for line in file_handle:
        #print(line.strip())
        print(line.decode().strip())

#-------- main program --------


#url = input("\nEnter a URL to retrieve contents (ex. http://westvalley.edu): ")
#show_contents(url)

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
show_contents(url)

