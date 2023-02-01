import re


def main():
    print(parse(input("HTML: ")))


# get html code for youtube embedded code and return shortened version of youtube link
def parse(s):
    # patter is just a html code
    # inside parenthesis will be real youtube link, just with 'embed' word inside it
    if youtube_link := re.search('<iframe.+?src="(.+)"></iframe>', s):
        # if its an html code save youtube's part in variable
        youtube_link = youtube_link.group(1)
    else:
        return None

    # shorten that link removing all non neccesery parts of links(http ,www), and leave only youtube link
    if short_link := re.search(
        r"(?:https?://(?:www\.)?)?(youtube.com/embed/xvFZjo5PgG0)", youtube_link
    ):
        short_link = short_link.group(1)
    else:
        return None

    # substitude with even shorter version, but add also https
    even_shorter_link = re.sub("youtube\.com/embed", "https://youtu.be", short_link)
    return even_shorter_link


if __name__ == "__main__":
    main()
