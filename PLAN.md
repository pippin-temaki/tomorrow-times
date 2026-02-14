# The Tomorrow Times — Project Plan

> *Today's newspaper from one year in the future*
> Created: 2026-02-14 | Updated: 2026-02-14

---

## 1. Concept & Positioning

### The Idea
A daily AI-generated online newspaper presenting plausible news from **exactly one year in the future**. Every article reads like real journalism — headlines, bylines, quotes, analysis — but describes events that haven't happened yet.

### What Makes This Unique
- **Not a prediction market** (Metaculus, Polymarket) — those are probabilistic bets. We tell *stories*.
- **Not sci-fi** — grounded in real trends, data, and extrapolation. 12 months away, not 50 years.
- **Not satire** — deadpan journalistic tone. The paper treats its future date as the present.
- **Built-in accountability** — every prediction is dated. A year later, reality catches up.

### Comparable Projects
| Project | What They Do | How We Differ |
|---------|-------------|---------------|
| **Metaculus** | Crowdsourced probability forecasts | Narrative news, not probability estimates |
| **Polymarket** | Prediction market trading | Editorial, not financial |
| **The Onion** | Satirical newspaper format | Plausible, not absurd |
| **Future Timeline** | Long-range predictions | Daily, near-future, newspaper-format |

---

## 2. Core Architecture: The World Simulation

### The Problem
Without a shared world state, predictions contradict each other within days. A ceasefire in one article, escalation in another. Two companies "winning" the same market.

### The Solution: Layered Architecture

```
┌─────────────────────────────────────────────┐
│         LAYER 3: THE NEWSPAPER               │
│  Journalists "report" on the world state     │
│  Headlines, articles, opinion, analysis      │
└──────────────────┬──────────────────────────┘
                   │ reads from
                   ▼
┌─────────────────────────────────────────────┐
│         LAYER 2: EVENT ENGINE                │
│  Daily events generated from world state     │
│  Cascading consequences, probabilistic       │
│  Some planned, some emergent                 │
└──────────────────┬──────────────────────────┘
                   │ modifies
                   ▼
┌─────────────────────────────────────────────┐
│         LAYER 1: WORLD STATE                 │
│  Persistent structured simulation            │
│  The "ground truth" of our future world      │
│  Versioned in git, evolves daily             │
└─────────────────────────────────────────────┘
```

### Layer 1: World State

A structured, persistent model of the world one year from now. This is the single source of truth that all content derives from.

#### State Domains

```yaml
# world-state/geopolitics.yaml
geopolitics:
  leaders:
    US: { head_of_state: "...", party: "...", approval: 0.0 }
    # ... all major nations
  conflicts:
    - id: "ukraine-russia"
      status: "active|ceasefire|resolved"
      parties: [...]
      recent_developments: [...]
  alliances:
    - { name: "NATO", members: [...], tensions: [...] }
  sanctions: [...]
  upcoming_elections: [...]

# world-state/economy.yaml
economy:
  global:
    gdp_growth: 0.0
    inflation_trend: "rising|stable|falling"
    key_rates: { fed: 0.0, ecb: 0.0 }
  markets:
    sp500: { level: 0, trend: "..." }
    crypto: { btc: 0, eth: 0, trend: "..." }
  companies:
    - { name: "Apple", market_cap: "...", trajectory: "...", key_products: [...] }
    - { name: "OpenAI", status: "...", latest: "..." }
  trade: [...]

# world-state/technology.yaml
technology:
  ai:
    frontier_models: [{ name: "...", org: "...", capabilities: [...] }]
    regulation: { us: "...", eu: "...", china: "..." }
    adoption_trend: "..."
  space:
    missions: [{ org: "...", target: "...", status: "..." }]
  energy:
    renewables_share: 0.0
    breakthroughs: [...]
  computing:
    quantum: { status: "...", leaders: [...] }

# world-state/culture.yaml
culture:
  entertainment:
    trending: [...]
    upcoming_releases: [...]
  sports:
    seasons: { nfl: { champion: "...", standings: [...] } }
  social:
    movements: [...]
    viral_topics: [...]
  demographics:
    trends: [...]

# world-state/science.yaml
science:
  breakthroughs: [...]
  climate:
    global_temp_anomaly: 0.0
    extreme_events: [...]
  health:
    pandemics: [...]
    treatments: [...]

# world-state/meta.yaml
meta:
  current_date: "2027-02-14"  # The simulated future date
  simulation_day: 1            # Days since simulation started
  seed_date: "2026-02-14"     # When simulation was initialized
  major_narrative_arcs:
    - id: "ai-regulation-wave"
      status: "active"
      summary: "..."
    - id: "mars-race"
      status: "building"
      summary: "..."
```

#### World State Principles
1. **Seeded from reality** — initialized with real-world data as of launch date
2. **Internally consistent** — every change cascades (war → sanctions → supply chain → prices)
3. **Probabilistic evolution** — not deterministic. The event engine rolls dice weighted by plausibility
4. **Versioned in git** — full history of how the simulated world evolved, diffable
5. **Human-readable** — YAML/JSON so humans (and LLMs) can easily inspect and reason about it

### Layer 2: Event Engine

The daily "simulation tick" that evolves the world state.

#### Daily Pipeline

```
1. LOAD current world state (all .yaml files)
2. GATHER real-world signals (news APIs, trends, prediction markets)
3. GENERATE daily events:
   a. LLM analyzes world state + signals
   b. Produces 8-15 events with cascading effects
   c. Each event tagged with: domain, impact, probability-was, narrative-arc
4. APPLY events to world state:
   a. Update affected state domains
   b. Record event log (world-state/events/YYYY-MM-DD.yaml)
   c. Track narrative arcs (new, progressing, resolving)
5. VALIDATE consistency:
   a. LLM "auditor" checks for contradictions
   b. Flag and resolve any conflicts
6. COMMIT updated world state to git
```

#### Event Types
- **Deterministic**: Logical consequences of current state (election results after campaign)
- **Probabilistic**: Weighted random (earthquake, tech breakthrough, scandal)
- **Cascading**: Second-order effects of previous events (trade war → recession → layoffs)
- **Arc events**: Part of ongoing narrative threads (space race milestones, political campaigns)

#### Narrative Arc Management
The engine tracks multi-day storylines:
```yaml
narrative_arcs:
  - id: "us-ai-regulation"
    started: "2027-02-14"
    status: "active"  # active | climax | resolving | resolved
    beats:
      - { date: "2027-02-14", event: "Senate committee announces AI bill" }
      - { date: "2027-02-18", event: "Tech CEOs testify" }
      - { date: "2027-03-01", event: "Bill passes committee vote" }
    projected_resolution: "2027-04-15"
    tension_level: 0.7  # 0-1, drives how much coverage it gets
```

### Layer 3: The Newspaper

The editorial layer that transforms world state + events into journalism.

#### Article Generation
```
1. READ today's events from Layer 2
2. PRIORITIZE by impact, novelty, narrative arc status
3. ASSIGN to sections (Front Page gets highest-impact)
4. GENERATE articles:
   - LLM writes as newspaper journalist
   - References world state for context/background
   - Maintains consistent "voice" per AI journalist persona
5. EDITORIAL PASS:
   - Check consistency with world state
   - Verify no contradictions with previous editions
   - Quality and style check
6. PUBLISH
```

---

## 3. Content Strategy

### Sections (Daily)
1. **Front Page** — 1 major headline + 2-3 secondary stories
2. **World** — Geopolitics, international affairs
3. **Tech & Science** — AI, space, biotech, climate tech
4. **Business & Markets** — Economy, companies, crypto
5. **Culture** — Entertainment, sports, social trends
6. **Opinion/Editorial** — "Letters from the editor" reflecting on the future
7. **The Ticker** — Short bullet-point predictions (stock prices, weather records, sports scores)
8. **Corrections** — Where past predictions were wrong (accountability section)

### Weekly Specials
- **Monday**: Deep-dive long-form feature
- **Friday**: "Weekend Edition" — lighter cultural predictions
- **Sunday**: "The Week Ahead" (in the future timeline)

### Quality Controls
- Each article cites its reasoning basis (collapsible "Prediction Basis" section)
- Confidence level per article: 🟢 High | 🟡 Medium | 🔴 Speculative
- No lazy predictions ("AI will get better") — must be specific and falsifiable
- Cross-reference prediction markets for calibration

### AI Journalist Personas
Recurring bylines that build reader familiarity:
- **Aria Chen** — Technology Correspondent
- **James Okafor** — World Affairs Editor
- **Sofia Martinez** — Business & Markets
- **Dr. Lena Park** — Science & Environment
- **Marcus Webb** — Culture & Sports
- **The Editor** — Opinion/Editorials

---

## 4. Data Sources for Grounding

### News & Current Events
- **NewsAPI** / **GNews API** — current headlines for trend detection
- **Google Trends** — rising search terms and interest patterns

### Prediction & Forecasting
- **Metaculus API** — community forecast probabilities
- **Polymarket** — market-priced probabilities on major events
- **Metaculus forecasting-tools** (GitHub) — AI forecasting framework

### Economic & Market Data
- **FRED** — macroeconomic indicators
- **Yahoo Finance API** — market data and trends

### Science & Technology
- **arXiv API** — research papers and trends
- **GitHub Trending** — open source momentum

### Climate
- **NOAA APIs** — climate data and projections

---

## 5. Tech Architecture

### Stack

```
┌─────────────────────────────────────────────┐
│              Daily Cron Job                   │
│         (GitHub Actions, 6 AM UTC)           │
└──────────────────┬──────────────────────────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
┌───────────────┐   ┌─────────────────────┐
│ World Sim     │   │ Data Fetcher        │
│ (Python)      │   │ (APIs → signals)    │
└───────┬───────┘   └─────────┬───────────┘
        │                     │
        ▼                     ▼
┌─────────────────────────────────────────────┐
│           Event Engine (Python + LLM)        │
│  Generates events → updates world state      │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│         Article Generator (LLM)              │
│  Events → newspaper articles (markdown)      │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│              Astro Static Site               │
│         Build → Cloudflare Pages             │
└──────────────────┬──────────────────────────┘
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
   Cloudflare    RSS     Newsletter
     Pages      Feed    (Buttondown)
```

### Repository Structure
```
tomorrow-times/
├── world-state/              # Layer 1: persistent world simulation
│   ├── geopolitics.yaml
│   ├── economy.yaml
│   ├── technology.yaml
│   ├── culture.yaml
│   ├── science.yaml
│   ├── meta.yaml
│   ├── narrative-arcs.yaml
│   └── events/              # Daily event logs
│       └── 2027-02-14.yaml
├── pipeline/                 # Layer 2: generation pipeline
│   ├── fetch_signals.py     # Data source fetchers
│   ├── event_engine.py      # World simulation tick
│   ├── article_generator.py # LLM article writing
│   ├── editor.py            # Quality/consistency check
│   ├── publisher.py         # Markdown output + newsletter
│   └── prompts/             # LLM prompt templates
│       ├── event_generation.md
│       ├── article_writing.md
│       ├── consistency_check.md
│       └── world_state_update.md
├── site/                     # Layer 3: Astro website
│   ├── src/
│   │   ├── layouts/
│   │   │   └── Newspaper.astro
│   │   ├── pages/
│   │   │   ├── index.astro      # Today's edition
│   │   │   ├── archive/         # Past editions
│   │   │   └── accuracy/        # Prediction scorecard
│   │   ├── components/
│   │   │   ├── Article.astro
│   │   │   ├── Masthead.astro
│   │   │   ├── Ticker.astro
│   │   │   └── ConfidenceBadge.astro
│   │   └── styles/
│   │       └── newspaper.css
│   ├── content/
│   │   └── editions/           # Generated daily content
│   │       └── 2027-02-14/
│   │           ├── front-page.md
│   │           ├── world.md
│   │           ├── tech.md
│   │           └── ...
│   └── astro.config.mjs
├── .github/
│   └── workflows/
│       └── daily-edition.yml   # Cron trigger
├── README.md
└── package.json
```

### Why Astro
- Content-first SSG with excellent markdown support
- Island architecture — mostly static, interactive where needed
- Great RSS/sitemap built-in
- Easy deploy to Cloudflare Pages (free tier)
- Content Collections for typed, validated article data

---

## 6. Design Direction

### Visual Identity
- **Classic broadsheet aesthetic** — multi-column layout, serif headlines, thin rules/borders
- **Masthead** with future date prominently displayed
- Black & white primary palette with one accent color (warm amber)
- Bylines use AI journalist personas

### Typography
- Headlines: **Playfair Display** or **Old Standard TT**
- Body: **Source Serif Pro** or **Lora**
- UI/meta: **Inter** or **IBM Plex Sans**

### Layout
- CSS Grid multi-column newspaper layout
- Responsive: broadsheet on desktop, single-column on mobile
- The Guardian's web layout as structural inspiration

---

## 7. Name & Branding

### Recommendation: **The Tomorrow Times**
- Immediately clear, memorable, alliterative, newspaper-sounding
- Domain: `tomorrowtimes.news` or `thetomorrowtimes.com`

### Tagline Ideas
- "Today's news, one year early"
- "All the news that's fit to predict"
- "Tomorrow's headlines, delivered today"

### Alternatives
| Name | Domain Ideas |
|------|-------------|
| The Forward Post | theforwardpost.com |
| The Future Record | thefuturerecord.com |
| The Advance | theadvance.news |
| Dateline Tomorrow | datelinetomorrow.com |

---

## 8. MVP Phases

### Phase 1: "First Edition" (2-3 weeks)
- [ ] Initialize world state from current real-world data
- [ ] Build event engine (Python + LLM)
- [ ] Build article generator
- [ ] Set up Astro site with newspaper layout
- [ ] GitHub Actions daily cron
- [ ] Deploy to Cloudflare Pages
- [ ] RSS feed
- [ ] Buy domain

### Phase 2: "Daily Circulation" (weeks 3-6)
- [ ] Newsletter signup + daily email
- [ ] Section pages and archives
- [ ] Prediction Basis collapsible sections
- [ ] Confidence level indicators
- [ ] Social sharing (auto-generated OG images)

### Phase 3: "The Corrections Column" (months 2-3)
- [ ] Prediction tracking system
- [ ] Automated Brier scoring
- [ ] Public accuracy dashboard
- [ ] Corrections section

### Phase 4: "Going Viral" (months 3-6)
- [ ] Social media auto-posting
- [ ] AI-generated editorial illustrations
- [ ] Interactive prediction features
- [ ] API for embedding predictions

---

## 9. Costs (MVP)

| Item | Monthly Cost |
|------|-------------|
| Domain (.news) | ~$2/mo |
| Cloudflare Pages | Free |
| LLM API (world sim + articles) | ~$50-120/mo |
| NewsAPI | Free tier |
| Buttondown newsletter | Free (< 100 subs) |
| GitHub Actions | Free |
| **Total** | **~$55-125/mo** |

*Note: World simulation adds ~$15-30/mo in additional LLM calls vs. simple article generation.*

---

## 10. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| World state contradictions | Consistency auditor LLM pass; git diffing |
| Simulation drift from reality | Re-ground from real signals daily; don't simulate in a vacuum |
| Predictions too vague | Enforce specificity + falsifiability rules |
| Predictions wildly wrong | Corrections column is a feature, not a bug |
| Legal issues | Clear disclaimers; no financial advice; entertainment framing |
| Costs grow with complexity | Start lean; optimize prompts; cache aggressively |

---

## Appendix: LLM Prompt Chain

### Step 1: Signal Analysis
> "Given these current real-world signals [data], analyze trends and identify the 10 most significant developing storylines."

### Step 2: World State Evolution
> "Given the current world state [state] and today's real-world signals [data], generate 8-15 events that would plausibly occur on [future date]. Each event must: (1) be consistent with the world state, (2) have cascading effects noted, (3) reference which narrative arcs it advances."

### Step 3: State Update
> "Apply these events to the world state. Output the updated YAML files. Flag any inconsistencies."

### Step 4: Article Writing
> "You are [journalist persona], writing for The Tomorrow Times dated [future date]. Given these events and the world state, write a [section] article. Write in deadpan journalistic style as if reporting current events. Include quotes from plausible sources."

### Step 5: Editorial Review
> "Review this article against the world state. Check for: contradictions with world state, contradictions with previous editions, implausible claims, quality and style issues. Output: approved/revise with notes."

### Prediction Scoring (Brier Score)
- Each prediction gets a probability (0-1)
- Outcome is binary (happened/didn't)
- Score = (prediction - outcome)²
- Lower is better; 0.25 is random; good forecasters < 0.15
