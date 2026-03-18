"""CLI for research-paper-agent."""
import sys, json, argparse
from .core import ResearchPaperAgent

def main():
    parser = argparse.ArgumentParser(description="AI agent that reads, summarizes, and synthesizes research papers")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = ResearchPaperAgent()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.search(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"research-paper-agent v0.1.0 — AI agent that reads, summarizes, and synthesizes research papers")

if __name__ == "__main__":
    main()
