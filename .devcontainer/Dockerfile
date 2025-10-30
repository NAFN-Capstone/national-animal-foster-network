# Use official Node.js image
FROM python:latest
# FROM node:20

#install packages
# RUN  apt-get update && apt-get -y install git 

# Set working directory
WORKDIR /app

# Copy source code
COPY . .

# Copy package files and install dependencies
# COPY package*.json ./
RUN pip install -r requirements.txt


WORKDIR /src/routes

EXPOSE 3000

# RUN python script.py
CMD ["python", "server.py"]

# Expose port and start app
# CMD ["npm", "run", "dev"]


