psql -Upostgres -c 'drop database socialnet;'
psql -Upostgres -c 'create database socialnet;'
psql -Upostgres -c 'grant all privileges on database socialnet to socialnet;'
