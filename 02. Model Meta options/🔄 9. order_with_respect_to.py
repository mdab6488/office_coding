# Purpose: Makes the object orderable relative to a foreign key (e.g., ordering answers within a question).

class Question(models.Model):
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        order_with_respect_to = 'question'

# Methods Added: get_answer_order(), set_answer_order(), get_next_in_order(), get_previous_in_order() 