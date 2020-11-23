from googleapiclient.discovery import build

# SCOPES = ["https://www.googleapis.com/auth/youtube"]


def url_encoder(item):
    return 'https://www.youtube.com/watch?v=' + item[u'contentDetails'][u'videoId']


def playlist(creds):
    youtube = build(
        "youtube", "v3", credentials=creds)

    # get by individual playlistId
    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId="PLui6Eyny-Uzx8YZ3Pw0r6jq6UuwYW61Rj",
        maxResults=50
    )
    response = request.execute()
    items = response[u'items']

    result = map(url_encoder, items)
    return result


if __name__ == "__playlist__":
    playlist()
