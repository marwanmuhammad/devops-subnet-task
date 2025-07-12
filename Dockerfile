FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install pandas matplotlib openpyxl

CMD ["python", "subnet_analyzer.py"]
