from app.agents.tools import search_library
from app.data.sample_documents import DOCUMENTS

def test_library_contains_healthcare_documents():
    assert len(DOCUMENTS) >= 3

def test_search_library_returns_matching_document():
    result = search_library("medical consultation symptoms medicines")
    assert "consultation" in result.lower() or "patient" in result.lower()

def test_search_library_reports_no_match():
    result = search_library("zzzxxyyqqv randomterm")
    assert "no matching passages" in result.lower()
