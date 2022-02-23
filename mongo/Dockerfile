FROM mongo:5.0.6

RUN mkdir -p /data/db/scripts

COPY . /data/db

RUN mongod --fork --logpath /var/log/mongodb.log --dbpath /data/db \
    && CREATE_FILES=/data/db/scripts/