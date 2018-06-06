from urllib import request

# I am Downloading HTML File
# https://www.w3.org/Style/Examples/011/firstcss.en.html

x = input('Enter the Link of File: ')
down_url = x

def download_file(c_url):
    response = request.urlopen(c_url);
    csv = str(response.read());
    lines = csv.split("\\n");

    down_named = r'down.html'
    # Change the extension according to your requirement e.g.
    # down_named = r 'down.csv'
    # Will download CSV file

    fw = open(down_named, 'w')
    for line in lines:
        fw.write(line + "\n")
    fw.close()

download_file(down_url)
print("\nDownload Completed")
