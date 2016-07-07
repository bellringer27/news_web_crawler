from selenium import webdriver
from time import sleep
url = "https://www.washingtonpost.com/news/morning-mix/wp/2016/07/06/video-captures-white-baton-rouge-police-officer-fatally-shooting-black-man-sparking-outrage/?hpid=hp_hp-top-table-main_mm-baton-rouge-1140am%3Ahomepage%2Fstory#comments"
driver = webdriver.Chrome()
driver.get(url)
sleep(5)
#while "<div class=\"fyre-stream-more\">" in driver.page_source:
 #   driver.find_element_by_class_name("fyre-stream-more").click()
  #  print("passed")
   # sleep(3)
#commentHTML = driver.find_elements_by_class_name('fyre-comment-wrapper')
#text = [comment.text for comment in commentHTML]
#text = commentHTML[0].get_attribute("innerHTML")
#print text
driver.find_element_by_class_name('echo-streamserver-controls-stream-more').click()

