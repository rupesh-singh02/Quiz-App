from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # A, B, C, or D

    def __str__(self):
        return self.text

class UserResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1)  # A, B, C, or D
    is_correct = models.BooleanField()

    def __str__(self):
        return f"{self.question.text} - {self.selected_option}"
