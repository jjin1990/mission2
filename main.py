while True:
    print("=" * 40)
    print("       🎯 개발 작업실 기초 퀴즈 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)
    choice = input("선택: ").strip()
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
