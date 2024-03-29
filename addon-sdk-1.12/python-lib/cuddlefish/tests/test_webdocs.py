# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import unittest

from cuddlefish.docs import webdocs

class WebDocTests(unittest.TestCase):

    def test_create_guide1_doc(self):
        root = os.path.join(os.getcwd() + \
            '/python-lib/cuddlefish/tests/static-files')
        web_docs = webdocs.WebDocs(root)
        guide = web_docs.create_guide_page(os.path.join(\
            root + '/doc/dev-guide-source/index.md'))
        self._test_common_contents(guide)
        self.assertTrue(\
            '<title>An Imposing Title - Add-on SDK Documentation</title>'\
            in guide)
        self.assertTrue('<p><em>Some words!</em></p>'\
            in guide)
        self.assertTrue('<div id="version">Version '\
            in guide)

    def test_create_guide2_doc(self):
        root = os.path.join(os.getcwd() + \
            '/python-lib/cuddlefish/tests/static-files')
        web_docs = webdocs.WebDocs(root)
        guide = web_docs.create_guide_page(os.path.join(\
            root + '/doc/dev-guide-source/no_h1.md'))
        self._test_common_contents(guide)
        self.assertTrue('<title>Add-on SDK Documentation</title>'\
            in guide)
        self.assertTrue('<h2>A heading</h2>'\
            in guide)

    def test_create_module_doc(self):
        root = os.path.join(os.getcwd() + \
            '/python-lib/cuddlefish/tests/static-files')
        web_docs = webdocs.WebDocs(root)
        module = web_docs.create_module_page(os.path.join(\
            root + '/doc/module-source/sdk/aardvark-feeder.md'))
        self._test_common_contents(module)
        self.assertTrue(\
            '<title>aardvark-feeder - Add-on SDK Documentation</title>'\
            in module)
        self.assertTrue(\
            '<h1>aardvark-feeder</h1>'\
            in module)
        self.assertTrue(\
            '<div class="module_description">'\
            in module)
        self.assertTrue(\
            '<p>The <code>aardvark-feeder</code> module simplifies feeding aardvarks.</p>'\
            in module)
        self.assertTrue(\
            '<h2 class="api_header">API Reference</h2>'\
            in module)
        self.assertTrue(\
            '<h3 class="api_header">Functions</h3>'\
            in module)
        self.assertTrue(\
            '<h4 class="api_name">feed(food)</h4>'\
            in module)
        self.assertTrue(
            '<p>Feed the aardvark.</p>'\
            in module)

    def _test_common_contents(self, doc):
        self.assertTrue(\
            '<a href="modules/sdk/anteater/anteater.html">anteater/anteater</a>' in doc)
        self.assertTrue(\
            '<a href="modules/sdk/aardvark-feeder.html">aardvark-feeder</a>' in doc)

if __name__ == "__main__":
    unittest.main()
