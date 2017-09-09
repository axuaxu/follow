from TwitterFollowBot import TwitterBot

my_bot = TwitterBot("mcon.txt")
my_bot.auto_follow_followers_of_user("TheHiddenWorId", count=25)