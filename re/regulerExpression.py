import re

multi_line = '''
<div>
你的头发还好吗
我还好
</div>
'''

pattern = re.compile(r'<div>(.*?)</div>',re.S)

ret = pattern.findall(multi_line)

print(ret)

string = 'i love you'

pattern = re.compile(r'l.*')

ret = pattern.sub('hate',string)

print(ret)

