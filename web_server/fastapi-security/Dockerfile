FROM python:3.11.9-slim
ENV HNSWLIB_NO_NATIVE=1
WORKDIR /app
RUN export HNSWLIB_NO_NATIVE=1
RUN apt-get update --fix-missing && apt-get install -y --fix-missing build-essential

# Install Rust
#RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
#ENV PATH="/root/.cargo/bin:${PATH}"

COPY . /app/

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
EXPOSE 8002

CMD ["fastapi", "run", "/app/main.py", "--host", "0.0.0.0", "--port", "8002"]