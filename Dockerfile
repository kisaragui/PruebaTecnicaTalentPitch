FROM apache/airflow:2.6.0-python3.10
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
 	  build-essential tzdata \
 	  apt-transport-https \
	  ca-certificates \
	  curl \
	  gnupg \
	  lsb-release\
	  python3-dev \
	  libpq-dev \
  && apt-get clean  \
  && apt-get autoremove -yqq --purge \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt
USER airflow

ENV PIP_USER=true

RUN pip install -r /requirements.txt
