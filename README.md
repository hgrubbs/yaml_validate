## YAML Validator and Jinja2 template renderer##

yaml_validate.py validates and PrettyPrints YAML.

jinja_render.py validates and renders jinja2 templates with variables provided by YAML.

### Example usage: ###

Validate YAML:
<pre><code>
# ./yaml_validate.py example.yml 
{'persons': [{'firstname': 'trillian',
              'lastname': 'mcmillan',
              'president': 'zaphod beeblebrox'},
             {'firstname': 'arthur',
              'lastname': 'dent',
              'president': 'zaphod beeblebrox'}]}
</code></pre>

Render Jinja2 template:
<pre><code>
# ./jinja_render.py example.yml example.j2 

People:

  First name: trillian
  Last name : mcmillan
  President : zaphod beeblebrox

  First name: arthur
  Last name : dent
  President : zaphod beeblebrox

</code></pre>
