# use python 3.13 slim
FROM python:3.13-slim

# set the working directory
WORKDIR /app


#Set environment vaiables
ENV PYTHONBUFFERED=1


# copy requirements first
COPY requirements.txt /app/requirements.txt


# install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the project
COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
