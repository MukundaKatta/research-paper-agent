"""Tests for ResearchPaperAgent."""
from src.core import ResearchPaperAgent
def test_init(): assert ResearchPaperAgent().get_stats()["ops"] == 0
def test_op(): c = ResearchPaperAgent(); c.search(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = ResearchPaperAgent(); [c.search() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = ResearchPaperAgent(); c.search(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = ResearchPaperAgent(); r = c.search(); assert r["service"] == "research-paper-agent"
