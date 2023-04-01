# ssg
A simple static-site generator written in Python.
## Compatibility
This works on my system, which runs Debian Bullseye. It probably works on other Linux distributions as well.
## Usage
- Clone this repository.
- Make sure you have Python 3+ installed, as well as the ``markdown`` package.
- Run ``python3 ssg.py`` to generate your output.
- Modify your top and bottom templates in ``layout/``, and write pure Markdown in ``content/``. Alternatively, feel free to write HTML pages - the top & bottom layouts will be pasted in, just like with Markdown.