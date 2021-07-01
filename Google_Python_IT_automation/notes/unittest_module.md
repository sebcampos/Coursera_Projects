# unittest module

The unit test module can be imported like so:
```
import unittest
```

Then a class object can be created to perform the test.
In this case we will import a function from a non existent library and use unittest to test it

```
from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
	def test_basic(self):
		testcase = "Lovelace, Ada"
		expected = "Ada Lovelace"
		self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
```



