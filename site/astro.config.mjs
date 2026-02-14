import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://tomorrow-times.pages.dev',
  output: 'static',
  
  // Cloudflare Pages configuration
  adapter: undefined, // Static site, no adapter needed
  
  vite: {
    ssr: {
      external: [],
    },
  },
});
