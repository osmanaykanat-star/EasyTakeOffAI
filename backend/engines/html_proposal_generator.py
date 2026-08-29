import datetime
from typing import Dict, Any
from ..trades.trade_base import ProjectTakeoff

class HTMLProposalGenerator:
    """
    Generates a clean, professional, printable HTML proposal
    mirroring the exact Excel proposal template layout.
    """

    @staticmethod
    def generate_html(project: ProjectTakeoff) -> str:
        date_val = project.date_str if project.date_str else datetime.date.today().strftime("%m/%d/%Y")
        to_company = (project.client_company or "").strip()
        attn_person = (project.client_name or "").strip()
        bidder_company = (project.bidder_company or "").strip()
        bidder_address = (project.bidder_address or "").strip()
        bidder_phone = (project.bidder_phone or "").strip()
        bidder_email = (project.bidder_email or "").strip()
        estimator_title = (project.estimator_title or "Senior Estimator").strip()

        if not to_company or to_company.upper() in ["GENERAL CONTRACTOR", "COMMERCIAL CONSTRUCTION", "CLIENT COMPANY", ""]:
            if any(k in attn_person.upper() for k in ["LLC", "INC", "CORP", "CONSTRUCTION", "BUILDERS", "GROUP", "MANAGEMENT", "PARTNERS", "DEVELOPMENT", "HOLDINGS"]):
                to_company = attn_person
                attn_person = "Project Estimator / Manager"
            else:
                to_company = "General Contractor / Construction Manager"

        if not attn_person:
            attn_person = "Project Manager"

        salutation_name = attn_person.split()[0].title() if attn_person and attn_person not in ["Project Manager", "Project Estimator / Manager"] else "Sir/Madam"
        project_name = project.project_name or "New Takeoff Project"
        estimator_name = project.estimator_name or ""

        # Aggregate total by symbol
        sym_totals: Dict[str, Dict[str, Any]] = {}
        for room in project.rooms:
            for item in room.items:
                if item.symbol not in sym_totals:
                    sym_totals[item.symbol] = {"qty": 0.0, "unit": item.unit}
                sym_totals[item.symbol]["qty"] += item.quantity

        # Group rooms by floor
        floors_dict: Dict[str, list] = {}
        for room in project.rooms:
            floors_dict.setdefault(room.floor_name, []).append(room)

        header_banner = f"""
  <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #2563eb; padding-bottom: 14px; margin-bottom: 24px;">
    <div>
      <div style="font-size: 22px; font-weight: 800; color: #1e3a8a; letter-spacing: -0.5px;">{bidder_company}</div>
      <div style="font-size: 13px; color: #475569; margin-top: 2px;">{bidder_address}</div>
      <div style="font-size: 13px; color: #475569;">{f'Tel: {bidder_phone}' if bidder_phone else ''}{f' | Email: {bidder_email}' if bidder_email else ''}</div>
    </div>
    <div style="text-align: right;">
      <div class="title-header" style="font-size: 24px; font-weight: 900; color: #0f172a; margin: 0;">PROPOSAL</div>
      <div class="date-row" style="margin: 4px 0 0 0; font-size: 13px; color: #64748b;">Date: <strong>{date_val}</strong></div>
    </div>
  </div>""" if bidder_company else f"""
  <div class="title-header">PROPOSAL</div>
  <div class="date-row">{date_val}</div>"""

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Proposal - {project_name}</title>
<style>
  body {{
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    color: #222;
    background: #f8fafc;
    padding: 30px;
    margin: 0;
  }}
  .proposal-card {{
    max-width: 960px;
    margin: 0 auto;
    background: #ffffff;
    padding: 40px 50px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    border-radius: 8px;
    border: 1px solid #e2e8f0;
  }}
  .print-btn-bar {{
    max-width: 960px;
    margin: 0 auto 20px auto;
    display: flex;
    justify-content: flex-end;
    gap: 12px;
  }}
  .btn {{
    padding: 8px 16px;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    border: none;
    font-size: 14px;
    transition: all 0.2s;
  }}
  .btn-print {{
    background: #2563eb;
    color: white;
  }}
  .btn-print:hover {{
    background: #1d4ed8;
  }}
  .btn-excel {{
    background: #10b981;
    color: white;
    text-decoration: none;
    display: inline-block;
    padding: 8px 16px;
  }}
  .btn-excel:hover {{
    background: #059669;
  }}
  .title-header {{
    font-size: 24px;
    font-weight: 800;
    letter-spacing: 0.5px;
    color: #0f172a;
    margin-bottom: 4px;
  }}
  .date-row {{
    font-size: 13.5px;
    color: #475569;
    margin-bottom: 20px;
  }}
  .meta-grid {{
    display: grid;
    grid-template-columns: 80px 1fr;
    row-gap: 6px;
    font-size: 14px;
    margin-bottom: 24px;
  }}
  .meta-label {{
    font-weight: 700;
    color: #334155;
  }}
  .meta-val {{
    color: #0f172a;
  }}
  .intro-text {{
    font-size: 13.5px;
    line-height: 1.6;
    color: #334155;
    margin-bottom: 20px;
  }}
  .summary-box {{
    background: #f1f5f9;
    padding: 12px 18px;
    border-radius: 6px;
    display: inline-block;
    margin-bottom: 24px;
    font-weight: bold;
    font-size: 15px;
    color: #0f172a;
    border-left: 4px solid #2563eb;
  }}
  .section-title {{
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 0.5px;
    color: #1e3a8a;
    background: #e2e8f0;
    padding: 8px 12px;
    margin-top: 24px;
    margin-bottom: 0;
    border: 1px solid #cbd5e1;
    border-bottom: none;
  }}
  table.takeoff-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin-bottom: 24px;
  }}
  table.takeoff-table th {{
    background: #1e293b;
    color: #ffffff;
    font-weight: 600;
    padding: 8px 10px;
    text-align: left;
    border: 1px solid #1e293b;
  }}
  table.takeoff-table td {{
    padding: 7px 10px;
    border: 1px solid #e2e8f0;
    color: #334155;
  }}
  table.takeoff-table tr:nth-child(even) {{
    background: #f8fafc;
  }}
  .floor-row td {{
    background: #f1f5f9;
    font-weight: 700;
    color: #0f172a;
  }}
  .room-header td {{
    background: #f8fafc;
    font-weight: 600;
    color: #1e3a8a;
  }}
  .num-cell {{
    text-align: right;
    font-variant-numeric: tabular-nums;
  }}
  .center-cell {{
    text-align: center;
  }}
  .totals-row td {{
    background: #eff6ff;
    font-weight: 700;
    color: #1e3a8a;
    border-top: 2px solid #93c5fd;
  }}
  .totals-table {{
    width: 100%;
    max-width: 500px;
    border-collapse: collapse;
    font-size: 13px;
    margin-bottom: 24px;
  }}
  .totals-table th {{
    background: #f1f5f9;
    text-align: left;
    padding: 6px 10px;
    border: 1px solid #cbd5e1;
  }}
  .totals-table td {{
    padding: 6px 10px;
    border: 1px solid #e2e8f0;
  }}
  .materials-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin-bottom: 24px;
  }}
  .materials-table th {{
    background: #f1f5f9;
    padding: 6px 10px;
    border: 1px solid #cbd5e1;
    font-weight: 700;
    text-align: left;
  }}
  .materials-table td {{
    padding: 6px 10px;
    border: 1px solid #e2e8f0;
  }}
  .notes-italic {{
    font-size: 12px;
    color: #64748b;
    font-style: italic;
  }}
  .notes-list {{
    font-size: 12.5px;
    line-height: 1.7;
    color: #475569;
    padding-left: 20px;
    margin-bottom: 24px;
  }}
  .sign-off {{
    margin-top: 30px;
    font-size: 14px;
    color: #334155;
  }}
  @media print {{
    body {{
      background: white;
      padding: 0;
    }}
    .proposal-card {{
      box-shadow: none;
      border: none;
      padding: 0;
    }}
    .print-btn-bar {{
      display: none;
    }}
  }}
</style>
</head>
<body>

<div class="print-btn-bar">
  <a href="/api/export/excel" class="btn btn-excel">📥 Download Excel File</a>
  <button onclick="window.print()" class="btn btn-print">🖨️ Print / Save as PDF</button>
</div>

<div class="proposal-card">
  {header_banner}

  <div class="meta-grid">
    <div class="meta-label">To:</div>
    <div class="meta-val"><strong>{to_company}</strong></div>
    <div class="meta-label">Attn:</div>
    <div class="meta-val">{attn_person}</div>
    <div class="meta-label">Re:</div>
    <div class="meta-val">{project_name}</div>
  </div>

  <div class="intro-text">
    Dear {salutation_name},<br>
    We hereby propose to furnish and install all materials and labor for <strong>{project.trade_category or 'the selected trades'}</strong> as detailed below in accordance with project drawings and specifications.
  </div>

  <div class="summary-box" style="display: flex; justify-content: space-between; align-items: center; background: #eff6ff; border: 1px solid #bfdbfe; border-left: 5px solid #2563eb; padding: 14px 20px; border-radius: 6px; margin-bottom: 24px;">
    <div>
      <strong style="color: #1e3a8a; font-size: 14px;">Scope Summary:</strong>
      <span style="color: #334155; font-size: 14px;"> {len(project.rooms)} Rooms / Areas ({project.trade_category or 'Selected Trades'})</span>
    </div>
    <div style="font-size: 15px; color: #1e3a8a;">
      <strong>Base Bid Total: </strong><span style="font-size: 18px; font-weight: 800; color: #2563eb;">${sum(sum(it.total_bid or (it.quantity * (it.material_price + it.labor_price)) for it in r.items) for r in project.rooms):,.2f}</span>
    </div>
  </div>

  <div class="section-title">DETAILED ROOM-BY-ROOM TAKEOFF BREAKDOWN</div>

  <table class="takeoff-table">
    <thead>
      <tr>
        <th style="width: 10%;">Symbol</th>
        <th style="width: 25%;">Finish Type</th>
        <th style="width: 18%;">Material Type</th>
        <th style="width: 7%; text-align: center;">Work</th>
        <th style="width: 10%; text-align: right;">Quantity</th>
        <th style="width: 6%; text-align: center;">Unit</th>
        <th style="width: 8%; text-align: right;">Mat ($)</th>
        <th style="width: 8%; text-align: right;">Labor ($)</th>
        <th style="width: 12%; text-align: right;">Line Bid ($)</th>
      </tr>
    </thead>
    <tbody>"""

        for floor_name, floor_rooms in floors_dict.items():
            html += f"""
      <tr class="floor-header-row">
        <td colspan="9" style="padding: 8px 10px; font-size: 13.5px; background: #e2e8f0; font-weight: 800; color: #0f172a;">📌 <strong>{floor_name.upper()}</strong></td>
      </tr>"""
            for room in floor_rooms:
                room_total = sum(it.total_bid or (it.quantity * (it.material_price + it.labor_price)) for it in room.items)
                html += f"""
      <tr class="room-header-row">
        <td colspan="7" style="background: #f8fafc; font-weight: bold; color: #1e3a8a; border-left: 3px solid #2563eb; padding: 6px 10px;">
          {room.room_name.upper()}
        </td>
        <td colspan="2" style="background: #f8fafc; text-align: right; font-weight: bold; color: #1e3a8a; padding: 6px 10px;">
          Room Subtotal: ${room_total:,.2f}
        </td>
      </tr>"""
                for item in room.items:
                    line_bid = item.total_bid or (item.quantity * (item.material_price + item.labor_price))
                    html += f"""
      <tr>
        <td><strong>{item.symbol}</strong></td>
        <td>{item.finish_type}</td>
        <td>{item.material_type}</td>
        <td class="center-cell">{item.work_type}</td>
        <td class="num-cell"><strong>{item.quantity:,.2f}</strong></td>
        <td class="center-cell">{item.unit}</td>
        <td class="num-cell">${item.material_price:,.2f}</td>
        <td class="num-cell">${item.labor_price:,.2f}</td>
        <td class="num-cell" style="font-weight: 700; color: #1e3a8a;">${line_bid:,.2f}</td>
      </tr>"""

        html += f"""
    </tbody>
  </table>

  <div class="section-title">TOTAL QUANTITIES BY MATERIAL SYMBOL</div>
  <table class="totals-table">
    <thead>
      <tr>
        <th>Symbol</th>
        <th style="text-align: right;">Total Quantity</th>
        <th style="text-align: center;">Unit</th>
      </tr>
    </thead>
    <tbody>"""

        for sym, data in sorted(sym_totals.items()):
            html += f"""
      <tr>
        <td><strong>{sym}</strong></td>
        <td class="num-cell"><strong>{data['qty']:,.2f}</strong></td>
        <td class="center-cell">{data['unit']}</td>
      </tr>"""

        html += f"""
    </tbody>
  </table>

  <div class="section-title">MATERIALS SPECIFICATION INFORMATION</div>
  <table class="materials-table">
    <thead>
      <tr>
        <th style="width: 45%;">Material / Specification</th>
        <th style="width: 18%; text-align: right;">Quantity</th>
        <th style="width: 12%; text-align: center;">Unit</th>
        <th style="width: 25%;">Scope Notes</th>
      </tr>
    </thead>
    <tbody>"""

        for sym, data in sorted(sym_totals.items()):
            spec = project.material_specs.get(sym)
            desc_text = f"<strong>{sym}</strong>: {spec.description}" if spec and spec.description else f"<strong>{sym}</strong>: Standard Specification"
            notes_text = spec.notes if spec and spec.notes else ""
            html += f"""
      <tr>
        <td>{desc_text}</td>
        <td class="num-cell">{data['qty']:,.2f} {data['unit']}</td>
        <td class="center-cell">{data['unit']}</td>
        <td class="notes-italic">{notes_text}</td>
      </tr>"""

        html += f"""
    </tbody>
  </table>

  <div class="section-title">EXCLUSIONS</div>
  <ul class="exclusion-list">"""

        exclusions = project.exclusions or [
            "1) Air freight any material.",
            "2) Premium/Overtime labor unless agreed in writing.",
            "3) Structural subfloor repair or major crack isolation beyond standard prep."
        ]
        for excl in exclusions:
            html += f"<li>{excl}</li>"

        html += f"""
  </ul>

  <div class="section-title">ABBREVIATIONS</div>
  <ul class="exclusion-list">
    <li><strong>S&I:</strong> Supply & Install</li>
    <li><strong>IO:</strong> Install Only</li>
  </ul>

  <div style="margin-top: 30px; margin-bottom: 24px; padding: 16px 20px; background: #f1f5f9; border-left: 4px solid #2563eb; border-radius: 4px;">
    <div style="font-size: 13px; color: #334155;">
      <strong>Respectfully Submitted By:</strong><br>
      <span style="font-size: 15px; font-weight: 800; color: #1e3a8a;">{estimator_name or 'Estimating Department'}</span> &mdash; <span style="color: #475569;">{estimator_title}</span><br>
      {f'<strong>{bidder_company}</strong>' if bidder_company else ''}{f' | Tel: {bidder_phone}' if bidder_phone else ''}{f' | Email: {bidder_email}' if bidder_email else ''}
    </div>
  </div>

  <!-- Enterprise E-Signature Authorization Block -->
  <div style="margin-top: 40px; padding: 24px; background: #f8fafc; border: 2px dashed #94a3b8; border-radius: 8px;">
    <div style="font-size: 15px; font-weight: 800; color: #1e3a8a; margin-bottom: 8px;">
      <i class="fa-solid fa-file-signature"></i> CLIENT ACCEPTANCE & DIGITAL AUTHORIZATION
    </div>
    <p style="font-size: 13px; color: #475569; margin: 0 0 16px 0;">
      By signing below, the Client agrees to the quantities, specifications, budget pricing, and terms & conditions outlined in this proposal.
    </p>
    <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 16px;">
      <div style="flex: 1; min-width: 200px;">
        <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">Authorized Representative Name</label>
        <input type="text" id="signerName" placeholder="Full Name" style="width: 100%; padding: 8px 10px; border: 1px solid #cbd5e1; border-radius: 4px; font-size: 13px;">
      </div>
      <div style="flex: 1; min-width: 200px;">
        <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">Title / Role</label>
        <input type="text" id="signerTitle" placeholder="e.g. Project Manager / GC" style="width: 100%; padding: 8px 10px; border: 1px solid #cbd5e1; border-radius: 4px; font-size: 13px;">
      </div>
      <div style="width: 150px;">
        <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">Date</label>
        <input type="text" id="signerDate" value="{date_val}" readonly style="width: 100%; padding: 8px 10px; border: 1px solid #cbd5e1; border-radius: 4px; font-size: 13px; background: #e2e8f0;">
      </div>
    </div>

    <label style="display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">Draw Signature (Touch / Mouse):</label>
    <div style="background: #ffffff; border: 1px solid #94a3b8; border-radius: 4px; width: 100%; max-width: 480px; height: 120px; position: relative;">
      <canvas id="sigPad" width="480" height="120" style="width: 100%; height: 100%; cursor: crosshair;"></canvas>
    </div>

    <div style="display: flex; gap: 10px; margin-top: 12px;">
      <button type="button" onclick="clearSigPad()" style="padding: 6px 14px; background: #64748b; color: white; border: none; border-radius: 4px; font-size: 12px; cursor: pointer; font-weight: 600;">Clear Pad</button>
      <button type="button" onclick="submitSig()" style="padding: 8px 20px; background: #16a34a; color: white; border: none; border-radius: 4px; font-size: 13px; cursor: pointer; font-weight: 700;">Accept & Sign Proposal</button>
    </div>
    <div id="sigStatus" style="display: none; margin-top: 12px; padding: 10px; background: #dcfce7; color: #166534; border-radius: 4px; font-size: 13px; font-weight: 700;"></div>
  </div>
</div>

<script>
  let sigCanvas = document.getElementById('sigPad');
  let sigCtx = sigCanvas ? sigCanvas.getContext('2d') : null;
  let isDrawing = false;

  if (sigCanvas && sigCtx) {{
    sigCtx.strokeStyle = '#0f172a';
    sigCtx.lineWidth = 2;
    sigCtx.lineCap = 'round';

    function getPos(e) {{
      let rect = sigCanvas.getBoundingClientRect();
      let clientX = e.touches ? e.touches[0].clientX : e.clientX;
      let clientY = e.touches ? e.touches[0].clientY : e.clientY;
      return {{ x: clientX - rect.left, y: clientY - rect.top }};
    }}

    function startDraw(e) {{ isDrawing = true; let p = getPos(e); sigCtx.beginPath(); sigCtx.moveTo(p.x, p.y); }}
    function draw(e) {{ if (!isDrawing) return; e.preventDefault(); let p = getPos(e); sigCtx.lineTo(p.x, p.y); sigCtx.stroke(); }}
    function endDraw() {{ isDrawing = false; }}

    sigCanvas.addEventListener('mousedown', startDraw);
    sigCanvas.addEventListener('mousemove', draw);
    sigCanvas.addEventListener('mouseup', endDraw);
    sigCanvas.addEventListener('touchstart', startDraw);
    sigCanvas.addEventListener('touchmove', draw);
    sigCanvas.addEventListener('touchend', endDraw);
  }}

  function clearSigPad() {{
    if (sigCtx && sigCanvas) {{
      sigCtx.clearRect(0, 0, sigCanvas.width, sigCanvas.height);
      document.getElementById('sigStatus').style.display = 'none';
    }}
  }}

  function submitSig() {{
    let name = document.getElementById('signerName').value.trim();
    if (!name) {{
      alert('Please enter the Authorized Representative Name.');
      return;
    }}
    let st = document.getElementById('sigStatus');
    st.style.display = 'block';
    st.innerHTML = '&#x2705; Proposal Accepted & Digitally Authorized by <strong>' + name + '</strong> on ' + new Date().toLocaleString() + ' (ID: ' + Math.random().toString(36).substring(2, 10).toUpperCase() + ')';
  }}
</script>
</body>
</html>"""
        return html

    @staticmethod
    def generate_sow_html(project: ProjectTakeoff) -> str:
        date_val = project.date_str if project.date_str else datetime.date.today().strftime("%m/%d/%Y")
        project_name = project.project_name or "25-19 27th Street, Astoria"
        estimator_name = project.estimator_name or ""

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Scope of Work (SOW) Bid - {project_name}</title>
<style>
  body {{
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    color: #1e293b;
    background: #f8fafc;
    padding: 30px;
    margin: 0;
  }}
  .sow-card {{
    max-width: 960px;
    margin: 0 auto;
    background: #ffffff;
    padding: 40px 50px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    border-radius: 8px;
    border: 1px solid #e2e8f0;
  }}
  .print-btn-bar {{
    max-width: 960px;
    margin: 0 auto 20px auto;
    display: flex;
    justify-content: flex-end;
    gap: 12px;
  }}
  .btn {{
    padding: 9px 18px;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    border: none;
    font-size: 14px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s;
  }}
  .btn-print {{ background: #2563eb; color: white; }}
  .btn-print:hover {{ background: #1d4ed8; }}
  .btn-excel {{ background: #10b981; color: white; }}
  .btn-excel:hover {{ background: #059669; }}
  .btn-proposal {{ background: #475569; color: white; }}
  .btn-proposal:hover {{ background: #334155; }}
  
  .title-block {{
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 16px;
    margin-bottom: 24px;
  }}
  .title-block h1 {{
    font-size: 22px;
    color: #1e3a8a;
    margin: 0 0 8px 0;
  }}
  .meta-row {{
    display: flex;
    gap: 30px;
    font-size: 14px;
    color: #475569;
  }}
  .sow-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin-bottom: 24px;
  }}
  .sow-table th {{
    background: #1e3a8a;
    color: white;
    padding: 10px;
    text-align: left;
    font-weight: 700;
    border: 1px solid #1e3a8a;
  }}
  .sow-table td {{
    padding: 8px 10px;
    border: 1px solid #cbd5e1;
  }}
  .sec-hdr {{
    background: #d9e1f2;
    font-weight: 800;
    color: #0f172a;
    font-size: 13.5px;
  }}
  .sub-hdr {{
    background: #f1f5f9;
    font-weight: 700;
    color: #1e293b;
  }}
  .num-cell {{
    text-align: right;
    font-weight: 600;
  }}
  .center-cell {{
    text-align: center;
  }}
  .notes-text {{
    font-size: 12px;
    color: #64748b;
    font-style: italic;
  }}
  .summary-row {{
    background: #f8fafc;
    font-weight: bold;
  }}
  .grand-total-row {{
    background: #fef3c7;
    font-weight: bold;
    font-size: 15px;
    color: #1e3a8a;
  }}
  @media print {{
    body {{ background: white; padding: 0; }}
    .sow-card {{ box-shadow: none; border: none; padding: 0; }}
    .print-btn-bar {{ display: none; }}
  }}
</style>
</head>
<body>

<div class="print-btn-bar">
  <a href="/api/export/sow-excel" class="btn btn-excel">📥 Download SOW Excel (.xlsx)</a>
  <a href="/api/export/html" class="btn btn-proposal" target="_blank">📄 Open Itemized Proposal</a>
  <button onclick="window.print()" class="btn btn-print">🖨️ Print / Save as PDF</button>
</div>

<div class="sow-card">
  <div class="title-block">
    <h1>BID SCOPE OF WORK (SOW) SCHEDULE</h1>
    <div class="meta-row">
      <div><strong>PROJECT:</strong> {project_name}</div>
      <div><strong>BIDDER / CONTRACTOR:</strong> {project.bidder_company or 'Commercial Subcontractor'}</div>
      <div><strong>ESTIMATOR:</strong> {estimator_name or 'Estimating Dept'} ({project.estimator_title or 'Senior Estimator'})</div>
      <div><strong>DATE:</strong> {date_val}</div>
    </div>
  </div>

  <table class="sow-table">
    <thead>
      <tr>
        <th style="width: 44%;">ITEM / SCOPE OF WORK</th>
        <th style="width: 16%; text-align: right;">QUANTITY / UNIT</th>
        <th style="width: 14%; text-align: right;">BID AMOUNT ($)</th>
        <th style="width: 26%;">SCOPE & DRAWING SPEC NOTES</th>
      </tr>
    </thead>
    <tbody>"""

        from .excel_generator import ExcelProposalGenerator
        sow_rows = ExcelProposalGenerator.get_dynamic_sow_rows(project)

        subtotal = 0.0
        tbody_html = ""
        for rtype, name, val, qty_str, note in sow_rows:
            if rtype == "SEC":
                tbody_html += f'\n      <tr class="sec-hdr"><td colspan="4">{name}</td></tr>'
            elif rtype == "SUB":
                tbody_html += f'\n      <tr class="sub-hdr"><td colspan="4">{name}</td></tr>'
            else:
                subtotal += float(val or 0.0)
                bid_str = f"${val:,.2f}" if val > 0 else "$0.00"
                tbody_html += f'\n      <tr><td>{name}</td><td class="num-cell">{qty_str}</td><td class="num-cell">{bid_str}</td><td class="notes-text">{note}</td></tr>'

        oh_profit = subtotal * 0.10
        insurance = subtotal * 0.03
        grand_total = subtotal + oh_profit + insurance

        tbody_html += f"""
      <tr class="summary-row"><td colspan="2"><strong>SUBTOTAL</strong></td><td class="num-cell"><strong>${subtotal:,.2f}</strong></td><td class="notes-text">Sum of scope items</td></tr>
      <tr class="summary-row"><td colspan="2"><strong>Overhead & Profit (10%)</strong></td><td class="num-cell">${oh_profit:,.2f}</td><td class="notes-text">10% Contractor Markup</td></tr>
      <tr class="summary-row"><td colspan="2"><strong>Insurance (3%)</strong></td><td class="num-cell">${insurance:,.2f}</td><td class="notes-text">3% Liability & GL Insurance</td></tr>
      <tr class="grand-total-row"><td colspan="2"><strong>GRAND TOTAL</strong></td><td class="num-cell"><strong>${grand_total:,.2f}</strong></td><td class="notes-text"><strong>Total Lump Sum Turnkey Bid</strong></td></tr>"""

        html += tbody_html + f"""
    </tbody>
  </table>

  <div style="margin-top: 30px; font-size: 14px; color: #334155;">
    Best regards,<br><br>
    <strong>{estimator_name}</strong>
  </div>
</div>

</body>
</html>"""
        return html
