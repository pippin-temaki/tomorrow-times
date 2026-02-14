#!/usr/bin/env python3
"""
article_generator.py - Newspaper Article Generator
Transforms events into journalistic articles
"""

import json
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


# AI Journalist personas
JOURNALISTS = {
    "aria_chen": {
        "name": "Aria Chen",
        "title": "Technology Correspondent",
        "expertise": ["ai", "tech", "computing", "internet"],
        "style": "clear_technical_explainer"
    },
    "james_okafor": {
        "name": "James Okafor",
        "title": "World Affairs Editor",
        "expertise": ["geopolitics", "conflicts", "diplomacy", "international"],
        "style": "analytical_balanced"
    },
    "sofia_martinez": {
        "name": "Sofia Martinez",
        "title": "Business & Markets",
        "expertise": ["economy", "markets", "companies", "trade"],
        "style": "data_driven"
    },
    "lena_park": {
        "name": "Dr. Lena Park",
        "title": "Science & Environment",
        "expertise": ["climate", "science", "health", "space"],
        "style": "accessible_scientific"
    },
    "marcus_webb": {
        "name": "Marcus Webb",
        "title": "Culture & Sports",
        "expertise": ["entertainment", "sports", "culture", "social"],
        "style": "engaging_narrative"
    },
    "the_editor": {
        "name": "The Editorial Board",
        "title": "Opinion/Editorials",
        "expertise": ["meta", "analysis", "opinion"],
        "style": "thoughtful_provocative"
    }
}


class ArticleGenerator:
    """Generates newspaper articles from events"""
    
    def __init__(self, world_state_dir: str = "../world-state"):
        self.world_state_dir = Path(world_state_dir)
        self.world_state = self._load_world_state()
        self.events = self._load_today_events()
        self.articles = []
    
    def _load_world_state(self) -> Dict[str, Any]:
        """Load current world state"""
        state = {}
        for yaml_file in self.world_state_dir.glob("*.yaml"):
            with open(yaml_file, 'r') as f:
                state[yaml_file.stem] = yaml.safe_load(f)
        return state
    
    def _load_today_events(self) -> List[Dict]:
        """Load today's generated events"""
        sim_date = self.world_state['meta']['current_date']
        events_path = self.world_state_dir / "events" / f"{sim_date}.yaml"
        
        if events_path.exists():
            with open(events_path, 'r') as f:
                data = yaml.safe_load(f)
                return data.get('events', [])
        
        return []
    
    def assign_journalist(self, event: Dict) -> Dict:
        """Match event to appropriate journalist persona"""
        domain = event.get('domain', 'general')
        
        # Simple matching logic - can be more sophisticated
        for journalist_id, journalist in JOURNALISTS.items():
            if any(keyword in domain for keyword in journalist['expertise']):
                return journalist
        
        # Default to general reporter
        return JOURNALISTS['james_okafor']
    
    def prioritize_events(self) -> List[Dict]:
        """Rank events by newsworthiness for article selection
        
        Factors:
        - Impact level (major > moderate > minor)
        - Narrative arc relevance (active arcs get priority)
        - Novelty vs continuity balance
        - Section diversity
        """
        # STUB: Simple sorting by impact
        impact_order = {"major": 3, "moderate": 2, "minor": 1}
        
        return sorted(
            self.events,
            key=lambda e: impact_order.get(e.get('impact', 'minor'), 0),
            reverse=True
        )
    
    def generate_articles(self, target_count: int = 8) -> List[Dict]:
        """Generate articles from prioritized events
        
        TODO: LLM article writing
        - For each event, generate a full newspaper article
        - Use appropriate journalist persona
        - Write in deadpan journalistic style (treating future as present)
        - Include:
          * Headline (punchy, informative)
          * Lede paragraph (who/what/when/where/why)
          * Body (2-4 paragraphs with quotes, context, analysis)
          * Confidence level (based on prediction uncertainty)
        
        LLM Prompt Structure:
        "You are {journalist_name}, {journalist_title} for The Tomorrow Times,
        writing on {future_date}. Given this event and world state context,
        write a news article. Treat the future date as the present.
        Include plausible quotes from relevant sources. Write in AP style."
        """
        print("📰 Generating newspaper articles...")
        
        prioritized = self.prioritize_events()[:target_count]
        
        for event in prioritized:
            journalist = self.assign_journalist(event)
            
            # STUB: Placeholder article generation
            # Real implementation uses LLM here
            
            article = {
                "headline": event.get('title', 'Untitled'),
                "byline": journalist['name'],
                "journalist_id": journalist,
                "section": self._assign_section(event),
                "confidence": self._calculate_confidence(event),
                "lede": "[PLACEHOLDER LEDE - LLM will generate]",
                "body": "[PLACEHOLDER BODY - LLM will generate full article text]",
                "event_ref": event.get('id'),
                "size": self._determine_article_size(event),
            }
            
            self.articles.append(article)
        
        print(f"  Generated {len(self.articles)} articles")
        return self.articles
    
    def _assign_section(self, event: Dict) -> str:
        """Assign article to newspaper section"""
        domain = event.get('domain', 'general')
        
        section_map = {
            'geopolitics': 'world',
            'technology': 'tech',
            'economy': 'business',
            'science': 'science',
            'climate': 'science',
            'culture': 'culture',
            'sports': 'culture',
        }
        
        return section_map.get(domain, 'general')
    
    def _calculate_confidence(self, event: Dict) -> str:
        """Determine confidence level for article"""
        probability = event.get('probability', 0.5)
        
        if probability >= 0.7:
            return 'high'
        elif probability >= 0.4:
            return 'medium'
        else:
            return 'speculative'
    
    def _determine_article_size(self, event: Dict) -> str:
        """Determine display size (major/secondary/standard)"""
        impact = event.get('impact', 'minor')
        
        size_map = {
            'major': 'major',
            'moderate': 'secondary',
            'minor': 'standard',
        }
        
        return size_map.get(impact, 'standard')
    
    def save_articles(self, output_dir: str = "../site/src/content/editions"):
        """Save articles as markdown files for Astro"""
        sim_date = self.world_state['meta']['current_date']
        
        edition_dir = Path(output_dir) / sim_date
        edition_dir.mkdir(parents=True, exist_ok=True)
        
        for article in self.articles:
            filename = f"{article['section']}-{article['event_ref']}.md"
            filepath = edition_dir / filename
            
            # Write as markdown with frontmatter
            with open(filepath, 'w') as f:
                f.write("---\n")
                f.write(yaml.dump({
                    "headline": article['headline'],
                    "byline": article['byline'],
                    "section": article['section'],
                    "confidence": article['confidence'],
                    "size": article['size'],
                    "date": sim_date,
                }))
                f.write("---\n\n")
                f.write(f"**{article['lede']}**\n\n")
                f.write(article['body'])
        
        print(f"📁 Articles saved to {edition_dir}")


def main():
    """Main entry point"""
    generator = ArticleGenerator()
    articles = generator.generate_articles()
    generator.save_articles()
    
    print(f"\n✅ Generated {len(articles)} articles")


if __name__ == "__main__":
    main()
