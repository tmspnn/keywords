from hanlp.utils.rules import split_sentence


class TokResource:
    def __init__(self, HanLP) -> None:
        self.HanLP = HanLP

    def on_post(self, req, res):
        text = req.media.get("text")
        result = {}

        if isinstance(text, str):
            sentences = split_sentence(text)
            result = self.HanLP(sentences, tasks="tok")
        elif isinstance(text, list):
            result = self.HanLP(text, tasks="tok")

        res.media = result
