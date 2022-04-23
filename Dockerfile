FROM mrismanaziz/man-userbot:buster

RUN git clone -b Rdwan-Userbot https://github.com/RidwanMusicProject/Rdwan-Userbot /home/Rdwan-Userbot/ \
    && chmod 777 /home/Rdwan-Userbot \
    && mkdir /home/Rdwan-Userbot/bin/

WORKDIR /home/Rdwan-Userbot/

CMD [ "bash", "start" ]
