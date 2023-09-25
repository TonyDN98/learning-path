
<h1>Module 1. Learn the Basics</h1>
<p>|__________________________________________|</p>

<h2>_WHAT'S THE MATTER IN THIS SECTION?_</h2>
<p>|_____________________________________________________________________|</p>

[Learn the basics](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/)
<p>|____________________________________|</p>

<ul>
    <li><a href="#u1">1. States of the WorkingDir</a></li>
    <li><a href="#u2">2. Commands</a></li>
    <li><a href="#u3">3. Tell git who you are</a></li>
    <li><a href="#u4">4. Git INIT</a></li>
    <li><a href="#u5">5. Add remote ORIGIN</a></li>
    <li><a href="#u6">6. Git PUSH </a></li>
    <li><a href="#u7">7. Collaborating</a></li>
</ul>


<h2 id="u1">1. States of the WorkingDir</h2>


<p id="goUP"></p>

<pre><code>
States of a WorkingDir
1. Staged -> has changes localDir;
2. Modified -> can be modified localDIr;
3. Commited;
</code></pre>

<h2 id="u2">2. Commands</h2>

<pre><code>
<b>$ git add</b> ->   files in the staging area;
<b>$ git commit</b> -> Commit all the files that are staged local;
<b>$ git push</b> -> Push the commits from the <b>localRepo</b> to the <b>RemoteRepo</b>
<b>$ git fetch</b> -> Get files from <b>RemoteRepo</b> to <b>localRepo</b> =>>> GIT PULL
<b>$ git merge</b> -> Put files from <b>localRepo</b> into <b>WorkingDir</b> and merge branches;
</code></pre>

<h2 id="u3">3. Tell git who you are</h2>

<pre><code>
$ git config --global user.name "TonyDN98"
$ git config --global user.mail "kh3@gmail.com"
$ git config --global --list # Check the info you provided;
</code></pre>

<h2 id="u4">4. Git INIT</h2>

<pre><code>
$ cd Desktop/Project
$ touch README.md # make file
$ git init #Init an empty repo
</code></pre>

<h2 id="u4">4.1 Add files to Staging AREA</h2>

<pre><code>
$ git add #Add all the files and stage them for commit;
or
$ git add specificFile.txt
</code></pre>

<h2 id="u4">4.2 List all files in Staging AREA</h2>

<pre><code>

 $ git status # Lists all new or modified files to be committed

</code></pre>


<h2 id="u4">4.3 Commit the  changes</h2>

<pre><code>
$ git commit -m "Commit changes with a readable message for others"
</code></pre>

<h2 id="u4">4.4 Unstage / Uncommit </h2>

<pre><code>
$ git reset HEAD~1
# Remove the most recent commit;
$ git commit -m "Another commit after reset"
# Another commit
</code></pre>

<h2 id="u5">5. Add remote ORIGIN </h2>

<pre><code>
$ git remote add origin remote_origin_URL
# Sets a new remote

# git remote -v
# List  the remote connections;
</code></pre>

<h2 id="u6">6. Git PUSH </h2>

<pre><code>
$ git push -u origin master
# pushes changes to RemoteRepo from master branch

</code></pre>

<h2 id="u7">7. Collaborating</h2>

<pre>
So imagine you and your friend are collaborating on a project. You both are working on the same project files. Each time you make some changes and <b>push</b> it into the master repo, your friend has to pull the changes that you pushed into the git repo. Meaning to make sure you’re working on the latest version of the git repo each time you start working, a <b>git pull</b> command is the way to go.
</pre>

<pre><code>
$ git pull origin master
# Get the latest changes from the remoteRepo
</code></pre>