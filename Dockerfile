FROM python:3.7.0-stretch
RUN useradd -m fbot
RUN pip install fbchat
COPY main.py /home/fbot
COPY config.cfg /home/fbot
USER fbot
CMD python /home/fbot/main.py