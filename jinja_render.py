#!/usr/bin/env python
# Short program to validate and render Jinja2 templates with variables from a YAML file
import pdb

import sys
try:
  import yaml
  from jinja2 import Template
except Exception as e:
  print("Python modules 'yaml' and 'jinja' must both be installed/importable!")
  print("Error: %s" % (e))
  sys.exit(1)

if len(sys.argv) < 2:
  print("Usage: jinja_render <yaml file> <jinja2 file>")
  sys.exit(1)

input_yaml= sys.argv[1]
input_jinja = sys.argv[2]

# read yaml file
try:
  unparsed_yaml = open(input_yaml).read()
except Exception as e:
  print("Failed to read %s!" % (input_yaml))
  print("Error: %s" % (e))
  sys.exit(1)

# parse yaml file
try:
  parsed_yaml = yaml.load(unparsed_yaml)
except Exception as e:
  print("Failed to parse %s!" % (input_file))
  print("Error: %s" % (e))
  sys.exit(1)

# read jinja2 template
try:
  j2_raw_template = open(input_jinja).read()
except Exception as e:
  print("Failed to read %s!" % (input_jinja))
  print("Error: %s" % (e))
  sys.exit(1) 

#render jinja2 template
try:
  j2_template = Template(j2_raw_template)
  print(j2_template.render(parsed_yaml))
except Exception as e:
  sys.stderr.write("Failed to parse %s\n" % (input_jinja))
  sys.stderr.write("Error: %s\n" % (e))
  sys.exit(1)
