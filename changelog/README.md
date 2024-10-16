Adding basic code for fetching Git commits.

```
cd changelog

docker build -t changelog .

docker run --rm --volume ./data:/code/data -e GIT_ACCESS_TOKEN=<your git access token> changelog --user=<user> --repo=<your repo goes here> --days=<n>

```


Example of a generated change log file using this tool will look like the following. Eg. 

File name:- change_log_20241007025357.txt

```
### add ###
 - Added a Classifier function to show only the relevant changes.


### change ###
 - First commit for the change Log tool.
 - Edit the README for a minor change.


### remove ###


### deprecate ###


### fix ###


### security ###


### others ###
 - Force the Git access token through a env variable.
 - Parameterize user and repo variables.
```
