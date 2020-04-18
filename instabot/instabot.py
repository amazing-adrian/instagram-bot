from time import sleep
from conf.cfg import USERNAME, PASSWORD
from bot.bot import Bot

def main():

    bot = Bot(USERNAME, PASSWORD)

    bot.explore_tags()
    bot.follow_users()
    bot.unfollow_users()
    print("All done!")




if __name__ == '__main__':
    main()