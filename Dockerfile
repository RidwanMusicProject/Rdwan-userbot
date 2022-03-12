FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/RidwanMusicProject/UserbotRdwn /home/UserbotRdwn/ \
    && chmod 777 /home/UserbotRdwn \
    && mkdir /home/UserbotRdwn/bin/

WORKDIR /home/UserbotRdwn/

CMD [ "bash", "start" ]
