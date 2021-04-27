#!/usr/bin/env python3

import sys
import random

value = random.randint(0, 3)
print(f"Returing exit code of: {value}")
sys.exit(value)
