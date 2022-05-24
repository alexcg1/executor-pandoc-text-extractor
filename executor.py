from jina import Executor, DocumentArray, requests
import subprocess


class PanDocTextExtractor(Executor):
    """PanDocExtractor uses pandoc to extract text from different filetypes and return that text as a Document"""
    @requests
    def extract_text(self, docs: DocumentArray, **kwargs):
        docs.apply(self._convert_file_to_text)

    def _convert_file_to_text(self, doc):
        doc.text = subprocess.getoutput(["pandoc", doc.uri, "--to", "plain"])
        return doc

