FROM python:3.13.0-slim as chroot

RUN /usr/sbin/useradd --no-create-home -u 1000 user

COPY flag.txt chal.py run.sh /home/user/
RUN chmod +x /home/user/run.sh  /home/user/chal.py

RUN flag_name=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 16) && \
  mv /home/user/flag.txt /home/user/flag_$flag_name.txt

FROM gcr.io/kctf-docker/challenge@sha256:0f7d757bcda470c3bbc063606335b915e03795d72ba1d8fdb6f0f9ff3757364f

COPY --from=chroot / /chroot

COPY nsjail.cfg /home/user/

CMD kctf_setup && \
  kctf_drop_privs \
  socat \
  TCP-LISTEN:1337,reuseaddr,fork \
  EXEC:"kctf_pow nsjail --config /home/user/nsjail.cfg -- /home/user/run.sh"
