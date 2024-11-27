from survey import AnonymouseSurvey

question = "最初に勉強した言語は何ですか？"
language_survey = AnonymouseSurvey(question)

language_survey.show_question
print("'q' を入力すると終了します\n")
while True:
    response = input("言語: ")
    if response == 'q':
        break
    language_survey.store_response(response)

print("\nアンケート調査にご協力ありがとうございます！")
language_survey.show_results()

