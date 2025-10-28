# Use official Node.js image
FROM python:3.12
# FROM node:20


#install packages
RUN  apt-get update && apt-get -y install git 

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

RUN npm run build 

# Expose port and start app
CMD ["npm", "run", "dev"]

EXPOSE 3000

