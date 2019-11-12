from locust import TaskSet, task
from loadTest import LoadTest


@task(1)
def post_auth(self):
    payload = """{"username": "admin", "password": "password123"}"""
    response = self.client.post("/auth", payload)
    print(response)


class Behavior(TaskSet):

    def on_start(self):
        self.client.headers["Content-Type"] = "application/json"
        self.client.headers["Accept"] = "application/json"

    tasks = [post_auth]


class AuthTest(LoadTest):
    task_set = Behavior
