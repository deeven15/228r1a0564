import urllib.request

response = urllib.request.urlopen("http://www.google.com")
print(response.read())
