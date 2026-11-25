# Mission 6 — Git and GitHub

## 1. Task / objective
Understand version control: check status, stage and commit changes, view history, create a branch, open a Pull Request
(PR) on GitHub, and explain how this workflow helps people collaborate.

## 2. Work completed
- Inspected the repository status, staged a single README, committed it and viewed the history (Task 6.1).
- Created the branch **`update-about`**, added a **"My Learning"** section to the root `README.md`, committed it and
  published the branch to GitHub (Task 6.2).
- Opened a Pull Request from `update-about` into `main`, reviewed the changed file and merged it, then switched back
  to `main` locally and pulled the latest changes (Task 6.3).
- Wrote a Git command glossary (Task 6.4).

**Pull Request status:** ✅ Merged — `update-about` → `main` (PR #1).

### Task 6.1 — Basic Git workflow

| Git operation | Command | What it does in my own words |
|---------------|---------|------------------------------|
| Check repository status | `git status` | Shows which branch I am on, which files changed, which are staged and which Git is not tracking yet. |
| Stage selected changes | `git add mission-06-git-github/README.md` | Puts *only that file's* changes into the "staging area" — a list of what will go into the next commit. |
| Create a commit | `git commit -m "message"` | Saves a permanent snapshot of everything staged, with a message, author and time. |
| View commit history | `git log --oneline` | Lists past commits, newest first, each with a short ID and its message. |

**Staging vs committing:** staging (`git add`) is like putting items into a box and choosing exactly what goes in;
committing (`git commit`) is sealing and labelling the box so it is saved in history. I can stage and unstage freely,
but a commit is a recorded checkpoint I can always go back to. Staging lets me commit only the files that belong
together, instead of everything I changed.

### Task 6.2 — Create and use a branch
```bash
git switch -c update-about        # create the branch and move onto it
git push -u origin update-about   # publish the branch to GitHub
git pull origin main              # bring in the My Learning section already added on main
# edit README.md → add a blank line before "## My Learning" and a new bullet about branches and PRs
git status                        # README.md shows as modified
git add README.md
git commit -m "Expand My Learning section with branches and pull requests"
git push                          # publish the new commit on update-about
```

### Task 6.3 — Pull Request
1. Opened the repository on GitHub, which showed a "Compare & pull request" button for `update-about`.
2. Set **base: `main`** ← **compare: `update-about`**.
3. Title: *Expand My Learning section with branches and pull requests*. Description: explains that the PR adds a short section about what
   I have learned so far.
4. Checked the **Files changed** tab — only `README.md` changed, with the new lines in green.
5. Merged the PR.
6. Back in the Terminal: `git switch main` and `git pull` to bring the merged change onto my computer.

**What a branch is:** a separate line of work. I can change files on a branch without touching `main`, so the main
version stays safe and working.

**What a Pull Request is:** a request on GitHub to merge one branch into another. It shows exactly what changed and
lets others review, comment and approve before the change is merged.

**Why they help teams:** several people can work on different branches at the same time without overwriting each
other's work. PRs make sure changes are checked before they reach `main`, and they keep a record of who changed what
and why.

### Task 6.4 — Git command glossary

| Operation | Command | One-line explanation |
|-----------|---------|----------------------|
| Initialise a repository | `git init` | Turns a normal folder into a Git repository so changes can be tracked. |
| Check status | `git status` | Shows what has changed, what is staged and which branch I am on. |
| Stage changes | `git add <file>` | Chooses which changes will go into the next commit. |
| Commit changes | `git commit -m "msg"` | Saves the staged changes as a snapshot with a message. |
| View history | `git log --oneline` | Lists previous commits with their IDs and messages. |
| Create / list branches | `git branch <name>` / `git branch` | Makes a new branch, or lists all branches (the current one has `*`). |
| Switch branches | `git switch <name>` | Moves my working folder to another branch. |
| Publish changes | `git push` | Uploads my local commits to GitHub. |
| Retrieve remote changes | `git pull` | Downloads new commits from GitHub and merges them into my local branch. |

## 3. Commands / tools used
`git status`, `git add`, `git commit`, `git log --oneline`, `git switch -c`, `git push -u origin`, `git switch`,
`git pull`, and the GitHub website (Compare & pull request, Files changed, Merge pull request).

## 4. My understanding
Git is a version control system on my computer that records snapshots (commits) of my project; GitHub stores the
repository online and adds collaboration tools like Pull Requests. The normal flow is: change files → `git status` →
`git add` → `git commit` → `git push`. Branches let me try changes safely, and PRs let changes be reviewed before they
join `main`. After merging on GitHub, my local `main` is behind until I run `git pull`.

## 5. Difficulties faced
- I first added the "My Learning" section by editing `README.md` directly on GitHub. That created a commit straight on
  `main` (*Add 'My Learning' section to README*) instead of on my branch.
- Because of that, `git commit` on `update-about` said **"nothing to commit, working tree clean"**, and GitHub's compare
  page said **"There isn't anything to compare — main and update-about are identical."**

## 6. How I resolved them
- Learned that a branch only differs from `main` if it has its own commits. I ran `git pull origin main` on
  `update-about` so it had the latest `main`, then made a new change on the branch (a blank line before the heading and
  a fourth bullet about branches and Pull Requests).
- `git status` now showed `README.md` as modified, so `git add`, `git commit` and `git push` worked, and the compare page
  showed 1 changed file. I opened PR #1 and merged it, then ran `git switch main` and `git pull`.
- Lesson: make changes on the branch, not directly on `main`, so they can be reviewed in a Pull Request.

## 7. Evidence / files
- `README.md` (this file) — Git workflow table, branch and PR notes, glossary.
- On GitHub: the `update-about` branch, the merged Pull Request, and the commit history (Insights → Network / Commits).

## 8. Commit details
- Branch commit: **`Expand My Learning section with branches and pull requests`** (on `update-about`, merged via PR #1).
- Mission commit: **`Complete Git and GitHub collaboration mission`**
- Both pushed to GitHub and verified.
