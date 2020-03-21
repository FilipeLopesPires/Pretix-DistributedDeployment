from locust import HttpLocust, TaskSet, between, task


class UserBehavior(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def get(self):
        self.client.get("/api/v1/organizers/t1/events/t1/orders/", headers={
                        "Authorization": "Token sjf0oyi4f5bugmduxsajiw5kkhw2dm0xb7acqftim5p9vc87ath6dyanw81xvtk0"})


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
