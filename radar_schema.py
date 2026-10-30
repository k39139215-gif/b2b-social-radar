"""
B2B Social Intent Radar - Data Models & Scoring Schema
======================================================
Copyright (c) 2026 Kartik. All rights reserved.
[PROPRIETARY & CONFIDENTIAL - SHOWCASE EDITION]
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class IntentLead:
    id: str
    platform: str # 'reddit' | 'twitter' | 'linkedin' | 'producthunt'
    url: str
    author: str
    title: str
    body_snippet: str
    matched_signals: List[str]
    intent_score: float # 0.0 to 100.0
    discovered_at: str
    company_domain: Optional[str] = None
    industry_category: Optional[str] = None
    recommended_action: str = "manual_review"

@dataclass
class PlatformScanConfig:
    platform_name: str
    enabled: bool
    poll_interval_seconds: int
    rate_limit_rpm: int
    target_channels: List[str]
