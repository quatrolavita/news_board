## DevelopsToday Test Task

This application implement simple news board API

# HOW TO START?

1. Clone git repo 

2. Install docker [tutorial](https://docs.docker.com/engine/install/ubuntu/)
3. `sudo docker-compose build `
4. `sudo docker-compose up`
5.  Than you can follow `http://localhost:8000/singup` and create account
6.  Than follow `http://localhost:8000/token` and create `access_token` every request need `Authorization` header with value : `Bearer <access_token>`

If you want to restart app just enter commands below:

```
sudo docker-compose down
sudo docker-compose up
```

#HOW TO TEST?

You cant explore postman collection https://documenter.getpostman.com/view/11675404/TVK5eNEB#a6622082-4900-4dbe-9f28-968e5faad467

Set up `Production base url` enviroment varible. It allow you to use test access token. 

Acording `Postman Collection` you can test any endpoint.

Test user credentials: `username`: `test` `password`: `testpassword`


This app is deployed on heroku https://floating-reef-25872.herokuapp.com/





