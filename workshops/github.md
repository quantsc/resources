This is a document designed to onboard people to Git and GitHub – two linked version control tools that greatly assist teams of developers share code and maintain document histories.

## Table of Contents

What is a Version Control System? What is Git?
Key Terms
Register with GitHub
Install Git
Configure an SSH Key
Git Configuration
GitHub Configuration
Creating a Sample Project
Start by creating a project repository in GitHub
Making and Uploading Changes
Working on a Team
Additional Resources

### What is a Version Control System? What is Git?
Version control is the practice of tracking and managing changes to software control. Say you and 3 other people are all editing one document. You write a paragraph but someone else wants to rewrite it. How do you programmatically (especially for larger teams with more documents) determine what the end document should look like?

Version control systems do this by keeping track of (and letting you edit) the history of edits. They also help by letting you create your own isolated branch of development, which you can edit without expecting incoming changes until you want to merge it into the main line of development.

Git is one such VCS.
### Key Terms
Branch - A place where you can put multiple commits without affecting the main line of code
Command Line Interface - A place that connects a computer user to a computer program or operating system
Commit - A snapshot of tracked changes to files
Directory - A file structure containing references to other files or more directories (think: a folder)
Merge - Putting a forked history of files back together
Pull - Fetching and replacing local code with code from remote repository
Push - Transferring local commits to the remote repository
Repo/Repository - This can be thought of as a bank of all documents in a project. There is typically a “remote” repository, where your team’s entire set of files and edits is stored, and a “local” repository, where only your documents are stored.
Text Editor - A place you edit text (think: Google Docs/MS Word but without all the formatting. Examples: VSCode, Atom, Sublime)
Tracked Files - Files that you are having Git find and update differences on (i.e. if there are new versions of the files, they’ll be updated)
Working Directory - The directory that you are currently in


### Register with GitHub
This is GitHub’s signup page Choose a username.

### Install Git
To install Git command line tools, go here and follow the instructions for your operating system.

### Configure an SSH Key
When contacting a remote server, Git uses the Secure Shell protocol (SSH) to encrypt/secure messages between you and the remote server. This requires generating one public and one private encryption key.
Note: Where you type commands depends on if you’re using Docker, Windows, Mac, etc.
If using Docker, just use your normal operating system. Docker reboots itself from a pre-canned image, which would erase your configurations
If using Windows, installing Git should let you either use Git Bash or unix commands in CMD
If using a VM, open Terminal inside your virtual desktop
If using a Mac, open Terminal inside your desktop
Enter the following command in your terminal, replacing ttrojan@usc.edu with your Github account’s affiliated email:
	`ssh-keygen -t rsa -b 2048 -C "ttrojan@usc.edu"`
When asked to enter a location in your computer to save the key, use the default:
`Generating public/private rsa key pair.
Enter file in which to save the key (/home/cs104/.ssh/id_rsa):`
You will be prompted to enter a passphrase for your private key. This is a good idea but not required. It will not show up as you type it (if you decide to use one). Press enter once you’ve entered a passphrase or if you don’t want to use one. If entering one, you’ll have to re-enter it to verify it.
You should then receive something like this:
`Your identification has been saved in /home/cs104/.ssh/id_rsa.
Your public key has been saved in /home/cs104/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:vC+4OG2u1PIeE0OKX9jiFFHuLnkYCBSsvIW8ybD873H ttrojan@usc.edu
The key's randomart image is:
+---[RSA 2048]----+
|   ++o.          |
|    S+.o *.*     |
|   +.X. o        |
|    0. o +       |
|   ..o  E .      |
|  .=S. . + .0    |
| .*=* ...        |
|.+.=o*. ..  *o*  |
| .++*oo. ..      |
+----[SHA256]-----+`
### Git Configuration
We’ll be saving your name, email, editor for commit messages, git message colors, and newline handling preferences.
Open your terminal.
To save your name and email (use the one affiliated with GitHub), enter:
`git config --global user.name "Tommy Trojan"`
`git config --global user.email "ttrojan@usc.edu"`

To say that you want easy-to-read colors in GitHub terminal print-outs, enter:
	`git config --global color.ui auto`
	
To say that you want a certain text-editor to be used when writing commit messages, enter:
	`git config --global core.editor "nano"`
	
Note: Options for the text editor include nano, emacs, vi, vim, etc
Miscellaneous (dealing with git-specific nuances):
`git config --global core.autocrlf input
git config --global push.default simple`
To see your configurations, enter:
`git config --list`
### GitHub Configuration
Now that you have SSH keys, you need to let GitHub know about them.
In your profile settings,
Put your name in the name field
In your SSH key settings,
Click `Add SSH Key`
Give the key a name (ex: ‘MacBook Key’)
In your Terminal (not GitHub), find your key by running `cat ~/.ssh/id_rsa.pub`
This will take a look at your id_rsa.pub file, where the contents are stored
Copy the output into the key field (in GitHub). This should start with ‘ssh-rsa’ and end with your email address.
Click `Add Key`
Recommended notification settings:
In your notification settings
Automatically watch repositories: ON
Participating: Email ON, Web ON
Watching: Email OFF, Web ON
In your email notification settings:
Comments on Issues and Pull Requests: ON
Pull Request reviews: ON
Pull Request pushes: ON
Include your own updates: OFF
### Creating a Sample Project
Let’s say you’re building a new project by yourself. You want to store all your files in one place and have them saved in GitHub.
#### Start by creating a project repository in GitHub.
1. Navigate to your repositories page and click “New”
  1. Enter a name for the repository. This just has to be different from your other repository names.
  1. Decide if you want to add
    1. a description,
    1. a README (where you can type more notes about the project – ex: setup instructions),
    1. a .gitignore (which will automatically tell git not to bother with tracking unnecessary files (ex: node_modules is generally not tracked because it’s very large and might cause some latency)
  1. Decide if you want the repo to be public or private
    1. Since this is just for practice, public is probably fine
1. Click “Create repository”
1. Navigate to the green “Code” dropdown and copy the “SSH” string (something like “git@github.com:username/repoName”)

1. Open your terminal. Navigate to the directory you’d like to work on this project. For example, if you want the folder to appear on your desktop, you could navigate there
  1. To navigate from the command line, you’ll likely be using two commands:
    1. ls - this lists the contents of the current directory, letting you know the names of everything inside (i.e. things you can navigate to)
    1. cd - this lets you change directory to whatever you type after cd
    1. Ex: if entering “ls” prints out “Desktop”, then “cd Desktop” will bring you into your Desktop folder
    1. Also, note that “cd ..” will bring you to the “parent” folder (i.e. one folder up) so that if you go into your Desktop and want to go back, “cd ..” will bring you back
    1. Also, note that you can hit the tab key to auto-fill file/folder names in the command line
      (entering “cd De[tab]” will autofill to “cd Desktop” as long as there’s no other files/folders to be confused with)
1. Clone the repository using: `git clone git@github.com:username/repoName`

1. You should now have a copy of the repository! To confirm this, type “ls” and you should see the name of the repository you created on GitHub.
If not, try going back to GitHub and instead copying the HTTPS version of the string (something like https://github.com/avonarnim/openCVPractice.git). Then redo step 5.
#### Making and Uploading Changes
Our main goal for this section is to be able to add files and changes of files to the repository and upload those changes.
1. Let’s start by adding a file to the folder. To save time, feel free to literally just make a copy of any small file (ex: a pdf you downloaded recently) and drop it into the directory you created in the “Creating Sample Project” section.
1. In your terminal, navigate to that directory.
1. Enter `git status`
  This lists all changes that we’ve made to the repository. For now, it should just mention the file you added
1. Enter `git add .``
  This will tell Git that you want it to start tracking a set of files
  Using “.” tells Git to track *everything* that is not yet tracked. To only track a few files, list the filenames
1. Enter `git commit -m “Random pdf”`
  This will create what can be thought of as a checkpoint. All your edits to tracked files will be saved.
1. Enter `git push`
  This will take any commits you’ve made and send them to the remote repository. For now, that should just mean sending the single copied-in file to GitHub.
1. Now, navigate to your repository in GItHub. You should now be able to see whatever you copied here.
1. If you perform edits from the browser (ex: uploading a new document), you should retrieve those edits locally by entering `git pull` in the terminal
To continue making and uploading changes on a solo project, you can just use this basic workflow of git status, add, commit, push.
### Working on a Team
As you enter a team setting, Git gets a bit hairier (especially when multiple people are working on the same files).
#### Branches
Generally, you want to have your work structured as “I am working on feature X, you are working on feature Y”. Therefore, each person should have their own branch(es) of the version history, where they can make edits without others interfering.
To create a branch, enter:
  `git checkout -b your-branch-name`
To change branches, enter:
  `git checkout other-branch-name`
To see local branches, enter:
  `git branch`
You can perform commits and pushes as usual in a branch. The only thing to note is that when pushing, you’ll be told to set an origin
Entering git push will yield a message like `use git push —set-upstream origin mainline`
	Follow those instructions, and the push will go through
	You will then be able to see your new branch and create a pull request from GitHub
Note that pull requests are like requests to merge your feature branch’s code into the mainline of code
To submit a pull request, you should type a descriptive message of what you’re requesting to merge and assign someone to look over the edits. It’s oftentimes good to show some test results (ex: backtest data)
#### Pulling Others’ Changes
Say someone has already made changes to the repository and you want to retrieve those changes.
If you’ve set up your feature branch, you can follow these steps:
`git checkout mainline`
`git pull`
`git checkout your-branch-name`
`git rebase mainline`
This will attempt to rewrite the history of the files *before* your edits, then lay your edits on top of that.
Note that you might run into merge conflicts over time. Usually, this is just a process of saying “accept my changes for this section of code, accept the incoming changes for other sections of code.” If you’re really worried about losing something, you can also save your files externally (but you should be committing often enough that it’s not an issue).
### Additional Resources
I highly recommend looking at Atlassian when you have Git questions. Here’s one sample resource they put out (a Git cheatsheet of commands)
