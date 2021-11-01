FROM ubuntu:20.04

RUN apt-get update
RUN apt-get  install socat

WORKDIR /root
COPY ./pwn pwn
COPY ./flag.txt flag.txt

EXPOSE 4340

CMD ["socat", "-T60", "TCP-LISTEN:4340,reuseaddr,fork,su=root", "EXEC:/root/pwn"]
