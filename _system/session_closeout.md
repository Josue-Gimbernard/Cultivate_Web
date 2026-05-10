# Session Closeout

For implementation work:

```powershell
python -m compileall app.py
python -m unittest discover -s tests
npm.cmd run lint:colors
node --check static\js\main.js
```

Git is initialized and pushed. If repo, auth, deploy, or commit behavior changes, update `memory/06-repo-and-deploy-operations.md`.
