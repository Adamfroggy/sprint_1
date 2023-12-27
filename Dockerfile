# Base Image
FROM python:3.8-slim

# Environment Configuration
WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    SHELL=/bin/bash \
    NAME=Welcome

# Application Code
COPY . /app

# Dependency Installation
RUN apt-get update
RUN apt-get install -y python3-pip curl
RUN apt-get install -y figlet
RUN apt-get install -y python3-pandas python3-numpy python3-sklearn
RUN apt-get clean
RUN pip install --upgrade pip
RUN apt-get install -y nano
RUN apt-get install -y git
RUN apt-get install -y nmap
RUN apt-get install -y gdb strace


# Generated FIGlet text
RUN figlet -f slant "WHAT UP ADAM!" > /app/figlet_output.txt

# Default Command
CMD ["python", "app.py"]
