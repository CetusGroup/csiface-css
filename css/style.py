# -*- coding: utf-8 -*-
import cssutils
from cssselect import parse


class StyleValue:
	"""
	1. «Ems» (em): «em» — это масштабируемая единица, которая используется в веб-документах.
		«em» равна текущему font-size,
		например, если font-size в документе 12pt, 1em равен 12pt.
		«em» масштабируема по своей природе, так 2em будет
		равен 24pt, 0.5em будет равна 6pt и т.д.
		Использование «em» становятся все более популярным в веб-документах из-за
		масштабируемости и возможности с пользой применять в мобильных устройствах.

	2. Pixels (px): «px» имеют фиксированный размер единиц,
		которые используются на экранах (например, для чтения на экране компьютера).
		Один пиксель равен одной точки на экране компьютера
		(самый малый элемент разрешения вашего экрана).
		Одна из проблем, с использованием px заключается в том, что эти единицы
		не позволяют изменять масштаб для слабовидящих читателей или мобильных устройств.
	3. Points (pt): «pt», традиционно используются в печатных СМИ
		(все, что должно быть напечатано на бумаге, и т.д.).
		Один «pt» равен 1 / 72 дюйма. «pt», так же, как и «px»,
		имеют фиксированный размер единицы и не могут масштабироваться.

	4. Percents (%): Единицы измерения в % похожи на «em»,
		за исключением нескольких принципиальных различий.
		Во-первых, текущий font-size равен 100% (т.е. 12pt = 100%).
		При использовании "%", ваш текст становится полностью
		масштабируемым для мобильных устройств и удобства пользователя (accessibility).
	"""
	_units = ("px", "pt", "em", "%")

	@classmethod
	def length(cls, value):
		for unit in cls._units:
			if value.endswith(unit):
				return (int(value[:len(value) - len(unit)]), unit)
		return (int(value), cls._units[0])

	@classmethod
	def font_family(cls, value):
		result = []
		for item in value.split(","):
			item = item.strip()
			if len(item) > 0:
				if item.startswith('\"') and item.endswith('\"'):
					item = item[1:-1]
				result.append(item)
		return result

	@classmethod
	def url(cls, value):
		return value[value.find("url(") + 4:value.find(")")].strip()


class PseudoNode:

	def __init__(self, name, parent=None, styleClass=None):
		self._name = "pseudo_node-%s" % name
		self._subnode = name
		self._parent = parent
		self._styleClass = styleClass
		self._styles = {}
		self._children = {}
	#if len(names) > 1:
	#	child = SubNode(names[1:], self, styleClass)
	#	self._children[child._name] = child

	def __repr__(self):
		return '%s[%s]' % (self.__class__.__name__, self._subnode)

class CsStyleManager:

	def link(self, css):
		"""возвращает результат парсинга в приложение"""
		rules = []
		sheet = cssutils.parseString(css)
		for rule in sheet:
			if rule.type == rule.STYLE_RULE:
				rules.append(rule)
		return rules

	def calc(self, node, rules, inheritance=True):
		"""возвращает словарь стилей узла"""
		styles = {}
		selectedRules = self.selectApplicableRules(node, rules)
		if inheritance and node._parent is not None:
			styles = self.calc(node._parent, rules)
		# styles = dict(styles, **node._styles)
		styles = dict(styles, **self.cascade(selectedRules))
		styles = dict(styles, **node._styles)
		return styles

	def calcPseudo(self, node, pseudo_nodes, rules, inheritance=True):
		"""возвращает словарь стилей для подузлов"""
		styles = {}
		for pseudo_node in pseudo_nodes:
			styles[pseudo_node] = self.calc(PseudoNode(pseudo_node, node), rules, inheritance)
		#styles[subnode] = self.calc(SubNode(subnode.split(":"), node), rules, inheritance)
		return styles

	def cascade(self, rules):
		specificity = {}
		styles = {}
		for selector, rule in rules:
			for style in rule.style:
				if style.name in styles:
					presence, idsNumber, classNumber, elementsNumber = specificity[style.name]
					if selector.specificity[1] < idsNumber and \
							selector.specificity[2] < classNumber and \
							selector.specificity[3] < elementsNumber:
						continue;
				styles[style.name] = style.value
				specificity[style.name] = selector.specificity
		return styles

	def selectApplicableRules(self, node, rules):
		result = []
		for rule in rules:
			for selector in rule.selectorList:
				# if self.isApplicable(node, selector):
				if SelectorWalker.isapplicable(selector.selectorText, node):
					result.append((selector, rule))
		return result
	"""
	# todo : add context selectors
	def isApplicable(self, node, selector):
		presence, idsNumber, classNumber, elementsNumber = selector.specificity
		nodeElement =node.__class__.__name__
		return  selector.selectorText == "*" or \
			selector.selectorText == nodeElement or \
			selector.selectorText == (".%s" % node._styleClass) or \
			selector.selectorText == ("#%s" % node._name) or \
			selector.selectorText == ("%s.%s" % (nodeElement, node._styleClass)) or \
			selector.selectorText == ("%s#%s" % (nodeElement, node._name))  or \
			selector.selectorText.find("%s:" % nodeElement) >= 0
	"""


class SelectorWalker:
	# debug ident
	_ident = 0
	_enable_debug = False

	@classmethod
	def isapplicable(cls, selector, node, enable_debug=False):
		cls._enable_debug = enable_debug
		s = parse(selector)
		for item in s:
			if cls.walk(item, node):
				return True
		return False

	@classmethod
	def walk(cls, element, node, parent=None):
		type_name = type(element).__name__
		proccessor = 'process_%s' % type_name.lower()
		if hasattr(cls, proccessor):
			method = getattr(cls, proccessor)
			cls._ident += 1
			result = method(element, node, parent=parent)
			cls._ident -= 1
			return result
		else:
			cls._debug("Warning !!! proccessor not found :", proccessor)
			return False

	@classmethod
	def _debug(cls, *args):
		if cls._enable_debug:
			print("%s%s" % ("  " * cls._ident, args))

	@classmethod
	def process_hash(cls, item, node, parent=None):
		cls._debug("Hash: ", item, node)
		return (item.id == "*" or item.id == node._name) and cls.walk(item.selector, node, item)

	@classmethod
	def process_class(cls, item, node, parent=None):
		cls._debug("Class: ", item, node)
		return item.class_name == node._styleClass and cls.walk(item.selector, node, item)

	@classmethod
	def process_attrib(cls, item, node, parent=None):
		cls._debug("Attrib: ", item, node)
		# print item.selector, item.namespace, item.attrib, item.operator, item.value
		if cls.operator == 'exists':
			return hasattr(node, item.attrib) and cls.walk(item.selector, node, item)
		else:
			return hasattr(node, item.attrib) and getattr(node, item.attrib) == item.value and cls.walk(item.selector, node, item)

	@classmethod
	def process_negation(cls, item, node, parent=None):
		cls._debug("Negation: ", item, node)
		return cls.walk(item.selector, node, item) and not cls.walk(item.subselector, node, item)

	@classmethod
	def process_pseudo(cls, item, node, parent=None):
		cls._debug("Pseudo: ", item, node)
		return isinstance(node, PseudoNode) and \
			   node._subnode == cls.get_full_pseudo_name(item) and \
			   cls.walk(cls.get_pseudo_element(item), node._parent, item)

	@classmethod
	def get_pseudo_element(cls, item):
		return item if type(item).__name__ != 'Pseudo' else  cls.get_pseudo_element(item.selector)

	@classmethod
	def get_full_pseudo_name(cls, item):
		return "%s:%s" % (cls.get_full_pseudo_name(item.selector), item.ident) if type(item.selector).__name__ == 'Pseudo' else item.ident

	@classmethod
	def process_function(cls, item, node, parent=None):
		cls._debug("Function: ", item, node)
		return cls.walk(item.selector)

	@classmethod
	def process_selector(cls, item, node, parent=None):
		cls._debug("Selector: ", item, node)
		# css3 support :: colon for pseudo (only at the end!!!)
		# cls._debug("!!!! Selector: ", item.pseudo_element)
		return cls.walk(item.parsed_tree, node, item)

	@classmethod
	def process_combinedselector(cls, item, node, parent=None):
		cls._debug("CombinedSelector : ", item, node)
		# cls._debug("combinator : ", item.combinator)
		# cls._debug("selector : ", item.selector)
		# cls._debug("subselector : ", item.subselector)
		# cls._debug("node : ", node)
		# cls._debug("parent : ", parent)
		return node is not None and \
			   cls.walk(item.subselector, node, item) and \
			   cls._proccess_context(item.selector, item.combinator, node, item)

	@classmethod
	def _proccess_context(cls, item, combinator, node, parent):
		cls._debug(" proccess_combinator: ", item, combinator, node)
		if node is None:
			return False
		if type(item).__name__ == "CombinedSelector":
			cls._debug("process_context.CombinedSelector : ", item)
			#cls._debug("process_context.combinator : ", item.combinator) 
			#cls._debug("process_context.selector : ", item.selector) 
			#cls._debug("process_context.subselector : ", item.subselector) 
			#cls._debug("process_context.node : ", node) 
			selectorNode = cls._findUp(item.subselector, node._parent, item)
			return  selectorNode is not None and \
					cls._proccess_context(item.selector, item.combinator, selectorNode, item)
		# return cls.process_context(item, node, parent)
		else:
			if combinator == ' ':
				return cls._findUp(item, node._parent, parent)
			elif combinator == '>':
				return cls.walk(item, node._parent, parent)
		return False

	@classmethod
	def process_element(cls, item, node, parent=None):
		cls._debug("Element: ", item.element, node)
		return item.element == "*" or item.element == node.__class__.__name__

	@classmethod
	def _findUp(cls, selector, node, parent):
		cls._debug("_findUp : ", selector, node)
		if node is None:
			return None
		if cls.walk(selector, node, parent):
			return node
		elif node._parent is not None:
			return cls._findUp(selector, node._parent, parent)
		else:
			return None

