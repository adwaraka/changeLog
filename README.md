Adding basic code for fetching Git commits.

`
docker build -t changelog .
docker run --rm --volume ./data:/code/data -e GIT_ACCESS_TOKEN=<your token goes here> changelog --user=<git user> --repo=<repository name>
`
