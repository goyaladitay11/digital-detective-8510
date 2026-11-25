# Mission 0 — Create your GitHub workspace

## 1. Task / objective
Create a correctly named public GitHub repository and prepare a clear folder structure (one folder per mission) with a
root README.

## 2. Work completed
- Chose the repository name **`digital-detective-8510`** (assignment name + last four digits of my USN).
- Created a local folder with exactly the same name and turned it into a Git repository.
- Created all mission folders, a `README.md` in each, an empty `number_converter.py` for Mission 5, and an
  `evidence/` folder.
- Wrote the root `README.md` with a project description and a mission index that links to every mission README.
- Created a public repository on GitHub with the same name (without an online README, so there is only one) and
  pushed the local files.

**Folders and files created**

```
digital-detective-8510/
├── README.md
├── evidence/
├── mission-00-setup/README.md
├── mission-01-computer-basics/README.md
├── mission-02-terminal/README.md
├── mission-03-operating-system/README.md
├── mission-04-programs/README.md
├── mission-05-numbers-data/README.md
├── mission-05-numbers-data/number_converter.py
├── mission-06-git-github/README.md
├── mission-07-networking/README.md
└── mission-08-final-report/README.md
```

**Tools checked**

| Tool | Command used | Version found |
|------|--------------|---------------|
| Python 3 | `python3 --version` | Python 3.14.8 |
| Git | `git --version` | git version 2.54.0 (Apple Git-157) |

## 3. Commands / tools used
| Command / tool | Purpose |
|----------------|---------|
| `python3 --version`, `git --version` | Check that Python 3 and Git are installed. |
| `mkdir` | Create the project folder and the mission folders. |
| `touch` | Create empty files such as `number_converter.py`. |
| `git init` | Turn the folder into a Git repository. |
| `git add`, `git commit` | Stage and save the setup files as the first commit. |
| `git remote add origin`, `git push -u origin main` | Connect the local folder to GitHub and upload it. |
| GitHub CLI (`gh`) | Sign in to GitHub from the Terminal and create the public repository. |

## 4. My understanding
A **repository** is a project folder that Git tracks. Git remembers every saved version (commit) of the files, so I can
see what changed and go back if something breaks. GitHub keeps a copy of the repository online so others (like my
instructor) can see it.

The structure is organised **by mission** so that each topic's notes, programs and evidence stay together. It makes the
repository easy to navigate, and because each mission is committed separately, the commit history shows my progress
step by step.

## 5. Difficulties faced
- The GitHub CLI (`gh`) was not installed and my computer had no SSH key, so at first I could not push to GitHub.
- Git did not have a name/email configured for commits.

## 6. How I resolved them
- Installed the GitHub CLI with Homebrew and signed in once with `gh auth login` through the browser.
- Set the commit author name and GitHub "noreply" email only for this repository, so my real email stays private.

## 7. Evidence / files
- `README.md` (root) — project introduction and mission index.
- This file — tools, versions and folder structure.

## 8. Commit details
- Commit message: **`Set up Digital Detective mission structure`**
- Pushed to GitHub and verified that the folders appear in the repository.
