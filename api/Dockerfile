
FROM python:slim

RUN apt update

RUN apt install -y python3-pip

#make requirements txt if adding/having more pip installs
RUN pip install "fastapi[all]"

#to start api server
CMD ["uvicorn", "main:app", "--reload"]