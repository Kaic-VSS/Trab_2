FROM python:3.12-slim
WORKDIR /app
COPY *.py /app/
RUN mkdir -p /app/data
ENV ATIVOS_JSON=/app/data/ativos.json
CMD ["python", "-u", "Menus_Alpha.py"]
