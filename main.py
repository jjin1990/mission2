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

def get_number(prompt, min_num, max_num):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("⚠️ 입력이 비어 있어요. 숫자를 입력하세요.")
            continue
        try:
            number = int(text)
        except ValueError:
            print("⚠️ 숫자를 입력하세요.")
            continue
        if number < min_num or number > max_num:
            print("⚠️ " + str(min_num) + "-" + str(max_num) + " 사이의 숫자를 입력하세요.")
            continue
        return number

def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("⚠️ 입력이 비어 있어요. 다시 입력하세요.")
            continue
        return text

class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None

    def play_quiz(self):
        if len(self.quizzes) == 0:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return 0
        print("📝 퀴즈를 시작합니다! (총 " + str(len(self.quizzes)) + "문제)")
        score = 0
        number = 1
        for quiz in self.quizzes:
            print("-" * 40)
            print("[문제 " + str(number) + "]")
            quiz.display()
            user_answer = get_number("정답 입력: ", 1, 4)
            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                score = score + 1
            else:
                print("❌ 오답입니다. 정답은 " + str(quiz.answer) + "번입니다.")
            number = number + 1
        print("=" * 40)
        print("🏆 결과: " + str(len(self.quizzes)) + "문제 중 " + str(score) + "문제 정답!")
        return score

    def add_quiz(self):
        print("📌 새로운 퀴즈를 추가합니다.")
        question = get_text("문제를 입력하세요: ")
        choices = []
        number = 1
        while number <= 4:
            choice = get_text("선택지 " + str(number) + ": ")
            choices.append(choice)
            number = number + 1
        answer = get_number("정답 번호 (1-4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        print("✅ 퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        if len(self.quizzes) == 0:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return
        print("📋 등록된 퀴즈 목록 (총 " + str(len(self.quizzes)) + "개)")
        print("-" * 40)
        number = 1
        for quiz in self.quizzes:
            print("[" + str(number) + "] " + quiz.question)
            number = number + 1
        print("-" * 40)
        
    def show_menu(self):
        print("=" * 40)
        print("       🎯 개발 작업실 기초 퀴즈 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def show_score(self):
        if self.best_score is None:
            print("⚠️ 아직 퀴즈를 풀지 않았습니다.")
        else:
            print("🏆 최고 점수: " + str(self.best_score) + "문제 정답")

    def run(self):
        while True:
            self.show_menu()
            try:
                choice = input("선택: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n프로그램을 종료합니다")
                break
            if choice == "1":
                score = self.play_quiz()
                if self.best_score is None or score > self.best_score:
                    self.best_score = score
                    print("🎉 새로운 최고 점수입니다!")
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quiz_list()
            elif choice == "4":
                self.show_score()
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요")


game = QuizGame()
game.run()