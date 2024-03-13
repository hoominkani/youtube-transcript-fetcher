FROM python:3.9.18-slim
WORKDIR /app
COPY ./backend/requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./backend/ /app/
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]