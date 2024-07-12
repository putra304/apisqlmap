FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y sqlmap

COPY sqlmap_api.py .

ENV PORT 8000

EXPOSE 8000

CMD ["python", "sqlmap_api.py"]
