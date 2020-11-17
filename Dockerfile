FROM jupyter/pyspark-notebook
WORKDIR /home/jovyan/work
COPY dataGenerator dataGenerator
EXPOSE 8888
CMD jupyter notebook