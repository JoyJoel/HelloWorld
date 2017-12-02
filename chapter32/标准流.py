import sys

# sys.stdin 标准输入流,相当于input
# sys.stout 标准输出流,相当于print


sys.stdout.write('Hello')
print('请输入信息:');x = sys.stdin.readline()[:]

print(x)

sys.stderr.write('错误消息')
sys.stderr.flush()          # 清空缓存