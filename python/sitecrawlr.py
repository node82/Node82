
import csv
import requests

hostsfile=open("/home/calvin/Downloads/sitemap_crawl_sample.csv", "r")

lines=hostsfile.readlines()
for line in lines:
    with open('/home/calvin/Downloads/sitemap_results.csv', 'a') as writeFile:
        line = line.rstrip()
        response = requests.get(line)
        writeFile.write(str(line) + "| response: " + str(response.status_code) +"\n")
        print(str(line) + "| response: " + str(response.status_code))
#    writeFile.(close)
