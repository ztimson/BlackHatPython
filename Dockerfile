FROM kalilinux/kali-rolling

RUN apt update -y && apt upgrade -y && \
    apt install -y python3 python3-pip

WORKDIR /root/

CMD ["tail", "-f", "/dev/null"]
