from instapy import InstaPy

session = InstaPy(username = "elizabethsehguh", password = "elizalikescats9660")
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage=100)
session.like_by_tags(["cats", "dogs" , "animals", "love"], amount = 4)
session.set_dont_like(["nsfw"])

session.end()
