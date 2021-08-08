"""
date: 2021/4/30 15:20
author: lee sure
"""
import pytest

class TestClass:

    def setCheck(self, check):
        self.check=check

    @property
    def getCheck(self):
        return self.check

    def test_one(self):
      x = "this"
      assert 'h' in x

    def test_two(self):
      x = "hello"
      assert hasattr(x, 'check')

    def test_three(self):
      a = "hello"
      b = "hello world"
      assert a in b

if __name__=="__main__":
    pytest.main("-v, test_1.py")
# tc=TestClass()
# tc.setCheck("as")
# print(tc.check)
