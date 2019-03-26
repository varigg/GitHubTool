from githubmetrics import GitHubMetrics
from github import Github


gitHubOrg=GitHubMetrics("octokit")
assert(gitHubOrg),""

#need mock repo and organization
gh=Github(login_or_token='c4d489d4558971d8209e93b2553d5afca68b9d41', per_page=100)
repo=gh.get_organization('octokit').get_repo('octokit.rb')
assert(gitHubOrg.getNumberOfForks(repo)==918), "Should be 918"
assert(gitHubOrg.getNumberOfStars(repo)==3043), "Shold be 3043"
assert(gitHubOrg.getNumberOfPullRequests(repo)==6), "Should be 6"
assert(gitHubOrg.getContributionPercentage(repo)==0.006535947712418301), "Should be 0.006535947712418301"

assert(gitHubOrg.getNumberOfForks(repo)==gitHubOrg.getMetric(repo,'forks')), "Should be the same"
assert(gitHubOrg.getNumberOfPullRequests(repo)==gitHubOrg.getMetric(repo,'pr')), "Should be the same"
assert(gitHubOrg.getContributionPercentage(repo)==gitHubOrg.getMetric(repo,'contrib')), "Should be the same"
assert(gitHubOrg.getNumberOfStars(repo)==gitHubOrg.getMetric(repo,'stars')), "Should be the same"

assert(gitHubOrg.findTopRepos(1,'stars')=={'rest.js': 3176}),""
assert(gitHubOrg.findTopRepos(1,'pr')=={'octokit.net': 21}),""
assert(gitHubOrg.findTopRepos(1,'forks')=={'octokit.rb': 918}),""
assert(gitHubOrg.findTopRepos(1,'contrib')=={'graphql.js': 1.0}),""