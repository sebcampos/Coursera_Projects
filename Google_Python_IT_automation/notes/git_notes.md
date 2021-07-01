# Git notes

## Commands

- `diff` will show the difference between two passed scripts or files, ie `diff -u validations1.py validations2.py` the `-u` flag changes the format to a more human readable one

- `patch` command will take a .diff file and apply the changes to a new file


- `git branch <new_branch_name>` will create a new branch

- `git checkout <branch>` will move the current working directory to that branch's head commit

- `git checkout -b <new_branch_name>` will create a new branch and move to it

- `git branch -d <branch_name>` will delete the branch

- `git log --graph --oneline` will graph our commits for us one line at a time display the branches divergence and resolutions/merges

- `git merge <branch_1> <branch2>` will merge 2 branches

- `git merge --abort` will abort the merge in progress 

- `git remote show origin` will show information about our git remote branch

- `git branch -r` will view remote branches currently being tracked

- `git pull` fetches remote updates and merges

- `git fetch` fetches remote updates but does NOT merge, used to review the changes in the remote

- `git remote` lists remote repos

- `git remote -v` lists remote repos verbosely

- `git remote show <name>` describes a single remote repo

- `git remote update` fetches the most up-to-date objects

- `git rebase <new_base_branch>` will make the given branch the new base  



## Merging

The git merge command takes the independant snapshots from one branch and "tangles" it with the second one
or, more acuratley, both branches will now point to the same commit


### Two merges
- fast forward
	brings the branch up to date with the new one adding new files and updating existing files

- Three way merge
	a commit was made on one branch after the divergence or initial split of the branches. changes continually made on both branches after the split will cause git to reconcile with a three way merge, usually tracking back the original point of divergence

### Merge Conflicts

When both branches we are trying to merge have edits to the same part of the same file will create a merge conflict.
When a merge conflict occurs our branches will not be able to reconcile and merge automatically, we can use `git status` to see more about the conflicts
our options are to run `--abort` or to fix the merge conflicts then use `git add <fixed_file>` before we can continue the merge. During this state we can open the files and see helpful feedback from git highlighting the conflicts. Once the conflicts are resolved we can continue with the commit


