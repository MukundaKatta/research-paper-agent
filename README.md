# research-paper-agent

**AI agent that reads, summarizes, and synthesizes research papers**

![Build](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-proprietary-red)

## Install
```bash
pip install -e ".[dev]"
```

## Quick Start
```python
from src.core import ResearchPaperAgent
 instance = ResearchPaperAgent()
r = instance.search(input="test")
```

## CLI
```bash
python -m src status
python -m src run --input "data"
```

## API
| Method | Description |
|--------|-------------|
| `search()` | Search |
| `index()` | Index |
| `rank()` | Rank |
| `filter()` | Filter |
| `get_suggestions()` | Get suggestions |
| `export_results()` | Export results |
| `get_stats()` | Get stats |
| `reset()` | Reset |

## Test
```bash
pytest tests/ -v
```

