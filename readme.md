* https://testdriven.io/courses/flask-celery/intro/
# Simple Test
Let's test things out by entering the Flask shell of the running web service:
```
docker-compose exec web flask shell
```
Then, run the following code:
```
>>> from project.users.tasks import divide
>>>
>>> divide.delay(1, 2)
<AsyncResult: d988f2c1-8b86-441f-a327-16ea2926c150>
```
Take note of the task ID (d988f2c1-8b86-441f-a327-16ea2926c150 in the above case).

Open a new terminal window, navigate to the project directory, and view the logs of the Celery worker:
```
docker-compose logs celery_worker
```
You should see something similar to:
```
celery_worker_1  | [2022-12-17 08:23:02,702: INFO/MainProcess] Task project.users.tasks.divide[d988f2c1-8b86-441f-a327-16ea2926c150] received
celery_worker_1  | [2022-12-17 08:23:07,712: INFO/ForkPoolWorker-8] Task project.users.tasks.divide[d988f2c1-8b86-441f-a327-16ea2926c150] succeeded in 5.006834200001322s: 0.5
```
In the first window, exit from the shell.

Now, let's enter shell of the redis service:

$ docker-compose exec redis sh
We used sh since bash is not available in this container.

Next, using the task ID from above, let's see the task result directly from Redis:
```
redis-cli
127.0.0.1:6379> MGET celery-task-meta-d988f2c1-8b86-441f-a327-16ea2926c150
1) "{\"status\": \"SUCCESS\", \"result\": 0.5, \"traceback\": null, \"children\": [], \"date_done\": \"2022-12-17T08:23:07.706892\", \"task_id\": \"d988f2c1-8b86-441f-a327-16ea2926c150\"}"
```
Make sure you can see the result in the Flower Dashboard as well.

# Useful Commands
To enter the shell of a specific container that's up and running, run the following command:
```
docker-compose exec <service-name> bash

# for example:
# docker-compose exec web bash
```
If you want to run a command against a new container that's not currently running, run:
```
docker-compose run --rm web bash
```
The --rm option tells docker to delete the container after you exit the bash shell.