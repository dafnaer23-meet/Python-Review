def create_youtube_video(title, discription,lik):
	dictvideo={"title":title,"discription":discription,"likes":0,"dislikes":0,"comments":0}
    return dictvideo


def like(dictvideo):
	if "likes" in dictvideo:
		dictvideo["likes"] = dictvideo["likes"]+1
	return dictvideo

def dislike(dictvideo):
	if "dislikes" in dictvideo:
		dictvideo["dislikes"] = dictvideo["dislikes"]+1
	return dislike

def add comments(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

new video =create_youtube_video("paint", "more paints")
for i in range(495):
	new_video = like(new_video)
new_video = dislike(new_video, "lia", "love it")
print(new_video)
