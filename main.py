class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)
        number = 1
        for choice in self.choices:
            print(str(number) + ". " + choice)
            number = number + 1

    def check_answer(self, user_answer):
        return user_answer == self.answer
def create_default_quizzes():
    quizzes = [
        Quiz("지금 내가 있는 폴더의 경로를 보여 주는 명령은?", ["ls", "cd", "pwd", "mkdir"], 3),
        Quiz("숨김 파일까지 목록으로 보여 주는 명령은?", ["ls", "ls -a", "ls -l", "pwd"], 2),
        Quiz("chmod 600을 적용한 파일의 권한은?", ["주인만 읽고 쓰기", "모두 읽고 쓰기", "주인만 실행", "모두 읽기만"], 1),
        Quiz("docker run -p 8080:80 에서 8080은?", ["컨테이너 안 포트", "내 컴퓨터(호스트) 포트", "이미지 버전", "컨테이너 개수"], 2),
        Quiz("컨테이너를 삭제해도 데이터를 남기는 방법은?", ["docker stop", "볼륨 연결", "docker ps", "이미지 다시 빌드"], 2),
    ]
    return quizzes

def show_menu():
    print("=" * 40)
    print("       🎯 개발 작업실 기초 퀴즈 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)

quizzes = create_default_quizzes()

while True:
    show_menu()
    try:
        choice = input("선택: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n프로그램을 종료합니다")
        break
    if choice == "1":
        print("퀴즈 풀기 (준비 중)")
    elif choice == "2":
        print("퀴즈 추가 (준비 중)")
    elif choice == "3":
        print("퀴즈 목록 (준비 중)")
    elif choice == "4":
        print("점수 확인 (준비 중)")
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요")
