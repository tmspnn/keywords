import falcon
import hanlp

from wsgiref.simple_server import make_server

from resources.RootResource import RootResource
from resources.TokResource import TokResource
from dict.dict_force import dict_force

HanLP = hanlp.load(
    hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)

HanLP["tok/fine"].dict_force = dict_force


app = falcon.App()

root_resource = RootResource()
tok_resource = TokResource(HanLP)

app.add_route("/", root_resource)
app.add_route("/tokenization", tok_resource)

if __name__ == "__main__":
    port = 8000
    with make_server("", port, app) as httpd:
        print("Serving on %s..." % port)
        httpd.serve_forever()
