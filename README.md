# URL Shortener RESTful API (Django)

URL Shortener is a cloud-enabled, deploy-ready, Django-powered RESTful API.

- Deploy with single docker-compose command
- Handel 300 requests per second
- Light and Fast✨
## Features

- 300 Requests per sec `tested on localhost(i5 8th gen intel processor, ssd hard drive, 8gb ram)`
- Mean latency: 4.4 ms `tested on localhost(i5 8th gen intel processor, ssd hard drive, 8gb ram)`
- Auto delete unused records in database every sunday at 1 am
- Methods: GET & POST
- Redis data caching
- Easy to deploy Docker project
- nginx load balancing
- Get total URL hits
- Lite images `total Size: 549.1MB` 


## Tech

URL Shortener API uses a number of open source/free projects to work properly:
- Django
- Django rest framework
- Nginx
- PostgreSQL
- Redis
- Python >=3.6
- Docker:latest

## Docker Get-Started

URL Shortener is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8000, so change this within the
docker-compose file if necessary.

```sh
git pull https://github.com/dpk-a7/url-shortener.git
```
This will pull the project to your present working directory

Run the below command to start the  URL Shortener service
```sh
cd url-shortener/
docker-compose up -d
```

> Note: For Django Admin page first login to to the container name `url_shortener_app_1` using
(`docker exec -it url_shortener_app_1 bash`) and run `python manage.py createsuperuser` after this you can access admin page at `localhost:8000\shortener\admin`.

Verify the deployment by navigating to your server address in
your preferred browser\postman.
```sh
http:\\localhost:8000\shortener
```

To stop running containers and delete the built images run:
```sh
docker-compose down && \
docker rmi url_shortener_app url_shortener_nginx url_shortener_db_manager
```
# Test images:
#### _Get Method in Browser at `localhost:8000\shortener`_
![http_get](https://raw.githubusercontent.com/dpk-a7/url-shortener/main/images/http_get.png)

#### _POST Method in Browser at `localhost:8000\shortener`_
![http_post](https://raw.githubusercontent.com/dpk-a7/url-shortener/main/images/http_post.png)

#### _POST Method in Postman at `localhost:8000\shortener`_
![postman](https://raw.githubusercontent.com/dpk-a7/url-shortener/main/images/postman.png)

#### _Docker Images `Ignore python, ubuntu images`_
![images](https://raw.githubusercontent.com/dpk-a7/url-shortener/main/images/images.jpg)


#### _Docker processes after `docker-compose up`_
5 Docker containers using default bridge network, nginx port open at `8000`
![ps](https://raw.githubusercontent.com/dpk-a7/url-shortener/main/images/ps.jpg)

#### _Without nginx and redis cache`loadtest -n 100 -k http://localhost:8000/shortener/`_
```cmd
C:\Users\Deepak Avudiappan>loadtest -n 100 -k http://127.0.0.1:8000/shortener/
[Thu Sep 16 2021 16:23:39 GMT+0530 (India Standard Time)] INFO Requests: 0 (0%), requests per second: 0, mean latency: 0 ms
[Thu Sep 16 2021 16:23:44 GMT+0530 (India Standard Time)] INFO Requests: 46 (46%), requests per second: 9, mean latency: 108.4 ms
[Thu Sep 16 2021 16:23:49 GMT+0530 (India Standard Time)] INFO Requests: 87 (87%), requests per second: 8, mean latency: 120.3 ms
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO Target URL:          http://127.0.0.1:8000/shortener/
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO Max requests:        100
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO Concurrency level:   1
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO Agent:               keepalive
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO Completed requests:  100
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO Total errors:        0
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO Total time:          11.0566781 s
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO Requests per second: 9
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO Mean latency:        110.2 ms
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO Percentage of the requests served within a certain time
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO   50%      110 ms
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO   90%      128 ms
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO   95%      185 ms
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO   99%      239 ms
[Thu Sep 16 2021 16:23:50 GMT+0530 (India Standard Time)] INFO  100%      239 ms (longest request)
```

#### _With nginx and redis cache`loadtest -n 100 -k http://localhost:8000/shortener/`_

```cmd
C:\Users\Deepak Avudiappan>loadtest -n 100 -k http://localhost:8000/shortener/
[Fri Sep 17 2021 15:33:53 GMT+0530 (India Standard Time)] INFO Requests: 0 (0%), requests per second: 0, mean latency: 0 ms
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO Target URL:          http://localhost:8000/shortener/
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO Max requests:        100
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO Concurrency level:   1
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO Agent:               keepalive
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO Completed requests:  100
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO Total errors:        0
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO Total time:          0.4462007 s
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO Requests per second: 224
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO Mean latency:        4.4 ms
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO Percentage of the requests served within a certain time
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO   50%      3 ms
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO   90%      4 ms
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO   95%      5 ms
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO   99%      35 ms
[Fri Sep 17 2021 15:33:54 GMT+0530 (India Standard Time)] INFO  100%      35 ms (longest request)
```
## License
MIT
