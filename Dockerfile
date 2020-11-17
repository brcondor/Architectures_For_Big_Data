FROM jupyter/pyspark-notebook
WORKDIR /home/jovyan/work
COPY dataGenerator /customLib/dataGenerator
ENV PYTHONPATH=$PYTHONPATH:/customLib/
EXPOSE 8888
CMD  jupyter notebook