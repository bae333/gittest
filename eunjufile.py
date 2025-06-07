import pandas as pd
from rapidfuzz.distance import Levenshtein  # 레벤슈타인 거리 계산 라이브러리 불러오기

# 레벤슈타인 거리 기반의 간단한 챗봇 클래스 정의
class LevenshteinChatBot:
    def __init__(self, filepath):
        # 파일 경로를 받아 학습용 질문과 답변 데이터를 불러옵니다.
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        """
        학습 데이터 CSV 파일을 불러와 질문(Q)과 답변(A)을 리스트 형태로 추출하는 함수
        """
        data = pd.read_csv(filepath)          # CSV 파일 읽기
        questions = data['Q'].tolist()        # 질문 컬럼(Q)을 리스트로 저장
        answers = data['A'].tolist()          # 답변 컬럼(A)을 리스트로 저장
        return questions, answers

    def find_best_answer(self, input_sentence):
        """
        사용자가 입력한 문장(input_sentence)과 학습 데이터의 각 질문 간
        레벤슈타인 거리를 계산하여 가장 유사한 질문의 답변을 반환하는 함수
        """
        # 모든 학습 질문과 입력 문장의 레벤슈타인 거리 계산
        distances = [Levenshtein.distance(input_sentence, q) for q in self.questions]
        
        # 가장 짧은 거리(= 가장 유사한 질문)의 인덱스 추출
        best_match_index = distances.index(min(distances))
        
        # 해당 인덱스에 해당하는 답변 반환
        return self.answers[best_match_index]

# 메인 실행 부분
if __name__ == "__main__":
    chatbot = LevenshteinChatBot("ChatbotData.csv")  # 챗봇 객체 생성
    print("레벤슈타인 챗봇에 오신 것을 환영합니다! '종료'를 입력하면 종료됩니다.")

    # 사용자와 대화 루프 실행
    while True:
        user_input = input("You: ")
        if user_input.lower() == "종료":  # 사용자가 '종료'를 입력하면 루프 종료
            print("챗봇을 종료합니다.")
            break
        response = chatbot.find_best_answer(user_input)  # 가장 유사한 질문의 답변 찾기
        print("Chatbot:", response)  # 챗봇의 응답 출력
