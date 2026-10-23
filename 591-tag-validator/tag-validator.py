class Solution:
  def isValid(self, code: str) -> bool:
    if code[0] != '<' or code[-1] != '>':
      return False

    containsTag = False
    stack = []

    def isValidCdata(s: str) -> bool:
      return s.find('[CDATA[') == 0

    def isValidTagName(tagName: str, isEndTag: bool) -> bool:
      nonlocal containsTag
      if not tagName or len(tagName) > 9:
        return False
      if any(not c.isupper() for c in tagName):
        return False

      if isEndTag:
        return stack and stack.pop() == tagName

      containsTag = True
      stack.append(tagName)
      return True

    i = 0
    while i < len(code):
      if not stack and containsTag:
        return False
    
