# Estocâe API

### inicialização do ambiente 

>Step-by-step setup tutorial of the Marketplace's backend.
>
>The tutorial assumes that the user's OS is UNIX based, **if not make the appropriate changes and select the correct OS in the documentation**. 
>
>_If running on Windows remember to enable Hyper-V and virtual environments._ 

#### Pre Requiments
* [Docker](https://docs.docker.com/engine/install/debian/)
> create docker group, _**you'll probably have to reboot after this**_.
```shell script
sudo groupadd docker
sudo usermod -aG docker $USER
```
* [Docker Compose](https://docs.docker.com/compose/install/)

#### Git clone
>Clone the project and go to the chosen directory, for example:
```shell script
git clone https://github.com/pcarvalho-dev/estocae-api
cd ~/estocae-api
```

#### Deploy
>Build project
```shell script
docker-compose up --build
```
>Regular run project
```shell script
docker-compose up
 ```

You ready to go!

> Redeploy restoring database 
#### You must to have python in your system
```shell script
python3 init.py
```

#### Migrations and DB
>To make a migration on the database use:
```shell script
docker-compose exec api flask db migrate -m"<your message>"
```
>if there's a conflict with the migration heads, run:
```shell script
bash db-merge.sh
``` 
>If you wish to update the db dupms, use:
```shell script
bash db-dump
```


### Relatorio de tests

docker-compose exec api python -m pytest "tests" -p no:warnings --cov="app"

