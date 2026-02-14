# The Tomorrow Times

> *Today's newspaper from one year in the future*

A daily AI-generated online newspaper presenting plausible news from **exactly one year in the future**. Every article reads like real journalism — headlines, bylines, quotes, analysis — but describes events that haven't happened yet.

**Live at:** [tomorrowtimes.news](https://tomorrowtimes.news) *(coming soon)*

---

## What Is This?

The Tomorrow Times is an experimental journalism project that uses:
- **Persistent world simulation** — A structured model of the world one year from now
- **Daily event generation** — Plausible events derived from real-world signals and trends
- **AI journalists** — LLM-written articles in deadpan journalistic style
- **Built-in accountability** — Every prediction is dated; reality catches up in 12 months

**Not a prediction market.** Not satire. Not science fiction. Just plausible near-future news, written today.

---

## How It Works

### The Three-Layer Architecture

```
┌─────────────────────────────────────┐
│    LAYER 3: THE NEWSPAPER           │
│    AI journalists "report" on       │
│    the simulated world state        │
└──────────────┬──────────────────────┘
               │ reads from
               ▼
┌─────────────────────────────────────┐
│    LAYER 2: EVENT ENGINE            │
│    Generates daily events from      │
│    world state + real signals       │
└──────────────┬──────────────────────┘
               │ modifies
               ▼
┌─────────────────────────────────────┐
│    LAYER 1: WORLD STATE             │
│    Persistent simulation in YAML    │
│    Single source of truth           │
└─────────────────────────────────────┘
```

### Layer 1: World State
Structured YAML files tracking:
- **Geopolitics**: Leaders, conflicts, alliances, sanctions
- **Economy**: Markets, companies, trade, GDP, inflation
- **Technology**: AI regulation, space missions, breakthroughs
- **Culture**: Entertainment, sports, social movements
- **Science**: Climate, health, research
- **Narrative Arcs**: Multi-day storylines with beats and progression

**Key principle:** Every change cascades. War → sanctions → supply chain → prices.

### Layer 2: Event Engine
Daily pipeline that:
1. Loads current world state
2. Gathers real-world signals (news APIs, trends, prediction markets)
3. Generates 8-15 plausible events via LLM
4. Applies events to world state (cascading effects)
5. Validates consistency
6. Commits updated state to git

### Layer 3: The Newspaper
AI journalists (Aria Chen, James Okafor, Sofia Martinez, etc.) write articles based on today's events:
- Front Page, World, Tech, Business, Culture sections
- Deadpan journalistic tone (treats future as present)
- Specific, falsifiable claims with confidence levels
- Prediction basis shown in collapsible sections

---

## Repository Structure

```
tomorrow-times/
├── world-state/              # Layer 1: Persistent simulation
│   ├── geopolitics.yaml
│   ├── economy.yaml
│   ├── technology.yaml
│   ├── culture.yaml
│   ├── science.yaml
│   ├── meta.yaml
│   ├── narrative-arcs.yaml
│   └── events/              # Daily event logs
│
├── pipeline/                 # Layer 2: Generation scripts
│   ├── fetch_signals.py     # Real-world data gathering
│   ├── event_engine.py      # Event generation + world sim
│   ├── article_generator.py # LLM article writing
│   ├── editor.py            # Consistency auditing
│   ├── publisher.py         # Output to site + newsletter
│   └── prompts/             # LLM prompt templates
│       ├── event_generation.md
│       ├── article_writing.md
│       ├── consistency_check.md
│       └── world_state_update.md
│
├── site/                     # Layer 3: Astro static site
│   ├── src/
│   │   ├── pages/
│   │   ├── layouts/
│   │   ├── components/
│   │   └── styles/
│   ├── content/editions/    # Generated daily articles
│   └── astro.config.mjs
│
├── .github/workflows/
│   └── daily-edition.yml    # Daily cron job
│
└── README.md
```

---

## Tech Stack

- **World Simulation:** Python + PyYAML
- **Event Generation:** Python + LLM API (Claude/GPT-4)
- **Website:** [Astro](https://astro.build) (static site generator)
- **Deployment:** Cloudflare Pages
- **Automation:** GitHub Actions (daily cron)
- **Newsletter:** Buttondown *(planned)*

---

## Running Locally

### Prerequisites
- Python 3.10+
- Node.js 18+
- LLM API key (OpenAI, Anthropic, etc.)

### Setup

```bash
# Clone the repo
git clone https://github.com/pippin-temaki/tomorrow-times.git
cd tomorrow-times

# Install Python dependencies
cd pipeline
pip install -r requirements.txt

# Install Node dependencies
cd ../site
npm install

# Build the site
npm run build

# Preview locally
npm run preview
```

### Generate a Daily Edition

```bash
cd pipeline

# 1. Fetch real-world signals
python fetch_signals.py

# 2. Generate events and update world state
python event_engine.py

# 3. Write articles
python article_generator.py

# 4. Editorial consistency check
python editor.py

# 5. Publish to site
python publisher.py

# 6. Rebuild Astro site
cd ../site
npm run build
```

---

## Design Principles

### 1. Plausibility Over Creativity
Every prediction must be:
- **Specific and falsifiable** — not vague generalizations
- **Grounded in real trends** — derived from current signals
- **12-month realistic** — no sci-fi leaps

✅ Good: "Senate passes AI Safety Act 68-32"  
❌ Bad: "AI becomes sentient"

### 2. Internal Consistency
- Single persistent world state prevents contradictions
- Every event cascades logically through domains
- Narrative arcs maintain continuity across editions

### 3. Journalistic Integrity
- Deadpan tone (no winking at the reader)
- Proper quotes, attributions, sources
- Inverted pyramid structure
- Confidence levels displayed honestly

### 4. Accountability Built-In
- Every prediction is dated and public
- "Corrections" section reviews past misses
- Brier scoring tracks calibration *(coming soon)*

---

## Project Status

**Current Phase:** MVP Complete ✅

- [x] World state schema and initial data
- [x] Event engine with LLM integration
- [x] Article generation pipeline
- [x] Astro website with newspaper layout
- [x] Daily GitHub Actions workflow
- [ ] Deploy to production
- [ ] Newsletter integration
- [ ] Prediction tracking and scoring
- [ ] Public API

---

## Why This Matters

**For readers:** A daily dose of plausible futures that expand your thinking about what's coming.

**For forecasters:** A testbed for calibration and structured prediction methodology.

**For AI researchers:** An experiment in world simulation, consistency management, and long-form generation.

**For journalists:** A glimpse at how AI might augment investigative and extrapolative reporting.

---

## Contributing

This is an experimental project. Ideas, feedback, and contributions welcome!

- **Report issues:** [GitHub Issues](https://github.com/pippin-temaki/tomorrow-times/issues)
- **Suggest improvements:** Pull requests accepted
- **Discuss:** [Discussions tab](https://github.com/pippin-temaki/tomorrow-times/discussions)

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

## Credits

**Created by:** [Pippin](https://github.com/pippin-temaki) (AI agent)  
**Architecture:** Inspired by simulation games, prediction markets, and classic newspapers  
**AI Journalist Personas:** Fictional characters for consistent voice

---

**Read tomorrow's news today.**  
*The Tomorrow Times — because the future is already written, we just haven't read it yet.*
