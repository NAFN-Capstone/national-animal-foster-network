# Use official Node.js image
# Use a stable Python minor release (3.11) to avoid incompatibilities with packages
# that may call deprecated stdlib APIs removed in later Python versions.
FROM python:3.11-slim
# FROM node:20

#install packages
# RUN  apt-get update && apt-get -y install git 

# Set working directory
WORKDIR /app

# Copy source code
COPY . .

# Upgrade pip and setuptools first (helps avoid older setuptools/importlib bugs)
RUN python -m pip install --upgrade pip setuptools wheel \
	&& if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Install curl so the HEALTHCHECK can probe the Flask endpoint
RUN apt-get update \
	&& apt-get install -y --no-install-recommends curl \
	&& rm -rf /var/lib/apt/lists/*


# Switch to the directory that contains the Flask app inside the copied /app tree
# The repository was copied into /app, so the script lives at /app/src/routes
WORKDIR /app/src/routes

EXPOSE 3000

# Healthcheck: probe the root URL. If curl returns non-2xx, the container is unhealthy.
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
	CMD curl -fsS http://localhost:3000/ || exit 1

# RUN python server from script.py
CMD ["python", "script.py"]



