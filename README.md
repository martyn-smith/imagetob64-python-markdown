Python-Markdown base-64 encoder for images
===

Based off the markdown-latex extension by Justin Bruce Van Horne (justinvh@gmail.com).

Rationale
---
The rationale for this package is to ease sharing of webpages with embedded images, by encoding them as base64.

Requirements
---
Python ^= 3.8
Markdown ^= 3.3.4

Installation
---
To install, copy or link to the /extensions folder of your markdown installation (This is a python builtin, so wthin dist-packages).
To use, add to markdown extensions like so: markdown(foo, extensions=["markdown.extensions.imagetob64"])

License and Guarantee
---
Licensed under Public Domain Mark 1.0. 
See http://creativecommons.org/publicdomain/mark/1.0/
ABSOLUTELY NO GUARANTEE provided.
