FROM python:3.10-slim
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# ensure the file will be created in the workdir
# no EXPOSE changes needed
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
