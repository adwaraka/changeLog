Build a barebones log dump site; not final display tool. Visible using http://localhost:8000

```
cd changelog-server/

docker build -t changelog_server .

docker run --rm -p 8000:8000 --volume ./{where the changelog dumps their data}:/code/logs changelog_server

// arvindd25@penguin:~/workspace/codeSamples/changeLog/changelog-server$ cd ../changelog
// arvindd25@penguin:~/workspace/codeSamples/changeLog/changelog$ docker run --rm -p 8000:8000 --volume ./data:/code/logs changelog_server

```