import random

class MutationEngine:
    def __init__(self):
        self.mutation_count = 0
    
    def generate_mutation(self, threat):
        """Generate AI-driven mutation response to threat"""
        self.mutation_count += 1
        
        threat_type = threat.get("type", "UNKNOWN")
        confidence = threat.get("confidence", 0.5)
        
        mutations = {
            "SQL_INJECTION": {
                "action": "block_ip",
                "reason": "SQL injection pattern detected - blocking source IP",
                "confidence": confidence,
                "patch": {
                    "type": "input_validation",
                    "rule": "sanitize_sql_input",
                    "implementation": "Add parameterized queries"
                }
            },
            "DDOS_ATTEMPT": {
                "action": "rate_limit",
                "reason": "Excessive requests detected - applying rate limiting",
                "confidence": confidence,
                "patch": {
                    "type": "rate_limiter",
                    "rule": "max_10_requests_per_10_seconds",
                    "implementation": "Token bucket algorithm"
                }
            },
            "SUSPICIOUS_PATTERN": {
                "action": "monitor",
                "reason": "Suspicious pattern detected - enhanced monitoring",
                "confidence": confidence,
                "patch": {
                    "type": "logging",
                    "rule": "log_all_requests_from_ip",
                    "implementation": "Increase logging verbosity"
                }
            }
        }
        
        mutation = mutations.get(threat_type, {
            "action": "alert",
            "reason": "Unknown threat pattern",
            "confidence": 0.5,
            "patch": {"type": "generic", "rule": "investigate"}
        })
        
        # Add AI-like reasoning
        mutation["ai_analysis"] = self._generate_ai_insight(threat_type)
        mutation["mutation_id"] = f"MUT-{self.mutation_count:04d}"
        
        return mutation
    
    def _generate_ai_insight(self, threat_type):
        """Simulate AI-generated insights"""
        insights = {
            "SQL_INJECTION": [
                "Pattern matches known SQLi attack vectors",
                "Attacker attempting database enumeration",
                "Recommend immediate IP blocking and input sanitization"
            ],
            "DDOS_ATTEMPT": [
                "Traffic pattern indicates automated bot",
                "Request rate exceeds normal user behavior by 400%",
                "Recommend adaptive rate limiting"
            ],
            "SUSPICIOUS_PATTERN": [
                "Payload contains potentially malicious code",
                "Pattern similarity to known exploit attempts: 78%",
                "Recommend enhanced monitoring"
            ]
        }
        
        return random.choice(insights.get(threat_type, ["Unknown threat pattern detected"]))
