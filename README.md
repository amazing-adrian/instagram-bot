Hello everyone, thanks for taking interest in this project!

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


The setup is explained in-depth in 'instructions.txt' file.
