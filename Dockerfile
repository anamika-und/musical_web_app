FROM python:3

# Create app directory
WORKDIR /app

# Bundle app source
COPY . /app

# Install app dependencies
RUN pip3 install -r requirements.txt

EXPOSE 5000
# ENTRYPOINT [ "python3"]
# CMD ["flask", "run", "--host=0.0.0.0"]
CMD [ "python3", "-m", "musical.music_app" ]