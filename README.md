# shawnr.com

This is Shawn's code blog repository. It is built with Pelican and some other
stuff.

## Setup

This site uses Pelican.

1. `pip install pelican markdown`
2. Clone the Pelican Themes repo: https://github.com/getpelican/pelican-themes/
3. Install the Flex theme: `pelican-themes -vi ~/path/to/pelican-themes/Flex`

## Deployment

To deploy this site, you must run the following commands:

1. Build the deployment files: `pelican content -o output -s publishconf.py`
2. Sync to a `gh-pages` branch: `ghp-import output`
3. Push changes to `master` branch on Github: `git push git@github.com:shawnr/shawnr.github.io.git gh-pages:master`
