FROM python:3.7.3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /usr/src/app/main.py

ENV SCHEDULE @minutely

CMD ["python", "main.py"]
