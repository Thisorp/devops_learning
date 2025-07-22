from flask import Flask
import redis
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'Hello! This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
