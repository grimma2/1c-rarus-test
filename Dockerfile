# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.11.9-alpine AS builder
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 

ENTRYPOINT ["python", "main.py"]

FROM builder as dev-envs
RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
CMD ["python", "main.py"]
