# PanDocTextExtractor

PanDocExtractor uses pandoc to extract text from different filetypes and return that text as a Document

## Usage

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://PanDocTextExtractor')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://PanDocTextExtractor')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
