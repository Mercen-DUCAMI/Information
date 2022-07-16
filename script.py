import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.instagram.com/mercen_lee/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["red", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "이석호")
write("description", "대구소프트웨어마이스터고 7기")
write("button", "인스타그램")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "생년월일": "2006년 2월 17일",
  "사용하는 언어": "파이썬과 스위프트",
  "좋아하는 것": "애플 제품들",
  "싫어하는 것": "C언어"
}
information(informations)
