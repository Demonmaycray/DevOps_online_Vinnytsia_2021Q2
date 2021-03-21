Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~
$ git connfig --list --global
git: 'connfig' is not a git command. See 'git --help'.

The most similar command is
        config

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~
$ git config --list --global
user.email=y.korchovyi@gmail.com
user.user=Demonmaycray

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~
$ git clone https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2.git
Cloning into 'DevOps_online_Vinnytsia_2021Q2'...
warning: You appear to have cloned an empty repository.

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~
$ cd DevOps_online_Vinnytsia_2021Q2

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2 (master)
$ cd m1

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1 (master)
$ cd Task1.1

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../

nothing added to commit but untracked files present (use "git add" to track)

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git add readme.txt

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        imeges/
        index.html


Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git commit -m "create new file"
[master (root-commit) 21bec59] create new file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 m1/Task1.1/readme.txt

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (5/5), 296 bytes | 296.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2.git
 * [new branch]      master -> master

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git init
Initialized empty Git repository in C:/Users/Demonmaycray/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/.git/

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git branch develop

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git checkout develop
Switched to branch 'develop'

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git add index.html

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git commit -m 'create .html file '
[develop 9b15bf6] create .html file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 m1/Task1.1/index.html

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git push
fatal: The current branch develop has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin develop


Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git branch images

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git checkout images
Switched to branch 'images'

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (images)
$ mkdir images

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (images)
$ cd images

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images (images)
$ git add 1.jpg

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images (images)
$ git add 2.jpg

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images (images)
$ git add 3.jpg

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images (images)
$ git commit -m 'create some images'
[images aacca37] create some images
 3 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 m1/Task1.1/images/1.jpg
 create mode 100644 m1/Task1.1/images/2.jpg
 create mode 100644 m1/Task1.1/images/3.jpg

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images (images)
$ git push
fatal: The current branch images has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin images


Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images (images)
$ git status
On branch images
nothing to commit, working tree clean

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images (images)
$ git push origin images
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 16 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (12/12), 1.26 MiB | 2.69 MiB/s, done.
Total 12 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'images' on GitHub by visiting:
remote:      https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2/pull/new/images
remote:
To https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2.git
 * [new branch]      images -> images

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images (images)
$ git checkout develop
Switched to branch 'develop'

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images
$ git status
fatal: failed to stat 'C:/Users/Demonmaycray/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images': Permission denied

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/images
$ cd ..

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git push origin develop
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'develop' on GitHub by visiting:
remote:      https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2/pull/new/develop
remote:
To https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2.git
 * [new branch]      develop -> develop

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git status
On branch develop
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        imeges/

no changes added to commit (use "git add" and/or "git commit -a")

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git add index.html

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git commit -m "modified file index.html"
[develop 53eb7e9] modified file index.html
 1 file changed, 11 insertions(+)

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git push
fatal: The current branch develop has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin develop


Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git branch styles

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git checkout styles
Switched to branch 'styles'

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (styles)
$ git push origin styles
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 481 bytes | 481.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'styles' on GitHub by visiting:
remote:      https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2/pull/new/styles
remote:
To https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2.git
 * [new branch]      styles -> styles

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (styles)
$ mkdir styles

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (styles)
$ cd styles

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/styles (styles)
$ git add styles.css
fatal: pathspec 'styles.css' did not match any files

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/styles (styles)
$ git add style.css

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/styles (styles)
$ git commit -m "create some styles"
[styles 6bfad9b] create some styles
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 m1/Task1.1/styles/style.css

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/styles (styles)
$ git push origin styles
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (5/5), 438 bytes | 438.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2.git
   53eb7e9..6bfad9b  styles -> styles

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1/styles (styles)
$ cd ..

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (styles)
$ git add index.html

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (styles)
$ git commit -m "chenged file index.html"
[styles f3e84fb] chenged file index.html
 1 file changed, 1 deletion(-)

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (styles)
$ git checkout develop
Switched to branch 'develop'

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git push
fatal: The current branch develop has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin develop


Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git push origin styles
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 430 bytes | 430.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2.git
   6bfad9b..f3e84fb  styles -> styles

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git add index.html

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git push
fatal: The current branch develop has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin develop


Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git push origin develop
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2.git
   9b15bf6..53eb7e9  develop -> develop

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git checkout images
Switched to branch 'images'

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (images)
$ git push origin images
Everything up-to-date

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (images)
$ git status
On branch images
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        imeges/

nothing added to commit but untracked files present (use "git add" to track)

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (images)
$ git checkout develop
Switched to branch 'develop'

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git marge images
git: 'marge' is not a git command. See 'git --help'.

The most similar command is
        merge

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git merge images
hint: Waiting for your editor to close the file...       0 [sig] bash 1429! sigpacket::process: Suppressing signal 18 to win32 process (pid 12116)
 683064 [sig] bash 1429! sigpacket::process: Suppressing signal 18 to win32 process (pid 12116)
117599078 [sig] bash 1429! sigpacket::process: Suppressing signal 18 to win32 process (pid 12116)
118868950 [sig] bash 1429! sigpacket::process: Suppressing signal 18 to win32 process (pid 12116)
119525041 [sig] bash 1429! sigpacket::process: Suppressing signal 18 to win32 process (pid 12116)
119689546 [sig] bash 1429! sigpacket::process: Suppressing signal 18 to win32 process (pid 12116)
120088678 [sig] bash 1429! sigpacket::process: Suppressing signal 18 to win32 process (pid 12116)
150231924 [sig] bash 1429! sigpacket::process: Suppressing signal 18 to win32 process (pid 12116)
Merge made by the 'recursive' strategy.
 m1/Task1.1/images/1.jpg | Bin 0 -> 895862 bytes
 m1/Task1.1/images/2.jpg | Bin 0 -> 63912 bytes
 m1/Task1.1/images/3.jpg | Bin 0 -> 389358 bytes
 3 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 m1/Task1.1/images/1.jpg
 create mode 100644 m1/Task1.1/images/2.jpg
 create mode 100644 m1/Task1.1/images/3.jpg

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git merge styles
Merge made by the 'recursive' strategy.
 m1/Task1.1/index.html       | 1 -
 m1/Task1.1/styles/style.css | 0
 2 files changed, 1 deletion(-)
 create mode 100644 m1/Task1.1/styles/style.css

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (develop)
$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git merge develop
Updating 21bec59..5d185be
Fast-forward
 m1/Task1.1/images/1.jpg     | Bin 0 -> 895862 bytes
 m1/Task1.1/images/2.jpg     | Bin 0 -> 63912 bytes
 m1/Task1.1/images/3.jpg     | Bin 0 -> 389358 bytes
 m1/Task1.1/index.html       |  10 ++++++++++
 m1/Task1.1/styles/style.css |   0
 5 files changed, 10 insertions(+)
 create mode 100644 m1/Task1.1/images/1.jpg
 create mode 100644 m1/Task1.1/images/2.jpg
 create mode 100644 m1/Task1.1/images/3.jpg
 create mode 100644 m1/Task1.1/index.html
 create mode 100644 m1/Task1.1/styles/style.css

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git log --help

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git log -p
commit 5d185be398d930d285181570a56828887ec6937b (HEAD -> master, develop)
Merge: 8240d21 f3e84fb
Merge: 8240d21 f3e84fb
Author: unknown <y.korchovyi@gmail.com>
Date:   Sun Mar 21 14:58:02 2021 +0200

    Merge branch 'styles' into develop

commit 8240d218373dcb0c632984f98bbcba9018c9e061
Merge: 53eb7e9 aacca37
Author: unknown <y.korchovyi@gmail.com>
Date:   Sun Mar 21 14:53:16 2021 +0200

    Merge branch 'images' into develop

commit f3e84fb29737e6d8142ac98508bca70965247ff3 (origin/styles, styles)
Author: unknown <y.korchovyi@gmail.com>
Date:   Sun Mar 21 14:28:24 2021 +0200

    chenged file index.html

diff --git a/m1/Task1.1/index.html b/m1/Task1.1/index.html
index b75461e..ad5844b 100644
--- a/m1/Task1.1/index.html
+++ b/m1/Task1.1/index.html
@@ -4,7 +4,6 @@
   <meta charset="utf-8">
    </head>
  <body>
-    <img src="imeges/1.jpg">
     <img src="imeges/2.jpg">
     <img src="imeges/3.jpg">
  </body>

commit 6bfad9bdd66f9b65c03312da994817a12ad1a2dc
Author: unknown <y.korchovyi@gmail.com>
Date:   Sun Mar 21 14:25:57 2021 +0200

    create some styles

diff --git a/m1/Task1.1/styles/style.css b/m1/Task1.1/styles/style.css
new file mode 100644
index 0000000..e69de29

commit 53eb7e956d51bd4466b2a69f00662c33d707ce26 (origin/develop)
Author: unknown <y.korchovyi@gmail.com>
Date:   Sun Mar 21 14:18:40 2021 +0200

    modified file index.html

diff --git a/m1/Task1.1/index.html b/m1/Task1.1/index.html
index e69de29..b75461e 100644
--- a/m1/Task1.1/index.html
+++ b/m1/Task1.1/index.html
@@ -0,0 +1,11 @@
+<!DOCTYPE HTML>
+<html>
+ <head>
+  <meta charset="utf-8">
+   </head>
+ <body>
+    <img src="imeges/1.jpg">
+    <img src="imeges/2.jpg">
+    <img src="imeges/3.jpg">
+ </body>
+</html>
\ No newline at end of file

commit aacca3794d1e354a23846ed2f92a2b3b2353e656 (origin/images, images)
Author: unknown <y.korchovyi@gmail.com>
Date:   Sun Mar 21 14:06:49 2021 +0200

    create some images

diff --git a/m1/Task1.1/images/1.jpg b/m1/Task1.1/images/1.jpg
new file mode 100644
index 0000000..2577787
Binary files /dev/null and b/m1/Task1.1/images/1.jpg differ
diff --git a/m1/Task1.1/images/2.jpg b/m1/Task1.1/images/2.jpg
new file mode 100644
index 0000000..a377635
Binary files /dev/null and b/m1/Task1.1/images/2.jpg differ
diff --git a/m1/Task1.1/images/3.jpg b/m1/Task1.1/images/3.jpg
new file mode 100644
index 0000000..8f196fa
Binary files /dev/null and b/m1/Task1.1/images/3.jpg differ

commit 9b15bf61030c72a0176acd2626348fdcd5cd6011
Author: unknown <y.korchovyi@gmail.com>
Date:   Sun Mar 21 14:03:33 2021 +0200

    create .html file

diff --git a/m1/Task1.1/index.html b/m1/Task1.1/index.html
new file mode 100644
index 0000000..e69de29

commit 21bec59f4e06b8c422d4925142c99384569d6a5e (origin/master)
Author: unknown <y.korchovyi@gmail.com>
Date:   Sun Mar 21 13:31:45 2021 +0200

    create new file

diff --git a/m1/Task1.1/readme.txt b/m1/Task1.1/readme.txt
new file mode 100644
index 0000000..e69de29
(END)

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)


Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git push origin --all
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (8/8), 859 bytes | 429.00 KiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2.git
   53eb7e9..5d185be  develop -> develop
   21bec59..5d185be  master -> master

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git reflog
5d185be (HEAD -> master, origin/master, origin/develop, develop) HEAD@{0}: merge develop: Fast-forward
21bec59 HEAD@{1}: checkout: moving from develop to master
5d185be (HEAD -> master, origin/master, origin/develop, develop) HEAD@{2}: merge styles: Merge made by the 'recursive' strategy.
8240d21 HEAD@{3}: merge images: Merge made by the 'recursive' strategy.
53eb7e9 HEAD@{4}: checkout: moving from images to develop
aacca37 (origin/images, images) HEAD@{5}: checkout: moving from develop to images
53eb7e9 HEAD@{6}: checkout: moving from styles to develop
f3e84fb (origin/styles, styles) HEAD@{7}: commit: chenged file index.html
6bfad9b HEAD@{8}: commit: create some styles
53eb7e9 HEAD@{9}: checkout: moving from develop to styles
53eb7e9 HEAD@{10}: commit: modified file index.html
9b15bf6 HEAD@{11}: checkout: moving from images to develop
aacca37 (origin/images, images) HEAD@{12}: commit: create some images
9b15bf6 HEAD@{13}: checkout: moving from develop to images
9b15bf6 HEAD@{14}: commit: create .html file
21bec59 HEAD@{15}: checkout: moving from master to develop
21bec59 HEAD@{16}: commit (initial): create new file

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git add task1.1_GIT.txt

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git commit -m "Execute command git reflog"
[master b81d866] Execute command git reflog
 1 file changed, 18 insertions(+)
 create mode 100644 m1/Task1.1/task1.1_GIT.txt

Demonmaycray@DESKTOP-8S7ON18 MINGW64 ~/DevOps_online_Vinnytsia_2021Q2/m1/Task1.1 (master)
$ git push
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 735 bytes | 735.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Demonmaycray/DevOps_online_Vinnytsia_2021Q2.git
   5d185be..b81d866  master -> master
