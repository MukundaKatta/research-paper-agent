"""Basic usage example for research-paper-agent."""
from src.core import ResearchPaperAgent

def main():
    instance = ResearchPaperAgent(config={"verbose": True})

    print("=== research-paper-agent Example ===\n")

    # Run primary operation
    result = instance.search(input="example data", mode="demo")
    print(f"Result: {result}")

    # Run multiple operations
    ops = ["search", "index", "rank]
    for op in ops:
        r = getattr(instance, op)(source="example")
        print(f"  {op}: {"✓" if r.get("ok") else "✗"}")

    # Check stats
    print(f"\nStats: {instance.get_stats()}")

if __name__ == "__main__":
    main()
