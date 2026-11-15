from quiz import Quiz

def create_default_quizzes():
    quizzes = [
        Quiz("지금 내가 있는 폴더의 경로를 보여 주는 명령은?", ["ls", "cd", "pwd", "mkdir"], 3),
        Quiz("숨김 파일까지 목록으로 보여 주는 명령은?", ["ls", "ls -a", "ls -l", "pwd"], 2),
        Quiz("chmod 600을 적용한 파일의 권한은?", ["주인만 읽고 쓰기", "모두 읽고 쓰기", "주인만 실행", "모두 읽기만"], 1),
        Quiz("docker run -p 8080:80 에서 8080은?", ["컨테이너 안 포트", "내 컴퓨터(호스트) 포트", "이미지 버전", "컨테이너 개수"], 2),
        Quiz("컨테이너를 삭제해도 데이터를 남기는 방법은?", ["docker stop", "볼륨 연결", "docker ps", "이미지 다시 빌드"], 2),
    ]
    return quizzes
