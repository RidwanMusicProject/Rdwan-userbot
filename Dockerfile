FROM mrismanaziz/man-userbot:buster

RUN git clone -b Rdwan-Userbot https://github.com/RidwanMusicProject/Rdwan-userbot /home/Rdwan-Userbot/ \
    && chmod 777 /home/Rdwan-userbot \
    && mkdir /home/Rdwan-userbot/bin/

WORKDIR /home/Rdwan-userbot/

CMD [ "bash", "start" ]
