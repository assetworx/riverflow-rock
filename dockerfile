#   _____  _                 __ _               
#  |  __ \(_)               / _| |              
#  | |__) |___   _____ _ __| |_| | _____      __
#  |  _  /| \ \ / / _ \ '__|  _| |/ _ \ \ /\ / /
#  | | \ \| |\ V /  __/ |  | | | | (_) \ V  V / 
#  |_|  \_\_| \_/ \___|_|  |_| |_|\___/ \_/\_/  
#
#  Riverflow AI Dockerfile.
                                              
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
LABEL maintainer="christian@meetaime.com"
RUN pip install keras tensorflow
COPY ./src /app
COPY ./model-files /app/model-files