FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app

RUN groupadd -r iucgroup && useradd -r -g iucgroup iucuser
RUN chown -R iucuser:iucgroup /app
USER iucuser

EXPOSE 5000
CMD [ "python", "app.py" ]