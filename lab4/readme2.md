```
docker build -t balis/coinbase-spark . # Build new image and automatically tag it as latest

docker network prune

docker network create coin-net

docker run --rm -p 8888:8888 -v "C:\Users\piotr:/home/jovyan/work" --network="coin-net" --name coinbase-notebook balis/coinbase-spark:latest start-notebook.sh --NotebookApp.token=""


```

if needed, replace `C:\Users\piotr` with your home directory