/**
 * EasyTakeOffAI - Visual Blueprint Takeoff Canvas & Geometry Viewer
 * Enterprise Module: Interactive plan viewer with room polygon overlays,
 * 2-way table sync, confidence badges, and 2-point scale calibration ruler.
 */

// ========== STATE ==========
let blueprintCanvas = null;
let blueprintCtx = null;
let polygonsData = [];
let auditData = null;
let highlightedPolyId = null;
let canvasScale = 1.0;
let canvasPanX = 0;
let canvasPanY = 0;
let isDragging = false;
let dragStartX = 0;
let dragStartY = 0;

// ========== INIT ==========
function initBlueprintViewer() {
    blueprintCanvas = document.getElementById('blueprintCanvas');
    if (!blueprintCanvas) return;
    blueprintCtx = blueprintCanvas.getContext('2d');
    blueprintCanvas.addEventListener('wheel', handleCanvasZoom, { passive: false });
    blueprintCanvas.addEventListener('mousedown', handleCanvasMouseDown);
    blueprintCanvas.addEventListener('mousemove', handleCanvasMouseMove);
    blueprintCanvas.addEventListener('mouseup', handleCanvasMouseUp);
    blueprintCanvas.addEventListener('click', handleCanvasClick);
    loadPolygonsAndAudit();
}

// ========== DATA LOADING ==========
async function loadPolygonsAndAudit() {
    try {
        const [polyRes, auditRes] = await Promise.all([
            fetch('/api/polygons'),
            fetch('/api/audit')
        ]);
        const polyData = await polyRes.json();
        const auditJson = await auditRes.json();
        polygonsData = polyData.polygons || [];
        auditData = auditJson;
        renderBlueprintCanvas();
        renderAuditPanel();
    } catch (e) {
        console.error('Blueprint viewer load error:', e);
    }
}

// ========== CANVAS RENDERING ==========
function renderBlueprintCanvas() {
    if (!blueprintCtx || !blueprintCanvas) return;
    const W = blueprintCanvas.width;
    const H = blueprintCanvas.height;
    blueprintCtx.clearRect(0, 0, W, H);
    blueprintCtx.save();
    blueprintCtx.translate(canvasPanX, canvasPanY);
    blueprintCtx.scale(canvasScale, canvasScale);

    // Draw grid
    blueprintCtx.strokeStyle = '#e2e8f0';
    blueprintCtx.lineWidth = 0.5;
    for (let x = 0; x < 3000; x += 50) {
        blueprintCtx.beginPath(); blueprintCtx.moveTo(x, 0); blueprintCtx.lineTo(x, 2000); blueprintCtx.stroke();
    }
    for (let y = 0; y < 2000; y += 50) {
        blueprintCtx.beginPath(); blueprintCtx.moveTo(0, y); blueprintCtx.lineTo(3000, y); blueprintCtx.stroke();
    }

    // Draw floor labels and room polygons
    let prevFloor = '';
    for (const poly of polygonsData) {
        if (poly.floor_name !== prevFloor) {
            prevFloor = poly.floor_name;
            blueprintCtx.fillStyle = '#1e293b';
            blueprintCtx.font = 'bold 14px Inter, system-ui, sans-serif';
            blueprintCtx.fillText(poly.floor_name, poly.x - 5, poly.y - 18);
        }

        const isHighlighted = (highlightedPolyId === poly.id);

        // Room polygon fill
        blueprintCtx.fillStyle = isHighlighted ? poly.style.stroke + '55' : poly.style.fill;
        blueprintCtx.fillRect(poly.x, poly.y, poly.width, poly.height);

        // Room polygon border
        blueprintCtx.strokeStyle = poly.style.stroke;
        blueprintCtx.lineWidth = isHighlighted ? 3.0 : 1.5;
        if (isHighlighted) {
            blueprintCtx.setLineDash([6, 3]);
        }
        blueprintCtx.strokeRect(poly.x, poly.y, poly.width, poly.height);
        blueprintCtx.setLineDash([]);

        // Room label
        blueprintCtx.fillStyle = '#0f172a';
        blueprintCtx.font = 'bold 11px Inter, system-ui, sans-serif';
        const labelText = poly.room_name.length > 22 ? poly.room_name.substring(0, 20) + '...' : poly.room_name;
        blueprintCtx.fillText(labelText, poly.x + 6, poly.y + 16);

        // Dimensions label
        blueprintCtx.fillStyle = '#64748b';
        blueprintCtx.font = '10px Inter, system-ui, sans-serif';
        blueprintCtx.fillText(`${poly.length_ft}' x ${poly.width_ft}' = ${poly.area_sqft} SF`, poly.x + 6, poly.y + 30);

        // Item count badge
        blueprintCtx.fillStyle = poly.style.stroke;
        blueprintCtx.font = '9px Inter, system-ui, sans-serif';
        blueprintCtx.fillText(`${poly.items_count} items`, poly.x + 6, poly.y + poly.height - 8);

        // Confidence badge (if audit data exists)
        if (auditData && auditData.room_audits) {
            const roomAudit = auditData.room_audits.find(a => a.room_name === poly.room_name && a.floor_name === poly.floor_name);
            if (roomAudit) {
                const bw = 52, bh = 16;
                const bx = poly.x + poly.width - bw - 4;
                const by = poly.y + 4;
                blueprintCtx.fillStyle = roomAudit.badge_color + '33';
                blueprintCtx.beginPath();
                blueprintCtx.roundRect(bx, by, bw, bh, 4);
                blueprintCtx.fill();
                blueprintCtx.fillStyle = roomAudit.badge_color;
                blueprintCtx.font = 'bold 8px Inter, system-ui, sans-serif';
                blueprintCtx.fillText(roomAudit.rating_label, bx + 3, by + 11);
            }
        }
    }

    blueprintCtx.restore();
}

// ========== AUDIT PANEL ==========
function renderAuditPanel() {
    const panel = document.getElementById('auditPanel');
    if (!panel || !auditData) return;

    let html = `
        <div class="audit-header" style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
            <div style="width:12px;height:12px;border-radius:50%;background:${auditData.status_color}"></div>
            <div>
                <div style="font-weight:700;font-size:0.95rem;color:#0f172a">${auditData.status_text}</div>
                <div style="font-size:0.8rem;color:#64748b">${auditData.total_rooms_audited} rooms audited &bull; Avg confidence: ${auditData.average_confidence}%</div>
            </div>
        </div>`;

    if (auditData.anomalies && auditData.anomalies.length > 0) {
        html += `<div style="max-height:200px;overflow-y:auto;">`;
        for (const a of auditData.anomalies) {
            const icon = a.type === 'WARNING' ? 'fa-triangle-exclamation' : 'fa-circle-info';
            const color = a.type === 'WARNING' ? '#f59e0b' : '#0284c7';
            html += `
                <div style="display:flex;gap:8px;padding:6px 0;border-bottom:1px solid #f1f5f9;font-size:0.8rem;">
                    <i class="fa-solid ${icon}" style="color:${color};margin-top:2px;flex-shrink:0"></i>
                    <div><strong style="color:#334155">[${a.room}]</strong> ${a.message}</div>
                </div>`;
        }
        html += `</div>`;
    } else {
        html += `<div style="text-align:center;padding:20px;color:#10b981;font-weight:600;"><i class="fa-solid fa-shield-check"></i> All rooms verified - Zero anomalies detected</div>`;
    }

    panel.innerHTML = html;
    panel.style.display = 'block';
}

// ========== CANVAS INTERACTIONS ==========
function handleCanvasZoom(e) {
    e.preventDefault();
    const delta = e.deltaY > 0 ? 0.9 : 1.1;
    canvasScale = Math.max(0.3, Math.min(canvasScale * delta, 4.0));
    renderBlueprintCanvas();
}

function handleCanvasMouseDown(e) {
    isDragging = true;
    dragStartX = e.clientX - canvasPanX;
    dragStartY = e.clientY - canvasPanY;
    blueprintCanvas.style.cursor = 'grabbing';
}

function handleCanvasMouseMove(e) {
    if (isDragging) {
        canvasPanX = e.clientX - dragStartX;
        canvasPanY = e.clientY - dragStartY;
        renderBlueprintCanvas();
    }
}

function handleCanvasMouseUp() {
    isDragging = false;
    if (blueprintCanvas) blueprintCanvas.style.cursor = 'crosshair';
}

function handleCanvasClick(e) {
    if (!blueprintCanvas) return;
    const rect = blueprintCanvas.getBoundingClientRect();
    const mx = (e.clientX - rect.left - canvasPanX) / canvasScale;
    const my = (e.clientY - rect.top - canvasPanY) / canvasScale;

    let found = null;
    for (const poly of polygonsData) {
        if (mx >= poly.x && mx <= poly.x + poly.width && my >= poly.y && my <= poly.y + poly.height) {
            found = poly;
            break;
        }
    }

    if (found) {
        highlightedPolyId = found.id;
        renderBlueprintCanvas();
        // Scroll to matching room row in takeoff table
        const rows = document.querySelectorAll('#takeoffTableBody tr.room-header-row');
        for (const row of rows) {
            const txt = row.textContent || '';
            if (txt.includes(found.room_name)) {
                row.scrollIntoView({ behavior: 'smooth', block: 'center' });
                row.style.transition = 'background 0.3s';
                row.style.background = '#dbeafe';
                setTimeout(() => { row.style.background = ''; }, 1500);
                break;
            }
        }
    } else {
        highlightedPolyId = null;
        renderBlueprintCanvas();
    }
}

// ========== TWO-WAY SYNC: Table -> Canvas ==========
function highlightRoomOnCanvas(roomName) {
    const poly = polygonsData.find(p => p.room_name === roomName);
    if (poly) {
        highlightedPolyId = poly.id;
        // Center canvas on the polygon
        if (blueprintCanvas) {
            const centerX = poly.x + poly.width / 2;
            const centerY = poly.y + poly.height / 2;
            canvasPanX = blueprintCanvas.width / 2 - centerX * canvasScale;
            canvasPanY = blueprintCanvas.height / 2 - centerY * canvasScale;
        }
        renderBlueprintCanvas();
    }
}

// ========== SETTINGS PANEL ==========
async function loadTradeSettings() {
    try {
        const res = await fetch('/api/settings');
        const settings = await res.json();
        // Populate settings form fields
        const wasteInput = document.getElementById('settingsTileWaste');
        if (wasteInput) wasteInput.value = settings.trade_rules.standard_tile_waste_pct;
        const lgWasteInput = document.getElementById('settingsLargeFormatWaste');
        if (lgWasteInput) lgWasteInput.value = settings.trade_rules.large_format_waste_pct;
        const wpBaseInput = document.getElementById('settingsWpBaseHeight');
        if (wpBaseInput) wpBaseInput.value = settings.trade_rules.waterproof_base_height_inches;
        const ceilingInput = document.getElementById('settingsDefaultCeiling');
        if (ceilingInput) ceilingInput.value = settings.trade_rules.default_ceiling_height_ft;
        const companyInput = document.getElementById('settingsCompanyName');
        if (companyInput) companyInput.value = settings.company.name;
        const licenseInput = document.getElementById('settingsLicenseNo');
        if (licenseInput) licenseInput.value = settings.company.license_no;
    } catch (e) {
        console.error('Settings load error:', e);
    }
}

async function saveTradeSettings() {
    try {
        const payload = {
            trade_rules: {
                standard_tile_waste_pct: parseFloat(document.getElementById('settingsTileWaste')?.value || 10),
                large_format_waste_pct: parseFloat(document.getElementById('settingsLargeFormatWaste')?.value || 15),
                waterproof_base_height_inches: parseFloat(document.getElementById('settingsWpBaseHeight')?.value || 6),
                default_ceiling_height_ft: parseFloat(document.getElementById('settingsDefaultCeiling')?.value || 9)
            },
            company: {
                name: document.getElementById('settingsCompanyName')?.value || '',
                license_no: document.getElementById('settingsLicenseNo')?.value || ''
            }
        };
        await fetch('/api/settings', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
        if (typeof showToast === 'function') showToast('Trade settings saved successfully!');
    } catch (e) {
        console.error('Settings save error:', e);
    }
}

// ========== AUTO INIT ==========
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(initBlueprintViewer, 500);
});
