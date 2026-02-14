# The Tomorrow Times — Plan Summary

> A daily AI-generated newspaper from one year in the future

## Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **SSG** | Astro | Content-first, modern DX, easy interactivity later |
| **Hosting** | Cloudflare Pages | Free, fast, global CDN |
| **Automation** | GitHub Actions (daily cron) | Free tier sufficient, integrates with git-as-database |
| **LLM** | Claude or GPT-4 | Multi-step prompt chain: signals → forecast → article → edit |
| **Newsletter** | Buttondown | Free tier, markdown-native, simple API |
| **Name** | The Tomorrow Times | Clear, memorable, alliterative. Domain: `tomorrowtimes.news` |
| **Tone** | Deadpan journalistic | Reports future events as fact — no hedging, no "we predict" |
| **Design** | Classic broadsheet + modern touches | Multi-column CSS Grid, serif headlines, confidence indicators |

## MVP Scope (2-3 weeks)

1. Astro site with newspaper CSS layout
2. Python pipeline: fetch data → LLM generates 5-8 articles → markdown output
3. GitHub Actions daily cron at 6 AM UTC
4. Deploy to Cloudflare Pages
5. RSS feed
6. Buy domain (`tomorrowtimes.news`)

**Estimated cost: ~$35-95/month** (mostly LLM API)

## What Makes It Special

- **Not predictions — it's a newspaper.** Reads like real journalism from the future.
- **Built-in accountability.** Every prediction is dated and scored when reality catches up.
- **The Corrections Column** turns being wrong into a feature.
- **Confidence indicators** (🟢🟡🔴) on every article.
- **Falsifiable claims** — no vague "AI will improve" — specific, testable predictions.

## Next Steps

1. [ ] Check domain availability for `tomorrowtimes.news` and alternatives
2. [ ] Scaffold Astro project with newspaper layout
3. [ ] Build proof-of-concept: generate one day's edition with a Python script + Claude API
4. [ ] Design masthead and visual identity
5. [ ] Set up GitHub repo and Actions pipeline
6. [ ] Generate first week of editions and review quality
7. [ ] Launch publicly with social media announcement

## Full Plan

See [PLAN.md](./PLAN.md) for complete details including content strategy, data sources, tech architecture, design direction, monetization ideas, and risk mitigations.
