# Project Portability and GitHub Integration Plan

This plan outlines the steps to make the `alpha-browser` project (Dashboard) portable so you can use it on your office computer by saving it to GitHub.

## User Review Required

> [!IMPORTANT]
> You will need a GitHub account. If you don't want your code to be public, we should create a **Private Repository**.
> The office computer will need Node.js and Python installed to run the full dashboard and video rendering scripts.

## Proposed Changes

### 1. Refactor Absolute Paths
We will replace hardcoded paths like `C:\Users\smile\alpha-browser` with dynamic relative paths.

#### [MODIFY] [list-outputs/route.ts](file:///c:/Users/smile/alpha-browser/src/app/api/list-outputs/route.ts)
- Use `process.cwd()` to dynamically locate the `output` folder.

#### [MODIFY] [play-video/route.ts](file:///c:/Users/smile/alpha-browser/src/app/api/play-video/route.ts)
- Use `path.join(process.cwd(), 'output', filename)` for video playback.

#### [MODIFY] [open-folder/route.ts](file:///c:/Users/smile/alpha-browser/src/app/api/open-folder/route.ts)
- Use `path.join(process.cwd(), 'output')` to open the folder.

---

### 2. Git Configuration & Optimization

#### [MODIFY] [.gitignore](file:///c:/Users/smile/alpha-browser/.gitignore)
- Ensure large generated files (like those in `output/` and `temp_audio/`) are ignored to keep the repository size manageable.
- We will keep `biblical_assets/`, `research/`, and `scripts/` as they are essential.

#### [NEW] [SETUP.md](file:///c:/Users/smile/alpha-browser/SETUP.md)
- Create a guide for the office computer:
    - Install Node.js & Python.
    - Run `npm install`.
    - Install Python dependencies (`moviepy`, `edge-tts`, etc.).

---

### 3. GitHub Integration
1. Initialize/Commit all changes locally.
2. Provide you with instructions to:
    - Create a new repository on GitHub.
    - Connect the local project to GitHub (`git remote add`).
    - Push the code.

## Verification Plan

### Automated Tests
- Verify that the dashboard still lists outputs correctly using relative paths.
- Check that `git status` shows a clean set of files to be committed.

### Manual Verification
- Test "Play Video" and "Open Folder" buttons on the dashboard to ensure relative paths work as expected.
- Confirm the project is successfully pushed to GitHub.
