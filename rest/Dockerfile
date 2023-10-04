FROM us.gcr.io/zekoder-dev-349809/zekoder/zeagent/rest-serve:0.1

COPY . .

RUN poetry config virtualenvs.create false && poetry install --no-interaction

ENV PORT=8080
ENV PYTHONPATH=/app

EXPOSE $PORT

CMD exec uvicorn --host 0.0.0.0 --port $PORT --workers 4 api:app