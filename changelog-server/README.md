Build a barebones log dump site; not final display tool. Visible using http://localhost:8000

```
cd changelog-server/

docker build -t changelog_server .

docker run --rm -p 5000:5000 --mount type=bind,source=./data,target=/app/data,bind-recursive=enabled changelog_server

```


To use the API

```
curl -s "http://localhost:5000/parameters?user=adwaraka&repo=binarytrees"
```