from trac.timeline.tests.functional import functionalSuite


def suite():
    suite = unittest.TestSuite()
    suite.addTest(web_ui.suite())
    suite.addTest(wikisyntax.suite())
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
