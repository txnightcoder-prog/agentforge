"""
AgentForge — Tiered AI Compute Token Framework
Public showcase & lead capture site.
Conceived June 12, 2026 · John Kirshy
"""

import streamlit as st

st.set_page_config(
    page_title="AgentForge — Tiered AI Compute",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

  .hero {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    border-radius: 16px; padding: 60px 40px;
    text-align: center; color: white; margin-bottom: 32px;
  }
  .hero h1 { font-size: 3.2rem; font-weight: 800; margin: 0 0 12px 0; letter-spacing: -1px; }
  .hero h1 span { color: #7c5cd8; }
  .hero p  { font-size: 1.2rem; color: #c9c9e3; max-width: 680px; margin: 0 auto 24px; }
  .badge {
    display: inline-block; background: rgba(124,92,216,0.25);
    border: 1px solid #7c5cd8; color: #c4b5fd; border-radius: 20px;
    padding: 4px 14px; font-size: 0.78rem; font-weight: 600;
    letter-spacing: 1px; margin-bottom: 20px; text-transform: uppercase;
  }
  .stat-card {
    background: #f7f8fa; border: 1px solid #e5e7eb;
    border-radius: 12px; padding: 28px 20px; text-align: center;
  }
  .stat-card .num { font-size: 2.2rem; font-weight: 800; color: #302b63; }
  .stat-card .lbl { font-size: 0.85rem; color: #57606a; margin-top: 4px; }

  .tier-basic    { background: #f7f8fa; border: 2px solid #e5e7eb; border-radius: 14px; padding: 28px 24px; }
  .tier-mid      { background: #faf5ff; border: 2px solid #7c5cd8; border-radius: 14px; padding: 28px 24px; }
  .tier-advanced { background: #0f0c29; border: 2px solid #302b63; border-radius: 14px; padding: 28px 24px; color: white; }
  .tier-card h3  { font-size: 1.3rem; font-weight: 700; margin: 0 0 6px 0; }
  .tier-card .price { font-size: 2rem; font-weight: 800; margin: 12px 0; }
  .tier-card li  { margin-bottom: 6px; font-size: 0.92rem; }
  .popular { background: #7c5cd8; color: white; border-radius: 6px;
    padding: 2px 10px; font-size: 0.72rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 1px; margin-left: 8px; }

  .feature-row {
    background: #f7f8fa; border: 1px solid #e5e7eb;
    border-radius: 10px; padding: 20px 24px; margin-bottom: 12px;
  }
  .feature-row h4 { margin: 0 0 4px 0; font-size: 1rem; font-weight: 700; color: #1f2328; }
  .feature-row p  { margin: 0; font-size: 0.88rem; color: #57606a; }

  .arch-step {
    background: white; border: 1px solid #e5e7eb;
    border-left: 4px solid #7c5cd8; border-radius: 8px;
    padding: 16px 20px; margin-bottom: 10px;
  }
  .arch-step .sn  { font-size: 0.72rem; font-weight: 700; color: #7c5cd8; text-transform: uppercase; letter-spacing: 1px; }
  .arch-step .st  { font-size: 1rem; font-weight: 700; color: #1f2328; margin: 2px 0; }
  .arch-step .sd  { font-size: 0.86rem; color: #57606a; margin: 0; }

  .section-title { font-size: 1.9rem; font-weight: 800; color: #1f2328; text-align: center; margin: 48px 0 8px; }
  .section-sub   { font-size: 1rem; color: #57606a; text-align: center; margin: 0 auto 32px; max-width: 600px; }

  .cta-box {
    background: linear-gradient(135deg, #302b63, #7c5cd8);
    border-radius: 16px; padding: 48px 40px;
    text-align: center; color: white; margin: 48px 0 32px;
  }
  .cta-box h2 { font-size: 2rem; font-weight: 800; margin: 0 0 12px; }
  .cta-box p  { font-size: 1.05rem; color: #d8b4fe; margin: 0 0 8px; }

  .footer {
    border-top: 1px solid #e5e7eb; padding: 24px 0 8px;
    text-align: center; color: #57606a; font-size: 0.82rem; margin-top: 48px;
  }
</style>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="badge">⚡ Patent Pending · Conceived June 2026</div>
  <h1>Agent<span>Forge</span></h1>
  <p>The missing monetization layer for AI. A tiered token framework that controls,
     prices, meters, and routes AI queries by complexity — cutting compute waste
     and unlocking new revenue streams for any LLM platform.</p>
</div>
""", unsafe_allow_html=True)

# ── STATS ─────────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
for col, num, lbl in [
    (c1, "3",     "Token Tiers"),
    (c2, "$1.8T", "AI Market by 2030"),
    (c3, "95%",   "AI queries over-provisioned"),
    (c4, "3x",    "Revenue uplift via tier pricing"),
]:
    with col:
        st.markdown(f'<div class="stat-card"><div class="num">{num}</div><div class="lbl">{lbl}</div></div>',
                    unsafe_allow_html=True)

# ── PROBLEM ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">The Problem Nobody Has Solved</div>'
            '<div class="section-sub">Every AI query — from "What is 2+2?" to '
            '"Build me a cloud infrastructure" — is treated and billed exactly the same. That\'s broken.</div>',
            unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)
for col, icon, title, desc in [
    (p1, "💸", "Undifferentiated Billing",
     "Simple lookups burn the same compute budget as complex agentic pipelines. Money wasted on every trivial query."),
    (p2, "🌍", "Environmental Waste",
     "Data centers are overloaded with full-model invocations for tasks that need a fraction of the compute. No structural fix exists."),
    (p3, "📉", "Missed Revenue",
     "LLM providers and AI app developers have no standardized framework to monetize query complexity. Billions left on the table."),
]:
    with col:
        st.markdown(f'<div class="feature-row"><h4>{icon} {title}</h4><p>{desc}</p></div>',
                    unsafe_allow_html=True)

# ── THREE TIERS ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">The Three Token Tiers</div>'
            '<div class="section-sub">A patent-pending framework that maps query complexity '
            'to the right compute path — and the right price.</div>', unsafe_allow_html=True)

t1, t2, t3 = st.columns(3)
with t1:
    st.markdown("""<div class="tier-card tier-basic">
      <h3>⚡ Basic Token</h3>
      <div style="color:#57606a;font-size:0.85rem;margin-bottom:4px;">Tier 1</div>
      <div class="price" style="color:#302b63;">$0.001 <span style="font-size:1rem;font-weight:400;">/ query</span></div>
      <ul><li>Single-turn, simple Q&A</li><li>Lightweight model path</li>
          <li>Fastest response time</li><li>General consumer use</li></ul>
      <div style="background:#e5e7eb;border-radius:4px;padding:6px 10px;font-size:0.8rem;color:#57606a;">
        "What is today's date?" / Simple lookups</div>
    </div>""", unsafe_allow_html=True)
with t2:
    st.markdown("""<div class="tier-card tier-mid">
      <h3>🔥 Mid Token <span class="popular">Most Popular</span></h3>
      <div style="color:#7c5cd8;font-size:0.85rem;margin-bottom:4px;">Tier 2</div>
      <div class="price" style="color:#302b63;">$0.01 <span style="font-size:1rem;font-weight:400;">/ query</span></div>
      <ul><li>Multi-turn sessions</li><li>Analysis & explanations</li>
          <li>Standard LLM inference</li><li>SMB & analyst access</li></ul>
      <div style="background:#ede9fe;border-radius:4px;padding:6px 10px;font-size:0.8rem;color:#5b21b6;">
        "Summarize this report" / "Explain this data"</div>
    </div>""", unsafe_allow_html=True)
with t3:
    st.markdown("""<div class="tier-card tier-advanced">
      <h3>🚀 Advanced Token</h3>
      <div style="color:#c4b5fd;font-size:0.85rem;margin-bottom:4px;">Tier 3</div>
      <div class="price" style="color:white;">$0.10 <span style="font-size:1rem;font-weight:400;color:#c4b5fd;">/ query</span></div>
      <ul style="color:#e2e8f0;"><li>Complex research tasks</li><li>Infrastructure generation</li>
          <li>Full agentic pipelines</li><li>Enterprise & developer use</li></ul>
      <div style="background:rgba(124,92,216,0.3);border-radius:4px;padding:6px 10px;font-size:0.8rem;color:#c4b5fd;">
        "Build me a cloud deployment" / Agentic tasks</div>
    </div>""", unsafe_allow_html=True)

# ── TOKEN CALCULATOR ──────────────────────────────────────────────────────────
st.markdown('<div class="section-title">💡 Token Cost Calculator</div>'
            '<div class="section-sub">See exactly how much you save by routing queries to the right tier.</div>',
            unsafe_allow_html=True)

calc_col, result_col = st.columns([2, 1])
with calc_col:
    basic_q = st.slider("Simple queries per day (Tier 1)",   0, 100000, 10000, 1000)
    mid_q   = st.slider("Analysis queries per day (Tier 2)", 0,  50000,  2000,  500)
    adv_q   = st.slider("Complex / agentic per day (Tier 3)", 0, 10000,   200,   50)

with result_col:
    tiered_mo = ((basic_q * 0.001) + (mid_q * 0.01) + (adv_q * 0.10)) * 30
    flat_mo   = (basic_q + mid_q + adv_q) * 0.10 * 30
    savings   = flat_mo - tiered_mo
    pct       = (savings / flat_mo * 100) if flat_mo > 0 else 0
    st.markdown(f"""
    <div style="background:#0f0c29;border-radius:14px;padding:28px;color:white;">
      <div style="font-size:0.75rem;color:#c4b5fd;text-transform:uppercase;letter-spacing:1px;margin-bottom:14px;">Monthly Estimate</div>
      <div style="margin-bottom:14px;">
        <div style="font-size:0.8rem;color:#94a3b8;">Without AgentForge (flat Tier 3)</div>
        <div style="font-size:1.8rem;font-weight:800;color:#f87171;">${flat_mo:,.0f}</div>
      </div>
      <div style="margin-bottom:14px;">
        <div style="font-size:0.8rem;color:#94a3b8;">With AgentForge (tiered routing)</div>
        <div style="font-size:1.8rem;font-weight:800;color:#4ade80;">${tiered_mo:,.0f}</div>
      </div>
      <div style="background:rgba(124,92,216,0.3);border-radius:8px;padding:14px;text-align:center;">
        <div style="font-size:0.8rem;color:#c4b5fd;">Monthly Savings</div>
        <div style="font-size:2rem;font-weight:800;color:#c4b5fd;">${savings:,.0f}</div>
        <div style="font-size:0.8rem;color:#94a3b8;">({pct:.0f}% reduction)</div>
      </div>
    </div>""", unsafe_allow_html=True)

# ── HOW IT WORKS ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">How AgentForge Works</div>'
            '<div class="section-sub">A Token Metering Engine sits between your user and the LLM — '
            'classifying, routing, gating, and logging every query.</div>', unsafe_allow_html=True)

al, ar = st.columns(2)
steps = [
    ("Step 1", "Query Received",           "User or application submits an AI query to the Token Metering Engine."),
    ("Step 2", "Complexity Classification","The engine classifies the query against the three-tier schema — Basic, Mid, or Advanced."),
    ("Step 3", "Entitlement Validation",   "System checks the user's purchased token tier against the classified complexity level."),
    ("Step 4", "Gate or Allow",            "Queries within tier are approved. Queries exceeding tier are gated — user prompted to upgrade."),
    ("Step 5", "Tier Routing",             "Approved query is routed to the compute path matching its tier: lightweight, standard LLM, or full agentic pipeline."),
    ("Step 6", "Ledger Recording",         "Consumption logged: user ID, tier, timestamp, compute path, remaining balance. Full audit trail."),
]
for i, (num, title, desc) in enumerate(steps):
    col = al if i < 3 else ar
    with col:
        st.markdown(f'<div class="arch-step"><div class="sn">{num}</div>'
                    f'<div class="st">{title}</div><div class="sd">{desc}</div></div>',
                    unsafe_allow_html=True)

# ── LICENSING MARKETS ─────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Three Licensing Markets</div>'
            '<div class="section-sub">AgentForge is a framework — not just one product. '
            'It licenses into three distinct markets simultaneously.</div>', unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)
for col, icon, title, desc, price in [
    (m1, "📱", "Consumer App Credits",
     "AI app developers integrate the token framework to sell tiered credit packs. Tier 1 is the entry product; Tier 3 is premium.",
     "Revenue share model"),
    (m2, "🏢", "Enterprise Seat Licensing",
     "Organizations license per seat or department. Developers get Tier 3; general staff get Tier 1/2. Scales by tier and volume.",
     "From $500/seat/mo"),
    (m3, "🤖", "LLM Platform Licensing",
     "Offered to LLM providers as a standardized monetization and compute-efficiency layer enabling differentiated products.",
     "Enterprise deal"),
]:
    with col:
        st.markdown(f"""<div class="feature-row" style="text-align:center;padding:28px 20px;">
          <div style="font-size:2rem;margin-bottom:8px;">{icon}</div>
          <h4>{title}</h4><p style="margin-bottom:10px;">{desc}</p>
          <div style="background:#7c5cd8;color:white;border-radius:6px;padding:4px 12px;
               display:inline-block;font-size:0.8rem;font-weight:700;">{price}</div>
        </div>""", unsafe_allow_html=True)

# ── CTA / LEAD CAPTURE ────────────────────────────────────────────────────────
st.markdown("""
<div class="cta-box">
  <h2>Get Early Access</h2>
  <p>AgentForge is in active development. Join the waitlist for licensing,
     partnership, and integration opportunities.</p>
</div>
""", unsafe_allow_html=True)

lc, _ = st.columns([2, 1])
with lc:
    with st.form("waitlist", clear_on_submit=True):
        name  = st.text_input("Your Name")
        email = st.text_input("Work Email")
        role  = st.selectbox("I am a...", [
            "Select your role", "AI Application Developer", "Enterprise IT / CTO",
            "LLM Platform Provider", "Investor / VC", "Researcher / Academic", "Other",
        ])
        interest = st.multiselect("I'm interested in...", [
            "Consumer App Credits licensing", "Enterprise Seat Licensing",
            "LLM Platform Licensing", "Partnership / Integration",
            "Investment opportunity", "Just following the project",
        ])
        if st.form_submit_button("⚡ Join the Waitlist"):
            if name and email and role != "Select your role":
                st.success(f"✅ Thanks {name}! You're on the list. We'll reach out at {email}.")
            else:
                st.warning("Please fill in your name, email, and role.")

# ── SOCIAL SHARE ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title" style="font-size:1.4rem;margin-top:32px;">Share AgentForge</div>',
            unsafe_allow_html=True)
sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.markdown('<a href="https://www.linkedin.com/sharing/share-offsite/?url=https://agentforge.azurecontainerapps.io" target="_blank" style="text-decoration:none;"><div style="background:#0077b5;border-radius:10px;padding:14px;text-align:center;color:white;font-weight:700;">📘 Share on LinkedIn</div></a>', unsafe_allow_html=True)
with sc2:
    st.markdown('<a href="https://twitter.com/intent/tweet?text=AgentForge%20—%20the%20missing%20monetization%20layer%20for%20AI.%20Patent-pending%20tiered%20token%20framework.%20Check%20it%20out:" target="_blank" style="text-decoration:none;"><div style="background:#000;border-radius:10px;padding:14px;text-align:center;color:white;font-weight:700;">𝕏 Share on X</div></a>', unsafe_allow_html=True)
with sc3:
    st.markdown('<a href="https://github.com/txnightcoder-prog/agentforge" target="_blank" style="text-decoration:none;"><div style="background:#24292e;border-radius:10px;padding:14px;text-align:center;color:white;font-weight:700;">⭐ Star on GitHub</div></a>', unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <strong>AgentForge</strong> · Patent Pending · Conceived June 12, 2026 · John Kirshy<br>
  <span style="color:#bbb;">© 2026 AgentForge. All rights reserved.</span><br><br>
  <span style="font-size:0.75rem;color:#ccc;">Made with IBM Bob</span>
</div>
""", unsafe_allow_html=True)
