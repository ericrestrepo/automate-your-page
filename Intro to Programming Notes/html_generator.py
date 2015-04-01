Session_Notes = ['Telling Computers What to Do',
                            [['Introduction to Serious Programming',
                            [['Title 1', 'Description 1'],
                             ['Title 2', 'Description 2'],
                             ['Title 3', 'Description 3']]],
                            ['Variables and Strings',
                            [['Variable', 'We use variables to create a name and to assign that name a value. In Python when we use the equals sign, it does not mean it does not mean equal, it means assignment. The format is: Name = Expression, for example: number = 8 * 5. Another way to think of this is that now the name refers to that value is was assigned and we use an arrow to represent this relationship. It is also important to note that variables can vary and they can change value throughout the program, so they may not refer to the same value at all times.'],
                             ['Strings', 'In the early days of computers people thought of computers as just large calculators that could do big computations, but it turns out computers anc operate on any data structure available. A string is an example of this type of data. A string is a sequence of characters surrounded by quotes. For example: "I like cookies". We can actually use the double quotes or the single quotes, but we just have to start and end with the same type. With strings it is important that we know that the operators work differently than with numbers and variables. For example the plus operator does not mean plus, but instead concatenation.'],
                             ['Indexing Strings', 'With strings we have a unique ability to extract a subsequence of characters and this is what is meant by indexing. To index a string we have to use square brackets and select the location we want to index. For example: "Eric"[0] --> "E". Also when we use negative numbers that means we start the indexing from the back of the string. For example: "Eric"[-1] --> "c". In addition to selecting an individual character in a string we can also select a sub sequence of a string. The structure for this is as follows: <string>[<expression>:<expression>] where the expressions must be equivant to numbers and the first expression is the start and the second is the end of the sub sequence.'],
                             ['Finding Strings in Strings', 'Using find is a built in Python method that work just like a proceedure we can define. It works like: <string>.find(<string>) and the output is the first position of the second input string in the first string. If the target string is not found the value produced is -1. ']]],
                             ['Inputs -> Functions -> Outputs',
                            [['Using Proceedures (Functions)', 'A proceedure is made like this: <proceedure>(<input>, <input>, ...) and it can have as many inputs as possible. The inputs are sometimes called opperands or arguments as well. There are built in proceedures like find or we can define our own proceedures as well by using a def like this: def <proceedure>(<input>): We can think of our proceedures as mapping inputs to outputs. We also have to make sure to use a return in order to get a result or an output.']]], 
                             ['Decisions and Repition: If and While',
                            [['Equality Comparisons', 'When we make decisions the format of the call is: <number><operator><number> and the output is not a number, but a boolean value, which is either true or false. We also need to remember that when we want to compare equality we must use the double equal sign because the single equal means assignment.'],
                             ['If Statements and Making Decisions', 'In order to make decisions we can use an if statement to test an expession and evaluate a block of code when the if statement is true and skip the block when it is false. The structure is as follows: if <test expression>: followed by an indented block of code. We can also use an else statement to follow the if to evaluate another block of code when the test expression for the if is false.'],
                             ['Or', 'The or operator does what it seems like is should, it evaluates two statements as true or false making the overall condition either true or false. The one thing to remember is that the or operator only evaluates what it needs to be true, so as long as it finds a true value before an error or a false value the overall statement will evaluate to true.'],
                             ['While Loops', 'Though we do not need any other constructs to write any program we could want other than, arthmetic, comparisons, proceedures and if, a loop helps us to do repetitive steps over and over more conveniently. The structure of the while statement is similar to the if statement and is as follows: while <test expression>: and below that there is an indented block of code that evaluates while the test expression is true. With the if statement the block evaluates either zero or 1 times, but with while it could evaluate zero to as many times as possible.'], 
                             ['Break Statement', 'Break statements help us by stoping a while loop even while the test condition is still true. The structure is similare to a while loop, but in the block of code that is evaluated there might be a if statement and a test conditon followed by a break statement. If the test condition is true then we break out of the loop and go to the next line of code outside the loop.']]],
                             ['Structured Data: Lists and For Loops',
                            [['List', 'Unlike a string which is only limited to a sequence of characters, a list can be a sequence of anything (numbers, strings, or other lists). The format for a list is: <list> --> [<expression>, <expression>, ...].'],
                             ['Mutation', 'Mutation means that we can change the value of a list after we have created it. When we change a string we can only change what the variable is reffering to, we do not actually change the string that that variable refers to. Even when we concatenate a new string to out existing string we are creating a new string and then also creating another new string that is the concatentation of the two strings and then we change what the variable refers to. Conversely, when we select and element in a list by indexing its location we can actually change the value of the element at that position.'],
                             ['Aliasing', 'When two variable refer to the same list or value, if the state of that list is changed then both of the variables refer to the new state of the list. If, however, we change what one of the variables refers to entirely then only that one variable changes and the other continues to refer to the other list.'], 
                             ['List Operations', 'There are many operations we can perform on lists. One opperation is to append, and with this operation we add an element to the end of a list. By doing this we are not creating a new list, we are merely modifying the old list. The format is as follows: <list>.append(<element>). Another operation is the plus operation which works a lot like concatenation in that when you add to lists it forms a new list that contains the elements of both lists. Another operation is length which tells us the length of a list. It is written like this: len(<list>). The output of len is the number of elements in the list and it can work on object that is a collection of things like strings.'], 
                             ['For Loops', 'This is a new kind of loop that is similar to a while loop only it works on lists. The format is as follows: for <name> in <list>: followed by an indented block of code, where name is a new variable that we can create. The nicer thing about a for loop than a while loop is we do not have to write code to advance the loop, it is done automatically so we cannot forget to advance the loop.'], 
                             ['More List Operations', 'The index function allows us to find a certain value in our list and it returns the location of the first occurence of that value. The format for index is as follows: <list>.index(<value>). If the value passed in is not int he list then the output will be an error. Another set of operators we can use on lists are "in" and "not in" and the result is either true or false. The format for this is: <value> in <list> and <value> not in <list>.']]]]]
                             


def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="content">
    <h2>
        ''' + concept_title
    html_text_2 = '''
    </h2>
    <p>
        ''' + concept_description
    html_text_3 = '''
    </p>
</div>'''
    
    full_concept_html = html_text_1 + html_text_2 + html_text_3
    return full_concept_html

def make_single_concept_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

def make_HTML_for_many_concepts(list_of_concepts):
    html_page = ''
    for concept in list_of_concepts:
         html_page = html_page + make_single_concept_HTML(concept)
    return html_page    

def generate_HTML_for_lesson(lesson_title, list_of_concepts):
    html_text_1 = '''
    <div class="lesson">
    <h1 class="lesson-heading"> ''' + lesson_title
    html_text_2 = ''' </h1> ''' + make_HTML_for_many_concepts(list_of_concepts)
    html_text_3 = ''' 
</div>'''

    full_lesson_html = html_text_1 + html_text_2 + html_text_3
    return full_lesson_html
    
def make_single_lesson_HTML(lesson):
    lesson_title = lesson[0]
    list_of_concepts = lesson[1]
    return generate_HTML_for_lesson(lesson_title, list_of_concepts)
    
def make_HTML_for_many_lessons(list_of_lessons):
    lesson_html_page = ''
    for lesson in list_of_lessons:
        lesson_html_page = lesson_html_page + make_single_lesson_HTML(lesson)
    return lesson_html_page
    
def generate_HTML_for_session(session_title, list_of_lessons):
     html_text_1 = '''<div class="session">''' + session_title
     html_text_2 = '''
</div> '''
     html_text_3 = make_HTML_for_many_lessons(list_of_lessons)
     
     full_session_html = html_text_1 + html_text_2 + html_text_3
     return full_session_html
     
def make_session_HTML(session):
    session_title = session[0]
    list_of_lessons = session[1]
    return generate_HTML_for_session(session_title, list_of_lessons)
    
print make_session_HTML(Session_Notes)






