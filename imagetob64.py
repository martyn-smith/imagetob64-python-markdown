"""
Python-Markdown base-64 encoder for images, based off the markdown-latex extension by Justin Bruce Van Horne <justinvh@gmail.com>

The rationale for this package is to ease sharing of webpages with embedded images, by encoding them as base64.
(Essentially the same approach as the aforementioned latex extension, but we already have the images).

To use, copy or link to the /extensions folder of your markdown installation (a python builtin, so wthin dist-packages)

Licensed under Public Domain Mark 1.0. 
See http://creativecommons.org/publicdomain/mark/1.0/
"""

from base64 import b64encode
import markdown
import re
import sys

# Base CSS template
IMG_CSS = \
        "<style scoped>img-inline { vertical-align: middle; }</style>\n"

regexp = re.compile("^!\[(.*)\]\((.*)\)$")

class ImagePreprocessor(markdown.preprocessors.Preprocessor):

    def __init__(self, args):
        assert(sys.version_info.major >= 3 and sys.version_info.minor >= 8)
        super().__init__(args)

    def run(self, lines):

        def embed(line):
            if im := regexp.match(line):
                png = open(im[2], "rb")
                data = png.read()
                data = bytes.decode(b64encode(data), "utf-8")
                png.close()
                return (f"<img class='' alt='{im[1]}' id='{im[1]}' src='data:image/png;base64,{data}'>")
            else:
                return line
        return [embed(l) for l in lines]

class ImagePostprocessor(markdown.postprocessors.Postprocessor):
    """This post processor extension just allows us to further
    refine, if necessary, the document after it has been parsed."""
    def run(self, text):
        # Inline a style for default behavior
        text = IMG_CSS + text
        return text

class MarkdownImage(markdown.Extension):
    """Wrapper for Preprocessor"""
    def extendMarkdown(self, md, md_globals):
        # Our base LaTeX extension
        md.preprocessors.add('image-to-b64',
                ImagePreprocessor(self), ">html_block")

def makeExtension(*args, **kwargs):
    """Wrapper for a MarkDown extension"""
    return MarkdownImage(*args, **kwargs)
