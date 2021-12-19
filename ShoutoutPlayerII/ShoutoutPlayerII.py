# Imports
import requests
import json
import random

Authorization = "Bearer 9f2o33yh8m2zhmbj8uaj29ll6cfm54"
OAuthAuthorization = "oauth:2p2ga0r8myd180ie7am6njt4d5kz1d"
clientid = "3e503jl1m9rx98bv72kp4ovy0u4lur" # this is my (assassin's) clientid

# this is going to be imported from chat.py script to scrape the name from the chat
# shoutoutname = 

# Using my own username as a test
url = "https://api.twitch.tv/helix/users?login=Zarenimizxax"

# Security stuff
payload={}
headers = {
  'Authorization': Authorization,
  'client-id': clientid
}

# Extracting the user ID from their name
response = requests.get(url, headers=headers, data=payload)
userJson = json.loads(response.text)
print(userJson)
userId = userJson['data'][0]['id']

print(userId)

# More security stucff
headers = {
  'Authorization': Authorization,
  'client-id': clientid
}

# Pulling a video from that user's page
videoRequest = requests.get('https://api.twitch.tv/helix/clips?broadcaster_id=' + userId, headers=headers)
pageURL = json.loads(videoRequest.text)
#print(pageURL)

# Generating a random number from 1-20 (default number of videos pulled is 20, that's plenty)
randomNumber = random.randint(0, 19)
print(randomNumber)

# Then we choose a video index from that list using the random number we created, and pull the URL
chooseVideo = pageURL['data'][randomNumber]['url']
print(chooseVideo)

# We get the thumbnail url in order to get the unique Id for the video
VideoThumbnail = pageURL['data'][randomNumber]['thumbnail_url']
print(VideoThumbnail)

# If statement to determine what URL format needs to be used for the clip

if "offset" in VideoThumbnail:
  # First round of splitting the url to isolate the Id
  SplitThumbnail = VideoThumbnail.split('twitch.tv/')
  print(SplitThumbnail)

  # Taking the second indexed item and split it again
  VideoID = SplitThumbnail[1].split("-preview")
  print(VideoID)

  # After the second split assign the video Id to a variable
  FinalVideoId = VideoID[0]
  print(FinalVideoId)

  # Assign the endpoint url to a variable and insert the video Id to create the link
  EndPointURL = "https://clips-media-assets2.twitch.tv/"+FinalVideoId+".mp4"
  print(EndPointURL)
else:
    # First round of splitting the url to isolate the Id
  SplitThumbnail = VideoThumbnail.split('C')
  print(SplitThumbnail)

  # Taking the second indexed item and split it again
  VideoID = SplitThumbnail[1].split("-")
  print(VideoID)

  # After the second split assign the video Id to a variable
  FinalVideoId = VideoID[0]
  print(FinalVideoId)

  # Assign the endpoint url to a variable and insert the video Id to create the link
  EndPointURL = "https://clips-media-assets2.twitch.tv/AT-cm%7C"+FinalVideoId+".mp4"
  print(EndPointURL)

