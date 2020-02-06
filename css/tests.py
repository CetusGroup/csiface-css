# -*- coding: utf-8 -*-

import style

class Widget:
	
	def __init__(self, name, parent=None, styleClass=None):
		self._name = name
		self._parent = parent
		self._styleClass = styleClass
		self._styles = {
			'color': 'red'
		}
		self._children = {}
		if self._parent is not None:
			self._parent._children[self._name] = self

class P(Widget):
	
	def __init__(self, name, parent=None, styleClass=None):
		Widget.__init__(self, name, parent, styleClass)
		self._styles['font-family'] = None

class A(Widget):
	
	def __init__(self, name, parent=None, styleClass=None):
		Widget.__init__(self, name, parent, styleClass)
		self._styles['text-decoration'] = 'blink'

class H2(Widget):
	
	def __init__(self, name, parent=None, styleClass=None):
		Widget.__init__(self, name, parent, styleClass)
		self._styles['font-size'] = '110%'

css = u'''
P {
  font-family: Garamond, serif;
}
h2 {
  font-size: 110%;
  color: red;
  background: white;
}
.note {
  color: red;
  background: yellow;
  font-weight: bold;
  font-family: Times;
}
P#paragraph1 {
  margin: 0;
  font-family: New Times;
}
A:hover {
  text-decoration: none;
}
#news P {
  color: blue;
}
P A {
  font-weight: normal;
}
P A:sdfasdf {
  background-color: red;
}
'''


sm = style.CsStyleManager()
rules = sm.link(css)

p1 = P('paragraph1')
p2 = P('p2', p1, 'note')
a1 = A('a1', p2)
h2 = H2('caption', p1)

assert sm.calc(p1, rules) == {'color': 'red', 'font-family': None, u'margin': u'0'}
assert sm.calc(p2, rules) == {'font-family': None, u'background': u'yellow', 'color': 'red', u'font-weight': u'bold', u'margin': u'0'}
assert sm.calc(a1, rules) == {'font-weight': u'normal', u'background': u'yellow', 'color': 'red', 'font-family': None, u'margin': u'0', 'text-decoration': 'blink'}
assert sm.calcPseudo(a1, ["hover"], rules, inheritance=False) == {'hover': {u'text-decoration': u'none'}}

# selector test
assert style.SelectorWalker.isapplicable("P#paragraph1 P.note A", a1) == True
assert style.SelectorWalker.isapplicable("P#paragraph1 A", a1) == True

assert style.SelectorWalker.isapplicable("P A", a1) == True
assert style.SelectorWalker.isapplicable("P P#paragraph1 P.note A", a1) == False
assert style.SelectorWalker.isapplicable("P#paragraph1 H2 .note A", a1) == False
assert style.SelectorWalker.isapplicable("P#paragraph1 .note H2", h2) == False
assert style.SelectorWalker.isapplicable("P#paragraph1 H2", h2) == True
assert style.SelectorWalker.isapplicable("A", a1) == True
assert style.SelectorWalker.isapplicable("#a1", a1) == True
assert style.SelectorWalker.isapplicable(".note", p2) == True
assert style.SelectorWalker.isapplicable("P .note", p2) == True
assert style.SelectorWalker.isapplicable("P > A", a1) == True
assert style.SelectorWalker.isapplicable("P#paragraph1 >  A", a1) == False
assert style.SelectorWalker.isapplicable("P#paragraph1 > P  A", a1) == True
assert style.SelectorWalker.isapplicable("P A", style.PseudoNode("hover", a1)) == False
assert style.SelectorWalker.isapplicable("P A:hover", style.PseudoNode("hover", a1)) == True
assert style.SelectorWalker.isapplicable("P A:hover:eee", style.PseudoNode("hover:eee", a1)) == True
assert style.SelectorWalker.isapplicable("P A:hover:eee", style.PseudoNode("hover:eee", a1)) == True
assert style.SelectorWalker.isapplicable("P#paragraph1 P A:hover:eee", style.PseudoNode("hover:eee", a1)) == True
#print style.SelectorWalker.isapplicable("P#paragraph1 P", a1, enable_debug=True)

