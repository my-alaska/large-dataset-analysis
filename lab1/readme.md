Make sure Java is installed on your machine. Preferably Java 8

```java -version```

Open jupyter

```jupyter notebook```

Run docker command

```docker run -p 8888:8888 -p 4040:4040 -v $HOME:/home/jovyan/work jupyter/all-spark-notebook```

If you're using windows replace `$HOME` with your user directory. For example `C:\Users\piotr`

Connect to localhost:8888 and localhost:4040 through your browser

if Jupyter prompts you for a token you can find it in the docker logs after running the command