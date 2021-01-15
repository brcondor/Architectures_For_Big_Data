FROM jupyter/pyspark-notebook
COPY dataGenerator /customLib/dataGenerator
ENV PYTHONPATH=$PYTHONPATH:/customLib/