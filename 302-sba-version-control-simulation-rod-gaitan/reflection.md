Reflection for SBA - Version Control

#
1) The steps you took to create and manage branches:
I actually did it a little different than the instructions dictated. While the SBA wanted us to create the 'feature/header' first I decided to 
- start by placing a boilerplate file (index.html) in the 'main' branch first
- then I saved, commited the creation of this file in branch 'main'
- then while still in the 'main' branch, I went ahead and created the 'feature/header' branch: 
$ git checkout -b feature/header
- while still in the 'feature/header' branch, I proceeded to add the code html code for the header and placed it before the <main> section of the 'index.html'
- then I saved, commited the creation of this file in the 'feature/header' branch
- then I switched back to teh 'main' branch
- then while still in the 'main' branch, I went ahead and created the 'feature/footer_sba' branch: 
$ git checkout -b feature/footer_sba
-- note, I had to name it 'feature/footer_sba', bc appearently there is alerady a 'feature/footer' and a 'feature/footer_2' branches from other projects in my repo
- while still in the 'feature/footer_sba' branch, I proceeded to add the html code for the footer and placed it BEFORE the <main> section of the 'index.html', expecting to create a conflict when merging at some point.
- then I saved, commited the creation of this file in the 'feature/footer_sba' branch
- then I switched back to the 'main' branch
- from which I first merged in the 'feature/header' branch, expecting no merge conflict
- thereafter merged in 'feature/footer_sba' branch, and as suspected merge conflict was generated
- Note: I also did create a conflict as the SBA stated by changing text in the feature/header by changing "Home of the 'Rod'" to  "Home of the 'Rod!!!'"

#
2) How you handled the merge conflict.
I had to determine the correct order of header, footer, and main content, since keeping both sides would've caused duplicate/misplaced markup. The way I handled it was as follows:
- while in <main|MERGING> state
- since the conflict happened at the local repo, I opened the conflicting file in VS Code
- I reinserted the header and footer code in their appropriate sections within the html file.
- then I removed the <<<<<<, =======, >>>>>>> markers
- then fixed text changes ("Home of the 'Rod'" to  "Home of the 'Rod!!!'")
- then I saved, commited the resolved chnages to the 'main' branch
- then pushed my local repo onto remote repo:
$ git push origin main

#
3) How the pull request process helped you ensure code quality and collaboration.
After pushing 'main' to GitHub, I created a 'review/main' branch and opened a PR comparing my changes against it. I then had a classmate review my PR, and found their feedback and approval helped me to catch things that I couldn't see when reviewing my own code. This made it clear that the PR process isn't just a formality before merging, but a real verification tool for catching issues and maintaining code quality before changes reaching the 'main' on GitHub.
