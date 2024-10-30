# 문자열 첫 글자 대문자로
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])

print(capitalize('fooBar')) # Foobar
print(capitalize('foobar', True)) # Foobar

# 1자리 미만
print('foobar'[:1]) # f
# 1자리 이상
print('foobar'[1:]) # oobar
# 대문자 변환
print('foobar'.upper()) # FOOBAR
# 소문자 변환
print('foobar'.lower()) # foobar