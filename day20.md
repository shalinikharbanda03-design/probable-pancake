You are an expert front-end developer. Build me a complete, fully working face puzzle game as a single self-contained HTML file (no external dependencies except what can load from cdnjs.cloudflare.com, cdn.jsdelivr.net, or unpkg.com).

FEATURES REQUIRED — deliver ALL of these in one complete response:

1. CAMERA ACCESS
   - On load, request webcam permission using getUserMedia()
   - Show a live video preview (front-facing camera preferred)
   - Display a 'Take Photo' button to snapshot the user's face onto a canvas

2. PUZZLE GENERATION
   - After snapshot, let the user choose difficulty: 3×3, 4×4, or 5×5 grid
   - Slice the captured face image into equal puzzle pieces
   - Randomly scramble the pieces (guarantee it is solvable)
   - Render each piece as a draggable tile at its scrambled position

3. DRAG & TOUCH GESTURE CONTROLS
   - Support both mouse drag (desktop) and touch drag (mobile/tablet)
   - When a piece is dropped onto another piece's cell, swap their positions
   - Snap pieces to the nearest grid cell on release
   - Highlight a piece with a coloured border while it is being dragged
   - Show a green border on pieces that land in their correct position

4. TIMER & MOVE COUNTER
   - Start the timer the moment the puzzle begins
   - Display elapsed time live (format: mm:ss.t)
   - Count and display total moves made
   - Show how many pieces are correctly placed out of the total

5. WIN DETECTION & RESULTS SCREEN
   - Detect automatically when all pieces are in the correct position
   - Stop the timer immediately on win
   - Show a results overlay with: final time, total moves, and difficulty
   - Save the top 5 best times to localStorage with date, time, moves, and difficulty
   - Display a leaderboard of saved best times

6. UI & POLISH
   - Clean, modern design
   - Works on desktop and mobile
   - 'Retake Photo' button
   - 'Play Again' button
   - 'New Photo' button
   - Responsive layout

TECHNICAL REQUIREMENTS:
- Single HTML file
- All CSS and JS inline
- No frameworks
- Must work in Chrome, Firefox, and Safari
- Camera must work over HTTPS or localhost
- Handle camera permission denied gracefully
- Do NOT leave placeholder comments

Output the complete HTML file in one code block. Do not truncate or summarise any section.
Result #
Now let me build the complete face puzzle game:Created a file, read a fileCreated a file, read a fileHere's your complete face puzzle game — all features delivered in one self-contained HTML file.
What's inside:

Camera — requests webcam on load with a face oval guide, graceful error message if denied
Snapshot — captures a square crop of your face, mirrors it naturally, shows a preview
Difficulty picker — 3×3 / 4×4 / 5×5 with highlighted selection cards
Puzzle generation — slices the image into equal pieces, randomly scrambles them
Drag & touch — mouse drag on desktop, touch drag on mobile/tablet; pieces snap to grid cells on release; dragging piece gets a purple glow; a cyan border highlights the drop target
Correct placement — green border appears on pieces in the right cell, tracked in real time
HUD — live timer (mm:ss.t format), move counter, placed count, grid size
Win detection — auto-detects when all pieces are placed, stops timer, shows results overlay
Leaderboard — top 5 best times saved to localStorage with time, moves, grid, and date
All buttons — Retake Photo, Play Again, New Photo, Change Difficulty

To use: Open the file via a local server (e.g. python3 -m http.server) or any HTTPS host — camera requires a secure context. Works in Chrome, Firefox, and Safari.
Now let me build the complete face puzzle game:Here's your complete face puzzle game — all features delivered in one self-contained HTML file.

**What's inside:**

- **Camera** — requests webcam on load with a face oval guide, graceful error message if denied
- **Snapshot** — captures a square crop of your face, mirrors it naturally, shows a preview
- **Difficulty picker** — 3×3 / 4×4 / 5×5 with highlighted selection cards
- **Puzzle generation** — slices the image into equal pieces, randomly scrambles them
- **Drag & touch** — mouse drag on desktop, touch drag on mobile/tablet; pieces snap to grid cells on release; dragging piece gets a purple glow; a cyan border highlights the drop target
- **Correct placement** — green border appears on pieces in the right cell, tracked in real time
- **HUD** — live timer (mm:ss.t format), move counter, placed count, grid size
- **Win detection** — auto-detects when all pieces are placed, stops timer, shows results overlay
- **Leaderboard** — top 5 best times saved to `localStorage` with time, moves, grid, and date
- **All buttons** — Retake Photo, Play Again, New Photo, Change Difficulty

**To use:** Open the file via a local server (e.g. `python3 -m http.server`) or any HTTPS host — camera requires a secure context. Works in Chrome, Firefox, and Safari.
file:///C:/Users/DELL/Downloads/face-puzzle.html
