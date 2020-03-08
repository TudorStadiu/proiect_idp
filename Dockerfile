FROM python:3.6

# Create app directory
WORKDIR /app

COPY . .

EXPOSE 8080
CMD [ "python", "server.py" ]
