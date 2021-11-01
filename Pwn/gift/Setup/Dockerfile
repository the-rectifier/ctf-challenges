FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y socat

# transfer files
WORKDIR /root
COPY gift ./pwn
COPY flag ./flag

EXPOSE 4337
CMD ["socat", "-T60", "TCP-LISTEN:4337,reuseaddr,fork,su=root", "EXEC:/root/pwn"]