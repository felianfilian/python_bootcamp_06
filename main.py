from us_states import us_states_quiz
import list_comp
import square_numbers
import data_overlap

# pong.start()
# crossing.start()
# mail_merge.start()
# csv_test.start()
# us_states_quiz.start()
# list_comp.start()
# square_numbers.start()
# data_overlap.start()

temps = {"Monday": 12, "Tuesday": 18, "Wednesday": 9}
temp_far = {day:(temp*9/5)+32 for (day, temp) in temps.items()}
print(temp_far)
