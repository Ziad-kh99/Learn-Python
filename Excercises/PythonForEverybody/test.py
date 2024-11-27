import urllib.request 


url = input('URL: ')

file_handle = urllib.request.urlopen(url)

for line in file_handle:
    print(line.decode().strip())

