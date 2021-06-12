from hanlp.utils.rules import split_sentence


class TokResource:
    def __init__(self, HanLP) -> None:
        self.HanLP = HanLP
        self.long_sentence_words = 20

    def on_post(self, req, res):
        text = req.media.get("text")
        sentences = []

        if isinstance(text, str):
            self.add_to_sentences(sentences, text)
        elif isinstance(text, list):
            for item in text:
                self.add_to_sentences(sentences, item)

        res.media = self.HanLP(sentences, tasks="tok")

    def add_to_sentences(self, sentences, text):
        if len(text) < self.long_sentence_words:
            sentences.append(text)
        else:
            for s in split_sentence(text):
                sentences.append(s)
