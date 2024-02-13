# Assginment 2
# Rohit George Rarichan 

In this project we were required to manipulate a journal and implement a code that would fulfill all the requirements of a normal journal entry. 

The code has 5 main functions and 1 optional function :- 

create_journal -  This function is used to creating a journal as per the file path given by the user and allow it to be edited and projected later. If the file path exists then it will open the journal that is already in the specified file path.

open_journal - this would allow the user to open the journal so that it can be used to add or view posts and make edits. This function also contains a uses another function read_file that will display file contents if user is willing to. 

edit_journal - this function will edit the journal contents based on the keywords -usr, -pwd, -posts, -post, -all and will change the existing information to the argument that is passed. 

print_journal - it contains all the same keywords as edit_journal but uses it to print the contents based on the post_ID. 

admin - this function disables the user inteface and communicates with the user in pure input formats. It is to be used by high levle programming users only. 

In addition to this we have the user_inteface function which is the standard for our entire code is the part that prints out an interactive user interface so that code development is easy for the user.