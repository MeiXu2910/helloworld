import requests
import time
import os

def get_github_repos_and_commits(username):
    """
    Fetch the list of repositories and the number of commits for each repository for a given GitHub user.
    """
    token = os.getenv("GITHUB_API_TOKEN", "your_personal_access_token_here")
    headers = {"Authorization": f"token {token}"}
    repos_url = f"https://api.github.com/users/{username}/repos"

    try:
        repos_response = requests.get(repos_url, headers=headers)
        repos_response.raise_for_status()

        repos_data = repos_response.json()
        repo_commit_counts = []

        for repo in repos_data:
            repo_name = repo.get("name")
            commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"

            time.sleep(2)  # Avoid hitting rate limits
            commits_response = requests.get(commits_url, headers=headers)

            if commits_response.status_code == 200:
                commits_data = commits_response.json()
                commit_count = len(commits_data)
                repo_commit_counts.append(f"Repo: {repo_name} Number of commits: {commit_count}")
            else:
                repo_commit_counts.append(f"Repo: {repo_name} Number of commits: Unknown (Error)")

        return repo_commit_counts

    except requests.exceptions.RequestException as e:
        return [f"Error: {str(e)}"]

if __name__ == "__main__":
    username = "MeiXu2910"
    results = get_github_repos_and_commits(username)
    for result in results:
        print(result)





