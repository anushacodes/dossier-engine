# 🕵️‍♂️ Executive & AI Technical Intelligence Dossier Engine

> **A multi-stage, anti-hallucination research pipeline built on the WAT (Workflows, Agents, Tools) architecture.**  
> Investigates executive interviewers and companies, uncovers their 2025/2026 AI roadmap, scores substance through an independent LLM Quality Judge, and compiles standalone matte-dark HTML & Markdown cheat sheets for high-stakes interviews and strategic coffee chats.

---

## ⚡ Quick Demo

Run a complete deep-research investigation with a single command:

```bash
./investigate "Dario Amodei" "Anthropic"
```

Output generated:
* 🌐 **Interactive HTML Dashboard**: `dossiers/anthropic_dario_amodei_dossier.html` (automatically opened in default browser)
* 📝 **Markdown Cheat Sheet**: `dossiers/anthropic_dario_amodei_dossier.md`
* 🛡️ **Judge Quality Score**: `96/100 [High Substance | Verified Grounding]`

---

## 🎯 Key Capabilities

| Capability | What It Does | Why It Matters |
| :--- | :--- | :--- |
| **🛡️ Pre-Flight Guardian** | Verifies search & LLM connectivity before execution | Eliminates silent fallbacks and fabricated filler when APIs fail |
| **🌐 Neural & Recency Search** | Exa (LinkedIn & talks) + Tavily (2025/2026 AI roadmap) | Extracts primary source disclosures rather than outdated SEO summaries |
| **🧠 Information Architect** | Dynamic LLM reasoning with auto model failover | Compiles 5-second TL;DRs, concrete metric pills, and tactical coaching tips |
| **⚖️ LLM Quality Judge** | Independent auditor grading substance (0–100) | Detects wishy-washy buzzwords and forces an automated hardening pass if score < 75 |
| **🖥️ Matte-Dark HTML HUD** | Standalone offline dashboard (`#080c14` / `#0f1624`) | Zero CDN dependencies, instant local load, sticky HUD, live filter, and 1-click question copy |

---

## 🏗️ Architecture & WAT Framework

This system strictly implements the **WAT Framework**:
1. **Workflows (SOPs)**: Standard Operating Procedures in `workflows/` defining intelligence protocols.
2. **Agents (Orchestrators)**: Multi-stage pipeline logic in `tools/investigate.py`.
3. **Tools (Execution)**: Fast, deterministic Python execution scripts in `tools/`.

```
                        [ ./investigate "Person" "Company" ]
                                        │
                                        ▼
                         [ Phase 1: Pre-Flight Guardian ]
                        (Validates Exa, Tavily, Groq keys)
                                        │
                    ┌───────────────────┴───────────────────┐
                    ▼                                       ▼
       [ Phase 2A: Exa Engine ]                [ Phase 2B: Tavily Engine ]
     • LinkedIn profile verification          • 2025/2026 AI investments
     • Thought leadership & talks             • Core business & moat disclosures
                    └───────────────────┬───────────────────┘
                                        │
                                        ▼
                    [ Phase 3: LLM Information Architect ]
                       (Synthesizes structured dossier JSON)
                                        │
                                        ▼
                       [ Phase 4: LLM Quality Judge Gate ]
                       (Audits metrics density & zero fluff)
                                 │              │
                     Score >= 75 │              │ Score < 75
                                 │              ▼
                                 │     [ Auto Hardening Pass ]
                                 │   (Forces entity extraction)
                                 │              │
                                 └──────┬───────┘
                                        │
                                        ▼
                  [ Phase 5: Deterministic HTML/MD Compiler ]
              • Standalone matte-dark HTML with 60s top HUD
              • Markdown cheat sheet for quick review
```

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.10+
* Free API keys for:
  * [Exa API](https://dashboard.exa.ai/) (LinkedIn neural search)
  * [Tavily AI](https://app.tavily.com/) (2025/2026 recency search)
  * [Groq Cloud](https://console.groq.com/) (Llama 3.3 / Qwen high-speed inference)

### 2. Setup Configuration
Clone the repository and copy the environment template:

```bash
git clone git@github.com:anushacodes/harness.git
cd harness
cp .env.example .env
```

Add your keys to `.env`:
```env
EXA_API_KEY=your_exa_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

---

## 💻 CLI Usage

### Direct Invocation
```bash
./investigate "<Interviewer Name>" "<Company Name>"
```

*Example:*
```bash
./investigate "Dario Amodei" "Anthropic"
./investigate "Jeff Weinstein" "Stripe"
```

### Advanced Flags
You can specify custom roles, meeting formats, notes, and specific profile URLs:

```bash
./investigate "Dario Amodei" "Anthropic" \
  --role "Staff AI Product Manager" \
  --meeting "Executive Technical Screen" \
  --links "https://www.linkedin.com/in/dario-amodei" \
  --notes "Emphasize frontier alignment, Computer Use APIs, and MCP ecosystem"
```

### Interactive Mode
Running `./investigate` with no arguments launches an interactive prompt:

```bash
./investigate
```

---

## 📂 Repository Layout

```
.
├── investigate                      # Root executable launcher (chmod +x)
├── AGENT.md                         # WAT architecture agent operating system
├── .env.example                     # Environment template with instructions
├── workflows/
│   └── research_company_and_interviewer.md  # 5-Phase research SOP & verification protocol
├── tools/
│   ├── investigate.py               # Main research engine (Guardian, Search, Architect, Judge)
│   └── render_dossier_html.py       # Deterministic HTML & Markdown compiler
├── templates/
│   ├── dossier_template.html        # Matte-dark standalone HTML dashboard
│   └── dossier_template.md          # Markdown cheat sheet template
└── dossiers/                        # Output generated dossiers
    ├── anthropic_dario_amodei_dossier.html
    ├── anthropic_dario_amodei_dossier.md
    ├── stripe_jeff_weinstein_dossier.html
    └── stripe_jeff_weinstein_dossier.md
```

---

## 🛡️ Anti-Hallucination & Quality Protocol

Every generated briefing adheres to four strict verification rules:
1. **Entity Disambiguation**: Enforces exact match filtering to prevent confusion with individuals of the same name at different organizations.
2. **Quantitative Density**: Prioritizes verified metrics (ARR, compute capacity, deal values, model versions, headcount) over vague buzzwords.
3. **Traceable Citations**: Every product, quote, and investment item links directly to its source URL in the Grounded Sources Directory.
4. **LLM Quality Gate**: If an initial draft relies on generic boilerplate, the independent auditor rejects the score and triggers an automatic hardening pass.

---

## 📄 License
MIT License. Created by [anushacodes](https://github.com/anushacodes).

