FROM python:3.8-alpine
RUN mkdir -p /code
COPY ./code /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["iptables". "-F"]
EXPOSE 5000
CMD ["python", "app.py"]
