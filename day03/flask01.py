from flask import Flask

app = Flask(__name__)    # name 이름을 통한 flask 객체 생성

@app.route("/")          # 라우팅을 위한 뷰함수 등록  # /로 요청하면
def hello():             # hello 함수가 실행되어 
  return "안녕하시렵니까!!"  # 화면에 글이 나타남

if __name__=="__main__":    # 만약에 터미널에서 직접 실행 파일이 main이라는 함수로 바뀌면
  app.run(host="0.0.0.0", debug=True)  # 서버를 구동시켜라!!  # 실행을 위한 명령문으로 보면 된다
                                       # debug=True 는 작업한 내용 서버에 바로바로 반영이 된다
