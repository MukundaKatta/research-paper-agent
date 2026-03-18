"""Tests for ResearchAgent."""
import pytest
from src.researchagent import ResearchAgent

def test_init():
    obj = ResearchAgent()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = ResearchAgent()
    result = obj.search_papers(input="test")
    assert result["processed"] is True
    assert result["operation"] == "search_papers"

def test_multiple_ops():
    obj = ResearchAgent()
    for m in ['search_papers', 'fetch_paper', 'summarize']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = ResearchAgent()
    r1 = obj.search_papers(key="same")
    r2 = obj.search_papers(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = ResearchAgent()
    obj.search_papers()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = ResearchAgent()
    obj.search_papers(x=1)
    obj.fetch_paper(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
