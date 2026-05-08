# Archive: AI-Powered Log Analysis (Lab 4)

## Project Initialization
- **Date:** 2026-05-08
- **Objective:** Build an AI-driven log analysis pipeline for Telecom monitoring.
- **Tools:** Python, Groq (Llama 3.1 8b), Kafka/ELK (Conceptual Architecture).

### Step 0: Project Scaffolding
- Created directory structure in `day9/lab4`.
- Initialized `archive.md` for logging development steps.
- Created `.gitignore` to protect sensitive `.env` files and API keys.

### Step 1: Log Generation
- Created `app.log` containing INFO, ERROR, and WARN levels.
- Error patterns include Kafka consumer lag and broker timeouts.
- Manually created file due to script execution restrictions in the current environment.

### Step 2 & 3: AI-Driven Root Cause Analysis
- Developed `groq_util.py` using Python `requests` library.
- Integrated Groq API (Model: `llama-3.1-8b-instant`).
- Designed specialized prompt for senior SRE-level log analysis.
- **Result:** Successfully identified Kafka lag and Broker timeout as dual root causes. 
- **Output:** Generated `analysis_report.md` via user-executed command.

### Step 4: Incident Summarization
- Extracted key insights from AI analysis to create a management-ready `incident_summary.md`.
- Documented remediation steps and long-term infrastructure recommendations.
- Finalized architecture diagrams and Medallion layer descriptions in `README.md`.
