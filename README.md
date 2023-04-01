# ssg
A simple static-site generator written in Python.
## Compatibility
> This software supports both Linux (tested on Debian), and MacOS (tested on 2020 M1 Mac Mini)
## Usage
- Clone (or fork) this repository.
- Make sure you have Python 3+ installed.
- Run ``python3 -m pip install markdown``
- Edit the templates in ``layout/``, and the pages in ``content/`` - Markdown & HTML content are both supported.
- When you're happy with what you've done, run ``python3 ssg.py`` to generate your site. The files will show up in ``output/``
- If you want to edit the appearance of your website, edit ``static/style.css`` with your own custom CSS.
## Hosting
If you'd like to deploy your site automatically, check out ``ci/github.yml`` for a GitHub Actions workflow. This automatically logs into your server, and uploads your site to a specified path. You have to do some more configuration on your server - [here](https://youtu.be/ATenAnk8eX4)'s a helpful video on how.