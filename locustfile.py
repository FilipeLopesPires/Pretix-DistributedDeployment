
from locust import * #HttpLocust, TaskSet, between, task

class UserBehavior(TaskSet):
    
    totalPurchaseAttempts = 0
    
    maxPurchaseAttempts = 800

    #def on_start(self):
    #    pass

    #def on_stop(self):
    #    pass

    @task
    def get(self):
        
        if UserBehavior.totalPurchaseAttempts == UserBehavior.maxPurchaseAttempts:
            return
        
        UserBehavior.totalPurchaseAttempts+=1
        print("Total Purchase Attempts: "+str(UserBehavior.totalPurchaseAttempts))
        
        r = [
            [
                "http://localhost:8888/ws/ws2020/",
                "http://localhost:8888/static/CACHE/css/e69921ab2b6e.css",
                "http://localhost:8888/media/pub/ws/ws2020/presale.a37ec5cea5997d87.css",
                "http://localhost:8888/static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
                "http://localhost:8888/static/jsi18n/en/djangojs.366c16383242.js",
                "http://localhost:8888/static/fonts/opensans_regular_macroman/OpenSans-Regular-webfont.79515ad07889.woff",
                "http://localhost:8888/static/fontawesome/fonts/fontawesome-webfont.af7ae505a9ee.woff2",
                "http://localhost:8888/static/fonts/opensans_bold_macroman/OpenSans-Bold-webfont.2e90d5152ce9.woff",
                "http://localhost:8888/static/lightbox/images/prev.84b76dee6b27.png",
                "http://localhost:8888/static/lightbox/images/next.31f15875975a.png",
                "http://localhost:8888/static/lightbox/images/loading.2299ad0b3f63.gif",
                "http://localhost:8888/static/lightbox/images/close.d9d2d0b1308c.png",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png",
            ],
            [
                "http://localhost:8888/ws/ws2020/?require_cookie=true",
                "http://localhost:8888/static/CACHE/css/e69921ab2b6e.css",
                "http://localhost:8888/media/pub/ws/ws2020/presale.a37ec5cea5997d87.css",
                "http://localhost:8888/static/CACHE/js/5b8f603ac609.js",
                "http://localhost:8888/static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
                "http://localhost:8888/static/jsi18n/en/djangojs.366c16383242.js",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png",
                "http://localhost:8888/static/fonts/opensans_italic_macroman/OpenSans-Italic-webfont.f42641eed834.woff"
            ],
            [
                "http://localhost:8888/ws/ws2020/checkout/start",
                "http://localhost:8888/ws/ws2020/checkout/questions/",
                "http://localhost:8888/static/CACHE/css/e69921ab2b6e.css",
                "http://localhost:8888/media/pub/ws/ws2020/presale.a37ec5cea5997d87.css",
                "http://localhost:8888/static/CACHE/js/5b8f603ac609.js",
                "http://localhost:8888/static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
                "http://localhost:8888/static/jsi18n/en/djangojs.366c16383242.js",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png"
            ],
            [
                #"http://localhost:8888/ws/ws2020/checkout/questions/", # post
                "http://localhost:8888/ws/ws2020/checkout/payment/",
                "http://localhost:8888/static/CACHE/css/e69921ab2b6e.css",
                "http://localhost:8888/media/pub/ws/ws2020/presale.a37ec5cea5997d87.css",
                "http://localhost:8888/static/CACHE/js/5b8f603ac609.js",
                "http://localhost:8888/static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
                "http://localhost:8888/static/jsi18n/en/djangojs.366c16383242.js",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png"
            ],
            [
                #"http://localhost:8888/ws/ws2020/checkout/payment/", # post
                "http://localhost:8888/ws/ws2020/checkout/confirm/",
                "http://localhost:8888/static/CACHE/css/e69921ab2b6e.css",
                "http://localhost:8888/media/pub/ws/ws2020/presale.a37ec5cea5997d87.css",
                "http://localhost:8888/static/CACHE/js/5b8f603ac609.js",
                "http://localhost:8888/static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
                "http://localhost:8888/static/jsi18n/en/djangojs.366c16383242.js",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png"
            ],
            [
                "http://localhost:8888/api/v1/organizers/ws/events/ws2020/orders/", # post
                #"http://localhost:8888/ws/ws2020/order/WBWFT/14xhln2apnqkl1r7/pay/1/complete",
                #"http://localhost:8888/ws/ws2020/order/WBWFT/14xhln2apnqkl1r7/?thanks=yes",
                "http://localhost:8888/static/CACHE/css/e69921ab2b6e.css",
                "http://localhost:8888/media/pub/ws/ws2020/presale.a37ec5cea5997d87.css",
                "http://localhost:8888/static/CACHE/js/5b8f603ac609.js",
                "http://localhost:8888/static/pretixpresale/js/ui/iframe.d76c0dc4351f.js",
                "http://localhost:8888/static/jsi18n/en/djangojs.366c16383242.js",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-194x194.4d77adfe376b.png",
                "http://localhost:8888/static/pretixbase/img/icons/favicon-16x16.ce949675f6e2.png"
            ]
        ]
        
        token = "yesixqytjfmbdqgzn1gkn1xqqxrsbof7frx6eeur4w2toiuqmdglbdn8bzprc4om"
        user_email = 'user'+str(UserBehavior.totalPurchaseAttempts)+'@example.org'
        
        for i in range(0,len(r)):
            for j in range(0,len(r[i])):
                if i==(len(r)-1) and j==0:
                    body = '{"detail":"", "email": "' + user_email + '","locale": "en","sales_channel": "web","invoice_address": {"is_business": "false","company": "Sample company","name_parts": {"full_name": "John Doe"},"street": "Sesam Street 12","zipcode": "12345","city": "Sample City","state": "","internal_reference": "","vat_id": ""},"positions": [{"item": 1,"attendee_name_parts": {"full_name": "Peter"},"answers": [{"question": 1,"answer": "23","options": []}]}] }'
                    self.client.post(r[i][j], headers={"Authorization": "Token " + token, "Content-Type": "application/json"}, data=body)
                self.client.get(r[i][j], headers={"Authorization": "Token " + token})

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

        sites = [
            'http://localhost:8888/t1/v/',
            'http://localhost:8888/t1/v/?require_cookie=true',
            'http://localhost:8888/t1/v/checkout/questions/',
            'http://localhost:8888/t1/v/checkout/payment/',
            'http://localhost:8888/t1/v/checkout/confirm/',
            'http://localhost:8888/t1/v/order/KWYWP/hqogxxc5rnaptrd8/?thanks=yes'
        ]

        for site in sites:
            tab.set_url(site)
            sleep(5)
        
    @seq_task(3)
    def launchBrowser(self):
        os.system("killall brave")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior # UserBehavior # UserBehaviorSequence
    wait_time = between(0.1, 0.9)
