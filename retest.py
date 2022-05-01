import re
import MeCab

hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')

text = '배송받기까지 12일 걸림. 연계된 택배사 확인 후 연락준다던 &#39;논픽션&#3'

print(hangul.sub('', text))