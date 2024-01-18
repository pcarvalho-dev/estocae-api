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

### autenticação no swagger

> cole o link no seu navergador após a inicialização do docker-compose up --build:
``` shell script
http://127.0.0.1:4000/docs#/ 
```

> click no botão Authorize

![Captura de tela de 2022-08-03 10-31-30](https://user-images.githubusercontent.com/50378596/182626006-7c4064d6-5446-44c3-ae1a-7597ddf9eb08.png)
<br>

>coloque a key informada a baixo no "api_key (apiKey)":

b2ZlcnRhcGxheXVzZXI6b2ZlcnRhcGxheXBhc3N3b3Jk


![Captura de tela de 2022-08-03 10-31-45](https://user-images.githubusercontent.com/50378596/182636158-bf5ea867-5b04-4f35-a2c4-3b7e1e7d869d.png)
<br>

>click em authorize

![Captura de tela de 2022-08-03 11-41-32](https://user-images.githubusercontent.com/50378596/182647536-efc0fd73-3300-4b67-ae16-18f2c88c40f7.png)
<br>

>Entre na rota Token

![Captura de tela de 2022-08-03 11-40-43](https://user-images.githubusercontent.com/50378596/182647841-db1a977d-41a0-4a40-86fe-a008161f52c2.png)
<br>

>click em Try it out

![Captura de tela de 2022-08-03 11-42-01](https://user-images.githubusercontent.com/50378596/182648173-a65d7154-4695-4741-b632-e0dcfcf46d2a.png)
<br>

>click em execute

![Captura de tela de 2022-08-03 11-42-16](https://user-images.githubusercontent.com/50378596/182648375-147dd514-e345-4caa-949e-ea0c38b80e32.png)
<br>

>copie o jwt sem as "aspas" gerado pelo rota token e cole no jwt  (http, Bearer). Pronto já pode visualizar as rotas

![Captura de tela de 2022-08-03 11-46-00](https://user-images.githubusercontent.com/50378596/182648489-11eca162-3147-438a-95de-69dbcbe47ee5.png)
<br>


### Relatorio de tests

docker-compose exec api python -m pytest "tests" -p no:warnings --cov="app"

