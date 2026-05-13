# Refactoring Bridge Server & UI Enhancement

This plan focuses on finalizing the modularization of the Bridge Server and upgrading the Connect AI sidebar UI with premium aesthetics.

## User Review Required

> [!IMPORTANT]
> I will be removing a large block of code (approx. 550 lines) from `extension.ts` that has already been refactored into `bridge_server.ts`. I will ensure all endpoints are fully migrated before deletion.

## Proposed Changes

### 1. Bridge Server Module
#### [MODIFY] [bridge_server.ts](file:///c:/Users/smile/connect-ai/src/bridge_server.ts)
- Add missing endpoints: `/api/evaluate`, `/api/evaluate-history`, and `/api/brain-inject`.
- Synchronize logic with the latest version found in `extension.ts` (including status bar messages and error handling).
- Ensure all dependencies (like `axios`, `fs`, `path`, `vscode`) are correctly used.

### 2. Extension Main Entry
#### [MODIFY] [extension.ts](file:///c:/Users/smile/connect-ai/src/extension.ts)
- Delete the orphaned code block (lines 8020–8578) following the `bridgeServer.startBridgeServer` call.
- Verify that all necessary parameters are passed to `startBridgeServer`.

### 3. Sidebar UI Enhancement
#### [MODIFY] [sidebar.html](file:///c:/Users/smile/connect-ai/assets/webview/sidebar.html)
- Enhance glassmorphism effects on the input area and buttons.
- Fine-tune the "Sovereign" palette for better contrast and depth.
- Add subtle micro-animations to chat messages.

## Verification Plan

### Automated Tests
- I will use a dummy client (or browser tools) to hit the following endpoints on `http://127.0.0.1:4825`:
  - `GET /ping`
  - `POST /api/brain-inject` (with mock data)
  - `POST /api/skill-inject` (with mock data)
- Verify VSCode notifications and status bar updates.

### Manual Verification
- Check the sidebar UI visually to ensure glassmorphism and the new palette look "premium".
- Confirm no compilation errors in `extension.ts` after the large deletion.
