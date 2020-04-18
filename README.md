Hello everyone, thanks for taking a look at this project of mine!

The bot has 3 steps every run:
    1)It likes a number of posts from a list of hashtags, both the number and the list being specified by the user.
    2)It then proceeds to follow a number of users which posts have been liked in the previous step.
    3)It unfollows users that the bot followed a number of days ago.

All of these 3 steps are carefully logged in .csv files (Excel tables), therefore the bot's activity
can be easily tracked by the user.

To prevent Instagram from detecting the bot, random time intervals are chosen between the bot's actions (a human being won't be able to like 100 posts and follow 50 users in a very short amount of time) along some other prevention measures.

The bot's running time depends on the user specified parameters that will be mentioned below.

After the setup is done, the bot is ready to run once a day.
The time it takes for the bot to run depends heavily on the amount of interactions it has to do.

For example if it has to like 15 posts from 9 different hashtags, then follow 30 accounts and unfollow the same number of accounts, then the process would take on average about 50 minutes.


=========================================IMPORTANT=========================================

It is strongly recommended to limit the bot's follow and unfollow numbers to under 100 a day. The number of posts liked should also be within reasonable human boundaries. No human would like 200 posts in an hour.


=========================================SETUP=========================================
1)Go to instabot/conf/cfg.py and set the username and password.
    Here you will also be able to configure the number of likes per hashtag, the number of users to follow and the number of days that the followed accounts stay followed.

    MIN_LIKES_PER_TAG - the minimum number of posts to like from each hashtag
    MAX_LIKES_PER_TAG - the maximum number of posts to like from each hashtag
    (These 2 values are used to prevent a pattern that can easily be detected by Instagram's bot detection algorithm)

    USERS_TO_FOLLOW - the number of users to follow from today's liked posts in the previous step
    DAYS_TO_UNFOLLOW - the number of days the users from previous step remain followed

2) Go to data/config/hashtags.txt and introduce the hashtags desired, one hashtag on each line. It should look like this:

beauty
cute
fitness
finance

