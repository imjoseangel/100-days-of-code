FROM ubuntu:bionic

LABEL maintainer=imjoseangel

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget ca-certificates \
    build-essential cmake pkg-config \
    libjpeg8-dev libtiff5-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev \
    libgtk-3-dev apt-utils \
    libatlas-base-dev gfortran \
    git curl vim python3-dev python3-pip \
    libfreetype6-dev libhdf5-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade setuptools
RUN pip3 install cython pystan
RUN pip3 install tensorflow && \
    pip3 install numpy pandas sklearn matplotlib seaborn jupyter pyyaml h5py psycopg2 sqlalchemy folium && \
    pip3 install keras --no-deps && \
    pip3 install opencv-python && \
    pip3 install imutils
RUN pip3 install fbprophet

RUN ["mkdir", "notebooks"]
WORKDIR /notebooks
COPY conf/.jupyter /root/.jupyter
ADD run_jupyter.sh /
RUN chmod +x /run_jupyter.sh


# Jupyter and Tensorboard ports
EXPOSE 8888 6006

# Store notebooks in this mounted directory
VOLUME /notebooks

CMD ["/run_jupyter.sh"]
