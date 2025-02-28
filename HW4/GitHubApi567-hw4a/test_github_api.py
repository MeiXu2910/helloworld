import unittest
from github_api import get_github_repos_and_commits

class TestGitHubAPI(unittest.TestCase):

    def test_valid_user(self):
        """Test a valid GitHub user with repositories"""
        result = get_github_repos_and_commits("torvalds")  
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_invalid_user(self):
        """Test an invalid GitHub user"""
        result = get_github_repos_and_commits("invaliduser123456789")
        self.assertTrue("Error" in result[0])

    def test_no_repositories(self):
        """Test a GitHub user with no repositories"""
        result = get_github_repos_and_commits("emptyuser123456")
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()




