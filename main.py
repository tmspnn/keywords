from wsgiref.simple_server import make_server
from hanlp.utils.rules import split_sentence

import os
import falcon
import hanlp

HanLP = hanlp.load(
    hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)


class Resource:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.media = {"service": "NLP"}

    def on_post(self, req, res):
        sentences = split_sentence(req.media.get("texts"))
        result = HanLP(sentences)
        res.media = result


app = falcon.App()

resource = Resource()

app.add_route("/", resource)

if __name__ == "__main__":
    PORT = os.getenv("PORT") or 23333
    with make_server("", PORT, app) as httpd:
        print("Serving on %s 8000..." % PORT)
        httpd.serve_forever()
