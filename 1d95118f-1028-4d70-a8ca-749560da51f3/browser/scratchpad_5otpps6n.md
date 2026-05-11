# Task: Verify Alpha Browser Functionality

## Status
- [ ] Navigate to http://localhost:3000
- [ ] Verify '웹 에이전트' click
- [ ] Verify '지식 라이브러리' click
- [ ] Verify 'CEO 루나' click
- [ ] Take screenshot of 'CEO 루나' page

## Findings
- Encountered a Build Error at http://localhost:3000:
  `You're importing a module that depends on usePathname into a React Server Component module. This API is only available in Client Components. To fix, mark the file (or its parent) with the "use client" directive.`
  File: `./src/app/layout.tsx (5:10)`
- The error persists after reload.
- Restricted from editing source files outside the browser directory.
