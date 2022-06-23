import time
import requests
import json
from datetime import datetime
import uuid
import re
import os

from Utils import Utils

class API:

    def __init__(self):
        pass
    
    def get_query(self, query, per_page, cursor):
        query = "https://api.openalex.org/" + query 
        query += "&per_page=" + str(per_page)
        query +=  "&cursor="+cursor
        return query

    def run(self, query, per_page=200, concepts=False):

        if not concepts:
            cur = "*"

            page_count = 0 

            folder = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

            if not os.path.exists(folder): os.makedirs(folder)

            while cur:

                api = self.get_query(query, per_page, cur)                
                data = requests.get(api).json()
                results = data["results"]
                cur = data["meta"]["next_cursor"]

                with open(os.path.join(folder+"/results.json"), "a+") as f:
                    for result in results:
                        f.write(json.dumps(result) + "\n")
                
                page_count = page_count+1

                print("Fetched " + str(page_count*per_page) + "/" + str(data["meta"]["count"]))
                time.sleep(1)
        else:
            query = self.getResponse("concepts", _values=[query])
            data = requests.get(query).json()
            return data