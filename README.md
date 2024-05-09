<h1>Overview</h1>

This python application contains 6 main states (in code): start_game, unable_to_play, select_difficulty, show_normal, show_medium and display_question. When you run the program, there isn't a defined state for what's shown on the screen; it's more like an <b>"init"</b> state, which displays the welcoming message and also contains the definition of different functionalities that will be later on used, such as the questions (normal and medium) and the buttons that the user can select. 

![image](https://github.com/cristina07a/State-machine/assets/122676393/0b685a35-3307-401a-aa59-c43f9372cc21)

After pressing the "Incepe" (Start) button, the state where the code goes is <b>start_game</b>. There, everything that is irrelevant from the previous page is removed. The user will get asked its first question, which is seemingly unrelated to the survey. On contrary to this, it's the most important question, because not everyone should answer what follows.

![image](https://github.com/cristina07a/State-machine/assets/122676393/aa9f7480-4641-4b7c-9539-0ee59e35432e)

By pressing "Nu" (No), the user goes to a different state: <b>unable_to_play</b>, which notifies him that his experience using this software is over. The survey can be restarted only by reopening the application.

![image](https://github.com/cristina07a/State-machine/assets/122676393/6b15763d-d2e5-472d-9cd8-030c2f4455cf)

By pressing "Da" (Yes), the user gets to choose its desired dificulty for the questions in a different state: <b>select_difficulty</b>. He has two options: normal and mediu (medium).

![image](https://github.com/cristina07a/State-machine/assets/122676393/fb14a457-01c9-4b3e-abdd-ccd4fadd3c61)

When the user chooses one of them, he is shown questions which he can answer. This state is defined by <b>show_normal</b> or <b>show_medium</b> together with <b>display_question</b>. The function display_question creates buttons that the user can select for the current question based on the provided answers predefined in questions (in __init__)

![image](https://github.com/cristina07a/State-machine/assets/122676393/bda601e0-8158-4832-957e-361afaaf46a7)

No matter which number the question has, if the user gets it wrong, he'll be redirected to a page that deletes its progress and lets him start over by pressing a button. This page is defined in the state <b>check_answer</b>. Basically, check_answer verifies the answers provided by the user and, based on them, it gives him 2 outcomes/states : the next question and a game over with retry possibility.

![image](https://github.com/cristina07a/State-machine/assets/122676393/5350eaac-2378-4ad9-90ca-6abe245655d7)

If the user gets all the answers right, he'll finish the current difficulty, but doesn't have the possibility to retry. As before, in order to try the other difficulty (for example), he has to reopen the application. This counts as two states, given the fact that there's a message for finishing both difficulties (example for one). This happens because, in <b>check_answer</b>, the screen that's made for finishing a difficulty is more of a template, the only thing that changes is the name of the difficulty.

![image](https://github.com/cristina07a/State-machine/assets/122676393/e83f9e97-4019-4176-83dc-8c01b1a4b0fc)

<h2>Additional info</h2>
The UI for this interface was made with tinkinter. Also, I made a diagram that counts all the states within this application. I added it to the repository, but I'll upload it here as well:

![image](https://github.com/cristina07a/State-machine/assets/122676393/c8f917ad-828f-472b-a18e-b751c72e33de)


