from jina import Executor, DocumentArray, requests
import subprocess


class PandocTextExtractor(Executor):
    """PandocExtractor uses pandoc to extract text from different filetypes and return that text as a Document"""
    @requests
    def extract_text(self, docs: DocumentArray, **kwargs):
        docs.apply(self._convert_file_to_text)

    def _convert_file_to_text(self, doc):
        command = f"pandoc {doc.uri} --to plain"

        try:
            doc.text = subprocess.getoutput(command)
        except:
            doc.text = "PandocTextExtractor failed to extract text"

        return doc

