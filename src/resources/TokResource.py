from hanlp.utils.rules import split_sentence


class TokResource:
    def __init__(self, HanLP) -> None:
        self.HanLP = HanLP

    def on_post(self, req, res):
        texts = req.media.get("texts")
        result = {}

        if isinstance(texts, str):
            sentences = split_sentence(texts)
            result = self.HanLP(sentences, tasks="tok")
        elif isinstance(texts, list):
            result = self.HanLP(texts, tasks="tok")

        res.media = result
