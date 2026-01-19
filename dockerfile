FROM python:3.14.0
WORKDIR /cube
COPY . .
CMD ["python","cube.py"]