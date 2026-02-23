from datetime import datetime
import random

class Honeypot:
    def __init__(self):
        self.logs = []
        self.fake_endpoints = [
            "/admin/secret",
            "/api/v1/users/all",
            "/database/backup",
            "/config/passwords",
            "/internal/keys"
        ]
    
    def log_request(self, ip, payload, threat_level):
        """Log all requests"""
        self.logs.append({
            "timestamp": datetime.now().isoformat(),
            "ip": ip,
            "payload": payload[:100],  # Truncate long payloads
            "threat_level": threat_level,
            "type": "request"
        })
    
    def log_attack(self, ip, attack_type, details):
        """Log detected attacks"""
        self.logs.append({
            "timestamp": datetime.now().isoformat(),
            "ip": ip,
            "attack_type": attack_type,
            "details": details,
            "threat_level": "MALICIOUS",
            "type": "attack"
        })
    
    def get_fake_endpoint(self):
        """Return a fake endpoint to redirect attackers"""
        return random.choice(self.fake_endpoints)
    
    def get_recent_logs(self, count=10):
        """Get most recent logs"""
        return self.logs[-count:] if self.logs else []
    
    def get_all_logs(self):
        """Get all logs"""
        return self.logs
