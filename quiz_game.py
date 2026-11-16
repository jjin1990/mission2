import json
import random
from datetime import datetime
from quiz import Quiz
from quiz_data import create_default_quizzes

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
        self.file_path = "state.json"
        self.quizzes = []
        self.best_score = None
        self.history = []
        self.load()

    def play_quiz(self):
        if len(self.quizzes) == 0:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return 0
        count = get_number("풀 문제 수를 입력하세요 (1-" + str(len(self.quizzes)) + "): ", 1, len(self.quizzes))
        print("📝 퀴즈를 시작합니다! (총 " + str(count) + "문제)")
        score = 0
        number = 1
        quizzes = random.sample(self.quizzes, count)        
        for quiz in quizzes:
            print("-" * 40)
            print("[문제 " + str(number) + "]")
            quiz.display()
            used_hint = False
            user_answer = get_number("정답 입력 (힌트: 0): ", 0, 4)
            if user_answer == 0:
                if quiz.hint == "":
                    print("💡 이 문제는 힌트가 없습니다.")
                else:
                    print("💡 힌트: " + quiz.hint)
                    used_hint = True
                user_answer = get_number("정답 입력: ", 1, 4)
            if quiz.check_answer(user_answer):
                if used_hint:
                    print("✅ 정답입니다! (힌트 사용: 0.5점)")
                    score = score + 0.5
                else:
                    print("✅ 정답입니다!")
                    score = score + 1
            else:
                print("❌ 오답입니다. 정답은 " + str(quiz.answer) + "번입니다.")
            number = number + 1
        print("=" * 40)
        print("🏆 결과: " + str(count) + "문제 중 " + str(score) + "점!")
        self.history.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "count": count,
            "score": score,
        })
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
        hint = get_text("힌트를 입력하세요: ")
        self.quizzes.append(Quiz(question, choices, answer, hint))
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

    def delete_quiz(self):
        if len(self.quizzes) == 0:
            print("⚠️ 삭제할 퀴즈가 없습니다.")
            return
        self.show_quiz_list()
        number = get_number("삭제할 퀴즈 번호 (1-" + str(len(self.quizzes)) + "): ", 1, len(self.quizzes))
        confirm = get_text("정말 삭제할까요? (y/n): ")
        if confirm != "y":
            print("삭제를 취소했습니다.")
            return
        removed = self.quizzes.pop(number - 1)
        print("🗑️ 삭제되었습니다: " + removed.question)

    def show_menu(self):
        print("=" * 40)
        print("       🎯 개발 작업실 기초 퀴즈 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 종료")
        print("=" * 40)

    def show_score(self):
        if self.best_score is None:
            print("⚠️ 아직 최고 점수가 없습니다.")
        else:
            print("🏆 최고 점수: " + str(self.best_score) + "점")
        if len(self.history) == 0:
            return
        print("📜 게임 기록 (총 " + str(len(self.history)) + "회)")
        print("-" * 40)
        number = 1
        for record in self.history:
            print("[" + str(number) + "] " + record["date"] + " | " + str(record["count"]) + "문제 중 " + str(record["score"]) + "점")
            number = number + 1
        print("-" * 40)

    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = []
            for item in data["quizzes"]:
                self.quizzes.append(Quiz(item["question"], item["choices"], item["answer"], item.get("hint", "")))
            self.best_score = data["best_score"]
            self.history = data.get("history", [])
            print("📂 저장된 데이터를 불러왔습니다. (퀴즈 " + str(len(self.quizzes)) + "개)")
        except FileNotFoundError:
            self.quizzes = create_default_quizzes()
            self.best_score = None
            self.history = []
            print("📂 저장 파일이 없어 기본 퀴즈로 시작합니다.")
        except (json.JSONDecodeError, KeyError, TypeError):
            self.quizzes = create_default_quizzes()
            self.best_score = None
            self.history = []
            print("⚠️ 저장 파일이 손상되어 기본 퀴즈로 복구합니다.")

    def save(self):
        data = {"quizzes": [], "best_score": self.best_score, "history": self.history}
        for quiz in self.quizzes:
            data["quizzes"].append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer,
                "hint": quiz.hint,
            })
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError:
            print("⚠️ 파일 저장 중 오류가 발생했습니다.")

    def run(self):
        while True:
            self.show_menu()
            try:
                choice = input("선택: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n프로그램을 종료합니다")
                self.save()
                break
            if choice == "1":
                score = self.play_quiz()
                if score > 0 and (self.best_score is None or score > self.best_score):
                    self.best_score = score
                    print("🎉 새로운 최고 점수입니다!")
                self.save()
            elif choice == "2":
                self.add_quiz()
                self.save()
            elif choice == "3":
                self.show_quiz_list()
            elif choice == "4":
                self.show_score()
            elif choice == "5":
                self.delete_quiz()
                self.save()
            elif choice == "6":
                print("프로그램을 종료합니다.")
                self.save()
                break
            else:
                print("⚠️ 잘못된 입력입니다. 1-6 사이의 숫자를 입력하세요")