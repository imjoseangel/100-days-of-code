# Python 3.6 Data Science Docker Container

This is fully ready Docker container with:

- NumPy
- Pandas
- Sklearn
- Matplotlib
- Seaborn
- pyyaml
- h5py
- Jupyter
- Tensorflow
- Keras
- OpenCV 3

It runs on top of [Ubuntu 18.04 Docker container](https://hub.docker.com/_/ubuntu/) ([Dockerfile](https://github.com/imjoseangel/docker-data-science/blob/devel/Dockerfile))

## Running container

Use ```notebooks``` forlder to store Jupyter Notebooks:

```sh
mkdir notebooks
```

Run Docker container with the following command:

```sh
docker run -it -p 8888:8888 -p 6006:6006 -d -v $(pwd)/notebooks:/notebooks --name datascience imjoseangel/datascience
```

**Parameters**:

- ```-p 8888:8888``` to export Jupyter Web interface
- ```-p 6006:6006``` to export TensorflowDashboard Web interface
- ```-d``` to run Docker container in background
- ```-v notebooks:/notebooks``` to mount just created *notebooks* folder Docker inside container
- - ```--name datascience``` to name your Docker container as *datascience*
