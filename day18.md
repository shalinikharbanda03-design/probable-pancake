Skill Name: brain-dump-action-planner

Description: Transform messy notes, meeting transcripts, voice memos, brainstorming sessions, and stream-of-consciousness thoughts into structured summaries, action plans, decisions, open questions, and task lists. Organize information clearly without inventing, assuming, or filling gaps. Preserve all names, dates, numbers, and terminology exactly as provided.

Instructions:

## Output Requirement

For Full Breakdown, Transcript Mode, and Merge Mode, generate the output as a complete interactive HTML artifact.

Requirements:

* Output a self-contained HTML artifact starting with <style>.
* Use a modern dashboard layout.
* Mobile responsive.
* Use cards, sections, badges, tables, and visual indicators.
* Do not use markdown.
* Use clean typography and strong visual hierarchy.
* Highlight important items using colored status badges.
* Make action items visually prominent.
* Use collapsible sections for long notes.
* Output only the HTML artifact.

### Required Sections

1. Summary

* Short overview of the note, meeting, transcript, or brain dump.

2. Key Takeaways

* Display as cards or structured highlights.

3. Action Items

* Interactive table containing:
* Task
* Owner
* Deadline
* Status

4. Open Questions

* Display unresolved topics and pending decisions.

5. Risks / Blockers

* Display dependencies, blockers, risks, and concerns.

6. Conflicts

* Display conflicting deadlines, owners, decisions, or information.

7. Additional Notes

* Supporting context that does not fit elsewhere.

8. Source Information (Merge Mode only)

* Display merged sources.

### Status Badges

Use:

* 🔴 High Priority
* 🟠 Medium Priority
* 🟢 Low Priority
* ⚠️ Conflict
* ❓ Open Question
* ✅ Completed
* ⏳ Pending

### Missing Information

If information is missing display:

'Not specified'

Never invent values.

### Transcript Mode

Include:

* Speaker Summary
* Decisions by Speaker
* Action Items by Speaker
* Attribution Notes when ownership is unclear

Use speaker labels exactly as provided.

### Merge Mode

Include:

* Duplicate Items Section
* Conflict Resolution Review Section
* Source Note

Never automatically resolve conflicts.

### Design Goals

The final artifact should feel like:

* Notion
* ClickUp
* Linear
* Asana
* Airtable
* Modern Project Dashboard

Use responsive cards, clean tables, section headers, badges, hover effects, soft shadows, and dashboard-style layouts.

Everything displayed must come directly from the provided notes.

Never add, infer, assume, predict, estimate, or complete missing information.

Generate the complete HTML directly starting with <style>.
<style>
Response/Result:-
  body {
  font-family: 'Inter', sans-serif;
  margin: 0;
  padding: 0;
  background: #f7f9fc;
  color: #333;
}
.dashboard {
  max-width: 1200px;
  margin: auto;
  padding: 20px;
}
h2 {
  font-size: 1.4rem;
  margin-bottom: 10px;
  color: #222;
}
.section {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}
.card {
  flex: 1;
  min-width: 200px;
  background: #f0f4ff;
  border-radius: 8px;
  padding: 15px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}
.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 600;
}
.badge.high { background: #ffdddd; color: #d00; }
.badge.medium { background: #ffeccc; color: #d67f00; }
.badge.low { background: #ddffdd; color: #0a0; }
.badge.conflict { background: #ffe0e0; color: #a00; }
.badge.open { background: #e0f0ff; color: #0077cc; }
.badge.completed { background: #d9ffd9; color: #008800; }
.badge.pending { background: #fff0cc; color: #cc8800; }
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}
table th, table td {
  padding: 10px;
  border-bottom: 1px solid #eee;
  text-align: left;
}
.collapsible {
  cursor: pointer;
  padding: 10px;
  background: #eef2f7;
  border-radius: 6px;
  margin-bottom: 10px;
}
.collapsible-content {
  display: none;
  padding: 10px;
  background: #fafafa;
  border-radius: 6px;
}
@media (max-width: 768px) {
  .cards { flex-direction: column; }
}
</style>

<div class="dashboard">

  <div class="section">
    <h2>Summary</h2>
    <p>Not specified</p>
  </div>

  <div class="section">
    <h2>Key Takeaways</h2>
    <div class="cards">
      <div class="card">Not specified</div>
      <div class="card">Not specified</div>
      <div class="card">Not specified</div>
    </div>
  </div>

  <div class="section">
    <h2>Action Items</h2>
    <table>
      <thead>
        <tr>
          <th>Task</th>
          <th>Owner</th>
          <th>Deadline</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Not specified</td>
          <td>Not specified</td>
          <td>Not specified</td>
          <td><span class="badge pending">⏳ Pending</span></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="section">
    <h2>Open Questions</h2>
    <ul>
      <li><span class="badge open">❓ Open Question</span> Not specified</li>
    </ul>
  </div>

  <div class="section">
    <h2>Risks / Blockers</h2>
    <ul>
      <li><span class="badge high">🔴 High Priority</span> Not specified</li>
    </ul>
  </div>

  <div class="section">
    <h2>Conflicts</h2>
    <ul>
      <li><span class="badge conflict">⚠️ Conflict</span> Not specified</li>
    </ul>
  </div>

  <div class="section">
    <h2>Additional Notes</h2>
    <div class="collapsible">Show Notes</div>
    <div class="collapsible-content">
      <p>Not specified</p>
    </div>
  </div>

</div>

<script>
document.querySelectorAll('.collapsible').forEach(button => {
  button.addEventListener('click', () => {
    const content = button.nextElementSibling;
    content.style.display = content.style.display === 'block' ? 'none' : 'block';
  });
});
</script>
Meeting alarm set for 10 AM Monday.
Discuss project Alpha timeline.
Rahul will prepare draft by Wednesday.
Need confirmation from finance team.
Risk: vendor delay.
Conflict: Marketing wants launch in July, Dev team says August.

<img width="700" height="462" alt="image" src="https://github.com/user-attachments/assets/98a7a40b-874a-4b4f-9152-f48af3f0a56b" />
<img width="686" height="465" alt="image" src="https://github.com/user-attachments/assets/f37842e6-ea9e-4ec4-b6b7-25909015ceca" />
<img width="641" height="129" alt="image" src="https://github.com/user-attachments/assets/fff81c14-8ac5-4e4b-bb92-a2d66dd3d3f9" />
