import requests
import json

headers = {
  'Authorization': 'Bearer zed1j7eq8jsjdyghj6yq1fdv0pgyd9',
  'client-id': 'x41vdnbddl0aynl06sj5iytgoc19pw'
}

videoRequest = requests.get('https://api.twitch.tv/helix/clips?id=BlatantShyGarageTakeNRG-NsY7s7BwJbTKwuou', headers=headers)
pageURL = json.loads(videoRequest.text)

print(pageURL)
