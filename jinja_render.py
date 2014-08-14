#!/usr/bin/env python
# Short program to validate and render Jinja2 templates with variables from a YAML file
# Supports sending a specific keys worth of data as top level variable to Jinja2

import sys

try:
  import yaml
  from jinja2 import Template
except Exception as e:
  print("Python modules 'yaml' and 'jinja' must both be installed/importable!")
  print("Error: %s" % (e))
  sys.exit(1)

if len(sys.argv) < 3:
  print("Usage: jinja_render <YAML file> <Jinja2 file> <YAML top-level variable>")
  sys.exit(1)

input_yaml= sys.argv[1]
input_jinja = sys.argv[2]
if len(sys.argv) == 4:
  top_level_key = sys.argv[3]
else:
  top_level_key = None

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

# assign top-level key if provided
if top_level_key is not None:
  try:
    parsed_yaml = parsed_yaml[top_level_key]
  except Exception as e:
    print("Failed to assign top-level-key %s" % (top_level_key))
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
