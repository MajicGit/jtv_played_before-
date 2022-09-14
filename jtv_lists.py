import requests

title_enabled = False 
try:
    import get_video_title
    title_enabled = True 
except:
    print("Couldn't import get_video_title. Please add a config file with a google API key as described in get_video-title.py if you want this tool to add the names of the videos")
MIN_PLAYS_FOR_LOOKUP = 30 # this is so you don't kill you API quota

videos = {}
moo_queuers = {}
print("Querying for videos, this may take a while")
for year in ["2021","2022"]:
    for week in range(1,53):
        try:
            r = requests.get(f"https://jungletv.live/raffles/weekly/{year}/{week}/tickets#",timeout=2)
        except:
            print("Encountered an error")
            print(f"Couldn't retrieve Data for week {week} and year {year}")
        body = r.text
        lines = body.rsplit("\n")

        for line in lines: 
            split = line.rsplit(",")
            if len(split) == 3 and split[0].isdigit():
                video_id = split[1]
                if video_id in videos:
                    videos[video_id] = videos[video_id] + 1
                else:
                    videos[video_id] = 1 
                if video_id == "mXnJqYwebF8":
                    address = split[2]
                    if address not in moo_queuers:
                        moo_queuers[address] = 0
                    moo_queuers[address] += 1 
moo_list = sorted(moo_queuers.items(), key=lambda x:x[1])
moo_list.reverse()
print(moo_list)
print("Got all the videos, saving to file")
with open("Output.txt","w",encoding="utf-8") as file:
    file.write("Video ID, Number of times played, Title \n")
    for video_id,num_plays in sorted(videos.items(),key= lambda x:x[1],reverse=True): #Sort videos by number of plays
        if num_plays > MIN_PLAYS_FOR_LOOKUP and title_enabled:
            title = get_video_title.get_video_title(video_id)
        elif title_enabled:
            title = "Too insignificant to look up."
        else:
            title = "No API key found"
        
        file.write(f'{video_id}, {num_plays}, "{title}" \n')

print("Infinite querying of specific Video IDs:")
while True:
    video = input("Video Id: ")
    if video in videos:
        print("Video has been played")
    else:
        print("Video might not have been played")