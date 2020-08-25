from instabot import Bot 


def post():

	bot = Bot() 
	bot.login(username = "mr.feeds_infomance", 
			password = "unknown0001")
	bot.upload_story_photo("insta_layout.jpg.STORIES.jpg")

        
post()