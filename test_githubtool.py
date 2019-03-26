from github import GitHub
import json

gitHubOrg=GitHub("octokit")
assert(gitHubOrg),""

with open("testrepo.json", 'r') as f:
        repo = json.load(f)

assert (gitHubOrg.getNumberOfForks(repo)==918),"Should be 918"
assert (gitHubOrg.getNumberOfStars(repo)==3043),"Should be 3043"
print("The following tests need mocks to be reliable. Just showing the data for now.")
print(gitHubOrg.getNumberOfPullRequests(repo))
print(gitHubOrg.getContributionPercentage(repo))