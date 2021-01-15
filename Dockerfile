FROM python
COPY . /app
WORKDIR /app
RUN pip3 install flask
RUN chmod +x /app/app.py
RUN chmod +x /app/main.py
#RUN pwd
#RUN ls -a
CMD ["python3", "/app/main.py"]
