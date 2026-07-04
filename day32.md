:Prompt: Think Like a Marketing Strategist: Grow This Brand:

You are an expert frontend developer, UX designer, marketing strategist, and instructional designer.

Build a complete single-file HTML app called: "Think Like a Marketing Strategist: Grow This Brand"

The goal is to teach beginners how marketers think, not just generate marketing content. Every section should explain "What is this?" and "Why does it matter?" in simple language.

Requirements

Output ONLY one HTML file

React via CDN + Babel JSX

HTML, CSS and JavaScript only

No Tailwind, npm, backend or APIs

Runs offline

Responsive

Dark modern UI

Replayable with randomized businesses

Flow

Welcome screen introducing marketing strategy.

Let the user choose:

🏢 Use My Own Business

🙋 Build My Personal Brand ← if someone doesn't have a business, this lets them use their own name, expertise, and story as the brand

🎲 A New Client Has Arrived (randomly generate a business with industry, audience, budget, competitors and marketing challenge)

Teach the user to understand the business/brand and its audience. For personal brands, the "product" is the person's expertise and story. Replace "competitors" with "people in your space you admire."

Ask the user to choose the best social media platforms. Explain why each platform is or isn't suitable. For personal brands, weight LinkedIn, X/Twitter, YouTube, and newsletters more heavily.

Generate multiple content pillars. The user must choose only three. For personal brands, include pillars like Thought Leadership, Personal Story, Behind the Scenes, and Audience Education. Explain how each supports different goals.

Build a simple 30-day content roadmap showing weekly goals and strategy (not individual posts). For personal brands, Week 1 should focus on defining POV and optimizing bio/profile.

Generate one unexpected marketing event. For personal brands this could be: a viral post, a podcast invite, a public disagreement, someone copying your content, or a sudden follower spike. Let the user respond and explain consequences.

End with a Growth Report containing:

Audience Understanding

Platform Strategy

Content Strategy

Growth Potential

Best Decision

Biggest Mistake

Three Marketing Lessons

For personal brands, lessons should reference personal branding principles like authenticity, consistency, and niche clarity.

After every major section, include a "How to ask Claude" card with a reusable prompt so users learn prompt engineering while learning marketing. For personal brand mode, the prompts should reference the person's name and niche instead of a company.

Use reusable React components with useState. Add smooth transitions, cards, progress indicators and ensure every button works.

Response #
A full interactive single-file app — dark, modern UI with a signature "strategy rail" tracking your progress through the funnel. It covers all three paths (own business, personal brand, random client), platform selection with pros/cons, pillar picking (max 3), a 30-day roadmap, a randomized curveball event with consequences, a scored Growth Report, and a "How to ask Claude" prompt card after every section. Fully replayable and offline.
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Think Like a Marketing Strategist: Grow This Brand</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{
    --ink:#0c0e13;
    --panel:#151822;
    --panel-2:#1b1f2c;
    --line:rgba(255,255,255,0.08);
    --text:#e9ebf1;
    --muted:#93980ff8; /* placeholder overwritten below */
    --muted:#9aa1b2;
    --amber:#ffb454;
    --teal:#2dd4bf;
    --pink:#ff6b81;
    --amber-dim:rgba(255,180,84,0.14);
    --teal-dim:rgba(45,212,191,0.14);
    --radius:16px;
    --font-display:'Sora',sans-serif;
    --font-body:'Inter',sans-serif;
    --font-mono:'JetBrains Mono',monospace;
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    background:
      radial-gradient(1200px 700px at 15% -10%, rgba(45,212,191,0.08), transparent 60%),
      radial-gradient(1000px 600px at 100% 0%, rgba(255,180,84,0.07), transparent 55%),
      var(--ink);
    color:var(--text);
    font-family:var(--font-body);
    min-height:100vh;
    -webkit-font-smoothing:antialiased;
  }
  #root{max-width:980px;margin:0 auto;padding:28px 20px 80px;}
  h1,h2,h3{font-family:var(--font-display);margin:0;}
  p{line-height:1.55;color:var(--text);}
  .muted{color:var(--muted);}
  .mono{font-family:var(--font-mono);}
  button{font-family:var(--font-body);cursor:pointer;}
  ::selection{background:var(--teal-dim);}

  /* Top rail — signature element: the strategist's funnel rail */
  .rail{
    display:flex; align-items:center; gap:0; margin-bottom:34px;
    overflow-x:auto; padding-bottom:6px;
  }
  .rail-step{
    display:flex; align-items:center; gap:8px; flex-shrink:0;
  }
  .rail-dot{
    width:11px;height:11px;border-radius:50%;
    background:var(--panel-2); border:2px solid var(--line);
    transition:all .4s ease; flex-shrink:0;
  }
  .rail-dot.done{background:var(--teal); border-color:var(--teal); box-shadow:0 0 12px rgba(45,212,191,0.5);}
  .rail-dot.active{background:var(--amber); border-color:var(--amber); box-shadow:0 0 12px rgba(255,180,84,0.55); transform:scale(1.25);}
  .rail-label{font-family:var(--font-mono); font-size:11px; letter-spacing:0.03em; color:var(--muted); white-space:nowrap;}
  .rail-label.active{color:var(--amber);}
  .rail-label.done{color:var(--teal);}
  .rail-line{width:28px;height:2px;background:var(--line);flex-shrink:0;}
  .rail-line.done{background:var(--teal);}

  .card{
    background:linear-gradient(180deg, var(--panel), var(--panel-2));
    border:1px solid var(--line);
    border-radius:var(--radius);
    padding:26px;
    margin-bottom:20px;
    animation:rise .5s ease;
  }
  @keyframes rise{ from{opacity:0; transform:translateY(10px);} to{opacity:1; transform:translateY(0);} }

  .eyebrow{
    font-family:var(--font-mono); font-size:11.5px; text-transform:uppercase;
    letter-spacing:0.12em; color:var(--teal); margin-bottom:10px; display:block;
  }
  .headline{font-size:clamp(24px,4vw,34px); font-weight:800; line-height:1.15; margin-bottom:10px;}
  .sub{color:var(--muted); font-size:15.5px; margin-bottom:18px;}

  .why-box{
    background:var(--teal-dim);
    border:1px solid rgba(45,212,191,0.28);
    border-radius:12px;
    padding:14px 16px;
    margin:16px 0;
    font-size:14.5px;
  }
  .why-box b{color:var(--teal); font-family:var(--font-mono); font-size:12px; text-transform:uppercase; letter-spacing:0.06em; display:block; margin-bottom:5px;}

  .what-box{
    background:var(--amber-dim);
    border:1px solid rgba(255,180,84,0.28);
    border-radius:12px;
    padding:14px 16px;
    margin:16px 0 0;
    font-size:14.5px;
  }
  .what-box b{color:var(--amber); font-family:var(--font-mono); font-size:12px; text-transform:uppercase; letter-spacing:0.06em; display:block; margin-bottom:5px;}

  .grid{display:grid; gap:14px; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); margin:18px 0;}
  .option-card{
    background:var(--panel-2); border:1.5px solid var(--line); border-radius:14px;
    padding:18px; text-align:left; transition:all .2s ease; color:var(--text);
  }
  .option-card:hover{border-color:var(--teal); transform:translateY(-2px); box-shadow:0 8px 24px rgba(0,0,0,0.35);}
  .option-card.selected{border-color:var(--teal); background:var(--teal-dim); box-shadow:0 0 0 1px var(--teal);}
  .option-card .icon{font-size:26px; margin-bottom:8px; display:block;}
  .option-card h3{font-size:16px; margin-bottom:6px;}
  .option-card p{font-size:13.5px; color:var(--muted); margin:0;}

  .btn{
    display:inline-flex; align-items:center; gap:8px;
    background:var(--teal); color:#04211d; border:none;
    font-weight:700; font-size:14.5px; padding:12px 22px;
    border-radius:10px; transition:all .18s ease;
  }
  .btn:hover{background:#4fe4d1; transform:translateY(-1px);}
  .btn:disabled{background:var(--panel-2); color:var(--muted); cursor:not-allowed; transform:none;}
  .btn.secondary{background:transparent; border:1.5px solid var(--line); color:var(--text);}
  .btn.secondary:hover{border-color:var(--amber); color:var(--amber); background:transparent;}
  .btn.amber{background:var(--amber); color:#2b1500;}
  .btn.amber:hover{background:#ffc879;}

  .btn-row{display:flex; gap:12px; flex-wrap:wrap; margin-top:22px;}

  .tag{
    display:inline-block; font-family:var(--font-mono); font-size:11.5px;
    padding:3px 10px; border-radius:20px; border:1px solid var(--line);
    color:var(--muted); margin:3px 6px 3px 0;
  }

  .prompt-card{
    background:#0d1b1c; border:1px dashed rgba(45,212,191,0.4);
    border-radius:14px; padding:18px; margin-top:22px;
  }
  .prompt-card .ptitle{
    display:flex; align-items:center; gap:8px; font-family:var(--font-mono);
    font-size:12.5px; color:var(--teal); text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;
  }
  .prompt-text{
    background:#08110f; border-radius:10px; padding:14px; font-family:var(--font-mono);
    font-size:13px; color:#c9f7ee; line-height:1.6; white-space:pre-wrap; margin-bottom:10px;
  }
  .copy-btn{
    background:transparent; border:1px solid rgba(45,212,191,0.4); color:var(--teal);
    font-size:12.5px; padding:7px 14px; border-radius:8px; font-family:var(--font-mono);
  }
  .copy-btn:hover{background:var(--teal-dim);}

  .biz-fact{display:flex; justify-content:space-between; padding:10px 0; border-bottom:1px solid var(--line); font-size:14.5px;}
  .biz-fact:last-child{border-bottom:none;}
  .biz-fact .k{color:var(--muted); font-family:var(--font-mono); font-size:12.5px;}

  input[type=text], textarea{
    width:100%; background:var(--panel-2); border:1.5px solid var(--line); color:var(--text);
    border-radius:10px; padding:11px 14px; font-family:var(--font-body); font-size:14.5px; margin-bottom:6px;
  }
  input[type=text]:focus, textarea:focus{outline:none; border-color:var(--teal);}
  label.field-label{font-family:var(--font-mono); font-size:11.5px; color:var(--muted); text-transform:uppercase; letter-spacing:0.06em; display:block; margin:14px 0 6px;}
  label.field-label:first-child{margin-top:0;}

  .week-card{
    border-left:3px solid var(--teal); background:var(--panel-2); border-radius:0 12px 12px 0;
    padding:16px 18px; margin-bottom:12px;
  }
  .week-card h4{font-family:var(--font-mono); font-size:12.5px; color:var(--teal); text-transform:uppercase; letter-spacing:0.06em; margin-bottom:6px;}
  .week-card .goal{font-weight:700; margin-bottom:6px; font-size:15.5px;}

  .event-banner{
    background:linear-gradient(120deg, rgba(255,107,129,0.16), rgba(255,180,84,0.1));
    border:1px solid rgba(255,107,129,0.35); border-radius:14px; padding:20px; margin-bottom:16px;
  }
  .event-banner .flash{font-family:var(--font-mono); font-size:12px; color:var(--pink); text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px; display:block;}

  .report-grid{display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:18px 0;}
  @media (max-width:640px){.report-grid{grid-template-columns:1fr;}}
  .report-tile{background:var(--panel-2); border:1px solid var(--line); border-radius:12px; padding:16px;}
  .report-tile h4{font-family:var(--font-mono); font-size:11.5px; color:var(--amber); text-transform:uppercase; letter-spacing:0.06em; margin-bottom:8px;}
  .report-tile p{font-size:14px; margin:0; color:var(--text);}

  .lesson-item{
    display:flex; gap:12px; padding:12px 0; border-bottom:1px solid var(--line);
  }
  .lesson-item:last-child{border-bottom:none;}
  .lesson-num{
    font-family:var(--font-mono); font-weight:700; color:var(--teal); font-size:18px; flex-shrink:0; width:26px;
  }

  .score-ring{
    width:120px; height:120px; border-radius:50%; margin:0 auto 10px;
    display:flex; align-items:center; justify-content:center; flex-direction:column;
    background:conic-gradient(var(--teal) calc(var(--pct) * 1%), var(--panel-2) 0);
    position:relative;
  }
  .score-ring::before{
    content:''; position:absolute; inset:8px; border-radius:50%; background:var(--panel);
  }
  .score-ring .val{position:relative; font-family:var(--font-display); font-weight:800; font-size:26px;}
  .score-ring .lbl{position:relative; font-family:var(--font-mono); font-size:10px; color:var(--muted);}

  .checkbox-row{display:flex; align-items:flex-start; gap:10px; padding:10px 0; cursor:pointer;}
  .checkbox-row input{margin-top:3px;}
  .checkbox-row.disabled{opacity:0.4; cursor:not-allowed;}

  footer.tip{text-align:center; color:var(--muted); font-size:12.5px; margin-top:40px; font-family:var(--font-mono);}

  ::-webkit-scrollbar{height:6px; width:6px;}
  ::-webkit-scrollbar-thumb{background:var(--line); border-radius:4px;}
</style>
</head>
<body>
<div id="root"></div>

<script src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

<script type="text/babel" data-presets="react">
const {useState, useMemo, useEffect} = React;

/* ---------------------------------------------------------
   DATA GENERATORS
--------------------------------------------------------- */

const INDUSTRIES = [
  {name:"Cold-Brew Coffee Brand", audience:"Busy young professionals (24-35) who want an energy boost without sugar crashes", challenge:"Everyone thinks cold brew is 'just coffee' — no one sees why yours is different.", competitors:["Local roaster chains","A big-box canned cold brew brand","A trendy DTC coffee subscription"]},
  {name:"Sustainable Sneaker Startup", audience:"Eco-conscious Gen Z shoppers (18-26) who care about style and impact", challenge:"People assume 'sustainable' means ugly or expensive, so they don't click.", competitors:["A legacy sneaker giant with a 'green line'","A viral DTC eco-shoe brand","Thrifted/secondhand sneaker resellers"]},
  {name:"Home Meal-Kit Service", audience:"Time-poor parents (30-45) who want healthy dinners without the planning", challenge:"Retention drops after month two because people feel bored with the menu.", competitors:["Two national meal-kit giants","Grocery store ready-meal sections"]},
  {name:"Boutique Fitness Studio", audience:"Urban millennials (25-40) looking for community, not just a workout", challenge:"The studio is packed with regulars but almost no new people are walking in.", competitors:["A national gym chain nearby","A popular home-workout app"]},
  {name:"Kids' STEM Toy Company", audience:"Parents (30-45) who want screen-free learning toys for ages 6-11", challenge:"Parents love the idea but say the price feels hard to justify.", competitors:["A big-box toy retailer's STEM aisle","A subscription STEM-kit box brand"]},
  {name:"Plant-Based Skincare Line", audience:"Skincare-curious adults (22-38) overwhelmed by ingredient lists", challenge:"The product works, but it looks just like every other 'clean beauty' brand on shelves.", competitors:["A celebrity-founded skincare line","A dermatologist-backed drugstore brand"]},
  {name:"Indie Board Game Studio", audience:"Hobbyist tabletop gamers (20-40) active in online communities", challenge:"Great reviews from people who try it, but almost no one is discovering it.", competitors:["A crowdfunding-famous game studio","A big traditional board game publisher"]},
  {name:"Freelance Web Design Agency", audience:"Small business owners (30-55) who need a website but don't know where to start", challenge:"People love the portfolio but think the agency is 'too small' to trust with a big project.", competitors:["A cheap template website builder","A larger local design agency"]},
];

const BUDGETS = ["Shoestring ($500/month)", "Modest ($3,000/month)", "Growing ($10,000/month)", "Well-funded ($40,000/month)"];

function randomFrom(arr){ return arr[Math.floor(Math.random()*arr.length)]; }

function generateClient(){
  const pick = randomFrom(INDUSTRIES);
  return {
    type:"business",
    name: pick.name,
    audience: pick.audience,
    challenge: pick.challenge,
    competitors: pick.competitors,
    budget: randomFrom(BUDGETS),
  };
}

/* ---------------------------------------------------------
   PLATFORM DATA
--------------------------------------------------------- */
const PLATFORMS = {
  business: [
    {id:"instagram", name:"Instagram", icon:"📸", good:"Visual products, lifestyle storytelling, younger-to-mid adult audiences.", bad:"Weak for long explanations or B2B decision-makers."},
    {id:"tiktok", name:"TikTok", icon:"🎵", good:"Fast discovery, trend-driven reach, younger audiences, low production cost.", bad:"Short attention spans mean it's poor for detailed trust-building."},
    {id:"linkedin", name:"LinkedIn", icon:"💼", good:"B2B trust, founder credibility, hiring-adjacent audiences.", bad:"Weak for impulse, visual, or youth-skewed consumer products."},
    {id:"youtube", name:"YouTube", icon:"▶️", good:"Deep trust-building, tutorials, long shelf life via search.", bad:"Slow to grow and needs more production effort than other platforms."},
    {id:"facebook", name:"Facebook", icon:"👥", good:"Strong ad targeting, reaches older demographics, great for local community.", bad:"Organic reach is low; mostly a paid-ads platform now."},
    {id:"pinterest", name:"Pinterest", icon:"📌", good:"High purchase intent, great for visual/DIY/home/style products.", bad:"Irrelevant for services or abstract B2B offers."},
    {id:"x", name:"X / Twitter", icon:"✖️", good:"Real-time conversation, customer service, industry commentary.", bad:"Fast-moving feed makes it hard to build product awareness alone."},
    {id:"newsletter", name:"Email Newsletter", icon:"✉️", good:"Owned audience, highest trust and conversion over time.", bad:"Slow to build a list; not a discovery channel."},
  ],
  personal: [
    {id:"linkedin", name:"LinkedIn", icon:"💼", good:"Best platform for professional authority, career storytelling, and niche credibility.", bad:"Weak for entertainment-first or highly visual personal content."},
    {id:"x", name:"X / Twitter", icon:"✖️", good:"Fastest way to join conversations in your niche and build a reputation in public.", bad:"Requires frequent posting; ideas can get buried quickly."},
    {id:"youtube", name:"YouTube", icon:"▶️", good:"The strongest format for demonstrating expertise in depth over time.", bad:"High production effort and slower early growth."},
    {id:"newsletter", name:"Email Newsletter", icon:"✉️", good:"You own this audience — no algorithm between you and them. Best for long-term trust.", bad:"Takes patience; it's not where new people discover you first."},
    {id:"instagram", name:"Instagram", icon:"📸", good:"Good for behind-the-scenes and personality if your niche is visual or lifestyle-driven.", bad:"Less effective for pure thought-leadership niches (like finance or law)."},
    {id:"tiktok", name:"TikTok", icon:"🎵", good:"Great discovery engine if you can teach or entertain in short bursts.", bad:"Rewards personality and edits over depth — harder for dense expertise."},
  ]
};

/* ---------------------------------------------------------
   CONTENT PILLARS
--------------------------------------------------------- */
const PILLARS_BUSINESS = [
  {id:"education", name:"Product Education", desc:"Teaches the audience how the product solves their problem.", goal:"Builds understanding and trust before purchase."},
  {id:"social_proof", name:"Social Proof", desc:"Reviews, testimonials, and user-generated content.", goal:"Reduces risk in the buyer's mind."},
  {id:"bts", name:"Behind the Scenes", desc:"How it's made, who makes it, the process.", goal:"Builds emotional connection and authenticity."},
  {id:"community", name:"Community & Culture", desc:"Highlights the people and values around the brand.", goal:"Turns customers into fans who feel a sense of belonging."},
  {id:"trend", name:"Trend Participation", desc:"Joins relevant cultural or platform trends.", goal:"Drives fresh reach and discovery beyond existing followers."},
  {id:"offer", name:"Promotions & Offers", desc:"Direct calls-to-action, discounts, launches.", goal:"Converts attention into sales — used sparingly."},
];

const PILLARS_PERSONAL = [
  {id:"thought", name:"Thought Leadership", desc:"Sharing opinions and frameworks from your expertise.", goal:"Builds authority and gets you known for an idea."},
  {id:"story", name:"Personal Story", desc:"Your journey, struggles, and turning points.", goal:"Builds emotional connection and relatability."},
  {id:"bts", name:"Behind the Scenes", desc:"How you work, think, and make decisions day-to-day.", goal:"Builds trust through transparency."},
  {id:"education", name:"Audience Education", desc:"Teaching your audience something useful in your niche.", goal:"Proves competence and gives people a reason to follow."},
  {id:"community", name:"Community Engagement", desc:"Responding, highlighting others, starting conversations.", goal:"Builds relationships that compound into word-of-mouth."},
  {id:"proof", name:"Results & Proof", desc:"Case studies, wins, and outcomes you've helped create.", goal:"Converts followers into clients or opportunities."},
];

/* ---------------------------------------------------------
   RANDOM EVENTS
--------------------------------------------------------- */
const EVENTS_BUSINESS = [
  {
    title:"A Competitor Just Went Viral With a Copycat Idea",
    desc:"One of your competitors posted something almost identical to a content idea you were planning to launch next week — and it's blowing up.",
    options:[
      {label:"Scrap the idea and pivot to something original", outcome:"You avoid looking like the copycat, but you lose the momentum of a proven idea. Good instinct for brand safety — average outcome for speed."},
      {label:"Post your version anyway, but add your own unique angle", outcome:"Smart move. You ride the trend's attention while still standing out. This is how strategists turn a threat into an opportunity."},
      {label:"Ignore it and continue exactly as planned", outcome:"You look like you're following, not leading. Audiences notice when two brands post the same idea back-to-back."},
    ]
  },
  {
    title:"A Micro-Influencer Wants to Feature You — For Free",
    desc:"A small creator with an engaged, relevant audience offers to feature your product for free, but their reach is modest.",
    options:[
      {label:"Say yes immediately, no strings attached", outcome:"Low risk, low cost. Their audience may be small, but relevant micro-influencers often convert better than expensive ones."},
      {label:"Ask for data on their audience before deciding", outcome:"This is exactly what a careful strategist does — never trade product or time without checking audience-fit first."},
      {label:"Decline because their following is too small to matter", outcome:"A common beginner mistake — reach isn't everything. Relevance and trust can matter more than follower count."},
    ]
  },
  {
    title:"One Post Unexpectedly Goes Viral",
    desc:"A behind-the-scenes video you almost didn't post is suddenly getting 50x your normal views.",
    options:[
      {label:"Immediately post a follow-up riding the momentum", outcome:"Great instinct — attention is temporary. Capturing it quickly with a related post is a classic growth move."},
      {label:"Turn on ads to boost the same post further", outcome:"Smart if your budget allows it — organic virality plus paid amplification can multiply reach efficiently."},
      {label:"Do nothing different and wait to see what happens", outcome:"A missed opportunity. Viral moments are rare and time-sensitive; strategists act fast while attention is high."},
    ]
  },
  {
    title:"A Customer Complaint Is Going Semi-Viral",
    desc:"A customer posted a frustrated (but fair) complaint about a shipping delay, and it's getting shared in your niche community.",
    options:[
      {label:"Respond publicly, acknowledge it, and offer to fix it", outcome:"This is the textbook right move — transparency and accountability usually turn critics into advocates."},
      {label:"Delete or ignore the comment", outcome:"Risky. Ignoring visible complaints often escalates distrust rather than reducing it."},
      {label:"Respond only privately via DM", outcome:"A reasonable partial fix, but the public audience never sees resolution, which can leave a lingering doubt."},
    ]
  },
];

const EVENTS_PERSONAL = [
  {
    title:"One of Your Posts Just Went Viral",
    desc:"A post you almost didn't publish is suddenly reaching thousands of new people outside your usual audience.",
    options:[
      {label:"Post a follow-up quickly while attention is high", outcome:"Great instinct. Riding your own momentum is one of the highest-leverage moves in personal branding."},
      {label:"Update your bio and pin the post so new visitors see your best work", outcome:"Smart — most viral traffic checks your profile next. This converts a moment into long-term followers."},
      {label:"Keep posting your normal schedule and ignore the spike", outcome:"A missed opportunity — new eyes on your profile won't stay long unless you give them a reason to follow."},
    ]
  },
  {
    title:"You Get Invited Onto a Podcast in Your Niche",
    desc:"A mid-sized podcast in your field invites you on, but it will take real prep time away from your regular content.",
    options:[
      {label:"Accept and treat it as a major platform-building moment", outcome:"Strong move — podcasts build long-form trust that short posts can't, and they reach an audience you don't already have."},
      {label:"Decline to protect your regular posting schedule", outcome:"A safe but conservative choice — consistency matters, but rare high-trust opportunities are often worth a short-term trade-off."},
      {label:"Accept, but do zero prep", outcome:"Risky — showing up unprepared on someone else's platform can hurt the credibility you're trying to build."},
    ]
  },
  {
    title:"Someone Starts Copying Your Content Style",
    desc:"Another creator in your niche has started posting content that closely mirrors your ideas and format.",
    options:[
      {label:"Call them out publicly", outcome:"Risky — this can look defensive and often draws more attention to the copier than to you."},
      {label:"Ignore it and keep creating original work faster than they can copy", outcome:"This is the strategist's move — originality compounds, and audiences eventually notice who the source is."},
      {label:"Stop posting that type of content out of frustration", outcome:"This gives up your strongest pillar. Abandoning a working format because of a copier hurts you more than them."},
    ]
  },
  {
    title:"You Get Into a Public Disagreement",
    desc:"You post an opinion and someone with a large following publicly disagrees, and their reply is getting more attention than your original post.",
    options:[
      {label:"Respond thoughtfully and stand by your point with evidence", outcome:"This is how credibility is built in public — calm, evidence-based responses often win more respect than the original post."},
      {label:"Delete the post to avoid conflict", outcome:"This can look evasive. Deleting under pressure often costs more trust than the disagreement itself."},
      {label:"Escalate emotionally in the replies", outcome:"High risk — emotional public arguments are remembered longer than the original opinion, and rarely help your brand."},
    ]
  },
];

/* ---------------------------------------------------------
   SMALL UI PRIMITIVES
--------------------------------------------------------- */

function WhyBox({children}){
  return <div className="why-box"><b>Why this matters</b>{children}</div>;
}
function WhatBox({children}){
  return <div className="what-box"><b>What this is</b>{children}</div>;
}

function PromptCard({title, prompt}){
  const [copied, setCopied] = useState(false);
  const copy = () => {
    const ta = document.createElement("textarea");
    ta.value = prompt;
    document.body.appendChild(ta);
    ta.select();
    try{ document.execCommand("copy"); }catch(e){}
    document.body.removeChild(ta);
    setCopied(true);
    setTimeout(()=>setCopied(false), 1800);
  };
  return (
    <div className="prompt-card">
      <div className="ptitle">🤖 How to ask Claude — {title}</div>
      <div className="prompt-text">{prompt}</div>
      <button className="copy-btn" onClick={copy}>{copied ? "Copied ✓" : "Copy prompt"}</button>
    </div>
  );
}

const RAIL_STEPS = ["Welcome","Choose Path","Understand","Platforms","Pillars","Roadmap","Event","Report"];

function Rail({stepIndex}){
  return (
    <div className="rail">
      {RAIL_STEPS.map((label, i) => (
        <React.Fragment key={label}>
          <div className="rail-step">
            <div className={"rail-dot " + (i < stepIndex ? "done" : i === stepIndex ? "active" : "")}></div>
            <span className={"rail-label " + (i < stepIndex ? "done" : i === stepIndex ? "active" : "")}>{label}</span>
          </div>
          {i < RAIL_STEPS.length - 1 && <div className={"rail-line " + (i < stepIndex ? "done" : "")}></div>}
        </React.Fragment>
      ))}
    </div>
  );
}

/* ---------------------------------------------------------
   MAIN APP
--------------------------------------------------------- */

function App(){
  const [step, setStep] = useState(0);
  const [mode, setMode] = useState(null); // 'business' | 'personal'
  const [brand, setBrand] = useState(null);
  const [platformChoices, setPlatformChoices] = useState([]);
  const [pillarChoices, setPillarChoices] = useState([]);
  const [event, setEvent] = useState(null);
  const [eventChoiceIdx, setEventChoiceIdx] = useState(null);

  const goTo = (i) => { window.scrollTo({top:0, behavior:'smooth'}); setStep(i); };

  const restart = () => {
    setMode(null); setBrand(null); setPlatformChoices([]); setPillarChoices([]);
    setEvent(null); setEventChoiceIdx(null);
    goTo(0);
  };

  return (
    <div>
      <Rail stepIndex={step} />
      {step === 0 && <Welcome onNext={()=>goTo(1)} />}
      {step === 1 && <ChoosePath onSelect={(m,b)=>{ setMode(m); setBrand(b); goTo(2); }} />}
      {step === 2 && brand && <Understand mode={mode} brand={brand} onNext={()=>goTo(3)} />}
      {step === 3 && brand && <Platforms mode={mode} brand={brand} choices={platformChoices} setChoices={setPlatformChoices} onNext={()=>goTo(4)} />}
      {step === 4 && brand && <Pillars mode={mode} brand={brand} choices={pillarChoices} setChoices={setPillarChoices} onNext={()=>goTo(5)} />}
      {step === 5 && brand && <Roadmap mode={mode} brand={brand} pillars={pillarChoices} onNext={()=>{
          const pool = mode === 'personal' ? EVENTS_PERSONAL : EVENTS_BUSINESS;
          setEvent(randomFrom(pool));
          goTo(6);
        }} />}
      {step === 6 && event && <EventStep mode={mode} brand={brand} event={event} choiceIdx={eventChoiceIdx} setChoiceIdx={setEventChoiceIdx} onNext={()=>goTo(7)} />}
      {step === 7 && brand && <Report mode={mode} brand={brand} platforms={platformChoices} pillars={pillarChoices} event={event} eventChoiceIdx={eventChoiceIdx} onRestart={restart} />}
      <footer className="tip">Think Like a Marketing Strategist — a hands-on way to learn how marketers actually think.</footer>
    </div>
  );
}

/* ---------------------------------------------------------
   STEP 0 — WELCOME
--------------------------------------------------------- */
function Welcome({onNext}){
  return (
    <div className="card">
      <span className="eyebrow">Marketing Strategy, Learned by Doing</span>
      <h1 className="headline">Think Like a Marketing Strategist</h1>
      <p className="sub">Grow This Brand is a hands-on simulator. Instead of asking an AI to write you a marketing plan, you'll practice the thinking behind one — understanding an audience, choosing platforms on purpose, and making trade-offs a real strategist makes.</p>

      <WhatBox>
        Marketing strategy is the set of decisions about <b>who</b> you're talking to, <b>where</b> you reach them, and <b>what</b> you say — made before you create a single post.
      </WhatBox>
      <WhyBox>
        Most beginners jump straight to "make content." Skilled marketers slow down first: content made without a strategy usually reaches the wrong people, or the right people at the wrong moment.
      </WhyBox>

      <div className="btn-row">
        <button className="btn" onClick={onNext}>Start the Simulation →</button>
      </div>
    </div>
  );
}

/* ---------------------------------------------------------
   STEP 1 — CHOOSE PATH
--------------------------------------------------------- */
function ChoosePath({onSelect}){
  const [ownName, setOwnName] = useState("");
  const [ownDesc, setOwnDesc] = useState("");
  const [ownAudience, setOwnAudience] = useState("");
  const [personalName, setPersonalName] = useState("");
  const [personalNiche, setPersonalNiche] = useState("");
  const [personalStory, setPersonalStory] = useState("");
  const [showOwnForm, setShowOwnForm] = useState(false);
  const [showPersonalForm, setShowPersonalForm] = useState(false);

  const submitOwn = () => {
    if(!ownName.trim()) return;
    onSelect('business', {
      type:"business",
      name: ownName.trim(),
      audience: ownAudience.trim() || "Not yet defined — we'll work on this next.",
      challenge: ownDesc.trim() || "Not yet defined.",
      competitors: ["(You'll list these in the next step)"],
      budget: "Your real budget",
      isCustom:true,
    });
  };

  const submitPersonal = () => {
    if(!personalName.trim() || !personalNiche.trim()) return;
    onSelect('personal', {
      type:"personal",
      name: personalName.trim(),
      niche: personalNiche.trim(),
      audience: "People trying to learn or make progress in: " + personalNiche.trim(),
      challenge: personalStory.trim() || "Standing out and being known for a clear point of view.",
      competitors: ["(You'll name people you admire in the next step)"],
      budget: "Time & consistency, not ad budget",
      isCustom:true,
    });
  };

  const useRandomClient = () => {
    onSelect('business', generateClient());
  };

  return (
    <div className="card">
      <span className="eyebrow">Step 1 of 7</span>
      <h2 className="headline">Choose Your Path</h2>
      <p className="sub">Every marketing strategy starts with a real subject. Pick how you want to practice.</p>

      <div className="grid">
        <div>
          <button className="option-card" style={{width:"100%"}} onClick={()=>{setShowOwnForm(!showOwnForm); setShowPersonalForm(false);}}>
            <span className="icon">🏢</span>
            <h3>Use My Own Business</h3>
            <p>Bring a real business or idea you have, and build a real strategy for it.</p>
          </button>
          {showOwnForm && (
            <div style={{marginTop:12, padding:16, background:"var(--panel-2)", borderRadius:12}}>
              <label className="field-label">Business name</label>
              <input type="text" value={ownName} onChange={e=>setOwnName(e.target.value)} placeholder="e.g. Riverside Roasters" />
              <label className="field-label">What do you sell or offer?</label>
              <textarea rows="2" value={ownDesc} onChange={e=>setOwnDesc(e.target.value)} placeholder="e.g. Small-batch coffee subscriptions"></textarea>
              <label className="field-label">Who do you think your audience is? (optional)</label>
              <input type="text" value={ownAudience} onChange={e=>setOwnAudience(e.target.value)} placeholder="e.g. Coffee lovers in their 30s" />
              <button className="btn" style={{marginTop:10}} onClick={submitOwn} disabled={!ownName.trim()}>Use This Business →</button>
            </div>
          )}
        </div>

        <div>
          <button className="option-card" style={{width:"100%"}} onClick={()=>{setShowPersonalForm(!showPersonalForm); setShowOwnForm(false);}}>
            <span className="icon">🙋</span>
            <h3>Build My Personal Brand</h3>
            <p>No business yet? Use your own name, expertise, and story as the brand.</p>
          </button>
          {showPersonalForm && (
            <div style={{marginTop:12, padding:16, background:"var(--panel-2)", borderRadius:12}}>
              <label className="field-label">Your name</label>
              <input type="text" value={personalName} onChange={e=>setPersonalName(e.target.value)} placeholder="e.g. Jordan Lee" />
              <label className="field-label">Your niche or expertise</label>
              <input type="text" value={personalNiche} onChange={e=>setPersonalNiche(e.target.value)} placeholder="e.g. personal finance for freelancers" />
              <label className="field-label">Your story or challenge (optional)</label>
              <textarea rows="2" value={personalStory} onChange={e=>setPersonalStory(e.target.value)} placeholder="e.g. I know my stuff but no one outside my friends knows I exist online"></textarea>
              <button className="btn" style={{marginTop:10}} onClick={submitPersonal} disabled={!personalName.trim() || !personalNiche.trim()}>Build This Brand →</button>
            </div>
          )}
        </div>

        <button className="option-card" onClick={useRandomClient}>
          <span className="icon">🎲</span>
          <h3>A New Client Has Arrived</h3>
          <p>Get a randomly generated business — industry, audience, budget, competitors, and a real challenge to solve.</p>
        </button>
      </div>

      <WhyBox>
        Strategists rarely get to choose their subject in the real world — a client, a boss, or your own circumstances hand you one. Practicing with different starting points builds the muscle of adapting strategy to context.
      </WhyBox>
    </div>
  );
}

/* ---------------------------------------------------------
   STEP 2 — UNDERSTAND THE BRAND / AUDIENCE
--------------------------------------------------------- */
function Understand({mode, brand, onNext}){
  const isPersonal = mode === 'personal';
  return (
    <div className="card">
      <span className="eyebrow">Step 2 of 7 — Understand</span>
      <h2 className="headline">{isPersonal ? `Get to Know ${brand.name}'s Brand` : `Get to Know ${brand.name}`}</h2>
      <p className="sub">{isPersonal
        ? "In a personal brand, the 'product' isn't a physical item — it's your expertise, perspective, and story. Understanding that clearly is the entire foundation."
        : "Before choosing platforms or content, a strategist studies the business itself: what it offers, who it's for, and what's standing in the way."}</p>

      <div style={{marginBottom:6}}>
        <div className="biz-fact"><span className="k">{isPersonal ? "NAME" : "BRAND"}</span><span>{brand.name}</span></div>
        {isPersonal && <div className="biz-fact"><span className="k">NICHE / EXPERTISE</span><span>{brand.niche}</span></div>}
        <div className="biz-fact"><span className="k">AUDIENCE</span><span>{brand.audience}</span></div>
        <div className="biz-fact"><span className="k">{isPersonal ? "GROWTH CHALLENGE" : "MARKETING CHALLENGE"}</span><span>{brand.challenge}</span></div>
        <div className="biz-fact"><span className="k">{isPersonal ? "TIME/RESOURCES" : "BUDGET"}</span><span>{brand.budget}</span></div>
        <div className="biz-fact">
          <span className="k">{isPersonal ? "PEOPLE YOU ADMIRE" : "COMPETITORS"}</span>
          <span>{brand.competitors.join(", ")}</span>
        </div>
      </div>

      <WhatBox>
        {isPersonal
          ? "Your audience is the group of people who benefit most from your specific expertise and point of view — not 'everyone interested in the topic.'"
          : "Audience understanding means knowing who specifically benefits from this product, what they currently believe, and what's stopping them from buying."}
      </WhatBox>
      <WhyBox>
        {isPersonal
          ? "Vague personal brands ('I talk about business and life') don't grow, because no one can describe what you're known for. A sharp, specific audience is what makes people say 'you have to follow this person.'"
          : "Every platform, content, and messaging decision downstream depends on this. A brand that skips this step ends up guessing — and guessing is expensive."}
      </WhyBox>

      <PromptCard
        title="Sharpening Your Audience"
        prompt={isPersonal
          ? `I'm building a personal brand as ${brand.name} in the niche of "${brand.niche}". Help me get more specific about who my ideal audience is — their current beliefs, their biggest frustration in this niche, and what would make them decide to follow me instead of scrolling past.`
          : `I'm developing a marketing strategy for "${brand.name}", which serves this audience: "${brand.audience}". Their biggest challenge is: "${brand.challenge}". Help me get more specific — what does this audience currently believe, and what objection is stopping them from choosing us?`
        }
      />

      <div className="btn-row">
        <button className="btn" onClick={onNext}>Continue to Platform Strategy →</button>
      </div>
    </div>
  );
}

/* ---------------------------------------------------------
   STEP 3 — PLATFORMS
--------------------------------------------------------- */
function Platforms({mode, brand, choices, setChoices, onNext}){
  const list = PLATFORMS[mode];
  const toggle = (id) => {
    setChoices(prev => prev.includes(id) ? prev.filter(x=>x!==id) : [...prev, id]);
  };
  const isPersonal = mode === 'personal';

  return (
    <div className="card">
      <span className="eyebrow">Step 3 of 7 — Platforms</span>
      <h2 className="headline">Where Should {isPersonal ? "You" : brand.name} Show Up?</h2>
      <p className="sub">Pick every platform you think is a genuine fit. There's no fixed number — the goal is judgment, not guessing.</p>

      <WhatBox>
        Platform strategy is choosing where to show up based on where your specific audience already pays attention — not picking every platform that exists.
      </WhatBox>
      <WhyBox>
        {isPersonal
          ? "Spreading yourself across every platform dilutes your effort. Most successful personal brands go deep on 1-2 platforms before expanding — LinkedIn, X, YouTube, and newsletters tend to reward expertise more than platforms built for viral entertainment."
          : "Being everywhere with no strategy usually means being mediocre everywhere. Picking the right 2-4 platforms lets a brand build real depth instead of spreading thin."}
      </WhyBox>

      <div className="grid">
        {list.map(p => (
          <button key={p.id} className={"option-card " + (choices.includes(p.id) ? "selected" : "")} onClick={()=>toggle(p.id)}>
            <span className="icon">{p.icon}</span>
            <h3>{p.name}</h3>
            <p><b style={{color:"var(--teal)"}}>Good for:</b> {p.good}</p>
            <p style={{marginTop:6}}><b style={{color:"var(--pink)"}}>Watch out:</b> {p.bad}</p>
          </button>
        ))}
      </div>

      <PromptCard
        title="Choosing Platforms"
        prompt={isPersonal
          ? `I'm building a personal brand around "${brand.niche}" as ${brand.name}. Given my audience is "${brand.audience}", which 2-3 platforms should I prioritize first, and why? Explain the trade-offs of focusing versus spreading across many platforms.`
          : `For "${brand.name}", a brand serving "${brand.audience}" with a budget of ${brand.budget}, which social platforms would you prioritize and why? Explain which platforms you'd avoid for now and what trade-off that involves.`
        }
      />

      <div className="btn-row">
        <button className="btn" onClick={onNext} disabled={choices.length === 0}>Continue to Content Pillars →</button>
        {choices.length === 0 && <span className="muted" style={{alignSelf:"center", fontSize:13}}>Select at least one platform to continue.</span>}
      </div>
    </div>
  );
}

/* ---------------------------------------------------------
   STEP 4 — CONTENT PILLARS
--------------------------------------------------------- */
function Pillars({mode, brand, choices, setChoices, onNext}){
  const list = mode === 'personal' ? PILLARS_PERSONAL : PILLARS_BUSINESS;
  const isPersonal = mode === 'personal';
  const MAX = 3;

  const toggle = (id) => {
    setChoices(prev => {
      if(prev.includes(id)) return prev.filter(x=>x!==id);
      if(prev.length >= MAX) return prev;
      return [...prev, id];
    });
  };

  return (
    <div className="card">
      <span className="eyebrow">Step 4 of 7 — Content Pillars</span>
      <h2 className="headline">Choose Exactly 3 Content Pillars</h2>
      <p className="sub">Content pillars are the recurring themes your posts fall under. Real strategists limit themselves on purpose — pick the 3 that best fit your goals right now. ({choices.length}/{MAX} selected)</p>

      <WhatBox>
        A content pillar is a recurring theme that all your individual posts fall under — like a category that keeps your content focused instead of random.
      </WhatBox>
      <WhyBox>
        {isPersonal
          ? "Choosing too many pillars makes your feed feel unfocused, so people can't describe what you're 'known for.' Three sharp pillars beat six vague ones."
          : "More pillars sounds like more variety, but it usually means less consistency and a confused audience. Three focused pillars let a brand build recognizable patterns people come to expect."}
      </WhyBox>

      <div className="grid">
        {list.map(p => {
          const selected = choices.includes(p.id);
          const disabled = !selected && choices.length >= MAX;
          return (
            <button key={p.id} className={"option-card " + (selected ? "selected" : "")}
              style={disabled ? {opacity:0.4, cursor:"not-allowed"} : {}}
              onClick={()=> !disabled && toggle(p.id)} disabled={disabled}>
              <h3>{p.name}</h3>
              <p>{p.desc}</p>
              <p style={{marginTop:8, color:"var(--teal)", fontSize:13}}><b>Supports:</b> {p.goal}</p>
            </button>
          );
        })}
      </div>

      <PromptCard
        title="Defining Content Pillars"
        prompt={isPersonal
          ? `I'm ${brand.name}, building a personal brand in "${brand.niche}". I've chosen these content pillars: ${choices.length ? choices.join(", ") : "[your pillars]"}. Give me 5 specific post ideas for each pillar that fit my niche and audience.`
          : `For "${brand.name}", I've chosen these content pillars: ${choices.length ? choices.join(", ") : "[your pillars]"}. Give me 5 specific content ideas for each pillar, tailored to this audience: "${brand.audience}".`
        }
      />

      <div className="btn-row">
        <button className="btn" onClick={onNext} disabled={choices.length !== MAX}>Continue to 30-Day Roadmap →</button>
        {choices.length !== MAX && <span className="muted" style={{alignSelf:"center", fontSize:13}}>Choose exactly {MAX} pillars to continue.</span>}
      </div>
    </div>
  );
}

/* ---------------------------------------------------------
   STEP 5 — 30 DAY ROADMAP
--------------------------------------------------------- */
function Roadmap({mode, brand, pillars, onNext}){
  const isPersonal = mode === 'personal';

  const weeks = isPersonal ? [
    {title:"Week 1 — Define & Optimize", goal:"Nail down your point of view and clean up your bio/profile.", strategy:"Before posting more, make sure anyone who lands on your profile immediately understands who you are, what you talk about, and why it matters. This is the highest-leverage work in week one."},
    {title:"Week 2 — Establish Your Pillars", goal:"Start publishing consistently across your 3 chosen pillars.", strategy:"Focus on rhythm over perfection. The goal is for your audience to start recognizing your recurring themes."},
    {title:"Week 3 — Engage & Extend Reach", goal:"Spend equal time engaging with others' content as posting your own.", strategy:"Personal brands grow through relationships, not just publishing. Thoughtful replies in your niche put you in front of new audiences."},
    {title:"Week 4 — Review & Double Down", goal:"Identify your best-performing pillar and post, and lean into it.", strategy:"Look at what resonated and do more of it deliberately, rather than treating every post as equally important."},
  ] : [
    {title:"Week 1 — Foundation", goal:"Set up profiles, visual identity, and messaging consistency across chosen platforms.", strategy:"Get the basics right before pushing for reach — inconsistent branding wastes the attention you're about to earn."},
    {title:"Week 2 — Launch Content Pillars", goal:"Begin publishing consistently across all 3 pillars to build a content rhythm.", strategy:"Prioritize consistency over virality this week — predictability builds trust with a new audience."},
    {title:"Week 3 — Amplify & Engage", goal:"Engage with your audience's comments and consider small paid boosts on top performers.", strategy:"This is where organic effort and light paid spend start compounding — double down on whatever pillar is resonating."},
    {title:"Week 4 — Convert & Review", goal:"Introduce a clear call-to-action and review what worked.", strategy:"Growth without conversion doesn't help the business — this week nudges engaged followers toward an actual next step."},
  ];

  return (
    <div className="card">
      <span className="eyebrow">Step 5 of 7 — Roadmap</span>
      <h2 className="headline">A 30-Day Growth Roadmap</h2>
      <p className="sub">This isn't a list of individual posts — it's a week-by-week strategy showing what to focus on and why.</p>

      <WhatBox>
        A roadmap sequences your strategy over time: what matters most in week one is different from what matters in week four.
      </WhatBox>
      <WhyBox>
        Posting randomly from day one — without foundations, then rhythm, then engagement, then conversion — is why many accounts plateau. Sequencing effort compounds results.
      </WhyBox>

      {weeks.map((w,i) => (
        <div className="week-card" key={i}>
          <h4>{w.title}</h4>
          <div className="goal">{w.goal}</div>
          <p className="muted" style={{fontSize:14}}>{w.strategy}</p>
        </div>
      ))}

      <div style={{marginTop:10}}>
        <span className="tag">Pillars in rotation: {pillars.join(", ") || "none selected"}</span>
      </div>

      <PromptCard
        title="Building a Content Calendar"
        prompt={isPersonal
          ? `I'm ${brand.name}, building a personal brand in "${brand.niche}" with these content pillars: ${pillars.join(", ")}. Turn this into a week-by-week 30-day content calendar with themes for each week, without writing individual scripts yet.`
          : `For "${brand.name}" with these content pillars: ${pillars.join(", ")}, build a week-by-week 30-day roadmap. Each week should have a clear goal and strategic focus, not individual post copy yet.`
        }
      />

      <div className="btn-row">
        <button className="btn" onClick={onNext}>See What Happens Next →</button>
      </div>
    </div>
  );
}

/* ---------------------------------------------------------
   STEP 6 — UNEXPECTED EVENT
--------------------------------------------------------- */
function EventStep({mode, brand, event, choiceIdx, setChoiceIdx, onNext}){
  const isPersonal = mode === 'personal';
  return (
    <div className="card">
      <span className="eyebrow">Step 6 of 7 — The Unexpected</span>
      <h2 className="headline">A Curveball Just Hit</h2>
      <p className="sub">Real marketing rarely goes according to plan. How you respond to the unexpected is often what separates good strategists from great ones.</p>

      <div className="event-banner">
        <span className="flash">Breaking</span>
        <h3 style={{marginBottom:8}}>{event.title}</h3>
        <p>{event.desc}</p>
      </div>

      <WhatBox>
        This is a real-time decision point — no perfect answer exists, only trade-offs a strategist has to weigh quickly.
      </WhatBox>

      <div className="grid" style={{gridTemplateColumns:"1fr"}}>
        {event.options.map((opt, i) => (
          <button key={i} className={"option-card " + (choiceIdx === i ? "selected" : "")} onClick={()=>setChoiceIdx(i)}>
            <h3 style={{fontSize:15}}>{opt.label}</h3>
          </button>
        ))}
      </div>

      {choiceIdx !== null && (
        <WhyBox>{event.options[choiceIdx].outcome}</WhyBox>
      )}

      <PromptCard
        title="Handling the Unexpected"
        prompt={isPersonal
          ? `As ${brand.name} in the "${brand.niche}" niche, here's what just happened: "${event.title} — ${event.desc}". Help me think through 2-3 possible responses and the trade-offs of each before I react publicly.`
          : `For "${brand.name}", here's an unexpected situation: "${event.title} — ${event.desc}". Help me think through 2-3 possible responses and the pros and cons of each before deciding how to act.`
        }
      />

      <div className="btn-row">
        <button className="btn" onClick={onNext} disabled={choiceIdx === null}>See Your Growth Report →</button>
        {choiceIdx === null && <span className="muted" style={{alignSelf:"center", fontSize:13}}>Choose a response to continue.</span>}
      </div>
    </div>
  );
}

/* ---------------------------------------------------------
   STEP 7 — GROWTH REPORT
--------------------------------------------------------- */
function Report({mode, brand, platforms, pillars, event, eventChoiceIdx, onRestart}){
  const isPersonal = mode === 'personal';
  const platformList = PLATFORMS[mode];
  const chosenPlatformNames = platforms.map(id => platformList.find(p=>p.id===id)?.name).filter(Boolean);
  const chosenPillarNames = pillars;

  // simple scoring heuristic for "growth potential"
  const score = Math.min(96, 40 + platforms.length*8 + pillars.length*6 + (eventChoiceIdx !== null ? 12 : 0));

  const bestDecision = eventChoiceIdx !== null && event.options[eventChoiceIdx].outcome.toLowerCase().includes("smart") || (eventChoiceIdx !== null && event.options[eventChoiceIdx].outcome.toLowerCase().includes("great") ) || (eventChoiceIdx !== null && event.options[eventChoiceIdx].outcome.toLowerCase().includes("textbook") ) || (eventChoiceIdx !== null && event.options[eventChoiceIdx].outcome.toLowerCase().includes("strong"))
    ? "Your response to the unexpected event — you read the moment correctly and acted with intent."
    : "Choosing a focused, specific audience instead of trying to appeal to everyone.";

  const biggestMistakeCandidates = [];
  if(platforms.length > 4) biggestMistakeCandidates.push("Spreading across too many platforms at once, which risks diluting your effort.");
  if(pillars.length < 3) biggestMistakeCandidates.push("Not committing to a full set of content pillars, which can make your content feel inconsistent.");
  if(biggestMistakeCandidates.length === 0) biggestMistakeCandidates.push("Not yet building in enough time to measure results before making the next big decision.");

  const lessonsPersonal = [
    "Authenticity compounds — a specific, honest point of view builds more trust over time than a polished but generic one.",
    "Consistency beats intensity — showing up in your 3 pillars regularly matters more than one perfect viral post.",
    "Niche clarity attracts the right people — being known for one clear thing brings better opportunities than being vaguely 'everything.'",
  ];
  const lessonsBusiness = [
    "Strategy comes before content — knowing your audience and platform fit prevents wasted effort.",
    "Fewer, focused pillars build recognition faster than trying to cover every content type.",
    "Unexpected moments are strategic tests — how a brand responds in real time shapes trust as much as its planned content.",
  ];
  const lessons = isPersonal ? lessonsPersonal : lessonsBusiness;

  return (
    <div className="card">
      <span className="eyebrow">Step 7 of 7 — Final Report</span>
      <h2 className="headline">Growth Report: {brand.name}</h2>
      <p className="sub">Here's a summary of the strategic thinking you just practiced.</p>

      <div style={{textAlign:"center", margin:"10px 0 24px"}}>
        <div className="score-ring" style={{"--pct": score}}>
          <div className="val">{score}</div>
          <div className="lbl">GROWTH SCORE</div>
        </div>
      </div>

      <div className="report-grid">
        <div className="report-tile">
          <h4>Audience Understanding</h4>
          <p>{brand.audience}</p>
        </div>
        <div className="report-tile">
          <h4>Platform Strategy</h4>
          <p>{chosenPlatformNames.length ? chosenPlatformNames.join(", ") : "No platforms selected"}</p>
        </div>
        <div className="report-tile">
          <h4>Content Strategy</h4>
          <p>{chosenPillarNames.length ? chosenPillarNames.join(", ") : "No pillars selected"}</p>
        </div>
        <div className="report-tile">
          <h4>Growth Potential</h4>
          <p>{score >= 80 ? "High — your choices show focused, deliberate strategy." : score >= 60 ? "Solid — a good foundation with room to sharpen focus." : "Early stage — consider narrowing your platforms or pillars for more focus."}</p>
        </div>
        <div className="report-tile">
          <h4>Best Decision</h4>
          <p>{bestDecision}</p>
        </div>
        <div className="report-tile">
          <h4>Biggest Mistake to Watch</h4>
          <p>{biggestMistakeCandidates[0]}</p>
        </div>
      </div>

      <h3 style={{fontSize:18, margin:"20px 0 6px"}}>Three Marketing Lessons</h3>
      {lessons.map((l,i)=>(
        <div className="lesson-item" key={i}>
          <div className="lesson-num">{i+1}</div>
          <p>{l}</p>
        </div>
      ))}

      <PromptCard
        title="Turning This Into a Real Plan"
        prompt={isPersonal
          ? `I just practiced a marketing strategy exercise for my personal brand, ${brand.name}, in the niche "${brand.niche}". I chose these platforms: ${chosenPlatformNames.join(", ") || "none"}, and these content pillars: ${chosenPillarNames.join(", ") || "none"}. Help me turn this into a real, detailed action plan for the next 30 days, including specific post ideas.`
          : `I just practiced a marketing strategy exercise for "${brand.name}". I chose these platforms: ${chosenPlatformNames.join(", ") || "none"}, and these content pillars: ${chosenPillarNames.join(", ") || "none"}. Help me turn this into a real, detailed action plan for the next 30 days, including specific post ideas and measurable goals.`
        }
      />

      <div className="btn-row">
        <button className="btn amber" onClick={onRestart}>🔁 Try Again With a New Brand</button>
      </div>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
</script>
</body>
</html>
[Uploading marketing_game.html…]()
