
def create_youtube_video(title, discription):
	dictvideo={"title":title,"discription":discription,"likes":0,"dislikes":0,"comments":{}}
	return dictvideo


def like(dictvideo):
	if "likes" in dictvideo:
		dictvideo["likes"] = dictvideo["likes"]+1
	return dictvideo

def dislike(dictvideo):
	if "dislikes" in dictvideo:
		dictvideo["dislikes"] = dictvideo["dislikes"]+1
	return dislike
def add_comment(dictvideo, username, comment_text):
	dictvideo["comments"][username] = comment_text
	return dictvideo

myvideo = create_youtube_video("me", "who i am")
print(myvideo)
like(myvideo)
dislike(myvideo)
print(myvideo)
add_comment(myvideo,"roni", "nice video!!xoxoxoxo")
print(myvideo)

	