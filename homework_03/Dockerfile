#docker run -it -p 8000:8000 web

FROM python:3.11.7-bookworm

WORKDIR /myapp
RUN pip install "poetry==1.7.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY ./main.py /myapp/

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000
