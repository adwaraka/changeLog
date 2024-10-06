Adding basic code for fetching Git commits.

`
docker build -t changelog .
docker run -e GIT_ACCESS_TOKEN=<your token comes here> changelog  --user=<> --repo=<>
`
