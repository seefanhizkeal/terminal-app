def terminal_command():
      command= input("Type a command for a defition: ")
      if (command == "touch"):
            print("\n|")
            print("What it does:The touch command allows you to create any type of file,but its blank.After you create the blank file,you can open it in a text editor by typing open`")
      if (command == "mkdir"):
          print("\n|")
          print("This command will allow you to create a directory(folder) right from the CLI.When you need a place to store new files,just use this commmad to add a new directory in the current working directory,or specify a full path to the location where you want the new directory to be placed.`")
      if (command == "cd"):
            print("\n|")
            print("This command will change the direcotry that you're currently working with in the terminal in order to execute other cammands on a different directory, view the contents of a different directory or open a file in a different directory. This is a very common command that will be used when working with the CLI. If you ever lose; your place and which directory you’re in, type pwd (print working directory) and press Return to echo the current path.`")
      if (command == "ls"):
            print("\n|")
            print("Use this command after navigating into a directory using the cd command to view the contents (files and directories) inside of the current directory. Use the argument -l (ls -l) to get even more information about each of the files, including the permissions, owner and date created.`")
      if (command == "cat"):
            print("\n|")
            print("The cat (short for “concatenate“) command is one of the most frequently used commands in Linux/Unix-like operating systems. cat command allows us to create single or multiple files, view content of a file, concatenate files and redirect output in terminal or files.`")
terminal_command()
