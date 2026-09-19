
psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan (main)
$ pwd
/c/Users/psrga/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan (main)
$ ls

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan (main)
$ cd ..

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216 (main)
$ ls -al
total 16
drwxr-xr-x 1 psrga 197609 0 Sep 19 15:07 ./
drwxr-xr-x 1 psrga 197609 0 Sep 17 15:40 ../
drwxr-xr-x 1 psrga 197609 0 Sep 18 17:29 .git/
drwxr-xr-x 1 psrga 197609 0 Sep 18 17:03 .github/
drwxr-xr-x 1 psrga 197609 0 Sep 18 16:58 302.5-activity-practice-pr/
drwxr-xr-x 1 psrga 197609 0 Sep 19 15:07 302-lab1-website-project-rod-gaitan/
drwxr-xr-x 1 psrga 197609 0 Sep 15 17:34 test_folder/

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216 (main)
$ ls
302.5-activity-practice-pr/  302-lab1-website-project-rod-gaitan/  test_folder/

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216 (main)
$ cd 302-lab1-website-project-rod-gaitan

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan (main)
$ mkdir buffer

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan (main)
$ ls
buffer/

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan (main)
$ mkdir website-project

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan (main)
$ ls
buffer/  website-project/

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan (main)
$ cd website-project

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ ls

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ t^C

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ touch index.html

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ ls
index.html

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git add .

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   index.html


psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git commit -m "Initial commit with basic HTML structure"^C

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   index.html


psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git log
commit 81bcd946e56a0a979a5de939689ffd9730cd2b8d (HEAD -> main, origin/main, origin/HEAD)
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Fri Sep 18 17:29:40 2026 -0400

    Add CI workflow for tests and linting

commit 6a16bffdf05416a9a6eeeed5e2374914a2695025
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Fri Sep 18 13:54:36 2026 -0400

    added 'index.html'

commit b50e5eee00f580e29aaf076728bb6ed13395ee9c
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Fri Sep 18 13:33:37 2026 -0400

    first commit

commit 5626300e9fe24a0f4c297a765b00dc10a326c254
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Wed Sep 16 13:08:24 2026 -0400


psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   index.html


psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git commit -m "Initial commit with basic HTML structure"
[main 126104d] Initial commit with basic HTML structure
 1 file changed, 8 insertions(+)
 create mode 100644 302-lab1-website-project-rod-gaitan/website-project/index.html

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git branch
  feature/footer
* main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout -b feature/navigation-bar
Switched to a new branch 'feature/navigation-bar'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/navigation-bar)
$ git branch
  feature/footer
* feature/navigation-bar
  main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/navigation-bar)
$ git status
On branch feature/navigation-bar
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/navigation-bar)
$ git add .

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/navigation-bar)
$ git status
On branch feature/navigation-bar
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   index.html


psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/navigation-bar)
$ git commit -m "added navigation bar"
[feature/navigation-bar 7d81550] added navigation bar
 1 file changed, 10 insertions(+), 1 deletion(-)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/navigation-bar)
$ git status
On branch feature/navigation-bar
nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/navigation-bar)
$ 

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/navigation-bar)
$ git branch
  feature/footer
* feature/navigation-bar
  main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/navigation-bar)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git branch
  feature/footer
  feature/navigation-bar
* main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout -b feature/footer
fatal: a branch named 'feature/footer' already exists

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git branch
  feature/footer
  feature/navigation-bar
* main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout -b feature/footer_2
Switched to a new branch 'feature/footer_2'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git branch
  feature/footer
* feature/footer_2
  feature/navigation-bar
  main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git status
On branch feature/footer_2
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git add .

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git commit -m "Added footer section"
[feature/footer_2 9b2455e] Added footer section
 1 file changed, 8 insertions(+)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git status
On branch feature/footer_2
nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git log
commit 9b2455effcdb966dafc46248283c8e68a695ee58 (HEAD -> feature/footer_2)
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 16:07:13 2026 -0400

    Added footer section

commit 126104d2b7b5a38b74fb9877489dbf51a391aacf (main)
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 15:22:50 2026 -0400

    Initial commit with basic HTML structure

commit 81bcd946e56a0a979a5de939689ffd9730cd2b8d (origin/main, origin/HEAD)
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Fri Sep 18 17:29:40 2026 -0400

    Add CI workflow for tests and linting

commit 6a16bffdf05416a9a6eeeed5e2374914a2695025
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Fri Sep 18 13:54:36 2026 -0400


psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ 

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git brnch
git: 'brnch' is not a git command. See 'git --help'.

The most similar command is
        branch

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git brnach
git: 'brnach' is not a git command. See 'git --help'.

The most similar command is
        branch

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git branch
  feature/footer
* feature/footer_2
  feature/navigation-bar
  main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout feature/navigation-bar
Switched to branch 'feature/navigation-bar'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/navigation-bar)
$ git checkout feature/footer_2
Switched to branch 'feature/footer_2'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ checkout main
bash: checkout: command not found

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/footer_2)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ 

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ 

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git merge feature/navigation-bar
Updating 126104d..7d81550
Fast-forward
 .../website-project/index.html                                | 11 ++++++++++-
 1 file changed, 10 insertions(+), 1 deletion(-)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git branch
  feature/footer
  feature/footer_2
  feature/navigation-bar
* main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git merge feature/footer_2
Auto-merging 302-lab1-website-project-rod-gaitan/website-project/index.html
CONFLICT (content): Merge conflict in 302-lab1-website-project-rod-gaitan/website-project/index.html
Automatic merge failed; fix conflicts and then commit the result.

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main|MERGING)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main|MERGING)
$ git add .

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main|MERGING)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   index.html


psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main|MERGING)
$ git commit -m "Resolved merge conflict and combined navigation bar and footer"
[main f5db009] Resolved merge conflict and combined navigation bar and footer

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ 

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ 

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git branch
  feature/footer
  feature/footer_2
  feature/navigation-bar
* main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout -b feature/hero-section
Switched to a new branch 'feature/hero-section'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/hero-section)
$ git status
On branch feature/hero-section
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hero-image.jpg

no changes added to commit (use "git add" and/or "git commit -a")

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/hero-section)
$ git add .

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/hero-section)
$ git status
On branch feature/hero-section
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hero-image.jpg
        modified:   index.html


psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/hero-section)
$ git commit -m "Add a hero section"
[feature/hero-section b077897] Add a hero section
 2 files changed, 6 insertions(+)
 create mode 100644 302-lab1-website-project-rod-gaitan/website-project/hero-image.jpg

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/hero-section)
$ git status
On branch feature/hero-section
nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/hero-section)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout -b feature/contact-form
Switched to a new branch 'feature/contact-form'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/contact-form)
$ git branch
* feature/contact-form
  feature/footer
  feature/footer_2
  feature/hero-section
  feature/navigation-bar
  main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/contact-form)
$ git status
On branch feature/contact-form
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/contact-form)
$ git add .

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/contact-form)
$ git commit -m "Add a contact-form"
[feature/contact-form 2f6be09] Add a contact-form
 1 file changed, 18 insertions(+)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/contact-form)
$ git status
On branch feature/contact-form
nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/contact-form)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git branch
  feature/contact-form
  feature/footer
  feature/footer_2
  feature/hero-section
  feature/navigation-bar
* main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout -b feature/testimonials
Switched to a new branch 'feature/testimonials'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/testimonials)
$ git status
On branch feature/testimonials
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/testimonials)
$ git add .

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/testimonials)
$ git commit -m "Add a testimonials section"
[feature/testimonials 77bad0a] Add a testimonials section
 1 file changed, 22 insertions(+)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/testimonials)
$ git status
On branch feature/testimonials
nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/testimonials)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout feature/hero-section
Switched to branch 'feature/hero-section'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/hero-section)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout feature/contact-form
Switched to branch 'feature/contact-form'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/contact-form)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout feature/testimonials
Switched to branch 'feature/testimonials'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/testimonials)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout hero
error: pathspec 'hero' did not match any file(s) known to git

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout feature/hero
error: pathspec 'feature/hero' did not match any file(s) known to git

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout feature/feature/hero-section
error: pathspec 'feature/feature/hero-section' did not match any file(s) known to git

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git checkout feature/hero-section
Switched to branch 'feature/hero-section'

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (feature/hero-section)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ 

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ 

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git branch
  feature/contact-form
  feature/footer
  feature/footer_2
  feature/hero-section
  feature/navigation-bar
  feature/testimonials
* main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git merge feature/hero-section
Updating f5db009..b077897
Fast-forward
 .../website-project/hero-image.jpg                     | Bin 0 -> 246247 bytes
 .../website-project/index.html                         |   6 ++++++
 2 files changed, 6 insertions(+)
 create mode 100644 302-lab1-website-project-rod-gaitan/website-project/hero-image.jpg

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git merge feature/contact-form
Auto-merging 302-lab1-website-project-rod-gaitan/website-project/index.html
Merge made by the 'ort' strategy.
 .../website-project/index.html                         | 18 ++++++++++++++++++
 1 file changed, 18 insertions(+)

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 7 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git merge feature/testimonials
Auto-merging 302-lab1-website-project-rod-gaitan/website-project/index.html
CONFLICT (content): Merge conflict in 302-lab1-website-project-rod-gaitan/website-project/index.html
Automatic merge failed; fix conflicts and then commit the result.

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main|MERGING)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 7 commits.
  (use "git push" to publish your local commits)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main|MERGING)
$ git add .

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main|MERGING)
$ git commit -m "Resolved merge conflict triggered after adding feature/testimonials branch ONLY"
[main 0675bbf] Resolved merge conflict triggered after adding feature/testimonials branch ONLY

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 9 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 9 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git log
commit 0675bbf1b5fb37f9d49f080a1ba151c4c163eebf (HEAD -> main)
Merge: 14cce3b 77bad0a
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 19:31:20 2026 -0400

    Resolved merge conflict triggered after adding feature/testimonials branch ONLY

commit 14cce3b26af6a68b8b78139d3ad1e7754c276cdd
Merge: b077897 2f6be09
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 18:56:02 2026 -0400

    Merge branch 'feature/contact-form'

commit 77bad0ac3744b80f128a823063fb157a9f586c7a (feature/testimonials)
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 18:04:29 2026 -0400

    Add a testimonials section

commit 2f6be09687fbb3410da2a0148545b6b84f6acf75 (feature/contact-form)
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 17:58:20 2026 -0400

    Add a contact-form

commit b077897da0d862643bf9ed0185b6eb66df71fa6f (feature/hero-section)
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 17:49:54 2026 -0400

    Add a hero section

commit f5db009daab88732e578cfbcb2d1c4c77517afaa
Merge: 7d81550 9b2455e
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 16:51:14 2026 -0400

    Resolved merge conflict and combined navigation bar and footer

commit 9b2455effcdb966dafc46248283c8e68a695ee58 (feature/footer_2)
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 16:07:13 2026 -0400

    Added footer section

commit 7d815506dce1c62156137525d49e7a420e898c9d (feature/navigation-bar)
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 15:46:34 2026 -0400

    added navigation bar

commit 126104d2b7b5a38b74fb9877489dbf51a391aacf
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Sat Sep 19 15:22:50 2026 -0400

    Initial commit with basic HTML structure

commit 81bcd946e56a0a979a5de939689ffd9730cd2b8d (origin/main, origin/HEAD)
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Fri Sep 18 17:29:40 2026 -0400

    Add CI workflow for tests and linting

commit 6a16bffdf05416a9a6eeeed5e2374914a2695025
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Fri Sep 18 13:54:36 2026 -0400

    added 'index.html'

commit b50e5eee00f580e29aaf076728bb6ed13395ee9c
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Fri Sep 18 13:33:37 2026 -0400

    first commit

commit 5626300e9fe24a0f4c297a765b00dc10a326c254
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Wed Sep 16 13:08:24 2026 -0400

    added an extra '?' to the 2nd print message

commit ebaeb3ff329ff6462a7fd564aa114f0d7eb06c8c
Author: PSStudent01 <rodgaitan01@gmail.com>
Date:   Tue Sep 15 18:14:59 2026 -0400

    created and updated python file

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)
$ git push origin main
Enumerating objects: 47, done.
Counting objects: 100% (47/47), done.
Delta compression using up to 12 threads
Compressing objects: 100% (31/31), done.
Writing objects: 100% (46/46), 236.53 KiB | 11.26 MiB/s, done.
Total 46 (delta 19), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (19/19), done.
To https://github.com/PSStudent01/2026-cax-216.git
   81bcd94..0675bbf  main -> main

psrga@LAPTOP-KGMU5T75 MINGW64 ~/Desktop/Per Scholas Python Essentials/2026 Python Essentials/2026-cax-216/302-lab1-website-project-rod-gaitan/website-project (main)