FROM python:3

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY 04_Azure_Docker_Flask.py .

EXPOSE 80

ENTRYPOINT ["python"]

CMD ["04_Azure_Docker_Flask.py"]