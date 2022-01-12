class Classifier:

    def __init__(self, language: str) -> None:
        self.language = language
        pass

    def extract_intent(self, query: str) -> str:
        raise NotImplementedError
