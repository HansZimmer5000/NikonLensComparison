# Starts all testsuite available.

from ghitempipelinetestsuite import GhItemPipelineTestsuite
from CrawledLensTestsuite import CrawledLensTestsuite
from CrawledLensesTestsuite import CrawledLensesTestsuite
from MongoAccessTestsuite import MongoAccessTestsuite
from LensIntegrationTestsuite import LensIntegrationTestsuite
import unittest

if __name__ == '__main__':
    testClassesToRun = [
        GhItemPipelineTestsuite,
        CrawledLensTestsuite,
        CrawledLensesTestsuite,
        MongoAccessTestsuite,
        LensIntegrationTestsuite
    ]

    unittestLoader = unittest.TestLoader()

    AllTestSuites = [] 
    for test_class in testClassesToRun:
        suite = unittestLoader.loadTestsFromTestCase(test_class)
        AllTestSuites.append(suite)

    UnifiedSuite = unittest.TestSuite(AllTestSuites)

    testRunner = unittest.TextTestRunner()
    testRunner.run(UnifiedSuite)
