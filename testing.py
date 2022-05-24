from executor import PandocTextExtractor
from docarray import Document, DocumentArray

docs = DocumentArray(
    [
        Document(uri="data/word.docx"),
    ]
)

e = PandocTextExtractor()

e.extract_text(docs)

print(docs[0].text)
