FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /var/www/api/
WORKDIR /var/www/api/
COPY api/requirements.txt /tmp/requirements.txt
COPY api/bootstrap.sh /opt/bin/bootstrap.sh
RUN pip install -r /tmp/requirements.txt
CMD /opt/bin/bootstrap.sh
