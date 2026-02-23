import re
from datetime import datetime, timedelta
from collections import defaultdict

class ThreatDetector:
    def __init__(self):
        self.blocked_ips = set()
        self.request_history = defaultdict(list)
        
        # SQL Injection patterns
        self.sql_patterns = [
            r"(\bOR\b.*=.*)",
            r"(';.*--)",
            r"(\bUNION\b.*\bSELECT\b)",
            r"(\bDROP\b.*\bTABLE\b)",
            r"(1=1)",
            r"(admin'--)",
        ]
        
        # Suspicious patterns
        self.suspicious_patterns = [
            r"(<script>)",
            r"(\.\.\/)",
            r"(\bexec\b)",
            r"(\bcmd\b)",
        ]
    
    def analyze(self, payload, ip):
        # Check for SQL injection
        for pattern in self.sql_patterns:
            if re.search(pattern, payload, re.IGNORECASE):
                return {
                    "level": "MALICIOUS",
                    "type": "SQL_INJECTION",
                    "pattern": pattern,
                    "confidence": 0.95
                }
        
        # Check for suspicious patterns
        for pattern in self.suspicious_patterns:
            if re.search(pattern, payload, re.IGNORECASE):
                return {
                    "level": "SUSPICIOUS",
                    "type": "SUSPICIOUS_PATTERN",
                    "pattern": pattern,
                    "confidence": 0.7
                }
        
        # Check for DDoS (rate limiting)
        self.request_history[ip].append(datetime.now())
        recent_requests = [
            t for t in self.request_history[ip]
            if datetime.now() - t < timedelta(seconds=10)
        ]
        self.request_history[ip] = recent_requests
        
        if len(recent_requests) > 20:
            return {
                "level": "MALICIOUS",
                "type": "DDOS_ATTEMPT",
                "pattern": "rate_limit_exceeded",
                "confidence": 0.9
            }
        
        return {
            "level": "NORMAL",
            "type": "CLEAN",
            "confidence": 1.0
        }
    
    def block_ip(self, ip):
        self.blocked_ips.add(ip)
    
    def is_blocked(self, ip):
        return ip in self.blocked_ips
