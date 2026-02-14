#!/usr/bin/env python3
"""
publisher.py - Publication Pipeline Orchestrator
Coordinates the entire daily pipeline and triggers site build
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path


class Publisher:
    """Orchestrates the daily publication pipeline"""
    
    def __init__(self):
        self.pipeline_dir = Path(__file__).parent
        self.project_root = self.pipeline_dir.parent
        self.site_dir = self.project_root / "site"
    
    def run_pipeline(self):
        """Execute the complete daily pipeline"""
        print("=" * 60)
        print("🗞️  THE TOMORROW TIMES - DAILY PUBLICATION PIPELINE")
        print("=" * 60)
        print(f"Started: {datetime.now()}\n")
        
        try:
            # Step 1: Fetch real-world signals
            print("\n[1/6] 🔍 FETCHING SIGNALS")
            self._run_script("fetch_signals.py")
            
            # Step 2: Generate events (evolve world state)
            print("\n[2/6] 🎲 GENERATING EVENTS")
            self._run_script("event_engine.py")
            
            # Step 3: Generate articles
            print("\n[3/6] 📰 GENERATING ARTICLES")
            self._run_script("article_generator.py")
            
            # Step 4: Editorial review
            print("\n[4/6] 📋 EDITORIAL REVIEW")
            self._run_script("editor.py")
            
            # Step 5: Build Astro site
            print("\n[5/6] 🏗️  BUILDING SITE")
            self._build_site()
            
            # Step 6: Commit changes to git
            print("\n[6/6] 💾 COMMITTING TO GIT")
            self._commit_changes()
            
            print("\n" + "=" * 60)
            print("✅ PUBLICATION COMPLETE")
            print("=" * 60)
            
        except Exception as e:
            print(f"\n❌ PIPELINE FAILED: {e}")
            sys.exit(1)
    
    def _run_script(self, script_name: str):
        """Run a pipeline script"""
        script_path = self.pipeline_dir / script_name
        
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=self.pipeline_dir,
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        
        if result.returncode != 0:
            print(f"Error in {script_name}:")
            print(result.stderr)
            raise Exception(f"{script_name} failed")
    
    def _build_site(self):
        """Build the Astro static site"""
        print("  Building Astro site...")
        
        # Install dependencies if needed
        if not (self.site_dir / "node_modules").exists():
            print("  Installing dependencies...")
            subprocess.run(
                ["npm", "install"],
                cwd=self.site_dir,
                check=True
            )
        
        # Build site
        result = subprocess.run(
            ["npm", "run", "build"],
            cwd=self.site_dir,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("  ✅ Site built successfully")
        else:
            print("  ❌ Build failed:")
            print(result.stderr)
            raise Exception("Site build failed")
    
    def _commit_changes(self):
        """Commit world state and content changes to git"""
        print("  Committing changes...")
        
        # Get current simulation date
        import yaml
        meta_path = self.project_root / "world-state" / "meta.yaml"
        with open(meta_path, 'r') as f:
            meta = yaml.safe_load(f)
            sim_date = meta['current_date']
        
        # Git add
        subprocess.run(
            ["git", "add", "world-state/", "site/src/content/"],
            cwd=self.project_root,
            check=True
        )
        
        # Git commit
        commit_msg = f"Edition {sim_date} - Daily update"
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=self.project_root,
            check=True
        )
        
        print(f"  ✅ Committed: {commit_msg}")
    
    def preview_site(self):
        """Start dev server for preview"""
        print("🌐 Starting preview server...")
        print("   Visit http://localhost:4321")
        print("   Press Ctrl+C to stop\n")
        
        subprocess.run(
            ["npm", "run", "dev"],
            cwd=self.site_dir
        )


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="The Tomorrow Times Publisher")
    parser.add_argument(
        '--preview',
        action='store_true',
        help='Start preview server instead of running pipeline'
    )
    
    args = parser.parse_args()
    
    publisher = Publisher()
    
    if args.preview:
        publisher.preview_site()
    else:
        publisher.run_pipeline()


if __name__ == "__main__":
    main()
