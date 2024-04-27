import time
from locust import HttpUser, task, between

# HTTP User is headless "browser" with self.client to generate requests.
class QuickstartUser(HttpUser):

    # Make simulated user wait between 1 and 5 seconds after each task (random)
    wait_time = between(1, 5)

    # A random task
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    # A Random task with weight 3 -- more likely to be picked than hello_world
    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

    # Special method to be called by each simulated user when they start. 
    # Use on_stop to be called when user stop.
    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})