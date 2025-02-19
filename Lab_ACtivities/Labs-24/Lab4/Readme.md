# Activity - 1: JavaScript as a Programming Language

In this activity, you need to find the largest prime number which is less than or equal to the number which is received as input. The HTML code is already provided to you in the file basic.html. You need to write javascript code in the same file, and submit. (If there is no prime number less than or equal to the given number, just print 0.) (Also, your final result string should be stored in the paragraph with id "result", see the HTML Code for you reference!)

# Activity - 2: User Registration Validation

## Objective:

Create a user registration form with an input validation using JavaScript. Handle errors and provide appropriate feedback to users.

## HTML:

Begin by completing the index.html file with a user registration form. Include the following fields with appropriate labels and input boxes/button with id strictly the same as:

    Full Name, id = fullName
    Email Address, id = email
    Password, id = password
    Confirm Password, id = confirmPassword
    Submit Button, id = submit

The submit button on clicking should call the function validateForm() from the script.js file.

Note:- If the same ids are not followed, you will face problem(s) in evaluation.

Use the appropriate type attribute for each input box. The full name input box will have the type text, the email address input box will have the type email, and the password and confirm password input boxes will have the type password. The submit button will have the type button. Follow this link to look at possible input field type attributes.

**Important Note:-** An empty \<div\> container with id feedback is provided in index.html. Do not modify it. Use that container in your JavaScript file to give back error messages/feedback.



## CSS:

In style.css just make sure that every component is centered and keep the background colour of the body as azure, as shown in this pic

## JavaScript:

Complete the script.js file. Most of the instructions are written as comments in that file.

You must complete the validateName, validateEmail, validatePassword, ConfirmPassword, and validateForm functions. These functions dont return anything.

Whenever you have to give feedback about a successful entry or an error message, refer to the instructions in the How to give your feedback/error message to the HTML page from a JavaScript file?

Now, read the content below to learn more about the functions of the script.js file.

When validateForm() is called, the try block has code that runs in the following order:-

    Checks if all fields are non-empty/filled or not. If not, throw the error message Error: All fields are required..
    Calls the validateName() function
    Calls the validateEmail() function
    Calls the validatePassword() function
    Calls the ConfirmPassword() function
    Gives the feedback Registration successful! (in green colour) to the HTML page.
The catch block contains the code that gives feedback to the HTML page about the error message it catches. The error message, if caught, will either be Error: All fields are required. or those thrown by any one of the validateName(), validateEmail(), validatePassword() or ConfirmPassword() functions.

Note:- The try block will reach step (6) successfully only if none of the steps (1) - (5) throw an error message.

The validateName() function :-

Check if the name is entered or not. If not, throw the error Error: Full name is required..
The validateEmail() function :-

Check if the email entered is valid or not. An email is valid if and only if:-
1. It contains exactly 1 @ and,
2.    There should be atleast one character to the left of @. If yes, those characters should only be a-z or 0-9, and,
3.  To the right of @ there should be exactly one . and,
4.  Between@ and . there should be atleast one character. If yes, those characters should be only from a to z, and,
5. To the right of ., there should be exactly 3 lowercase English characters.
6. This check is conveniently possible by Regex. Use the test() function of JavaScript to make it happen. Follow this link to learn more about it.
7. If the email is invalid, throw the error message Error: Invalid Email Address..

The **validatePassword()** function :-

Check if the password entered is atleast 8 characters long. If not, throw the error message Error: Password must be at least 8 characters.

The **ConfirmPassword()** function :-

Check if the re-entered password matches or not. If not, throw the error message Error: Passwords do not match.

**How to give your feedback/error message to the HTML page from a JavaScript file?**

Using **innerHTML**, we can use the \<div\> feedback container of HTML to give the error messages/responses back. Follow this link to learn more about innerHTML.

When all fields are validated successfully, then on clicking Submit, Registration successful! should be printed in green color. If any one of the fields is invalidated, then on clicking Submit, an error message should appear in red.

We can use the span tag along with the innerHTML to adjust the color of the feedback. Follow this link to learn more about the span tag.


# Activity - 3: Counting Stairs

Let's talk The Office! It's stair-mageddon, and Stanley is in trouble. He must climb the stairs to his office on the first floor because the elevator has broken down. Erin, the receptionist, comes down to cheer him on.



Say there are n stairs in the staircase. In a single step, Stanley can climb a single stair, or he can climb two stairs. Stanley is trying to stall. He won't budge until Erin can answer the following question: How many ways are there for Stanley to climb the stairs?



Write your code in the script.html file provided. Javascript code should also be written in that file only. Your final result string should be stored in the paragraph with id "result". See the HTML code for your reference.

# Activity - 4: Let's Manipulate

In this activity we will use javascript to manipulate html files provided.

There is one sample.html file provided to you, which has its script linked to dom.js. You need to write your code in dom.js, to manipulate the html webpage as follows:

1. For all images (with \<img\> tag), change the source of the image to be timepass.png

2. Delete all the \<h1\> heading tags. (Remember, no other headings should get deleted.)

3. For all paragraphs (with \<p\> tags), change the content of the paragraphs to be "Enough of JavaScript, lets stop."

4. Change all the \<h2\> content to make it uppercase. So, suppose you have a h2 heading saying Dont Stop, then it should be converted to DONT STOP

5. For any \<div\> container with element id = div1, add a heading (\<h3\>) with no text inside it.



All these changes will happen when you click the Change button. The change button in your html file will call a function in your javascript code. So, you need to edit that function in dom.js.

Once you click the Evaluate button, the results will be shown after a few seconds, so please wait.