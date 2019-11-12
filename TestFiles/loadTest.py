from locust import HttpLocust


class LoadTest(HttpLocust):
    min_wait = 2000
    max_wait = 10000
