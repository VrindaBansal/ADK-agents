# ADK Learning Projects

> A curated collection of mini projects built with Google's Agent Development Kit (ADK) to master different agent development techniques and patterns through hands-on experience.

---

## Project Goals

This repository contains hands-on mini projects designed to:
- Learn ADK fundamentals through practical examples
- Explore different agent patterns and techniques
- Build a reference collection of working ADK implementations
- Practice structured agent development

## Setup

### Prerequisites
- Python 3.9+
- Google Cloud Project (for Gemini API access)

### Installation

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd adk-agents
```

**2. Create and activate virtual environment**
```bash
python -m venv .venv

# Activate (choose your platform)
# macOS/Linux:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\activate.bat
# Windows PowerShell:
.venv\Scripts\Activate.ps1
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create `.env` files in each agent directory with your credentials:
```bash
# For Gemini API
GOOGLE_GENAI_API_KEY=your_api_key_here

# OR for Vertex AI
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_GENAI_USE_VERTEXAI=True
```

## Running the Agents

### Web UI (Recommended)
```bash
# Navigate to the root directory
cd adk-agents

# Start the web interface
adk web

# Open http://localhost:8000 in your browser
# Select your agent from the dropdown menu
```

### Command Line
```bash
# Run specific agent
adk run <agent-name>

# Example:
adk run stock-agent
```

### API Server
```bash
# Start API server
adk api_server

# Your agents will be available via REST API
```

## Technologies Used

- **Google ADK** — Agent development framework
- **Pydantic** — Data validation and schema definition
- **yfinance** — Stock market data (Yahoo Finance API)
- **Gemini 2.0 Flash** — Large language model
- **FastAPI** — Web framework (underlying ADK infrastructure)

## Contributing

Feel free to:
- Add new learning projects
- Improve existing agents
- Share interesting ADK patterns
- Report issues or suggestions

## Additional Resources

- [ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Python GitHub](https://github.com/google/adk-python)
- [ADK Samples](https://github.com/google/adk-samples)
- [Gemini API Documentation](https://ai.google.dev/)

## License

This project is for educational purposes. Please refer to individual dependencies for their respective licenses.

---

<div align="center">

**Happy Agent Building!**

*Built with curiosity to learn ADK*

</div>
