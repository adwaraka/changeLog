Using Flask for the server for the changelogs

```
cd changelog-server/

docker build -t changelog_server .

docker run --rm -p 5000:5000 --mount type=bind,source=./data,target=/app/data,bind-recursive=enabled changelog_server

```


To use the API

```
curl -s "http://localhost:5000/parameters?user=adwaraka&repo=binarytrees"
```