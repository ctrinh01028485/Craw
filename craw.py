from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

playlist = input("link playlist: ")

#mơ trinh duyet
browser = webdriver.Chrome(executable_path='chromedriver.exe')

#truy cap link
browser.get(playlist)
sleep(1)

#lay link video 
#linkvideo = browser.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer[2]/div[2]/a").get_attribute("href")
linkvideo = browser.find_elements_by_xpath("//*[@id='content']/a")#.get_attribute("href")

#luu vao file
#filename = "link.txt"
#filelink = open(filename, "w")
listvideo = []
for i in linkvideo:
    getid = i.get_attribute("href")
    listvideo.append("https://www.y2mate.com/youtube-mp3/" + getid[32:43])
    #filelink.write(i.get_attribute("href") + "\n")


#.close()

#mo link video vao y2mate
#filetxt = open("link.txt")
#listvideo = filetxt.readlines()
videoindex = 0
while videoindex < len(listvideo):
     browser.execute_script("window.open('"+listvideo[videoindex].strip()+"')")
     videoindex += 1

i = input()

browser.close()


