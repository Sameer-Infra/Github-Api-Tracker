import requests

def get_github_profile(username):

    url = f"https://api.github.com/users/{username}"

    print(f"Github s {username} ka data nikal rha hu...")
    response = requests.get(url)

    if response.status_code == 200:
        profile_data = response.json()


        asli_name = profile_data.get("name", "Name nhi mila ")
        repos_count = profile_data.get("public_repos", 0)
        user_bio = profile_data.get("bio", "No Bio")

        print(f"\n--- 😎 Github profile Details ---")
        print(f"Name: {asli_name}")
        print(f" Public Repositories: {repos_count}")
        print(f" Bio: {user_bio}")
    else:
        print(f" Username nhi mila ya API down h ! Code: {response.status_code}")

get_github_profile("Sameer-Infra")
