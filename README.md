# 🧬 PROJECT CHIMERA: The Digital Immune System

<div align="center">

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Node](https://img.shields.io/badge/node-16+-green.svg)
![React](https://img.shields.io/badge/react-18.2-61dafb.svg)
![FastAPI](https://img.shields.io/badge/fastapi-0.104-009688.svg)

**An AI-driven cybersecurity system that mimics a biological immune system**

*Traditional security is a wall; Chimera is an immune system. It detects, adapts, and evolves in real-time.*

[Features](#-features) • [Quick Start](#-quick-start) • [Demo](#-demo-mode) • [Documentation](#-documentation) • [Architecture](#-architecture)

</div>

---

## 🎯 The Concept

Just as the human immune system learns and adapts to new threats, Project Chimera creates a living defense system that:

- 🔍 **Detects** threats in real-time using pattern recognition
- 🧠 **Analyzes** attack vectors with AI-driven intelligence
- 🧬 **Mutates** defenses dynamically to counter new threats
- 📊 **Visualizes** security as a living, breathing organism

## ✨ Features

### 🛡️ Core Security Features

- **Threat Detection Engine**
  - SQL Injection pattern matching
  - DDoS detection via rate limiting
  - Suspicious payload analysis
  - Multi-level threat classification (NORMAL/SUSPICIOUS/MALICIOUS)

- **AI Mutation Engine**
  - Adaptive response generation
  - Automatic IP blocking
  - Dynamic rate limiting
  - Input validation suggestions
  - Confidence scoring system

- **Honeypot System**
  - Attacker redirection to fake endpoints
  - Complete activity logging
  - IP tracking and audit trails
  - Behavioral analysis

- **Attack Simulator**
  - Built-in SQL injection simulation
  - DDoS attack patterns
  - Mixed attack scenarios
  - One-click demo mode

### 🎨 Visualization Features

- **3D Living Cell Metaphor**
  - Real-time Three.js rendering
  - Color-coded health states (Green → Yellow → Red)
  - Particle system for request visualization
  - Dynamic scaling based on system health
  - Smooth 60 FPS animations

- **Live Dashboard**
  - Real-time statistics
  - Attack counter
  - Mutation history
  - Live activity logs
  - Threat level indicators

## 🚀 Quick Start

### Prerequisites

Ensure you have the following installed:
- **Python** 3.8 or higher
- **Node.js** 16 or higher
- **npm** 7 or higher
- **pip** (Python package manager)

### Installation

#### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd project-chimera
```

#### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI server
python main.py
```

✅ Backend will be running at `http://localhost:8000`

#### 3. Frontend Setup

Open a new terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install Node dependencies
npm install

# Start the development server
npm run dev
```

✅ Frontend will be running at `http://localhost:5173`

### Windows Quick Start

Use the provided batch files:
```bash
# Terminal 1
start-backend.bat

# Terminal 2
start-frontend.bat
```

## 🎮 Demo Mode

1. **Open your browser** to `http://localhost:5173`
2. **Observe the healthy system** - Green glowing cell rotating smoothly
3. **Click "SIMULATE ATTACK"** button
4. **Select attack type**:
   - SQL Injection
   - DDoS Attack
   - Mixed Attack
5. **Watch the magic happen**:
   - Cell turns red as threats are detected
   - AI generates mutation responses
   - Logs appear in real-time
   - System adapts and blocks attackers

## 📊 System Components


### Backend (Python/FastAPI)
- `main.py`: API server and request handler
- `detector.py`: Threat detection patterns
- `mutation_engine.py`: AI mutation response generator
- `honeypot.py`: Attack logging and fake endpoints
- `attacker_simulator.py`: Built-in attack simulator

### Frontend (React/Three.js)
- `App.jsx`: Main application
- `Dashboard.jsx`: Stats and controls
- `CellVisualization.jsx`: 3D immune system visualization
- `api.js`: Backend API client

## 🎨 Visual Design

- **Green Cell**: Healthy system (NORMAL)
- **Yellow Cell**: Elevated threat (SUSPICIOUS)
- **Red Cell**: Under attack (CRITICAL)
- **Particles**: Incoming requests
- **Red Particles**: Detected threats

## 🔧 API Endpoints

- `GET /status` - System health and statistics
- `POST /request` - Process incoming request
- `GET /logs` - Retrieve all logs
- `POST /simulate-attack` - Trigger attack simulation

## 🎤 Pitch

"Traditional security is a wall; Chimera is an immune system. It detects, adapts, and evolves in real-time."

## 📝 Technical Stack

- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: React, Vite, Three.js, TailwindCSS
- **Visualization**: Three.js for 3D graphics

## 🏆 Hackathon Ready

This project is designed to be:
- ✅ Runnable in under 5 minutes
- ✅ Visually impressive
- ✅ Demo-ready with built-in attack simulator
- ✅ Simple, readable code
- ✅ Complete with documentation

## 🔮 Future Enhancements

- Real LLM integration (OpenAI API)
- WebSocket for real-time updates
- More attack patterns
- Network traffic visualization
- Export threat reports


## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         Frontend (React + Three.js)     │
│              localhost:5173              │
└────────────────┬────────────────────────┘
                 │ HTTP/JSON
                 │ (CORS enabled)
┌────────────────▼────────────────────────┐
│       Backend (Python + FastAPI)        │
│              localhost:8000              │
│                                          │
│  ┌──────────┐  ┌──────────┐  ┌────────┐│
│  │Detector  │  │Mutation  │  │Honeypot││
│  │ Engine   │  │ Engine   │  │ System ││
│  └──────────┘  └──────────┘  └────────┘│
└──────────────────────────────────────────┘
```

## 🎨 Visual Design

The UI uses a futuristic cybersecurity theme:

- **Color Palette**: Pastel neons (cyan, purple, pink) on dark slate background
- **Typography**: Modern sans-serif with monospace for logs
- **Animations**: Smooth 60 FPS with Three.js
- **Responsive**: Works on desktop and large tablets

### Health States

| State | Color | Meaning |
|-------|-------|---------|
| 🟢 NORMAL | Green | System healthy, no threats |
| 🟡 ELEVATED | Yellow | Suspicious activity detected |
| 🔴 CRITICAL | Red | Active attack in progress |

## 📖 Documentation

Comprehensive documentation is available:

- **[START_HERE.md](START_HERE.md)** - Quick orientation guide
- **[QUICK_START.md](QUICK_START.md)** - 30-second setup
- **[SETUP.md](SETUP.md)** - Detailed installation instructions
- **[DEMO_GUIDE.md](DEMO_GUIDE.md)** - Presentation script (3-5 minutes)
- **[PITCH.md](PITCH.md)** - Complete pitch deck
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture diagrams
- **[API_EXAMPLES.md](API_EXAMPLES.md)** - API testing examples
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues and fixes
- **[INDEX.md](INDEX.md)** - Complete documentation index

## 🔌 API Endpoints

### GET /status
Get current system status and statistics
```bash
curl http://localhost:8000/status
```

### POST /request
Process and analyze a request
```bash
curl -X POST http://localhost:8000/request \
  -H "Content-Type: application/json" \
  -d '{"ip":"192.168.1.100","payload":"SELECT * FROM users"}'
```

### POST /simulate-attack
Trigger attack simulation
```bash
curl -X POST http://localhost:8000/simulate-attack \
  -H "Content-Type: application/json" \
  -d '{"type":"sql_injection"}'
```

### GET /logs
Retrieve all activity logs
```bash
curl http://localhost:8000/logs
```

**Interactive API Docs**: Visit `http://localhost:8000/docs` for Swagger UI

## 🧪 Testing

### Manual Testing
```bash
# Test backend health
curl http://localhost:8000/status

# Test SQL injection detection
curl -X POST http://localhost:8000/request \
  -H "Content-Type: application/json" \
  -d '{"ip":"192.168.1.100","payload":"'\'' OR 1=1"}'
```

### Attack Simulations
Use the built-in attack simulator:
1. Open the frontend
2. Click "SIMULATE ATTACK"
3. Select attack type
4. Observe system response

## 🛠️ Development

### Project Structure
```
project-chimera/
├── backend/                 # Python/FastAPI backend
│   ├── main.py             # API server
│   ├── detector.py         # Threat detection
│   ├── mutation_engine.py  # AI mutations
│   ├── honeypot.py         # Attack logging
│   └── attacker_simulator.py
├── frontend/               # React/Three.js frontend
│   └── src/
│       ├── App.jsx         # Main app
│       ├── Dashboard.jsx   # Stats panel
│       ├── CellVisualization.jsx
│       └── api.js          # API client
└── docs/                   # Documentation (13 files)
```

### Tech Stack

**Backend:**
- Python 3.8+
- FastAPI (API framework)
- Uvicorn (ASGI server)
- Regex (Pattern matching)

**Frontend:**
- React 18
- Vite (Build tool)
- Three.js (3D graphics)
- TailwindCSS (Styling)

### Adding New Threat Patterns

Edit `backend/detector.py`:
```python
self.sql_patterns = [
    r"(\bOR\b.*=.*)",
    r"(';.*--)",
    # Add your pattern here
]
```

### Customizing Mutations

Edit `backend/mutation_engine.py`:
```python
mutations = {
    "YOUR_THREAT_TYPE": {
        "action": "your_action",
        "reason": "Your reason",
        # ... more config
    }
}
```

## 🐛 Troubleshooting

### Backend won't start
```bash
# Reinstall dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.8+
```

### Frontend won't start
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install

# Check Node version
node --version  # Should be 16+
```

### Port already in use
```bash
# Windows: Find and kill process
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or change port in main.py and api.js
```

See **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** for more solutions.

## 🚀 Deployment

### Local Demo (Current)
- Perfect for hackathons and presentations
- No infrastructure needed
- Runs on localhost

### Cloud Deployment (Future)
- **Backend**: Heroku, Railway, Fly.io, or AWS
- **Frontend**: Vercel, Netlify, or Cloudflare Pages
- **Database**: PostgreSQL or MongoDB for persistent logs

### Docker (Coming Soon)
```bash
docker-compose up
```

## 🎯 Use Cases

- **Hackathon Demos**: Impressive visual presentation
- **Security Education**: Teaching adaptive security concepts
- **Proof of Concept**: Demonstrating AI-driven security
- **Research**: Exploring biological security metaphors
- **Portfolio**: Showcasing full-stack + AI skills

## 🔮 Future Enhancements

### Short-term
- [ ] WebSocket for true real-time updates
- [ ] More attack patterns (XSS, CSRF, etc.)
- [ ] Export logs to JSON/CSV
- [ ] Enhanced particle effects

### Medium-term
- [ ] Real LLM integration (OpenAI GPT-4)
- [ ] Database persistence (PostgreSQL)
- [ ] User authentication
- [ ] Multiple system instances

### Long-term
- [ ] Distributed architecture
- [ ] Real network traffic analysis
- [ ] Machine learning threat detection
- [ ] Enterprise dashboard
- [ ] Threat intelligence feeds
- [ ] Kubernetes deployment

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📊 Project Stats

- **Total Files**: 34
- **Lines of Code**: ~1,500
- **Documentation**: ~3,000+ lines
- **Setup Time**: 5 minutes
- **Demo Time**: 3-5 minutes
- **Completeness**: 100%

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by biological immune systems
- Built for hackathon demonstrations
- Designed for educational purposes

## 📞 Support

- **Documentation**: See [INDEX.md](INDEX.md) for complete guide
- **Issues**: Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Questions**: Open an issue on GitHub

## 🎤 The Pitch

> "In nature, the immune system doesn't just block threats—it learns, adapts, and evolves. Project Chimera brings that same intelligence to cybersecurity. We're not building better walls; we're building a living defense system."

---

<div align="center">

**Project Chimera: The Digital Immune System**

*Detect. Adapt. Evolve.*

Built with ❤️ for hackathons everywhere

[⬆ Back to Top](#-project-chimera-the-digital-immune-system)

</div>
