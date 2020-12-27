# url2pdf-readable 
Scripts to convent a web article (URL) to a readable PDF. Designed to read web articles on e-readers.

Example:
`./url2pdf-readable https://writings.stephenwolfram.com/2019/07/mitchell-feigenbaum-1944-2019-4-66920160910299067185320382/ example_article.pdf --readable --scroll --delay 10`

See how [the article](https://writings.stephenwolfram.com/2019/07/mitchell-feigenbaum-1944-2019-4-66920160910299067185320382/) got converted into [`example_article.pdf`](https://github.com/235/url2pdf-readable/blob/main/example_article.pdf) output.

Command line options:
```
   Usage: url2pdf-readable [URL] [PDF_OUT_FILE] [--readable] [--verbose]
    URL                link to "print" into a PDF file
    PDF_OUT_FILE       name of the output PDF file

   Optional arguments:
     -f, --firefox     (default) use "$FIREFOX_BIN" to render a PDF file
     (TBD) -c, --chrome use "$CHROME_BIN" to render a PDF file
     -d n, --delay n   "n" seconds delay to download & render all images (10sec default)
     -r, --readable    covert URL webpage into a "readable" article
     -s, --scroll      scroll through the article to load lazy images
     -v, --verbose     increase the verbosity
     -h, --help        show this help message and exit
   (The last -c or -f option takes priority)
```

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
