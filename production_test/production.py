import time
from locust import HttpUser, TaskSet, task, between, LoadTestShape
import csv
import math

# Source: https://thilani-mahaarachchi.medium.com/generating-custom-loads-with-locust-cffe72078f6b

class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/")

class User(HttpUser):
    wait_time = between(0.1, 0.3)
    tasks = {UserTasks}
    host = "http://127.0.0.1"

class CustomShape(LoadTestShape):
    stages = []

    with open("./production_test/test2900.csv", "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        for row in reader_variable:
            stages.append({"duration": (int(row[1])-39600)//300, "users": math.ceil(float(row[3])), "spawn_rate": 25})
        print(stages)

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
