def get_ question_afterlquestion_id = 0, qulz_1d=1):
open()
query
SELECT quiz_content. id, question.question, question.answer, question.wrong1, question.wrong:
FRON question, quiz_content
WHERE quiz_conten.question_id == question.id
AND quiz_content.id > ? AND quiz_content.quiz_id ==?
ORDER BY quiz_content.id "''
cursor.execute(query, [question_id, quiz_id] )
result = cursor. fetchone()
close()
return result
