import re


TEXT = "TEST 1:1 Here are words. 1:2 Now the second verse. 1:3 This is the third verse, 1:4 Fourth verse also has the word second."

# pattern = re.compile(r"(\d+:\d+)(.+?)(?=\d+:\d+|$)")
# pattern = re.compile(r"([0-9]{1,3}:[0-9]{1,3}).*(Levi.*)")

pattern = re.compile(r"(?!\d+:\d+)(.+?)(second)(.+?)(?=\d+:\d+|$)")

matches = pattern.finditer(TEXT)

for m in matches:
    print("Group 1: ", m.group(1))
    print("Group 2: ", m.group(2))
    print("Group 3: ", m.group(3))
    # print ("Group 4: ", m.group(4))
