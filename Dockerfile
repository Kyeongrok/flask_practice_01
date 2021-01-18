FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN chmod +x /app/app.py
RUN chmod +x /app/main.py
#RUN pwd
#RUN ls -a
CMD ["python3", "/app/main.py"]
