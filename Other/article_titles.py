import requests


def getArticleTitles(author):
    URL = "https://jsonmock.hackerrank.com/api/articles?author={author}&page={page_number}"

    titles = []

    page_number = 1
    while 1:
        articles_response = requests.get(
            URL.format(author=author, page_number=page_number)
        )
        articles_response.raise_for_status()

        articles_json = articles_response.json()
        articles = articles_json["data"]

        for article in articles:
            if title := article["title"]:
                titles.append(title)
            elif story_title := article["story_title"]:
                titles.append(story_title)
            else:
                continue

        if articles_json["total_pages"] == page_number:
            break

        page_number += 1

    return titles


print(len(getArticleTitles("coloneltcb")))
