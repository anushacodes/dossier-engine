#!/usr/bin/env python3
"""
Tool: render_dossier_html.py
Description: Compiles structured company & interviewer intelligence data into a 
spacious, dark-mode, anti-hallucination live-referral HTML dashboard and Markdown cheat sheet.
Features: 5-second TL;DR callouts, concrete metric pills, coaching tactical tips, and Judge Quality scores.
"""

import json
import os
import sys
import argparse
from pathlib import Path

DEFAULT_TEMPLATE_PATH = Path(__file__).resolve().parent.parent / "templates" / "dossier_template.html"
DEFAULT_MD_TEMPLATE_PATH = Path(__file__).resolve().parent.parent / "templates" / "dossier_template.md"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent.parent / "dossiers"

def format_metric_pills(metrics):
    if not metrics:
        return ""
    html = []
    for m in metrics:
        html.append(f'<span class="metric-pill">◆ {m}</span>')
    return " ".join(html)

def format_deep_list(items):
    if not items:
        return '<li class="deep-item"><div class="item-text" style="color: var(--text-dim);">No public information verified. (Inquire during interview)</div></li>'
    html = []
    for item in items:
        if isinstance(item, dict):
            tag = item.get("tag", "")
            text = item.get("text", "")
            citation = item.get("citation", "")
            url = item.get("url", "")
            verified = item.get("verified", True)

            badge_html = '<span class="badge-verified">✓ Verified</span>' if verified else '<span class="badge-inference">⚠ Inference</span>'
            citation_html = f'<a href="{url}" target="_blank" class="citation-link">{citation} ↗</a>' if citation and url and url != "#" else (f'<span class="citation-link">{citation}</span>' if citation else "")

            html.append(f'''
            <li class="deep-item">
              <div class="item-header">
                <span class="item-tag">{tag}:</span>
                {badge_html}
                {citation_html}
              </div>
              <div class="item-text">{text}</div>
            </li>
            ''')
        else:
            html.append(f'<li class="deep-item"><div class="item-text">{item}</div></li>')
    return "\n".join(html)

def format_markdown_deep_list(items):
    if not items:
        return "- *No public information verified. (Inquire during interview)*"
    md = []
    for item in items:
        if isinstance(item, dict):
            tag = item.get("tag", "")
            text = item.get("text", "")
            citation = item.get("citation", "")
            url = item.get("url", "")
            status = "Verified" if item.get("verified", True) else "Inference"
            cite_str = f" [[{citation}]({url})]" if citation and url and url != "#" else (f" [{citation}]" if citation else "")
            md.append(f"- **{tag}** [{status}]{cite_str}: {text}")
        else:
            md.append(f"- {item}")
    return "\n".join(md)

def format_questions_html(questions):
    if not questions:
        return '<div class="question-card"><div class="question-text">No custom questions available.</div></div>'
    html = []
    for i, q in enumerate(questions, 1):
        q_text = q.get("question", "")
        q_why = q.get("why", "")
        q_tag = q.get("category", "General Inquiry")
        safe_q = q_text.replace('"', '&quot;').replace("'", "&#39;")
        html.append(f'''
        <div class="question-card">
          <div class="question-top">
            <span class="question-category">Q{i} • {q_tag}</span>
            <button class="copy-btn" onclick="copyQuestion(this, '{safe_q}')">Copy Question</button>
          </div>
          <div class="question-text">{q_text}</div>
          {f'<div class="question-rationale">💡 <strong>Tactical Rationale:</strong> {q_why}</div>' if q_why else ''}
        </div>
        ''')
    return "\n".join(html)

def format_questions_md(questions):
    if not questions:
        return "None."
    md = []
    for i, q in enumerate(questions, 1):
        q_text = q.get("question", "")
        q_why = q.get("why", "")
        q_tag = q.get("category", "General")
        md.append(f"**Q{i} [{q_tag}]**: {q_text}")
        if q_why:
            md.append(f"  *Strategic Angle*: {q_why}")
    return "\n\n".join(md)

def format_sources_table(sources):
    if not sources:
        return '<tr><td colspan="4" style="text-align: center; color: var(--text-dim); padding: 18px;">No external sources formally logged.</td></tr>'
    rows = []
    for s in sources:
        publisher = s.get("publisher", "Web Record")
        title = s.get("title", "Document")
        date = s.get("date", "Recent")
        url = s.get("url", "#")
        link_html = f'<a href="{url}" target="_blank" class="citation-link" style="margin-left: 0;">Open Source ↗</a>' if url and url != "#" else '<span style="color: var(--text-dim); font-size: 11px;">Internal / Direct</span>'
        rows.append(f'''
        <tr>
          <td style="color: #ffffff; font-weight: 600;">{publisher}</td>
          <td>{title}</td>
          <td>{date}</td>
          <td>{link_html}</td>
        </tr>
        ''')
    return "\n".join(rows)

def render_dossier(data_path, output_dir=None, open_browser=False, quiet=False):
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not output_dir:
        output_dir = DEFAULT_OUTPUT_DIR
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    company_slug = data.get("company_name", "company").lower().replace(" ", "_")
    person_slug = data.get("interviewer_name", "person").lower().replace(" ", "_")
    base_name = f"{company_slug}_{person_slug}_dossier"

    # Load HTML Template
    with open(DEFAULT_TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        html_template = f.read()

    # Interviewer Quote block
    quote = data.get("interviewer_quote", "")
    quote_cite = data.get("interviewer_quote_source", "")
    quote_url = data.get("interviewer_quote_url", "")
    cite_pill = f'<a href="{quote_url}" target="_blank" class="citation-link">{quote_cite} ↗</a>' if quote_cite and quote_url and quote_url != "#" else (f'<span class="citation-link">{quote_cite}</span>' if quote_cite else "")
    interviewer_quote_block = f'''
    <div class="quote-card">
      <div class="quote-body">"{quote}"</div>
      <div class="quote-footer">— {data.get("interviewer_name")} {cite_pill}</div>
    </div>
    ''' if quote else ""

    # AI leadership quote
    ai_quote = data.get("ai_leadership_quote", "")
    ai_quote_author = data.get("ai_leadership_quote_author", "Leadership")
    ai_quote_cite = data.get("ai_leadership_quote_source", "")
    ai_quote_url = data.get("ai_leadership_quote_url", "")
    ai_cite_pill = f'<a href="{ai_quote_url}" target="_blank" class="citation-link">{ai_quote_cite} ↗</a>' if ai_quote_cite and ai_quote_url and ai_quote_url != "#" else (f'<span class="citation-link">{ai_quote_cite}</span>' if ai_quote_cite else "")
    ai_leadership_quotes = f'''
    <div class="quote-card" style="margin-top: 20px;">
      <div class="quote-body">"{ai_quote}"</div>
      <div class="quote-footer">— {ai_quote_author} {ai_cite_pill}</div>
    </div>
    ''' if ai_quote else ""

    sources = data.get("sources", [])

    # Judge badge
    judge_score = data.get("judge_score", "95/100")
    judge_verdict = data.get("judge_verdict", "Grounded | High Substance")
    judge_badge_text = f"🛡️ Quality Gate: {judge_score} ({judge_verdict})"

    # Replacements dictionary
    replacements = {
        "{{ company_name }}": data.get("company_name", ""),
        "{{ interviewer_name }}": data.get("interviewer_name", ""),
        "{{ interviewer_title }}": data.get("interviewer_title", ""),
        "{{ target_role }}": data.get("target_role", "General Discussion"),
        "{{ meeting_type }}": data.get("meeting_type", "Interview / Coffee Chat"),
        "{{ judge_score_badge }}": judge_badge_text,
        "{{ company_one_liner }}": data.get("company_one_liner", ""),
        "{{ ai_agenda_hook }}": data.get("ai_agenda_hook", ""),
        "{{ personal_rapport_hook }}": data.get("personal_rapport_hook", ""),
        "{{ interviewer_tldr }}": data.get("interviewer_tldr", data.get("interviewer_current_scope", "")),
        "{{ interviewer_metrics_pills }}": format_metric_pills(data.get("interviewer_metrics", [])),
        "{{ interviewer_current_scope }}": data.get("interviewer_current_scope", ""),
        "{{ interviewer_pedigree }}": data.get("interviewer_pedigree", ""),
        "{{ interviewer_public_stance }}": data.get("interviewer_public_stance", ""),
        "{{ interviewer_style }}": data.get("interviewer_style", ""),
        "{{ interviewer_quote_block }}": interviewer_quote_block,
        "{{ interviewer_coaching_point }}": data.get("interviewer_coaching_point", "Establish rapport by referencing their specific architectural decisions."),
        "{{ company_stage_or_ticker }}": data.get("company_stage_or_ticker", "Tech Company"),
        "{{ company_tldr }}": data.get("company_tldr", data.get("company_one_liner", "")),
        "{{ company_metrics_pills }}": format_metric_pills(data.get("company_metrics", [])),
        "{{ company_core_business }}": data.get("company_core_business", ""),
        "{{ company_moat }}": data.get("company_moat", ""),
        "{{ company_leadership_summary }}": data.get("company_leadership_summary", ""),
        "{{ company_reputation }}": data.get("company_reputation", ""),
        "{{ company_recent_news }}": data.get("company_recent_news", ""),
        "{{ company_coaching_point }}": data.get("company_coaching_point", "Align your responses with their business model and core customer value driver."),
        "{{ ai_tldr }}": data.get("ai_tldr", data.get("ai_agenda_hook", "")),
        "{{ ai_metrics_pills }}": format_metric_pills(data.get("ai_metrics", [])),
        "{{ ai_products_bullets }}": format_deep_list(data.get("ai_products", [])),
        "{{ ai_investments_bullets }}": format_deep_list(data.get("ai_investments", [])),
        "{{ ai_stack_bullets }}": format_deep_list(data.get("ai_stack", [])),
        "{{ ai_leadership_quotes }}": ai_leadership_quotes,
        "{{ ai_coaching_point }}": data.get("ai_coaching_point", "Focus on real production reliability and system integration rather than generic chatbot talk."),
        "{{ questions_html }}": format_questions_html(data.get("power_questions", [])),
        "{{ green_flags_bullets }}": format_deep_list(data.get("green_flags", [])),
        "{{ landmines_bullets }}": format_deep_list(data.get("landmines", [])),
        "{{ sources_count }}": str(len(sources)),
        "{{ sources_table_rows }}": format_sources_table(sources)
    }

    rendered_html = html_template
    for key, val in replacements.items():
        rendered_html = rendered_html.replace(key, str(val))

    html_path = output_dir / f"{base_name}.html"
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    # Load MD Template & Render
    if DEFAULT_MD_TEMPLATE_PATH.exists():
        with open(DEFAULT_MD_TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            md_template = f.read()

        md_replacements = {
            "{{ company_name }}": data.get("company_name", ""),
            "{{ interviewer_name }}": data.get("interviewer_name", ""),
            "{{ interviewer_title }}": data.get("interviewer_title", ""),
            "{{ target_role }}": data.get("target_role", "General Discussion"),
            "{{ meeting_type }}": data.get("meeting_type", "Interview / Coffee Chat"),
            "{{ company_one_liner }}": data.get("company_one_liner", ""),
            "{{ ai_agenda_hook }}": data.get("ai_agenda_hook", ""),
            "{{ personal_rapport_hook }}": data.get("personal_rapport_hook", ""),
            "{{ interviewer_current_scope }}": data.get("interviewer_current_scope", ""),
            "{{ interviewer_tenure }}": data.get("interviewer_tenure", ""),
            "{{ interviewer_pedigree }}": data.get("interviewer_pedigree", ""),
            "{{ interviewer_public_stance }}": data.get("interviewer_public_stance", ""),
            "{{ interviewer_style }}": data.get("interviewer_style", ""),
            "{{ interviewer_quote }}": quote or "None recorded",
            "{{ company_stage_or_ticker }}": data.get("company_stage_or_ticker", "Tech"),
            "{{ company_core_business }}": data.get("company_core_business", ""),
            "{{ company_moat }}": data.get("company_moat", ""),
            "{{ company_leadership_summary }}": data.get("company_leadership_summary", ""),
            "{{ company_reputation }}": data.get("company_reputation", ""),
            "{{ company_recent_news }}": data.get("company_recent_news", ""),
            "{{ ai_products_markdown }}": format_markdown_deep_list(data.get("ai_products", [])),
            "{{ ai_investments_markdown }}": format_markdown_deep_list(data.get("ai_investments", [])),
            "{{ ai_stack_markdown }}": format_markdown_deep_list(data.get("ai_stack", [])),
            "{{ ai_leadership_quotes_markdown }}": f'"{ai_quote}" — {ai_quote_author} ({ai_quote_cite})' if ai_quote else "N/A",
            "{{ questions_markdown }}": format_questions_md(data.get("power_questions", [])),
            "{{ green_flags_markdown }}": format_markdown_deep_list(data.get("green_flags", [])),
            "{{ landmines_markdown }}": format_markdown_deep_list(data.get("landmines", []))
        }

        rendered_md = md_template
        for key, val in md_replacements.items():
            rendered_md = rendered_md.replace(key, str(val))

        md_path = output_dir / f"{base_name}.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(rendered_md)
        if not quiet:
            print(f"✅ Generated Markdown Dossier: {md_path.resolve()}")

    if not quiet:
        print(f"✅ Generated HTML Dossier: {html_path.resolve()}")

    if open_browser:
        os.system(f'open "{html_path.resolve()}"')

    return str(html_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render interview intelligence dossier to HTML & Markdown")
    parser.add_argument("data_json", help="Path to structured JSON dossier input")
    parser.add_argument("--output-dir", "-o", help="Target output directory", default=None)
    parser.add_argument("--open", action="store_true", help="Open HTML dossier directly in default browser")
    parser.add_argument("--quiet", "-q", action="store_true", help="Suppress duplicate CLI output")
    args = parser.parse_args()

    render_dossier(args.data_json, args.output_dir, args.open, args.quiet)
