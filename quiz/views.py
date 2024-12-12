import random
from django.shortcuts import render, redirect
from .models import Question, UserResponse

def start_quiz(request):
    # Initialize session variables for score and questions answered
    request.session['score'] = 0
    request.session['questions_answered'] = 0
    request.session['answered_questions'] = []  # Initialize answered questions list
    return redirect('get_question')

def get_question(request):
    # Fetch all questions from the database
    questions = list(Question.objects.all())
    
    # Get answered questions from the session, default to an empty list if not set
    answered_questions = request.session.get('answered_questions', [])
    
    # Filter out already answered questions
    unanswered_questions = [q for q in questions if q.id not in answered_questions]
    
    # If there are no unanswered questions, redirect to results
    if not unanswered_questions:
        return redirect('results')

    # Select a random question from unanswered ones and store its ID in the session
    question = random.choice(unanswered_questions)
    request.session['current_question_id'] = question.id

    return render(request, 'question.html', {'question': question})

def submit_answer(request):
    if request.method == "POST":
        selected_option = request.POST.get('option')
        question_id = request.session.get('current_question_id')
        
        # Fetch the current question from the database
        question = Question.objects.get(id=question_id)

        # Check if the selected option is correct
        is_correct = selected_option == question.correct_option

        # Save the user's response
        UserResponse.objects.create(
            question=question,
            selected_option=selected_option,
            is_correct=is_correct,
        )

        # Ensure 'score' is initialized before updating it
        if 'score' not in request.session:
            request.session['score'] = 0
            
        # Update session score and questions answered count
        request.session['score'] += int(is_correct)  
        
        if 'questions_answered' not in request.session:
            request.session['questions_answered'] = 0
            
        request.session['questions_answered'] += 1
        
        # Track the answered question ID
        answered_questions = request.session.get('answered_questions', [])
        answered_questions.append(question_id)
        request.session['answered_questions'] = answered_questions  # Update session

        # Redirect to get the next question
        return redirect('get_question')

def results(request):
    total_questions = request.session.get('questions_answered', 0)
    score = request.session.get('score', 0)

    context = {
        'total_questions': total_questions,
        'score': score,
        'correct_answers': score,
        'incorrect_answers': total_questions - score,
    }
    
    # Clear session data after displaying results (optional)
    if 'score' in request.session:
        del request.session['score']
    if 'questions_answered' in request.session:
        del request.session['questions_answered']
    if 'answered_questions' in request.session:
        del request.session['answered_questions']
    
    return render(request, 'results.html', context)
