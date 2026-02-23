import requests
import random
import time

class AttackerSimulator:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.attack_ips = [f"192.168.1.{i}" for i in range(100, 110)]
    
    def sql_injection_attack(self):
        """Simulate SQL injection attacks"""
        payloads = [
            "' OR '1'='1",
            "admin'--",
            "1' UNION SELECT * FROM users--",
            "'; DROP TABLE users--",
            "1=1",
        ]
        
        results = []
        for payload in payloads:
            try:
                response = requests.post(
                    f"{self.base_url}/request",
                    json={
                        "ip": random.choice(self.attack_ips),
                        "payload": payload
                    },
                    timeout=5
                )
                results.append(response.json())
            except Exception as e:
                results.append({"error": str(e)})
        
        return results
    
    def ddos_attack(self):
        """Simulate DDoS attack"""
        results = []
        attacker_ip = random.choice(self.attack_ips)
        
        for i in range(25):
            try:
                response = requests.post(
                    f"{self.base_url}/request",
                    json={
                        "ip": attacker_ip,
                        "payload": f"request_{i}"
                    },
                    timeout=5
                )
                results.append(response.json())
            except Exception as e:
                results.append({"error": str(e)})
        
        return results
    
    def mixed_attack(self):
        """Simulate mixed attack patterns"""
        results = []
        results.extend(self.sql_injection_attack()[:2])
        time.sleep(0.5)
        results.extend(self.ddos_attack()[:10])
        return results
