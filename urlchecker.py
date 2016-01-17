def get_url_status(url):
	try:
		r=requests.head(url)
		return url,r.status_code
	except requests.ConnectionError:
		print "Failed to connect"
		return url,'dns error'
	except requests.exceptions.InvalidSchema:
		print "Invalid Schema"
		return url,'invalid schema'
	except UnicodeDecodeError:
		print "encoding error"
		return url,"Encoding error"

results={}

with open('filename.csv','r') as infile:
	for url in infile:
		url_status = get_url_status(url.strip())
		results[url_status[0]] = url_status[1]

writer = csv.writer(open('output.csv','wb'))

for key, value in results.items():
	writer.writerow([key,value])




#getredirect

def new_url(url):
	try:
		url_new = urllib2.urlopen(url).geturl()
		return url,url_new
	except urllib2.HTTPError:
		print "Does not exist anymore"
		return url,'404'

results2={}

with open('redir.csv','r') as infile:
	for url in infile:
		url_redir = new_url(url)
		results[url_redir[0]] = url_redir[1]
			
