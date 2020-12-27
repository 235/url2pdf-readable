# url2pdf-readable 
Scripts to convent a web article (URL) to a readable PDF. Designed to read web articles on e-readers.

Example:
`url2pdf-readable https://www.theguardian.com/tv-and-radio/2020/dec/15/the-archers-weird-genius-peculiarly-english-epic aaba21.pdf -f -v -r -s`

See `example_article.pdf` as output.

## How does it render a readable URL?

Offers two browsers to render and print a page to PDF:
  - Firefox:
    - Allows converting an article to a readable format
    - Cannot run headless to print into PDF yet [see bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1407238), uses Xvfb and xdotool to automate printing to a PDF using a full instance in a virtual framebuffer
  - Chrome:
    - Does not offer an experimental "readability" extension through the command line yet
    - Runs headless to print PDF

Dependencies:
  1. Firefox or Chrome
  2. Bash
  3. Xvfb and xdtool if using Firefox. E.g.: `sudo apt install xvfb xdotool`

Alternatives, and why they didn't work for me:
  1. `weasyprint` or `xhtml2pdf` are good reporting engines for HTML to PDF, but they require manual pagination, do not offer "readability" option.
  2. several solutions based on Node.js
 
## Platforms:
 - Linux
 - other Unix and MacOs could work

## Changelog:
v0.1:
 - initial release, Firefox support only
