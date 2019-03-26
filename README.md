# GitHubTool
A command-line tool that allows a user to display a ranked list of repos for a Github organization.
<pre>
Usage:
  githubtool.py [options] org
Options:
  -n number     Number of repos to show [default: 10]
  -m metric     A metric to rank by. Recognized metrics are:
                forks - number of forks[default]
                stars - number of stars
                pr - number of pull requests
                contrib - contribution rate(pull requests/forks)
</pre>

Requirements  
Requires [python3](https://www.python.org/) and [requests](http://docs.python-requests.org/en/master/) intalled. To install the requests libary run <code>python3 -m ensurepip</code> and <code>'pip3 install requests'</code>.