import sys
from github import Github

class GitHubMetrics:   

    def __init__(self, org):
        self.org = org
        self.g = Github(login_or_token='c4d489d4558971d8209e93b2553d5afca68b9d41', per_page=100)
    def getOrgRepos(self):
        try:
            return self.g.get_organization(self.org).get_repos()
        except:
            print ("The organization '"+self.org+"' could not be found.")
            sys.exit(2)
        

    def getNumberOfForks(self, repo):
        return int(repo.forks_count)


    def getNumberOfStars(self, repo):
        return int(repo.stargazers_count)


    def getNumberOfPullRequests(self, repo):
        return repo.get_pulls().totalCount


    def getContributionPercentage(self, repo):
        if self.getNumberOfForks(repo)==0:
            return 0
        return self.getNumberOfPullRequests(repo)/self.getNumberOfForks(repo)

    def getMetric(self,repo,metric):
        if metric == "forks":
            return self.getNumberOfForks(repo)
        elif metric == "stars":
            return self.getNumberOfStars(repo)
        elif metric == "pr":
            return self.getNumberOfPullRequests(repo)
        elif metric == "contrib":
            return self.getContributionPercentage(repo)

    def findTopRepos(self, length, metric):
        topRepos={}
        repoMetrics={}
        for repo in self.getOrgRepos():
            value=self.getMetric(repo,metric)
            if value in repoMetrics :                
                repoMetrics[value].append(repo.name)
            else:
                repoMetrics[value] = [repo.name]               
        metricList = sorted(repoMetrics.keys(), reverse=True)
        count=0
        for number in metricList:
            for repoName in repoMetrics[number]:
                #print(repoName+'\t'+str(number))
                topRepos[repoName]=number    
                count=count+1   
                if count >= length:
                    return topRepos    
        return topRepos

            