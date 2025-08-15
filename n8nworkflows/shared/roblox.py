import requests

def get_user_id(username):
    url = "https://users.roblox.com/v1/usernames/users"
    payload = {
        "usernames": "bartek121099",
        "excludeBannedUsers": True
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    data = response.json()
    if data["data"]:
        return data["data"][0]["id"]
    return None


def get_username_history(user_id, limit=10, sort_order="Asc"):
    url = f"https://users.roblox.com/v1/users/{user_id}/username-history"
    params = {
        "limit": limit,
        "sortOrder": sort_order
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["data"]


if __name__ == "__main__":
    username = "SomeRobloxName"  # Replace with the Roblox username
    user_id = get_user_id(username)

    if user_id:
        print(f"User ID for {username}: {user_id}")
        history = get_username_history(user_id, limit=10)
        if history:
            for entry in history:
                print(f"Name: {entry['name']} – Changed At: {entry.get('created', '(unknown)')}")
        else:
            print("No previous usernames found.")
    else:
        print("User not found.")
