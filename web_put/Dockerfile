FROM python


# Install required python packages
RUN python -m venv /opt/venv
RUN /opt/venv/bin/python -m pip install --force --upgrade pip
RUN /opt/venv/bin/python -m pip install --force --upgrade setuptools
RUN /opt/venv/bin/python -m pip install tox
ADD . /opt/project
RUN /opt/venv/bin/python -m pip install /opt/project


# Entrypoint
WORKDIR /opt/project
EXPOSE 8081
ENV FLASK_APP=src/webput
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8081
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONWARNINGS=d
ENV WEBPUT_SECRET_KEY=!
ENTRYPOINT ["/opt/venv/bin/flask"]
CMD ["run"]
