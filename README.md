# celery-pool-asyncio-example
This repository contain a minimal working example of [celery-pool-asyncio](https://github.com/kai3341/celery-pool-asyncio) to work Celery pool to run coroutine tasks. Same code base can be use too for testing redbeat scheduler (Which is not supporting coroutine tasks at this moment).


## Execute below commands to run this example code
To run celery worker
```sh
$ celery -A task worker -l debug -P celery_pool_asyncio:TaskPool
```

To run celery beat
```sh
$ celery beat -A task -l debug
```
Note: In order to run this sample code with [Redbeat Scheduler](https://github.com/sibson/redbeat), change scheduler configuration in config.py to redbeat.RedBeatScheduler
