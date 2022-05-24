FROM jinaai/jina:latest

RUN apt-get update && apt-get install pandoc

# install requirements before copying the workspace
COPY requirements.txt /requirements.txt
RUN pip install --default-timeout=1000 --compile -r requirements.txt

# setup the workspace
COPY . /workspace
WORKDIR /workspace

ENTRYPOINT ["jina", "executor", "--uses", "config.yml"]
