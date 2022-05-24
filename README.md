# PanDocTextExtractor

PandocTextExtractor uses [pandoc](https://pandoc.org) to extract text from different filetypes and store it in `doc.text`

## Usage

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://PandocTextExtractor')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://PandocTextExtractor')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
