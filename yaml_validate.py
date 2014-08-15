#!/usr/bin/env python
# Short program to validate and prettyprint parsed YAML, by Hunter Grubbs <hunter.grubbs@gmail.com>

import sys
try:
  import yaml
  import pprint
except Exception as e:
  print("Python modules 'yaml' and 'pprint' must both be installed/importable!")
  print("Error: %s" % (e))
  sys.exit(1)

if len(sys.argv) < 2:
  print("Usage: yaml_validate <YAML file>")
  sys.exit(1)

input_file = sys.argv[1]

try:
  unparsed_yaml = open(input_file).read()
except Exception as e:
  print("Failed to read %s!" % (input_file))
  print("Error: %s" % (e))
  sys.exit(1)

try:
  parsed_yaml = yaml.load(unparsed_yaml)
except Exception as e:
  print("Failed to parse %s!" % (input_file))
  print("Error: %s" % (e))
  sys.exit(1)

pp = pprint.PrettyPrinter()
pp.pprint(parsed_yaml)
