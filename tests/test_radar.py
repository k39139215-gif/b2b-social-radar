import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from radar_schema import IntentLead, PlatformScanConfig
from radar_engine import SocialIntentRadarEngine, INTENT_SIGNALS

def test_intent_scoring_high_intent():
    """Verifies that high-intent buying signals are correctly scored."""
    engine = SocialIntentRadarEngine(dry_run=True)
    sample_text = "Looking for a highradius alternative for bank reconciliation and cash application."
    score, matched = engine.score_content(sample_text)
    
    assert score >= 70.0
    assert "highradius alternative" in matched
    assert "bank reconciliation" in matched
    assert "cash application" in matched

def test_intent_scoring_zero_intent():
    """Verifies that unrelated casual text scores 0.0."""
    engine = SocialIntentRadarEngine(dry_run=True)
    sample_text = "Beautiful sunset today in San Francisco."
    score, matched = engine.score_content(sample_text)
    
    assert score == 0.0
    assert len(matched) == 0

def test_intent_lead_data_model():
    """Verifies IntentLead data model instantiation and field defaults."""
    lead = IntentLead(
        id="lead_101",
        platform="reddit",
        url="https://reddit.com/r/accounting/123",
        author="cfo_expert",
        title="Automating cash application in NetSuite",
        body_snippet="Need advice on reconciling bank lockboxes faster.",
        matched_signals=["cash application"],
        intent_score=85.0,
        discovered_at="2026-10-31T12:00:00Z"
    )
    assert lead.id == "lead_101"
    assert lead.platform == "reddit"
    assert lead.intent_score == 85.0
    assert lead.recommended_action == "manual_review"

def test_platform_scan_config():
    """Verifies PlatformScanConfig validation."""
    config = PlatformScanConfig(
        platform_name="reddit",
        enabled=True,
        poll_interval_seconds=60,
        rate_limit_rpm=30,
        target_channels=["accounting", "fintech"]
    )
    assert config.platform_name == "reddit"
    assert config.enabled is True
    assert len(config.target_channels) == 2
