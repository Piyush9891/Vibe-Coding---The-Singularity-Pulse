from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uvicorn
from detector import ThreatDetector
from mutation_engine import MutationEngine
from honeypot import Honeypot
import json

app = FastAPI(title="Project Chimera")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
detector = ThreatDetector()
mutation_engine = MutationEngine()
honeypot = Honeypot()

# System state
system_state = {
    "health": 100,
    "threat_level": "NORMAL",
    "total_requests": 0,
    "attacks_blocked": 0,
    "mutations": []
}

@app.get("/status")
async def get_status():
    return {
        **system_state,
        "logs": honeypot.get_recent_logs(10),
        "active_blocks": list(detector.blocked_ips)
    }

@app.post("/request")
async def process_request(request: Request):
    body = await request.json()
    client_ip = body.get("ip", "unknown")
    payload = body.get("payload", "")
    
    system_state["total_requests"] += 1
    
    # Check if IP is blocked
    if detector.is_blocked(client_ip):
        honeypot.log_attack(client_ip, "BLOCKED", "IP previously blocked")
        return {"status": "blocked", "redirect": honeypot.get_fake_endpoint()}
    
    # Detect threat
    threat = detector.analyze(payload, client_ip)
    
    # Log the request
    honeypot.log_request(client_ip, payload, threat["level"])
    
    if threat["level"] == "MALICIOUS":
        system_state["attacks_blocked"] += 1
        system_state["health"] = max(0, system_state["health"] - 10)
        system_state["threat_level"] = "CRITICAL"
        
        # Trigger mutation
        mutation = mutation_engine.generate_mutation(threat)
        system_state["mutations"].append({
            "timestamp": datetime.now().isoformat(),
            "mutation": mutation
        })
        
        # Apply mutation (block IP)
        if mutation["action"] == "block_ip":
            detector.block_ip(client_ip)
        
        return {
            "status": "threat_detected",
            "threat": threat,
            "mutation": mutation,
            "redirect": honeypot.get_fake_endpoint()
        }
    
    elif threat["level"] == "SUSPICIOUS":
        system_state["health"] = max(0, system_state["health"] - 5)
        system_state["threat_level"] = "ELEVATED"
    else:
        system_state["health"] = min(100, system_state["health"] + 1)
        system_state["threat_level"] = "NORMAL"
    
    return {"status": "ok", "threat": threat}

@app.get("/logs")
async def get_logs():
    return honeypot.get_all_logs()

@app.post("/simulate-attack")
async def simulate_attack(request: Request):
    body = await request.json()
    attack_type = body.get("type", "sql_injection")
    
    from attacker_simulator import AttackerSimulator
    simulator = AttackerSimulator()
    
    results = []
    if attack_type == "sql_injection":
        results = simulator.sql_injection_attack()
    elif attack_type == "ddos":
        results = simulator.ddos_attack()
    elif attack_type == "mixed":
        results = simulator.mixed_attack()
    
    return {"results": results, "count": len(results)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
