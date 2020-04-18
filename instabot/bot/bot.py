from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from conf.cfg import *
import datetime as dt
import pandas as pd
import random
import os.path

class Bot:
    def __init__(self, usr, pwd):
        self.project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        chromedriver_path = self.project_path + '\\bin\\chromedriver.exe'
        options = Options()
        options.headless = False
        options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.usr = usr
        self.driver.get('https://instagram.com')
        print('Opened Chrome!')
        sleep(2)

        self.likes = pd.read_csv(f"{self.project_path}/data/logs/likes.csv")
        self.follows = pd.read_csv(f"{self.project_path}/data/logs/follows.csv")
        self.unfollows = pd.read_csv(f"{self.project_path}/data/logs/unfollows.csv")
        self.__login(usr, pwd)

    def __login(self, usr, pwd):
        # login_button = '/html/body/div[1]/section/main/article/div[2]/div[2]/p/a'
        # self.driver.find_element_by_xpath(login_button).click()
        # sleep(2)

        usr_field = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input'
        pwd_field = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'

        self.driver.find_element_by_xpath(usr_field).send_keys(usr)
        self.driver.find_element_by_xpath(pwd_field).send_keys(pwd)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(10)
        
        try:
            self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        except:
            print('Could not press "Not Now".')
        print('Logged in!')
        sleep(3)

    def __follow_user(self, usr):
        # Go to user to follow
        user_path = 'https://instagram.com/' + usr + '/'
        self.driver.get(user_path)
        
        try:
            button = self.driver.find_element_by_xpath('//button[contains(text(), "Follow")]')                        
            if button.text == "Follow":
                sleep(random.randint(8, 13))
                print(f"Followed {usr}!")
                button.click()
                return True
        except:
            sleep(random.randint(5, 8))
            print("Already following " + usr)
            return False

    def __unfollow_user(self, usr):
        user_path = 'https://instagram.com/' + usr
        self.driver.get(user_path)
        
        try:
            sleep(random.randint(5, 10))            
            self.driver.find_element_by_xpath('//*[@aria-label="Following"]').click()   
            sleep(random.randint(2, 5))         
            self.driver.find_element_by_xpath('//button[contains(text(), "Unfollow")]').click()
            print("Unfollowed " + str(usr) + "!")
            return True
        except:
            print("Could not unfollow " + usr)
            return False

        sleep(1)

    def like_posts_from_tag(self, tag):
        tag_path = 'https://instagram.com/explore/tags/' + tag + '/'
        users_liked = []
        
        self.driver.get(tag_path)
        sleep(2)

        first_post = '/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]'
        self.driver.find_element_by_xpath(first_post).click()
        sleep(1)
        
        # Begin liking posts process
        i = 0
        while i < random.randint(MIN_LIKES_PER_TAG, MAX_LIKES_PER_TAG):
            sleep(random.randint(12, 23))
            try:
                self.driver.find_element_by_xpath('//section/span/button/*[name()="svg" and @aria-label="Unlike"]')
                print("Post already liked.")
            except:
                self.driver.find_element_by_xpath('//*[name()="svg" and @aria-label="Like"]').click()
                print("Pressed!")

                # Log the likes
                try:
                    username = self.driver.find_element_by_xpath('//article/header/div[2]/div[1]//*[name()="a"]').text
                    if username not in users_liked:
                        users_liked.append([username, dt.datetime.now().strftime("%Y-%m-%d"), dt.datetime.now().strftime("%H:%M:%S")])
                    print(username + " added to users list.")
                except:
                    print("Couldn't get user from posts of #" + tag)
            self.driver.find_element_by_xpath('//a[contains(text(), "Next")]').click()
            i = i + 1
            
        
        return users_liked

    def explore_tags(self):
        self.likes = pd.read_csv(f"{self.project_path}/data/logs/likes.csv")
        self.likes.dropna()

        f = open(f'{self.project_path}/data/config/hashtags.txt', 'r')
        
        hashtags = f.readlines()
        hashtags = [tag.rstrip('\n') for tag in hashtags]
        f.close()

        for tag in hashtags:
            user_data = self.like_posts_from_tag(tag)

            df = pd.DataFrame(columns=['Date', 'Time', 'User', 'Hashtag'])
            df.dropna()

            for i in user_data:
                df = df.append({
                    'Date': i[1],
                    'Time': i[2],
                    'User': i[0],
                    'Hashtag': tag
                }, ignore_index=True)

            self.likes = self.likes.append(df, ignore_index=True)

            self.likes.dropna()
            self.likes.to_csv(f'{self.project_path}/data/logs/likes.csv', index=False)

    def follow_users(self):
        self.follows = pd.read_csv(f"{self.project_path}/data/logs/follows.csv")
        self.follows.dropna()

        today = self.likes.loc[self.likes['Date'] == dt.datetime.now().strftime("%Y-%m-%d")]
        users = today['User'].unique()
        random.shuffle(users)

        for user in users[:USERS_TO_FOLLOW]:
            if self.__follow_user(user) == True:
                self.follows = self.follows.append({
                    'Date': dt.datetime.now().strftime("%Y-%m-%d"),
                    'Time': dt.datetime.now().strftime("%H:%M:%S"),
                    'User': user
                }, ignore_index=True)

        print("Finished following!")

        self.follows.dropna()
        self.follows.to_csv(f'{self.project_path}/data/logs/follows.csv', index=False)

    def unfollow_users(self):
        self.follows = pd.read_csv(f"{self.project_path}/data/logs/follows.csv")
        
        date = (dt.datetime.today() - dt.timedelta(days=DAYS_TO_UNFOLLOW)).date().strftime("%Y-%m-%d")

        today = self.follows.loc[self.follows['Date'] == str(date)]
        users = today['User'].unique()

        

        for user in users:
            if self.__unfollow_user(user) == True:
                self.unfollows = self.unfollows.append({
                    'Date': dt.datetime.now().strftime("%Y-%m-%d"),
                    'Time': dt.datetime.now().strftime("%H:%M:%S"),
                    'User': user
                }, ignore_index=True)

        self.unfollows.dropna()
        self.unfollows.to_csv(f"{self.project_path}/data/logs/unfollows.csv", index=False)
