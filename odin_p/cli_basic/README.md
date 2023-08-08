# Command Line Basics

[Commands Explained](https://www.softcover.io/read/fc6c09de/unix_commands/basics#uid31)

`$whoami` -> codespace  
`cd ~` -> change dir to Home  
`touch file.ext` -> create a file  
`rm file.ext` -> remove a file  
`mkdir name` -> make dir   
`rmdir name`-> remove dir

## Practice
With your newly discovered CLI super powers, practice `creating a folder` and a few files using the `mkdir`, `touch`, and `cd` commands introduced in the previous step. As an example, a basic website might have a main `index.html` file, a CSS stylesheet file called `style.css`, and a folder for images. Think about how you could create these files with the commands and put it into practice!

```bash
mkdir practice
cd practice
mkdir images
touch index.html
touch style.css
```

## Practice
`Create` a new directory in your home directory with the name test.
`Navigate` to the test directory.
`Create` a new file called `test.txt`. Hint: use the `touch` or `echo` command.
Open your newly created file in VSCode and make some changes, save the file, and close it.
`Navigate back` out of the test directory.
`Delete` the `test` directory.

```bash
mkdir test
cd test
touch test.txt
rm test.txt
cd ..
rmdir test
```






