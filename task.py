import config

from celery import Celery
from datetime import datetime
import random


app = Celery('test')
app.config_from_object(config)


@app.task
async def add_task(a, b):

    try:
        x = random.randint(2,200)
        y = random.randint(3,500)
        result = x+y
        print("Sum is:"+str(result))
    except Exception as e:
        raise
    return u'add task'


@app.task
async def test(a,b):
    print("Current time:"+str(datetime.now()))
    return u'time test'
