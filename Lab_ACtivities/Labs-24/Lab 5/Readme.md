Only including Make Questions not GDB

# Activity 1 : Let's make a Makefile!

In the current working directory(/home/labDirectory), you will find a src/ directory with two subdirectories, src1/ and src2/. In each of these we have several cpp files along with their corresponding header files. For each of these C++ files, compile it to a corresponding object file with the same name and a .o extension. (Use the flags -Wall and --std=c++17 for these compilations). All these object files should be placed in the current working directory(/home/labDirectory).

Apart from the src/ directory, we have a main/ directory which contains several C++ files with each of them having a main function. For this case we have files main1.cpp to main9.cpp. We want to create executables by linking each of them with all the created object files in the current working directory. The name of the executable should be the same as the name of the C++ file. (Use the same flags as earlier ). All of these executables should be created in the current working directory.

Finally after running the make command, the current working directory should contain all the object files corresponding to every C++ file in the subdirectories of src/ and all the executables corresponding to every C++ file in the main/ directory. No other new file should be present at any other location.

(Note: No two of the src C++ files or the main C++ files have same names, so you may not worry about name conflicts.)

Additionally create a **clean** target to remove all the object files and executables in the current working directory, and regaining the directory to its initial state.



Marking scheme for this question is as follows:

- 20 Marks for achieving everything mentioned in the question. (i.e., Correctly working `make` and `make clean` and not violating the very purpose of a makefile(Refer Reading 1 below)

- 10 Marks for achieving the same in less number of target rules than the number of files to be compiled.

(Hint: Patterns can be of some help?)



## Reading 1:

One can easily write a makefile with just 2 targets : all and clean, and satisfy the creation and removal of required files. Consider the simple case, where we have just three main files, namely main1.cpp, main2.cpp and main3.cpp and no other object files. We wish to write a makefile to manage this small project. Refer to the following two different Makefile codes.


You would notice that when a change is made to main2.cpp, re-run of make recompiles and creates all executables in the first case, whereas in the second case, only the main2 executable is recreated. Which one of this do you think is correct?


## Reading 2:

You may notice that not all the C++ files in the main directory includes all the header files of the src/ directory. For eg. main3.cpp doesn't include "rem.h", which means ideally, any changes to rem.h shouldn't affect the executable created from main3.cpp i.e., main3. But for simplicity of writing code, let's assume that any change in any header file of src/ will lead to recompilation of every main file. You see this is a potential improvement that can be "made" in make, There are other tools which are built on top of make and provide this functionality. But for now, let's not get into its details. This is not a part of syllabus. But for the curious ones, refer to https://www.math.colostate.edu/~yzhou/computer/writemakefile.html


## BONUS: -- (NOT PART OF SYLLABUS)

Can you write a MakeFile which can handle cases where there may be multiple subdirectories inside src/ and each of these subdirectories contains multiple .cpp files. There may also be several .cpp files in the main/ directory?

Curious ones can read about the wildcards * in make.

References:

https://www.gnu.org/software/make/manual/html_node/Wildcard-Function.html

(This website is downloaded in make directory of this repo)

# Activity 2 : Making a Makefile again

In this question, you are supposed to write a makefile for a small project in the file named Makefile. In the current working directory(/home/labDirectory), we have:

- 5 cpp files (of the 5 cpp files, 2 of them have a main function, the other 3 don't.)
- 3 header files
- 1 Makefile


After running make command, the final working directory should have the following files:

The original 9 files as shown above
- 3 Object files corresponding to the 3 cpp files in this directory which do not have the main function.
- 2 Executables corresponding to the 2 cpp files with the main function.
- **No other files** should be present anywhere else in the working directory.


We will also run the following command make `CXXFLAGS="--std=c++11 -Wall -Werror"` to compile the code with the given flags. Use **CXXFLAGS for both compilation and linking**. We may use different flags during final evaluation, so make sure that the flags are not hardcoded in the makefile. (Read HINT given at the end of description.) On simply running `make`, you can use just the `--std=c++11` flag.



Also, create a target that removes all the created object files and executables without removing any original files. For this we will run the command make restore.



For creation of every object and executable file, take care of the dependencies, to ensure minimal recompilation. By this we mean that if a file A is dependent on B but not on C, then a change to B should trigger the recompilation of A but a change to C should not trigger the recompilation of A.



### NOTE:

For final evaluation, we will be using the given complete set of files only. We will not change/add new files or change the content of the files.
However, there may be change in marking scheme and recompilation testcases.


**HINT: OVERRIDING VARIABLES**

An argument that contains = specifies the value of a variable,: v=x sets the value of the variable v to x. If you specify a value in this way, all ordinary assignments of the same variable in the makefile are ignored; we say they have been overridden by the command line argument The most common way to use this facility is to pass extra flags to compilers. For example, in a makefile, lets say you create and set the value of variable CFLAGS to -g, and use them as compilation flags.

`CFLAGS=-g`

`cc -c $(CFLAGS) foo.c`

Each time you run make, you can override this value if you wish. For example, if you run make `CFLAGS=-g -O`, each C compilation will be done with `cc -c -g -O`.