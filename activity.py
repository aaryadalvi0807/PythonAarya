from collections import defaultdict

def process_user_activity(records):
    unique_users = set()
    activity_count = defaultdict(int)
    user_activity_map = defaultdict(set)
    user_total_activity = defaultdict(int)

    for _, username, activities in records:
        unique_users.add(username)

        for activity in activities:
            activity_count[activity] += 1
            user_activity_map[username].add(activity)
            user_total_activity[username] += 1

    # sort activities for each user
    for user in user_activity_map:
        user_activity_map[user] = sorted(user_activity_map[user])

    # find most active user (handle tie lexicographically)
    max_count = max(user_total_activity.values())
    most_active_user = min(
        user for user, count in user_total_activity.items()
        if count == max_count
    )

    return {
        "unique_users": unique_users,
        "activity_count": dict(activity_count),
        "user_activity_map": dict(user_activity_map),
        "most_active_user": most_active_user
    }


# -------- EXECUTION PART (IMPORTANT) --------
records = [
    (1, "alice", ["login", "view", "logout"]),
    (2, "bob", ["login", "view"]),
    (3, "alice", ["login", "purchase"]),
    (4, "david", ["login", "view", "purchase", "logout"]),
]

result = process_user_activity(records)
print(result)
