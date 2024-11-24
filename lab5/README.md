First run in command line in this directory after running docker on windows

```
docker build -t adzd/graphframes-spark-windows .
```

Then run:

```
docker run --rm -p 8888:8888 --name graphframes-notebook adzd/graphframes-spark-windows:latest start-notebook.sh --ip='*' --NotebookApp.token='' --NotebookApp.password=''
```

You will have an issue with saving. You need to change permissions. Run the following command:

```
docker exec -it graphframes-notebook bash
```

And then in container's bash:

```
chmod -R 777 /work
exit
```

And only then access `http://127.0.0.1:8888/lab`

Remember to download the notebook after saving it as it's only saved in the container.