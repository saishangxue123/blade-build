# Copyright (c) 2011 Tencent Inc.
# All rights reserved.
#
# Author: Michaelpeng <michaelpeng@tencent.com>
# Date:   October 20, 2011


"""
 This is the test module for prebuild_cc_library target.

"""


import blade_test


class TestPrebuildCcLibrary(blade_test.TargetTest):
    """Test cc_library """
    def setUp(self):
        """setup method. """
        self.doSetUp('cc')

    def testGenerateRules(self):
        """Test that rules are generated correctly.

        Scons can use the rules for dry running.

        """
        self.assertTrue(self.runBlade())
        copy_lower_line = self.findCommand('cp ')
        com_upper_line = self.findCommand(['puppercase.cpp.o', '-c'])
        upper_depends_libs = self.findCommand('libuppercase.so')

        self.assertIn('cc/libprebuilt.so', copy_lower_line)
        self.assertIn('lib64/libprebuilt.so', copy_lower_line)

        self.assertTrue(upper_depends_libs)
        self.assertIn('libuppercase.so', upper_depends_libs)


if __name__ == '__main__':
    blade_test.run(TestPrebuildCcLibrary)
