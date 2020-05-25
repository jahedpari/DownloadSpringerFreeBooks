

import requests

# put the url of the interested books in a txt file and give its address here
f = open("../articles/SpringerBooks.txt", "r")
# read the list of books to be downloaded
data = f.readlines()
f.close()

# The following lines will go through each link and download it in the "articles" folders.
# Make sure to create such a folder!

i=0
while i<len(data):
    title= data[i]
    i += 2
    url= data[i]
    url = url.replace("http", "https")
    url = url.replace("openurl?genre=book&isbn=", "content/pdf/10.1007%2F")+'.pdf'
    i += 1
    response = requests.get(url,stream=True)
    des='../articles/'+title+'.pdf'
    print ("downloading:", title , "url:" ,url)
    with open(des, 'wb') as f:
        f.write(response.content)

print("Done!")


