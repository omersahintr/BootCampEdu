
import threading
import requests as req
import time

## Don't use threading for this function:
def get_web(urls):
    start_time = time.time()
    json_data = []
    for url in urls:
        json_data.append(req.get(url).json())

    end_time = time.time()
    dif_time = end_time - start_time
    print(f"Time: {dif_time}")
    return json_data


urls = ['https://postman-echo.com/delay/2'] * 8 # 8 times request delay 2 seconds

#get_web(urls) # Time: 24.787731170654297 seconds
####################################################



## Use threading for this class and function:
class ThreadingOptimizer(threading.Thread):
    json_data = []

    def __init__(self,url): ## for inheritance
        super().__init__()
        self.url = url

    def run(self):
        response = req.get(self.url)
        self.json_data.append(response.json())
        return self.json_data
    

def get_web_thread(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        t = ThreadingOptimizer(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(t)

    end_time = time.time()
    dif_time = end_time - start_time
    print(f"Time: {dif_time}")

urls = ['https://postman-echo.com/delay/2'] * 8 # 8 times request delay 2 seconds
    
get_web_thread(urls) #####
                    # <ThreadingOptimizer(Thread-1, stopped 123145345273856)>
                    #<ThreadingOptimizer(Thread-2, stopped 123145362063360)>
                    #<ThreadingOptimizer(Thread-3, stopped 123145378852864)>
                    #<ThreadingOptimizer(Thread-4, stopped 123145395642368)>
                    #<ThreadingOptimizer(Thread-5, stopped 123145412431872)>
                    #<ThreadingOptimizer(Thread-6, stopped 123145429221376)>
                    #<ThreadingOptimizer(Thread-7, stopped 123145446010880)>
                    #<ThreadingOptimizer(Thread-8, stopped 123145462800384)>
                    #Time: 4.561605930328369

