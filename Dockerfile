FROM mrismanaziz/man-userbot:buster

RUN git clone -b Rdwan-Userbot https://github.com/RidwanMusicProject/Rdwan-userbot /home/Rdwan-Userbot/ \
    && chmod 777 /home/Rdwan-Userbot \
    && mkdir /home/Rdwan-Userbot/bin/

COPY ./sample_config.env ./config.env* /home/Rdwan-Userbot/

WORKDIR /home/Rdwan-Userbot/

CMD ["python3", "-m", "userbot"]
