# Research Paper Agent

AI research assistant — find papers, generate literature reviews

## Features

- Analysis - Gap Identifier
Analysis - Literature Review
Api
Search - Arxiv
Search - Pubmed
Search - Semantic Scholar
Visualization - Citation Network

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Key Dependencies:** pydantic,fastapi,uvicorn,anthropic,openai,numpy
- **Containerization:** Docker + Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

### Installation

```bash
git clone https://github.com/MukundaKatta/research-paper-agent.git
cd research-paper-agent
pip install -r requirements.txt
```

### Running

```bash
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up
```

## Project Structure

```
research-paper-agent/
├── src/           # Source code
├── tests/         # Test suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## License

MIT
