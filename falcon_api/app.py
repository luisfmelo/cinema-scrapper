import json

import falcon


class MainHandler:
    """docstring for MainHandler"""

    def on_get(self, req, resp):
        try:
            data = "Hello Welcome to Docker -> Nginx -> Gunicorn -> Falcon"
            resp.body = json.dumps({'code': 200, 'detail': data})
        except Exception as e:
            print(e)
            resp.body = json.dumps({'code': 400, 'detail': 'ERROR'})


api = falcon.API()

api.add_route('/', MainHandler())

