# shawnr.com

This is Shawn's code blog repository. It is built with Pelican and some other
stuff.

## Deployment

To deploy this site, you must run the following commands:

1. Build the deployment files: `pelican content -o output -s publishconf.py`
2. Sync to a `gh-pages` branch: `ghp-import output`
3. Push changes to `master` branch on Github: `git push git@github.com:shawnr/shawnr.github.io.git gh-pages:master`
