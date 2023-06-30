FROM untergeek/curator:8.0.2

USER root

RUN >>/var/spool/cron/crontabs/nobody \
    echo '* * * * * /curator/curator /.curator/create_post_index.yml'

ENTRYPOINT ["crond"]
CMD ["-f", "-d8"]
