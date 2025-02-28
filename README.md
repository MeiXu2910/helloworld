# GitHub API Repository Fetcher (HW 04a)

## Overview
This project is a Python script that fetches a GitHub user's repositories and counts the number of commits in each repository.

## Dependencies
- Python 3.x
- `requests` module (`pip install requests`)
- `unittest` module (built-in for testing)

## Installation & Usage

### Clone the Repository
```
git clone https://github.com/MeiXu2910/helloworld.git
cd helloworld/GitHubApi567-hw4a
```

### Configure Your GitHub Token
1. Generate a **GitHub Personal Access Token (PAT)** [here](https://github.com/settings/tokens).
2. Ensure it has `public_repo` scope.
3. Set it as an environment variable:
   ```sh
   export GITHUB_TOKEN=your_actual_token_here
   ```

### Run the Main Script
```
python github_api.py
```

### Run Unit Tests
```
python -m unittest test_github_api.py
```

## Continuous Integration (CI/CD)
This project uses **Travis CI** for continuous integration to ensure all tests pass before merging.

### Setting Up Travis CI
1. Sign in to [Travis CI](https://travis-ci.com/) using GitHub.
2. Enable your repository.
3. Add a `.travis.yml` file with the following content:

```yaml
language: python
python:
  - "3.8"
install:
  - pip install requests
script:
  - python -m unittest test_github_api.py
```

4. Push the `.travis.yml` file to your repository.
5. Ensure the build passes with the badge in `README.md`:

```
[![Build Status](https://travis-ci.com/MeiXu2910/helloworld.svg?branch=main)](https://travis-ci.com/MeiXu2910/helloworld)
```

## Example Output
```
Repo: Linux Number of commits: 500
Repo: Kernel Number of commits: 1200
```

## Important Notes
- GitHub API has rate limits. If you exceed the limit, wait before retrying.
- Avoid hardcoding your personal access token in public repositories.

## Assignment Requirements Fulfilled
 Fetch GitHub API data correctly
 Implemented unit tests
 Configured CI/CD with Travis CI
 Provided detailed documentation

## Thought Process & Challenges
### Design Approach
1. **Modular Structure**: The function is separated for better testability.
2. **Error Handling**: Handled request failures using `try-except`.
3. **Pagination**: Considered for handling large repositories.

### Testing Challenges & Solutions
- **API Rate Limits**:
  - Used authentication to increase request limits.
  - Added `time.sleep(2)` to avoid excessive requests.
- **Handling Invalid Users**:
  - Tested with non-existent usernames.
- **GitHub API Response Changes**:
  - Used `get()` to access JSON keys safely.

## Conclusion
This assignment successfully implements GitHub API integration with testing and CI/CD to ensure reliability and correctness.