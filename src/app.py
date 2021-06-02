from wsgiref.simple_server import make_server
from hanlp.utils.rules import split_sentence

import falcon
import hanlp

HanLP = hanlp.load(
    hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)

tok = HanLP["tok/fine"]

tok.dict_force = {
    "和服务": ["和", "服务"]
}


class Resource:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.media = {"service": "NLP"}

    def on_post(self, req, res):
        sentences = split_sentence(req.media.get("texts"))
        result = HanLP(sentences, tasks="tok")
        res.media = result


app = falcon.App()

resource = Resource()

app.add_route("/", resource)

if __name__ == "__main__":
    port = 8000
    with make_server("", port, app) as httpd:
        print("Serving on %s..." % port)
        httpd.serve_forever()
