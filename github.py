import sys
import requests
import re

class GitHub:
    headers = {'Authorization': 'token c4d489d4558971d8209e93b2553d5afca68b9d41',
    'Accept' : 'application/vnd.github.v3+json'}
    

    def __init__(self, org):
        self.org = org

    def getOrgRepos(self):
        response = requests.get(
            'https://api.github.com/orgs/'+self.org+'/repos', headers=self.headers)
        if(response.status_code == 200):
            return response.json()
        else:
            print("The organization '"+self.org+"' could not be found on GitHub.")
            sys.exit(2)

    def getPullRequests(self, repo):
        #Try to forcing pagination to 1 and use the page inumber in the last page as the count
        #response = requests.get(repo.get('pulls_url')+'?per_page=1', headers=self.headers)
        #link=response.headers['Link']
        #m=re.match(r'page=(\d+)>; rel="last"',link)
        #print(m.group(0))    
        
        #use search API
        #how to get past the 30 results limit?
        response=requests.get('https://api.github.com/search/issues?q=+type:pr+org:'+self.org+"+repo:"+repo.get('name'),headers=self.headers)   

        return response.json()


    def getNumberOfForks(self, repo):
        return int(repo.get("forks_count"))


    def getNumberOfStars(self, repo):
        return int(repo.get("stargazers_count"))


    def getNumberOfPullRequests(self, repo):
        num= len(self.getPullRequests(repo).get('items'))
        #print(repo.get('name'))
        #print(num)
        return num


    def getContributionPercentage(self, repo):
        return len(self.getPullRequests(repo))/int(repo.get("forks"))

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
        repos=self.getOrgRepos()
        repoMetrics = {}
        for repo in repos:            
            value=self.getMetric(repo,metric)
            if value in repoMetrics :                
                repoMetrics[value].append(repo.get("name"))
            else:
                repoMetrics[value] = [repo.get("name")]               
        metricList = sorted(repoMetrics.keys(), reverse=True)
        count=0
        for number in metricList:
            for repoName in repoMetrics[number]:
                print(repoName+'\t'+str(number))
                count=count+1
                if count > length:
                    sys.exit(0)    


            