import pandas as pd
from rapidfuzz.distance import Levenshtein  # 빠른 레벤슈타인 거리 계산 라이브러리

# 레벤슈타인 거리 기반 챗봇 클래스 정의
class LevenshteinChatBot:
    def __init__(self, filepath):
        # 질문과 답변 데이터를 불러옵니다
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()
        answers = data['A'].tolist()
        return questions, answers

    def find_best_answer(self, input_sentence):
        distances = [Levenshtein.distance(input_sentence, q) for q in self.questions]
        best_match_index = distances.index(min(distances))
        return self.answers[best_match_index]

if __name__ == "__main__":
    chatbot = LevenshteinChatBot("ChatbotData.csv")
    print("레벤슈타인 챗봇에 오신 것을 환영합니다! '종료'를 입력하면 종료됩니다.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "종료":
            print("챗봇을 종료합니다.")
            break
        print("Chatbot:", chatbot.find_best_answer(user_input))
