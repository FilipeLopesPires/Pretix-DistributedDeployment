
from locust import * #HttpLocust, TaskSet, between, task
from chromote import *

import os
from time import sleep

class UserBehavior(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def get(self):
        self.client.get("/api/v1/organizers/t1/events/t1/orders/", headers={
                        "Authorization": "Token sjf0oyi4f5bugmduxsajiw5kkhw2dm0xb7acqftim5p9vc87ath6dyanw81xvtk0"})

class UserBehaviorSequence(TaskSequence):
    
    @seq_task(1)
    def launchBrowser(self):
        os.system("brave https://duckduckgo.com/ --headless --remote-debugging-port=9222")
    
    @seq_task(2)
    def accessPretix(self):
        chrome = Chromote()
        print(chrome)

        tab = chrome.tabs[0]
        print(tab)

        '''
        sites = [
            'https://github.com',
            'http://stackoverflow.com',
        ]

        for site in sites:
            tab.set_url(site)
            sleep(5)
        '''
        
    @seq_task(3)
    def launchBrowser(self):
        os.system("killall brave")

class WebsiteUser(HttpLocust):
    task_set = UserBehaviorSequence #UserBehavior
    wait_time = between(0.1, 0.9)
