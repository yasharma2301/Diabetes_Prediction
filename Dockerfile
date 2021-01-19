FROM continuumio/anaconda3:4.4.0
COPY . /app
EXPOSE 8000
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]