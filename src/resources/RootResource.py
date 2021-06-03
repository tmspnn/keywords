import falcon


class RootResource:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.media = {"service": "NLP", "version": "1.0.0"}
