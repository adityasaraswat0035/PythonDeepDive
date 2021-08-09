import sys
import counter
segments=sys.argv[1:]
full_text=' '.join(segments)
output='# words:{},#chars:{}'.format(*counter.count(full_text))
print(output)