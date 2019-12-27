from html.parser import HTMLParser
import urllib.request
class myparser(HTMLParser):
   def handle_starttag(self, tag, attrs):
       if (tag == "a"):
           for a in attrs:
               if (a[0] == 'href'):
                   link = a[1]
                   if (link.find('http') >= 0):
                       print(link)

url = "https://cloudnfv.wordpress.com/"
request = urllib.request.urlopen(url)
parser = myparser()
parser.feed(request.read().decode('utf-8'))
