import emoji

text = input("Input: ")

# index of ':', which is beginning of our text_emoji
index_1 = text.find(":")

# find the index of secodn ':', which is the end of our emoji
for c in text:
    if c == ":":
        # it will first find the first ":", kind of bug)))
        index_2 = text.index(c, (index_1 + 1))

# there we will store our emoji
text_emoji = ""

# that's where we need indicies
# second is '+1' becouse its exclusive
for c in text[index_1 : (index_2 + 1)]:
    text_emoji += c

# replace in users input text_emoji with real emoji
text = text.replace(text_emoji, emoji.emojize(text_emoji))

print(text)


# or just

print(emoji.emojize(text))

#ROFL
