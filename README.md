# chatgpt-local
a local instance of chatgpt, to run when demand on the web version is high


## local build and run
docker build -t gpt3-playground .
docker run --name gpt3-playground -p 5000:5000 gpt3-playground

## pull docker image and run
