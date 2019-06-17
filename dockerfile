#
#  _______  ___   __   __  _______ 
# |   _   ||   | |  |_|  ||       |
# |  |_|  ||   | |       ||    ___|
# |       ||   | |       ||   |___ 
# |       ||   | |       ||    ___|
# |   _   ||   | | ||_|| ||   |___ 
# |__| |__||___| |_|   |_||_______|
#
# Rock Dockerfile
# @riverflow-docker:0.1

# Metadata
FROM python:3
MAINTAINER christian@meetaime.com

# Set working directory
WORKDIR /usr/src/rock

# Install dependencies
RUN pip install Flask
RUN pip install PyYAML

# So far, only support Keras on TF
RUN pip install tensorflow keras

# Copy Rock instance to Docker container
COPY ./rock-instance/ /usr/src/rock

# Run Flask
CMD [ "python", "./app.py" ]