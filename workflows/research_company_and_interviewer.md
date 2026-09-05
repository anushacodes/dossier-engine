# Workflow: Executive & AI Technical Intelligence Dossier

## Objective
To conduct multi-source, factually verified, and technically deep intelligence research on a **target company** and a **specific interviewer/contact**, zeroing in on their **strategic AI agenda**, model architecture, compute infrastructure, capital allocation, and executive thesis. The final output is compiled into a spacious, dark-mode, anti-hallucination **Local HTML Dashboard** and **Markdown Cheat Sheet** designed for split-second glanceability during live calls.

---

## The 3 Anti-Hallucination Safeguards (Strict Protocol)

> [!CAUTION]
> **Zero Tolerance for Generic Filler**: Fabricating plausible-sounding technical stacks, false product features, or imaginary quotes destroys credibility. Follow these mandatory rules:

1. **Mandatory Source Attribution**:
   - Every product, partnership, dollar figure, and quote must trace to an official source (company press release, SEC filing, arXiv paper, engineering blog, verified podcast/talk, or LinkedIn post).
   - In the dossier, attach the publisher, publication date, and verification URL.
2. **Factual Status Demarcation**:
   - `✓ Verified Fact`: Explicitly confirmed by primary documentation.
   - `⚠ Strategic Inference`: Logically derived from hiring trends, public job listings, or secondary industry reporting (must be explicitly labeled as such).
3. **The "Inquire" Fallback (Never Guess)**:
   - If an internal detail is confidential or unavailable in public records (e.g., specific internal evals, confidential GPU cluster sizing, unreleased products), **DO NOT GUESS**.
   - Instead, convert the knowledge gap into a high-caliber **Power Question** for the candidate to ask during the call (e.g., *"No public disclosures on internal prompt-caching hit rates. Ask the interviewer: 'How is your team measuring cache invalidation latency in production?'"*).

---

## 5-Phase Deep Research Protocol

### Phase 1: Interviewer Intelligence (The Person)
- **Current Scope & Team Ownership**: Exact team, title, direct reporting lines, and current deliverables.
- **Career Pedigree & Tenure**: Timeline of prior stints (e.g., Ex-Google Brain, Ex-OpenAI, Ex-Baidu), educational degrees (B.S./M.S./Ph.D. institutions and thesis topics).
- **Public Footprint & Technical Thesis**:
  - Authored arXiv papers, patents, or conference presentations (NeurIPS, ICML, CVPR, re:Invent).
  - Specific authored essays or blog posts (e.g., Dario Amodei's *"Machines of Loving Grace"*).
  - Personal stance on technical trade-offs (e.g., scaling laws, mechanistic interpretability, latency vs. reasoning depth).
- **Verbatim Standout Quote**: Exact quote with origin, year, and context.

### Phase 2: Company Fundamentals & Defensible Moat
- **Core Business Model**: Monetization engine, pricing tiers (API tokens, enterprise seat licensing, usage minimums), primary customer segments.
- **Defensible Moat**: What protects them? (Proprietary data flywheels, compute alliances, developer distribution, high switching costs).
- **Executive Leadership**: CEO, CTO, Head of AI, and Co-founders with their technical backgrounds and management style.
- **Engineering Reputation**: Market perception (e.g., rigorous safety research, fast product shipping, infrastructure scale, developer-first documentation).
- **Recent Material Milestones**: Major deals, funding rounds, valuations, acquisitions, or restructuring within the last 6-12 months.

### Phase 3: AI Technical Strategy & Compute Infrastructure
Dig beyond surface-level PR into the actual technical fabric:
1. **Active Production AI Products**:
   - Model families deployed (e.g., Claude 3.5 Sonnet, Claude 3.7 Sonnet, GPT-4o, Llama 3.3).
   - Novel agentic capabilities (e.g., Computer Use APIs, Model Context Protocol (MCP), prompt caching, tool use).
   - Enterprise integrations and security boundaries.
2. **Compute Capacity, Chips & Cloud Infrastructure**:
   - Primary cloud providers and agreements (e.g., AWS Bedrock, Google Cloud Vertex AI, Azure).
   - Silicon commitments: Custom ASICs (AWS Trainium, Google TPUs) vs. Nvidia GPUs (H100/H200/B200).
   - Scale of infrastructure commitments (e.g., gigawatt deals, cluster projects like Project Rainier).
3. **Safety Frameworks & Evaluation Standards**:
   - Governance policies (e.g., Responsible Scaling Policy / RSP, AI Safety Levels / ASL).
   - Red-teaming, alignment methodology (RLHF, Constitutional AI, RLAIF, mechanistic interpretability).
4. **Capital Allocation & M&A**:
   - Strategic investments, corporate venture funds, startup acquisitions.

### Phase 4: Tactical Radar & Tailored Power Questions
- **Green Flags (Lean Into)**: Cultural values and engineering dogmas they pride themselves on (e.g., Constitutional AI, empirical scaling laws, taste in software).
- **Landmines (Avoid / Handle with Tact)**: Sensitive topics, legal disputes, compute bottlenecks, rate-limiting outages, or departed co-founders.
- **3-5 High-Impact Questions**:
  - Blends the interviewer's specific technical background with the company's long-term roadmap.
  - Includes a "Tactical Rationale" explaining why asking this establishes authority.

### Phase 5: Verification & Compilation
- Compile structured intelligence into `.tmp/dossier_data.json`.
- Populate all sources into the `sources` array with title, date, publisher, and URL.
- Execute the compiler:
  ```bash
  python3 tools/render_dossier_html.py .tmp/dossier_data.json --output-dir dossiers/ --open
  ```

---

## Quality & Anti-Hallucination Checklist
Before viewing or delivering the dossier:
- [ ] Every single bullet has a verifiable fact, citation, or is explicitly tagged as `[⚠ Inference]`.
- [ ] All quotes have exact authors, sources, and dates.
- [ ] No generic AI filler (e.g., "uses AI to enhance customer experiences") is present without concrete naming of the model/product.
- [ ] The top 60-Second HUD can be digested in under 3 seconds on camera.
- [ ] The HTML dashboard renders cleanly with dark mode, generous padding, and functioning filter/copy buttons.
