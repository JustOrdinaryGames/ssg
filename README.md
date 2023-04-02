# ssg
A simple static-site generator written in Python.
## Compatibility
> This software supports both Linux (tested on Debian), and MacOS (tested on 2020 M1 Mac Mini)
## Usage
Note: This requires basic knowledge of HTML, and CSS in order to use successfully.
- Click [here](https://raw.githubusercontent.com/sbstnlol/ssg/master/ssg.py), and copy everything on screen into a new ``.py`` file on your computer.
- Move the ``.py`` file into an empty directory.
- Install the Markdown & BeautifulSoup libraries with ``python3 -m pip install markdown beautifulsoup4``
- Generate the required filestructure with ``python3 ssg.py``
- Edit ``layout/top.html`` & ``layout/bottom.html`` as needed, and create either ``.md`` or ``.html`` files in ``content/``
- When you're happy with what you've created, run ``python3 ssg.py`` again to generate your site. The files will appear in ``output/``