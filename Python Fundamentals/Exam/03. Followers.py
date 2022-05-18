data = input()

followers = {}

while data != "Log out":
    split_data = data.split(": ")
    command = split_data[0]
    if command == "New follower":
        username = split_data[1]
        if username not in followers:
            followers[username] = {"Likes": 0, "Comments": 0}
    elif command == "Like":
        username, count = split_data[1], int(split_data[2])
        if username not in followers:
            followers[username] = {"Likes": count, "Comments": 0}
        else:
            followers[username]["Likes"] += count
    elif command == "Comment":
        username = split_data[1]
        if username not in followers:
            followers[username] = {"Likes": 0, "Comments": 1}
        else:
            followers[username]["Comments"] += 1
    elif command == "Blocked":
        username = split_data[1]
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]

    data = input()

sorted_followers = sorted(followers.items(), key=lambda kvpt: (-(kvpt[1]["Likes"] + kvpt[1]["Comments"]), kvpt[0]))

print(f"{len(followers)} followers")
for username, data in sorted_followers:
    total_like_comment = data["Likes"] + data["Comments"]
    print(f"{username}: {total_like_comment}")

