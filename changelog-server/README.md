Build a barebones log dump site; not final display tool. Visible using http://localhost:8000

```
docker build -t changelog_server .

docker run -p 8000:8000 --volume ./{where the changelog dumps their data}:/code/logs changelog_server

```