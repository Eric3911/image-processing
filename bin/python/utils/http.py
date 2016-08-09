__author__ = 'feng'
import requests
import json
import time
import hashlib
import os
import base64

class Http((object)):
    def __init__(self):
        self.IMAGE_FILE_NOT_EXISTS = -1
        self.IMAGE_NETWORK_ERROR = -2
        self.IMAGE_PARAMS_ERROR = -3
        self.PERSON_ID_EMPTY = -4
        self.GROUP_ID_EMPTY  = -5
        self.GROUP_IDS_EMPTY = -6
        self.IMAGES_EMPTY    = -7
        self.FACE_IDS_EMPTY  = -8
        self.FACE_ID_EMPTY   = -9
        self.LIST_TYPE_INVALID = -10
        self.IMAGE_PATH_EMPTY = -11

        self.EXPIRED_SECONDS = 2592000
    def post(self, url, data):
        req_type = 'imageidentify'
        headers = self.get_headers(req_type)
        r = {}
        # print json.dumps(data)
        try:
            r = requests.post(url, headers=headers, data=json.dumps(data))
            if r.status_code != 200:
                return {'httpcode': r.status_code, 'errorcode': '', 'errormsg': '', "session_id": '', "image_id": '',
                        "image_height": 0, "image_width": 0, "face": [{}]}
            ret = r.json()

        except Exception as e:
            return {'httpcode': 0, 'errorcode': "", 'errormsg': str(e), "session_id": '',
                    "image_id": '', "image_height": 0, "image_width": 0, "face": [{}]}

        return ret

    def get_headers(self, req_type):


        headers = {
            'Content-Type': 'text/json'
        }

        return headers

    def detect(self,image_path):
        m2 = hashlib.md5()
        t = str(int(time.time()))
        t = "1470705185"
        #41e857576c18f3692b9bff75e7059148
        #1470705185
        #mysql ae6e5fbc1ea6b59c17876cad24a40ea9

        # print t
        m2.update(t+"N6AG2WHLH74S5WC5")
        # print m2.hexdigest()
        sign = m2.hexdigest()
        print sign
        filepath = os.path.abspath(image_path)
        if not os.path.exists(filepath):
            print {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "session_id":'', "image_id":'', "image_height":0, "image_width":0, "face":[{}]}
            return
        base64Img = base64.b64encode(open(filepath, 'rb').read()).rstrip()

        data = {
            "appid": "youyuan",
            "sign": sign,
            "timestamp": t,
            "base64": base64Img
        }
        # print data
        # res = self.post('http://localhost:3002/detect', data)
        res = self.post('http://180.76.143.82:3002/detect', data)
        print res

        # print res['results']
        # print res['retmsg']
if __name__ == '__main__':
    h = Http()
    # h.detect("../../../public/images/p3.jpg")
    h.detect("../../../public/images/ln.jpg")
    # h.detect("/Users/fengxuting/Downloads/photo/photo_pass/photo_pass/1464318494483A9B1A59.jpg")
    # h.detect("/Users/fengxuting/Downloads/photo/photo_pass/photo_pass/1464318775245A552D29.jpg")
