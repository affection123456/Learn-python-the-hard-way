# encoding: utf-8
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
   "I had this thing.", 
   "That you could type up right.", 
   "But it didn't sing.", 
   "So I said goodnight."
)  # It's just a style.

# If you are printing Chinese, please use %s and don't use %r.Try the code below.
# print formatter % (u'平', u'凡', u'之', u'路')