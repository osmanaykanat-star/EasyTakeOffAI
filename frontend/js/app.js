// EasyTakeOffAI Client Application Logic
let projectData = null;
let selectedTrades = ["Tile & Stone"];

const AVAILABLE_TRADES = [
    { id: "Tile & Stone", name: "Tile, Stone & Tops", desc: "Ceramic & porcelain tiles, engineered stone & granite countertops, splash, waterproofing, mud-set & marble saddles.", icon: "fa-cubes", color: "#2563eb", bg: "#eff6ff", border: "#bfdbfe" },
    { id: "Flooring & Wood", name: "Hardwood & Flooring", desc: "Hardwood floor refinishing, sanding & polyurethane, LVT vinyl planks, carpet tiles & rubber base.", icon: "fa-layer-group", color: "#d97706", bg: "#fffbeb", border: "#fde68a" },
    { id: "Painting", name: "Painting & Finishes", desc: "Full interior apartment & facility painting, primer, eggshell latex, wall prep, doors & trim.", icon: "fa-paint-roller", color: "#059669", bg: "#ecfdf5", border: "#a7f3d0" },
    { id: "Millwork & Carpentry", name: "Cabinets & Millwork", desc: "Kitchen cabinet refinishing & replacement doors, bathroom vanity millwork, door hardware & handles.", icon: "fa-hammer", color: "#7c3aed", bg: "#f5f3ff", border: "#ddd6fe" },
    { id: "Plumbing", name: "Plumbing & Fixtures", desc: "Stainless steel undermount kitchen sinks, bathroom toilets, faucets, trim & Americast bathtubs.", icon: "fa-faucet", color: "#0284c7", bg: "#f0f9ff", border: "#bae6fd" },
    { id: "HVAC & Mechanical", name: "HVAC & Mechanical", desc: "PTAC unit replacements, heating equipment, gas line capping & air distribution diffusers.", icon: "fa-fan", color: "#0891b2", bg: "#ecfeff", border: "#a5f3fc" },
    { id: "Electrical", name: "Electrical & Lighting", desc: "LED recessed lighting, troffers, lighting fixtures, switching, power & EV chargers.", icon: "fa-bolt", color: "#ca8a04", bg: "#fefce8", border: "#fef08a" },
    { id: "Exterior & Pavers", name: "Exterior, Roof & Pavers", desc: "Terrace & roof concrete pavers deep powerwashing, parapet stone coping repairs & joint sealant.", icon: "fa-building", color: "#475569", bg: "#f8fafc", border: "#cbd5e1" },
    { id: "Demolition", name: "Demolition & Prep", desc: "Selective interior demolition, partition walls, ceiling soffit removal, island demolition & disposal.", icon: "fa-trowel", color: "#dc2626", bg: "#fef2f2", border: "#fecaca" }
];

document.addEventListener("DOMContentLoaded", () => {
    setupDragAndDrop();
    loadProject();
    checkUserProfile();
});

// Setup drag and drop events on window and dropzone
function setupDragAndDrop() {
    ["dragenter", "dragover", "dragleave", "drop"].forEach(eventName => {
        window.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    const dropzone = document.getElementById("dropzone");
    if (!dropzone) return;

    ["dragenter", "dragover"].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            preventDefaults(e);
            dropzone.classList.add("drag-hover");
        }, false);
    });

    ["dragleave", "drop"].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            preventDefaults(e);
            dropzone.classList.remove("drag-hover");
        }, false);
    });

    dropzone.addEventListener("drop", (e) => {
        preventDefaults(e);
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files && files.length > 0) {
            uploadFile(files[0]);
        }
    }, false);
}

// Load current project from backend
async function loadProject() {
    try {
        const q = selectedTrades.length > 0 ? `?trades=${encodeURIComponent(selectedTrades.join(','))}` : '';
        const res = await fetch(`/api/project${q}`, { cache: "no-store", headers: { "Cache-Control": "no-cache", "Pragma": "no-cache" } });
        projectData = await res.json();
        if (projectData.selected_trades && projectData.selected_trades.length > 0) {
            selectedTrades = projectData.selected_trades;
        }
        renderProject();
        if (typeof loadPolygonsAndAudit === 'function') {
            loadPolygonsAndAudit();
        }
    } catch (e) {
        showToast("Error loading project: " + e.message);
    }
}

// Clear / Reset the Room Takeoff Generator input fields
function resetRoomCalculator() {
    document.getElementById("calcFloor").value = "";
    document.getElementById("calcRoomName").value = "";
    document.getElementById("calcLength").value = "";
    document.getElementById("calcWidth").value = "";
    document.getElementById("calcTileHt").value = "";
    document.getElementById("calcFloorTile").value = "";
    document.getElementById("calcWallTiles").value = "";
    document.getElementById("calcBullnose").value = "";
    document.getElementById("calcWaterproof").checked = true;
    document.getElementById("calcMudset").checked = true;
    document.getElementById("calcEpoxy").checked = false;
    document.getElementById("calcSaddle").checked = false;
}

// Clear Entire Project Memory
async function clearCurrentProject() {
    if (!confirm("Are you sure you want to clear current takeoff and start a fresh project?")) return;
    try {
        const res = await fetch("/api/project/clear", { method: "POST", headers: { "Cache-Control": "no-cache" } });
        const data = await res.json();
        projectData = data.project;

        const resEl = document.getElementById("analysisResults");
        if (resEl) resEl.style.display = "none";
        const statEl = document.getElementById("uploadStatus");
        if (statEl) statEl.style.display = "none";

        resetRoomCalculator();
        renderProject();
        if (typeof loadPolygonsAndAudit === 'function') {
            loadPolygonsAndAudit();
        }
        showToast("🧹 Project memory cleared! Ready for new drawing upload.");
    } catch (e) {
        showToast("Error clearing project: " + e.message);
    }
}

// Create New Project (Reset)
async function createNewProjectPrompt() {
    const projName = prompt("Start New Project\n\nPlease enter the project name:", "New Takeoff Project");
    if (projName === null) return;

    try {
        const res = await fetch(`/api/project/new?name=${encodeURIComponent(projName.trim() || "New Takeoff Project")}`, {
            method: "POST",
            headers: { "Cache-Control": "no-cache" }
        });
        const data = await res.json();
        projectData = data.project;

        const resEl = document.getElementById("analysisResults");
        if (resEl) resEl.style.display = "none";
        const statEl = document.getElementById("uploadStatus");
        if (statEl) statEl.style.display = "none";

        resetRoomCalculator();
        renderProject();
        if (typeof loadPolygonsAndAudit === 'function') {
            loadPolygonsAndAudit();
        }
        showToast("✨ Started fresh project: " + projectData.project_name);
    } catch (e) {
        showToast("Error creating project: " + e.message);
    }
}

// Load Selected Trained Benchmark Project
async function loadSampleProject(sampleId) {
    if (!sampleId) return;
    try {
        const res = await fetch(`/api/project/load_sample?sample_id=${encodeURIComponent(sampleId)}`, {
            method: "POST",
            headers: { "Cache-Control": "no-cache" }
        });
        const data = await res.json();
        projectData = data.project;
        if (projectData.selected_trades && projectData.selected_trades.length > 0) {
            selectedTrades = projectData.selected_trades;
        }
        renderProject();
        if (typeof loadPolygonsAndAudit === 'function') {
            loadPolygonsAndAudit();
        }
        showToast("📚 Loaded benchmark training: " + (projectData.project_name || sampleId));
    } catch (e) {
        showToast("Error loading benchmark: " + e.message);
    }
}

function categorizeTakeoffItem(item) {
    const ftUpper = (item.finish_type || "").toUpperCase();
    const mtUpper = (item.material_type || "").toUpperCase();
    const symUpper = (item.symbol || "").toUpperCase();
    const unitUpper = (item.unit || "").toUpperCase();

    // 1. Waterproofing & Floor Preparation
    if (
        symUpper.includes("WATERPROOF") || 
        symUpper.includes("MUD-SET") || 
        symUpper.includes("MUDSET") || 
        symUpper.includes("SOUNDPROOF") ||
        mtUpper.includes("WATERPROOF") ||
        mtUpper.includes("MUD-SET") ||
        mtUpper.includes("MUDSET") ||
        mtUpper.includes("PREP") ||
        ftUpper.includes("PREPARATION")
    ) {
        return "PREP";
    }

    // 2. Doorway Transition Saddles / Thresholds
    if (
        symUpper.includes("SADDLE") || 
        (symUpper === "SS" && unitUpper === "PCS") ||
        ftUpper.includes("SADDLE") || 
        mtUpper.includes("SADDLE") ||
        unitUpper === "PCS"
    ) {
        return "SADDLE";
    }

    // 3. Baseboards / Cove Base
    if (
        symUpper.includes("BASE") || 
        symUpper.startsWith("B-") || 
        symUpper.startsWith("WB-") || 
        symUpper.startsWith("WBT-") || 
        ftUpper.includes("BASE") || 
        mtUpper.includes("BASE") || 
        unitUpper === "LN FT" || 
        unitUpper === "LF"
    ) {
        return "BASE";
    }

    // 4. Metal Edge Trim
    if (
        symUpper.includes("TRIM") || 
        symUpper === "MS" || 
        ftUpper.includes("TRIM") || 
        mtUpper.includes("TRIM")
    ) {
        return "TRIM";
    }

    // 5. Floor Tile & Stone
    if (
        unitUpper.includes("SQ") && (
            ftUpper.includes("FLOOR") || 
            ftUpper.includes("LANDING") || 
            ftUpper.includes("STEP") || 
            ftUpper.includes("RISER") || 
            ftUpper.includes("PAVER")
        )
    ) {
        return "FLOOR";
    }

    // 6. Wall Tile & Ceramic / Mosaic Walls (Excluding Solid Surface / Quartz Countertops)
    if (
        unitUpper.includes("SQ") && (
            ftUpper.includes("WALL") || 
            ftUpper.includes("SPLASH") || 
            ftUpper.includes("BACKSPLASH") || 
            ftUpper.includes("NICHE") || 
            ftUpper.includes("SURROUND") || 
            ftUpper.includes("TUB TOP") || 
            ftUpper.includes("TUB INSIDE") || 
            ftUpper.includes("CASING") ||
            ftUpper.includes("WAINSCOT") ||
            ftUpper.includes("CEILING") ||
            ftUpper.includes("LEDGER") ||
            symUpper.startsWith("WT-") ||
            symUpper.startsWith("WL-") ||
            symUpper.startsWith("BS-")
        ) && !ftUpper.includes("COUNTERTOP") && !ftUpper.includes("VANITY")
    ) {
        return "WALL";
    }

    // 7. Countertops / Vanities / Slabs / Solid Surface / Tops
    if (
        unitUpper.includes("SQ") && (
            ftUpper.includes("COUNTERTOP") || 
            ftUpper.includes("VANITY") || 
            ftUpper.includes("ISLAND") || 
            ftUpper.includes("DESK") || 
            ftUpper.includes("TOP") || 
            ftUpper.includes("APRON") || 
            ftUpper.includes("SURROUND") || 
            ftUpper.includes("MILLWORK") || 
            symUpper.startsWith("SS-") || 
            symUpper.startsWith("ST-") || 
            symUpper.startsWith("QZ-") || 
            symUpper.startsWith("SC-") || 
            mtUpper.includes("SOLID SURFACE") || 
            mtUpper.includes("QUARTZ") || 
            mtUpper.includes("STONE") || 
            mtUpper.includes("MARBLE") ||
            mtUpper.includes("SLAB")
        )
    ) {
        return "COUNTERTOP";
    }

    return "OTHER";
}

// Render project information, tables and stats
function renderProject() {
    if (!projectData) return;

    renderTradeDropdown();
    renderTradeModalGrid();

    document.getElementById("projectName").value = projectData.project_name || "";
    document.getElementById("clientName").value = projectData.client_name || "";
    document.getElementById("clientCompany").value = projectData.client_company || "";
    document.getElementById("estimatorName").value = projectData.estimator_name || "";
    document.getElementById("projectDate").value = projectData.date_str || new Date().toLocaleDateString();
    document.getElementById("currentTradeName").innerText = projectData.trade_category || (selectedTrades.join(", "));

    const tbody = document.getElementById("takeoffTableBody");
    tbody.innerHTML = "";

    let totalRooms = (projectData.rooms || []).length;
    let totalFloorSqft = 0;
    let totalWallSqft = 0;
    let totalTopsSqft = 0;
    let totalPrepSqft = 0;
    let totalBaseLnft = 0;
    let totalSaddlesPcs = 0;
    let baseBidTotal = 0;

    const symbolTotals = {};

    if (totalRooms === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="11" class="empty-state-cell">
                    <div class="empty-state">
                        <i class="fa-solid fa-compass-drafting empty-icon"></i>
                        <h4>No Rooms Added Yet</h4>
                        <p>Drag & drop your <strong>Architectural PDF Drawings or ZIP Archives</strong> into the upload box on the left (for automated AI takeoff) or use the <strong>"Room Takeoff Generator"</strong> to calculate and add rooms manually.</p>
                    </div>
                </td>
            </tr>
        `;
        document.getElementById("detailedTotalsCard").style.display = "none";
    } else {
        document.getElementById("detailedTotalsCard").style.display = "block";
        const floors = {};
        projectData.rooms.forEach((room, rIdx) => {
            if (!floors[room.floor_name]) floors[room.floor_name] = [];
            floors[room.floor_name].push({ room, rIdx });
        });

        for (const floorName in floors) {
            const floorTr = document.createElement("tr");
            floorTr.className = "floor-row";
            floorTr.innerHTML = `<td colspan="11"><i class="fa-solid fa-layer-group"></i> ${floorName}</td>`;
            tbody.appendChild(floorTr);

            floors[floorName].forEach(({ room, rIdx }) => {
                let roomTotal = 0;
                room.items.forEach(item => {
                    const lineBid = item.total_bid || (item.quantity * (item.material_price + item.labor_price));
                    roomTotal += lineBid;

                    if (!symbolTotals[item.symbol]) {
                        symbolTotals[item.symbol] = {
                            symbol: item.symbol,
                            finish_type: item.finish_type,
                            material_type: item.material_type,
                            work_type: item.work_type,
                            unit: item.unit,
                            totalQty: 0,
                            material_price: item.material_price,
                            labor_price: item.labor_price,
                            totalAmount: 0
                        };
                    }
                    symbolTotals[item.symbol].totalQty += item.quantity;
                    symbolTotals[item.symbol].totalAmount += lineBid;

                    const cat = categorizeTakeoffItem(item);
                    if (cat === "FLOOR") totalFloorSqft += item.quantity;
                    else if (cat === "WALL") totalWallSqft += item.quantity;
                    else if (cat === "COUNTERTOP") totalTopsSqft += item.quantity;
                    else if (cat === "PREP") totalPrepSqft += item.quantity;
                    else if (cat === "BASE") totalBaseLnft += item.quantity;
                    else if (cat === "SADDLE") totalSaddlesPcs += item.quantity;
                });
                baseBidTotal += roomTotal;

                const roomTr = document.createElement("tr");
                roomTr.className = "room-row room-header-row";
                roomTr.style.cursor = "pointer";
                roomTr.title = "Click to locate room on blueprint canvas";
                roomTr.onclick = () => {
                    if (typeof highlightRoomOnCanvas === "function") {
                        highlightRoomOnCanvas(room.room_name);
                        switchTab("blueprintTab");
                    }
                };
                roomTr.innerHTML = `
                    <td colspan="9">
                        <strong><i class="fa-solid fa-door-open"></i> ${room.room_name}</strong> (${room.items.length} items)
                        <span class="badge" style="margin-left: 10px; background: rgba(56, 189, 248, 0.15); color: #38bdf8; font-size: 0.72rem; cursor: pointer;">
                            <i class="fa-solid fa-crosshairs"></i> Locate on Blueprint
                        </span>
                    </td>
                    <td class="text-right"><strong>$${roomTotal.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</strong></td>
                    <td class="text-center"><button class="del-btn" title="Delete Room" onclick="event.stopPropagation(); deleteRoom(${rIdx})"><i class="fa-solid fa-trash"></i></button></td>
                `;
                tbody.appendChild(roomTr);

                room.items.forEach((item, itemIdx) => {
                    const itemTotal = item.total_bid || (item.quantity * (item.material_price + item.labor_price));
                    const itemTr = document.createElement("tr");
                    const workBadge = item.work_type === "IO" ? '<span class="badge" style="background:#0284c7;color:#fff;">IO (Install)</span>' : '<span class="badge">S&I</span>';
                    itemTr.innerHTML = `
                        <td style="padding-left: 28px; color: #94a3b8;"><i class="fa-solid fa-arrow-turn-down-right"></i></td>
                        <td><strong>${item.symbol}</strong></td>
                        <td>${item.finish_type}</td>
                        <td>${item.material_type}</td>
                        <td>${workBadge}</td>
                        <td class="text-right"><strong>${item.quantity.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1})}</strong></td>
                        <td>${item.unit}</td>
                        <td class="text-right">
                            <input type="number" step="0.01" class="table-input" value="${item.material_price}" onchange="updateItemPrice(${rIdx}, ${itemIdx}, 'material_price', this.value)">
                        </td>
                        <td class="text-right">
                            <input type="number" step="0.01" class="table-input" value="${item.labor_price}" onchange="updateItemPrice(${rIdx}, ${itemIdx}, 'labor_price', this.value)">
                        </td>
                        <td class="text-right"><strong>$${itemTotal.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</strong></td>
                        <td></td>
                    `;
                    tbody.appendChild(itemTr);
                });
            });
        }
    }

    document.getElementById("statTotalRooms").innerText = totalRooms;
    document.getElementById("statFloorTileSqft").innerText = totalFloorSqft.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1});
    document.getElementById("statWallTileSqft").innerText = totalWallSqft.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1});
    if (document.getElementById("statTopsSqft")) {
        document.getElementById("statTopsSqft").innerText = totalTopsSqft.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1});
    }
    document.getElementById("statPrepSqft").innerText = totalPrepSqft.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1});
    document.getElementById("statBaseBid").innerText = "$" + baseBidTotal.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});

    renderDetailedBreakdown(symbolTotals, totalRooms, totalFloorSqft, totalWallSqft, totalTopsSqft, baseBidTotal);
    renderPriceManager(symbolTotals);
    renderMaterialSpecs(symbolTotals);
}

// Render Detailed Totals Breakdown Grid
function renderDetailedBreakdown(symbolTotals, totalRooms, totalFloorSqft, totalWallSqft, totalTopsSqft, baseBidTotal) {
    const grid = document.getElementById("breakdownGrid");
    if (!grid) return;
    grid.innerHTML = "";

    document.getElementById("totalScopeBadge").innerText = `${totalRooms} Rooms | ${totalFloorSqft.toFixed(1)} SF Floor | ${totalWallSqft.toFixed(1)} SF Wall | ${totalTopsSqft.toFixed(1)} SF Tops`;

    for (const sym in symbolTotals) {
        const item = symbolTotals[sym];
        const card = document.createElement("div");
        card.className = "breakdown-card";
        card.innerHTML = `
            <div class="breakdown-card-header">
                <span class="breakdown-symbol">${item.symbol}</span>
                <span class="badge ${item.work_type === 'IO' ? 'badge-info' : 'badge-active'}">${item.work_type}</span>
            </div>
            <div class="breakdown-qty">${item.totalQty.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1})} <span class="breakdown-unit">${item.unit}</span></div>
            <div class="breakdown-details">
                <span>${item.finish_type} - ${item.material_type}</span>
                <strong>$${item.totalAmount.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</strong>
            </div>
        `;
        grid.appendChild(card);
    }
}

function renderPriceManager(symbolTotals) {
    const tbody = document.getElementById("priceTableBody");
    tbody.innerHTML = "";

    if (Object.keys(symbolTotals).length === 0) {
        tbody.innerHTML = `<tr><td colspan="6" class="text-center" style="padding: 24px; color: #94a3b8;">Materials and quantities will appear here once rooms are added.</td></tr>`;
        return;
    }

    for (const sym in symbolTotals) {
        const item = symbolTotals[sym];
        const subtotal = item.totalQty * (item.material_price + item.labor_price);
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td><strong>${item.symbol}</strong></td>
            <td>${item.unit}</td>
            <td class="text-right"><strong>${item.totalQty.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1})}</strong></td>
            <td>
                <input type="number" step="0.01" class="table-input" id="bulk_mat_${item.symbol}" value="${item.material_price}">
            </td>
            <td>
                <input type="number" step="0.01" class="table-input" id="bulk_lab_${item.symbol}" value="${item.labor_price}">
            </td>
            <td class="text-right"><strong>$${subtotal.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}</strong></td>
        `;
        tbody.appendChild(tr);
    }
}

// Render Material Specs with Editable Budget Prices, Descriptions & Notes
function renderMaterialSpecs(symbolTotals) {
    const tbody = document.getElementById("specsTableBody");
    tbody.innerHTML = "";

    const specs = projectData.material_specs || {};
    for (const sym in specs) {
        const s = specs[sym];
        const totalQty = symbolTotals && symbolTotals[sym] ? symbolTotals[sym].totalQty : 0;
        const budgetVal = s.budget_price !== null && s.budget_price !== undefined ? s.budget_price : "";

        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td><strong>${s.symbol}</strong></td>
            <td>
                <input type="text" class="table-input w-100" id="spec_desc_${s.symbol}" value="${s.description || ''}" placeholder="Material specification description...">
            </td>
            <td>${s.unit || "SQ FT"}</td>
            <td class="text-right">
                <input type="number" step="0.01" class="table-input text-right" id="spec_budget_${s.symbol}" value="${budgetVal}" placeholder="0.00" style="width: 110px;">
            </td>
            <td class="text-right">
                <strong>${totalQty > 0 ? totalQty.toLocaleString(undefined, {minimumFractionDigits: 1, maximumFractionDigits: 1}) + ' ' + (s.unit || 'SQ FT') : '-'}</strong>
            </td>
            <td>
                <input type="text" class="table-input w-100" id="spec_notes_${s.symbol}" value="${s.notes || ''}" placeholder="Submittal / spec notes...">
            </td>
        `;
        tbody.appendChild(tr);
    }
}

async function saveMaterialSpecs() {
    const specsPayload = {};
    const specs = projectData.material_specs || {};

    for (const sym in specs) {
        const descEl = document.getElementById(`spec_desc_${sym}`);
        const budgetEl = document.getElementById(`spec_budget_${sym}`);
        const notesEl = document.getElementById(`spec_notes_${sym}`);

        if (descEl && budgetEl && notesEl) {
            const bVal = parseFloat(budgetEl.value);
            specsPayload[sym] = {
                description: descEl.value.trim(),
                budget_price: isNaN(bVal) ? null : bVal,
                notes: notesEl.value.trim()
            };
        }
    }

    try {
        const res = await fetch("/api/project/update_specs", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ specs: specsPayload })
        });
        const data = await res.json();
        projectData = data.project;
        if (projectData && projectData.trade_category) { selectedTrades = [projectData.trade_category]; }
        renderProject();
        showToast("✨ Material specifications & budget prices saved!");
    } catch (e) {
        showToast("Error saving specs: " + e.message);
    }
}

async function uploadFile(file) {
    const fname = file.name.toLowerCase();
    if (!fname.endsWith(".pdf") && !fname.endsWith(".zip") && !fname.endsWith(".xlsx") && !fname.endsWith(".xls")) {
        showToast("Please select or drop a valid PDF drawing, ZIP archive, or Excel proposal (.xlsx).");
        return;
    }

    const statusEl = document.getElementById("uploadStatus");
    const resultsEl = document.getElementById("analysisResults");
    if (statusEl) {
        statusEl.style.display = "block";
        statusEl.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Processing & Auto-Calculating Takeoff for ${file.name}...`;
    }
    if (resultsEl) resultsEl.style.display = "none";

    const formData = new FormData();
    formData.append("file", file);

    try {
        const res = await fetch("/api/upload_drawing", {
            method: "POST",
            body: formData,
            headers: { "Cache-Control": "no-cache" }
        });
        const data = await res.json();
        if (statusEl) statusEl.style.display = "none";
        if (resultsEl) resultsEl.style.display = "flex";

        projectData = data.project;
        if (projectData && projectData.trade_category) { selectedTrades = [projectData.trade_category]; }
        renderProject();
        if (typeof loadPolygonsAndAudit === 'function') {
            loadPolygonsAndAudit();
        }

        const badgeType = data.is_zip ? `<span class="badge badge-active"><i class="fa-solid fa-file-zipper"></i> ZIP (${data.pdf_count} PDFs)</span>` : "";
        if (resultsEl) {
            resultsEl.innerHTML = `
                ${badgeType}
                <span class="badge badge-active"><i class="fa-solid fa-file"></i> ${data.total_pages} Pages</span>
                <span class="badge badge-active"><i class="fa-solid fa-bath"></i> ${data.extracted_rooms_count} Rooms Extracted</span>
                <span class="badge badge-active"><i class="fa-solid fa-check-double"></i> Auto-Calculated!</span>
            `;
        }
        showToast(`🎉 Auto-Takeoff Completed! ${data.extracted_rooms_count} rooms & quantities calculated.`);
    } catch (e) {
        if (statusEl) statusEl.style.display = "none";
        showToast("Drawing processing error: " + e.message);
    }
}

function handleFileUpload(event) {
    const file = event.target.files[0];
    if (file) uploadFile(file);
}

async function applyBulkPrices() {
    const prices = {};
    const symbolTotals = {};
    (projectData.rooms || []).forEach(r => {
        r.items.forEach(i => { symbolTotals[i.symbol] = true; });
    });

    for (const sym in symbolTotals) {
        const matInput = document.getElementById(`bulk_mat_${sym}`);
        const labInput = document.getElementById(`bulk_lab_${sym}`);
        if (matInput && labInput) {
            prices[sym] = {
                material_price: parseFloat(matInput.value) || 0.0,
                labor_price: parseFloat(labInput.value) || 0.0
            };
        }
    }

    try {
        const res = await fetch("/api/project/update_prices", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prices })
        });
        const data = await res.json();
        projectData = data.project;
        if (projectData && projectData.trade_category) { selectedTrades = [projectData.trade_category]; }
        renderProject();
        showToast("Unit prices updated successfully!");
    } catch (e) {
        showToast("Error updating prices: " + e.message);
    }
}

function updateItemPrice(rIdx, itemIdx, field, val) {
    if (projectData && projectData.rooms[rIdx] && projectData.rooms[rIdx].items[itemIdx]) {
        projectData.rooms[rIdx].items[itemIdx][field] = parseFloat(val) || 0.0;
        renderProject();
    }
}

async function generateAndAddRoom() {
    const floor_name = document.getElementById("calcFloor").value.trim() || "1ST FLOOR";
    const room_name = document.getElementById("calcRoomName").value.trim() || "NEW RESTROOM";
    const length_ft = parseFloat(document.getElementById("calcLength").value) || 10.0;
    const width_ft = parseFloat(document.getElementById("calcWidth").value) || 8.0;
    const wall_tile_height_ft = parseFloat(document.getElementById("calcTileHt").value) || 9.0;
    
    const floor_tile_symbol = document.getElementById("calcFloorTile").value.trim() || "TL-01";
    const wall_tiles_raw = document.getElementById("calcWallTiles").value.trim();
    const wall_tile_symbols = wall_tiles_raw ? wall_tiles_raw.split(",").map(s => s.trim()).filter(Boolean) : ["TL-3.1", "TL-3.2"];
    const bullnose_symbol = document.getElementById("calcBullnose").value.trim() || "TL-3/BULLNOSE";

    const include_waterproofing = document.getElementById("calcWaterproof").checked;
    const include_mudset = document.getElementById("calcMudset").checked;
    const include_epoxy = document.getElementById("calcEpoxy").checked;
    const include_saddle = document.getElementById("calcSaddle").checked;

    const payload = {
        room_name,
        floor_name,
        length_ft,
        width_ft,
        ceiling_height_ft: 9.0,
        wall_tile_height_ft,
        door_count: 1,
        floor_tile_symbol,
        wall_tile_symbols,
        wall_tile_percentages: wall_tile_symbols.map(() => 1.0 / wall_tile_symbols.length),
        bullnose_symbol,
        include_waterproofing,
        include_mudset,
        include_epoxy,
        include_saddle,
        saddle_type: "STONE",
        work_type: "IO"
    };

    try {
        const calcRes = await fetch("/api/calculate_room", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const calculatedRoom = await calcRes.json();

        const addRes = await fetch("/api/project/add_room", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(calculatedRoom)
        });
        const data = await addRes.json();
        projectData = data.project;
        
        document.getElementById("calcRoomName").value = "";
        document.getElementById("calcLength").value = "";
        document.getElementById("calcWidth").value = "";
        
        renderProject();
        showToast(`Calculated & added ${room_name}!`);
    } catch (e) {
        showToast("Error adding room: " + e.message);
    }
}

async function deleteRoom(rIdx) {
    if (!confirm("Are you sure you want to delete this room?")) return;
    try {
        const res = await fetch(`/api/project/rooms/${rIdx}`, { method: "DELETE" });
        const data = await res.json();
        projectData = data.project;
        if (projectData && projectData.trade_category) { selectedTrades = [projectData.trade_category]; }
        renderProject();
        showToast("Room deleted.");
    } catch (e) {
        showToast("Error deleting room: " + e.message);
    }
}

async function saveProjectDetails() {
    const payload = {
        project_name: document.getElementById("projectName").value.trim(),
        client_name: document.getElementById("clientName").value.trim(),
        client_company: document.getElementById("clientCompany").value.trim(),
        estimator_name: document.getElementById("estimatorName").value.trim()
    };
    try {
        const res = await fetch("/api/project", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        projectData = data.project;
        showToast("Project details saved!");
    } catch (e) {
        showToast("Error saving details: " + e.message);
    }
}

async function loadSampleProject(sampleId) {
    try {
        const res = await fetch(`/api/project/load_sample?sample_id=${sampleId}`, { method: "POST" });
        const data = await res.json();
        projectData = data.project;
        if (projectData && projectData.trade_category) { selectedTrades = [projectData.trade_category]; }
        renderProject();
        showToast(`Loaded ${sampleId.toUpperCase()} sample project.`);
    } catch (e) {
        showToast("Error loading sample: " + e.message);
    }
}

function toggleTradeDropdown(e) {
    if (e) e.stopPropagation();
    const menu = document.getElementById("tradeDropdownMenu");
    if (!menu) return;
    const isVisible = menu.style.display === "block";
    menu.style.display = isVisible ? "none" : "block";
    if (!isVisible) {
        renderTradeDropdown();
    }
}

document.addEventListener("click", (e) => {
    const container = document.querySelector(".dropdown-trade-container");
    const menu = document.getElementById("tradeDropdownMenu");
    if (container && menu && !container.contains(e.target)) {
        menu.style.display = "none";
    }
});

function renderTradeDropdown() {
    const countBadge = document.getElementById("tradeCountBadge");
    if (countBadge) {
        countBadge.innerText = selectedTrades.length;
    }

    const tradeNameEl = document.getElementById("currentTradeName");
    if (tradeNameEl) {
        if (selectedTrades.length === 1) {
            tradeNameEl.innerText = selectedTrades[0];
        } else if (selectedTrades.length === AVAILABLE_TRADES.length) {
            tradeNameEl.innerText = "All Trades";
        } else {
            tradeNameEl.innerText = `${selectedTrades[0]} +${selectedTrades.length - 1}`;
        }
    }

    const list = document.getElementById("tradeDropdownList");
    if (!list) return;
    list.innerHTML = "";

    AVAILABLE_TRADES.forEach(t => {
        const isSelected = selectedTrades.some(st => st.toLowerCase().replace(/[^a-z]/g, '') === t.id.toLowerCase().replace(/[^a-z]/g, ''));
        const item = document.createElement("div");
        item.className = `trade-dropdown-item ${isSelected ? 'active' : ''}`;
        item.innerHTML = `
            <div class="trade-dropdown-item-left">
                <div class="trade-dropdown-item-icon" style="background: ${isSelected ? t.color : '#334155'}; color: #ffffff;">
                    <i class="fa-solid ${t.icon}"></i>
                </div>
                <span>${t.name}</span>
            </div>
            <i class="fa-solid ${isSelected ? 'fa-square-check' : 'fa-square'} trade-checkbox-custom" style="color: ${isSelected ? '#38bdf8' : '#64748b'}; font-size: 1.1rem;"></i>
        `;
        item.onclick = (e) => {
            e.stopPropagation();
            toggleTrade(t.id);
        };
        list.appendChild(item);
    });
}

function renderTradeModalGrid() {
    const grid = document.getElementById("modalTradeGrid");
    if (!grid) return;

    const countEl = document.getElementById("modalSelectedCount");
    if (countEl) {
        countEl.innerText = `${selectedTrades.length} of ${AVAILABLE_TRADES.length} Trades Active`;
    }

    grid.innerHTML = "";
    AVAILABLE_TRADES.forEach(t => {
        const isSelected = selectedTrades.some(st => st.toLowerCase().replace(/[^a-z]/g, '') === t.id.toLowerCase().replace(/[^a-z]/g, ''));
        const card = document.createElement("div");
        card.className = `trade-card ${isSelected ? 'active' : ''}`;
        card.style.cursor = "pointer";
        card.style.display = "flex";
        card.style.gap = "10px";
        card.style.padding = "10px 12px";
        card.style.borderRadius = "8px";
        card.style.border = isSelected ? "2px solid #2563eb" : "1px solid #334155";
        card.style.background = isSelected ? "rgba(37, 99, 235, 0.15)" : "#0f172a";
        card.style.transition = "all 0.15s ease";

        card.innerHTML = `
            <div style="font-size: 1.3rem; color: ${isSelected ? '#38bdf8' : '#64748b'}; padding-top: 2px;">
                <i class="fa-solid ${t.icon}"></i>
            </div>
            <div style="flex: 1;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                    <h4 style="font-size: 0.85rem; font-weight: 700; color: ${isSelected ? '#ffffff' : '#cbd5e1'}; margin: 0;">${t.name}</h4>
                    <i class="fa-solid ${isSelected ? 'fa-square-check' : 'fa-square'}" style="color: ${isSelected ? '#38bdf8' : '#64748b'}; font-size: 0.95rem;"></i>
                </div>
                <p style="font-size: 0.72rem; color: #94a3b8; margin: 0; line-height: 1.3;">${t.desc}</p>
            </div>
        `;

        card.onclick = () => toggleTrade(t.id);
        grid.appendChild(card);
    });
}

async function toggleTrade(tradeId) {
    const matchIdx = selectedTrades.findIndex(st => st.toLowerCase().replace(/[^a-z]/g, '') === tradeId.toLowerCase().replace(/[^a-z]/g, ''));
    if (matchIdx >= 0) {
        if (selectedTrades.length > 1) {
            selectedTrades.splice(matchIdx, 1);
        } else {
            showToast("En az bir trade seçili kalmalıdır.");
            return;
        }
    } else {
        selectedTrades.push(tradeId);
    }
    await applyTradesFilter();
}

async function selectTradePreset(preset) {
    if (preset === 'tile_only') {
        selectedTrades = ["Tile & Stone"];
    } else if (preset === 'all') {
        selectedTrades = AVAILABLE_TRADES.map(t => t.id);
    } else if (preset === 'clear') {
        selectedTrades = ["Tile & Stone"];
    }
    await applyTradesFilter();
}

async function applyTradesFilter() {
    try {
        const res = await fetch(`/api/project/set_trades`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ trades: selectedTrades })
        });
        const data = await res.json();
        projectData = data.project;
        if (projectData && projectData.trade_category) { selectedTrades = [projectData.trade_category]; }
        renderProject();
        showToast(`Trade güncellendi: ${selectedTrades.join(", ")}`);
    } catch (e) {
        showToast("Hata: " + e.message);
    }
}

function openProposalHtml() {
    const q = selectedTrades.length > 0 ? `?trades=${encodeURIComponent(selectedTrades.join(','))}` : '';
    window.open(`/api/export/html${q}`, '_blank');
}

function openSowHtml() {
    const q = selectedTrades.length > 0 ? `?trades=${encodeURIComponent(selectedTrades.join(','))}` : '';
    window.open(`/api/export/sow-html${q}`, '_blank');
}

function exportToExcel() {
    if (!projectData || !projectData.rooms || projectData.rooms.length === 0) {
        if (!confirm("Seçili trade'ler için mahal bulunmuyor. Yine de boş şablon indirmek ister misiniz?")) return;
    }
    const q = selectedTrades.length > 0 ? `?trades=${encodeURIComponent(selectedTrades.join(','))}` : '';
    window.location.href = `/api/export/excel${q}`;
    showToast(`Teklif Excel dosyası hazırlanıyor (${selectedTrades.join(', ')})...`);
}

function exportToSowExcel() {
    if (!projectData || !projectData.rooms || projectData.rooms.length === 0) {
        if (!confirm("Seçili trade'ler için mahal bulunmuyor. Yine de boş SOW indirmek ister misiniz?")) return;
    }
    const q = selectedTrades.length > 0 ? `?trades=${encodeURIComponent(selectedTrades.join(','))}` : '';
    window.location.href = `/api/export/sow-excel${q}`;
    showToast(`SOW Excel dosyası hazırlanıyor (${selectedTrades.join(', ')})...`);
}

function switchTab(tabId) {
    document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
    document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));
    
    const buttons = document.querySelectorAll(".tab-btn");
    buttons.forEach(b => {
        if (b.getAttribute("onclick") && b.getAttribute("onclick").includes(tabId)) {
            b.classList.add("active");
        }
    });

    const pane = document.getElementById(tabId);
    if (pane) pane.classList.add("active");

    if (tabId === 'blueprintTab' && typeof renderBlueprintCanvas === 'function') {
        if (typeof loadPolygonsAndAudit === 'function') {
            loadPolygonsAndAudit();
        } else {
            setTimeout(renderBlueprintCanvas, 100);
        }
    }
    if (tabId === 'settingsTab' && typeof loadTradeSettings === 'function') {
        loadTradeSettings();
    }
}

function openTradeModal() {
    document.getElementById("tradeModal").style.display = "flex";
    renderTradeModalGrid();
}
function closeTradeModal() {
    document.getElementById("tradeModal").style.display = "none";
}

function showToast(msg) {
    const t = document.getElementById("toast");
    t.innerText = msg;
    t.style.display = "block";
    setTimeout(() => { t.style.display = "none"; }, 3000);
}

// ============================================================
// USER & COMPANY REGISTRATION ONBOARDING LOGIC
// ============================================================
let userProfile = null;

async function checkUserProfile() {
    try {
        // 1. Check if PIN was previously authorized
        const pinAuth = localStorage.getItem("easyTakeOff_pinUnlocked");
        if (pinAuth === "true") {
            document.body.classList.remove("app-locked");
            const modal = document.getElementById("registrationModal");
            if (modal) modal.style.display = "none";
            
            const localProf = localStorage.getItem("easyTakeOff_userProfile");
            if (localProf) {
                try { applyUserProfile(JSON.parse(localProf)); } catch(e) {}
            }
            return;
        }

        // 2. Check if registered on server
        const res = await fetch("/api/user/profile", { cache: "no-store", headers: { "Cache-Control": "no-cache", "Pragma": "no-cache" } });
        if (res.ok) {
            const serverProf = await res.json();
            if (serverProf && serverProf.is_registered && serverProf.company_name) {
                userProfile = serverProf;
                localStorage.setItem("easyTakeOff_userProfile", JSON.stringify(serverProf));
                document.body.classList.remove("app-locked");
                const modal = document.getElementById("registrationModal");
                if (modal) modal.style.display = "none";
                applyUserProfile(userProfile);
                return;
            }
        }
        
        // Unregistered & Not PIN Unlocked -> show PIN access gate by default
        userProfile = null;
        document.body.classList.add("app-locked");
        clearRegistrationForm();
        openRegistrationModal(false);
        switchGateTab('pin');
    } catch (e) {
        console.warn("Could not check user profile:", e);
        userProfile = null;
        document.body.classList.add("app-locked");
        clearRegistrationForm();
        openRegistrationModal(false);
        switchGateTab('pin');
    }
}

function switchGateTab(tabName) {
    const pinTab = document.getElementById("tabPinBtn");
    const formTab = document.getElementById("tabFormBtn");
    const pinView = document.getElementById("gatePinView");
    const formView = document.getElementById("registrationForm");

    if (tabName === "pin") {
        if (pinTab) pinTab.classList.add("active");
        if (formTab) formTab.classList.remove("active");
        if (pinView) pinView.style.display = "block";
        if (formView) formView.style.display = "none";
        setTimeout(() => document.getElementById("accessPinInput")?.focus(), 50);
    } else {
        if (pinTab) pinTab.classList.remove("active");
        if (formTab) formTab.classList.add("active");
        if (pinView) pinView.style.display = "none";
        if (formView) formView.style.display = "block";
        setTimeout(() => document.getElementById("regCompanyName")?.focus(), 50);
    }
}

async function unlockWithPin() {
    const pinInput = document.getElementById("accessPinInput");
    const err = document.getElementById("pinErrorMsg");
    const pin = (pinInput?.value || "").trim();

    if (!pin) {
        if (err) { err.style.display = "block"; err.innerText = "Please enter a PIN code."; }
        return;
    }

    try {
        const res = await fetch("/api/auth/pin", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ pin: pin })
        });
        const data = await res.json();
        if (data && data.authenticated) {
            localStorage.setItem("easyTakeOff_pinUnlocked", "true");
            document.body.classList.remove("app-locked");
            const modal = document.getElementById("registrationModal");
            if (modal) modal.style.display = "none";
            if (err) err.style.display = "none";
            showToast("⚡ Application unlocked successfully via PIN!");
            return;
        }
    } catch (e) {
        console.warn("Server PIN check fallback:", e);
        if (pin === "3531") {
            localStorage.setItem("easyTakeOff_pinUnlocked", "true");
            document.body.classList.remove("app-locked");
            const modal = document.getElementById("registrationModal");
            if (modal) modal.style.display = "none";
            if (err) err.style.display = "none";
            showToast("⚡ Application unlocked successfully via PIN!");
            return;
        }
    }

    if (err) {
        err.style.display = "block";
        err.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Invalid PIN code. Please try again or fill the registration form.';
    }
    if (pinInput) {
        pinInput.value = "";
        pinInput.focus();
    }
}

function clearRegistrationForm() {
    if (document.getElementById("regCompanyName")) document.getElementById("regCompanyName").value = "";
    if (document.getElementById("regEstimatorName")) document.getElementById("regEstimatorName").value = "";
    if (document.getElementById("regEstimatorTitle")) document.getElementById("regEstimatorTitle").value = "Senior Estimator";
    if (document.getElementById("regAddress")) document.getElementById("regAddress").value = "";
    if (document.getElementById("regPhone")) document.getElementById("regPhone").value = "";
    if (document.getElementById("regEmail")) document.getElementById("regEmail").value = "";
    if (document.getElementById("regWebsite")) document.getElementById("regWebsite").value = "";
    if (document.getElementById("regTradeSpecialty")) document.getElementById("regTradeSpecialty").value = "Tile & Stone";
    if (document.getElementById("regLicenseNo")) document.getElementById("regLicenseNo").value = "";
}

function applyUserProfile(prof) {
    if (!prof) return;
    const navBtn = document.getElementById("navCompanyName");
    if (navBtn && prof.company_name) {
        navBtn.innerText = prof.company_name;
    }

    if (document.getElementById("regCompanyName")) document.getElementById("regCompanyName").value = prof.company_name || "";
    if (document.getElementById("regEstimatorName")) document.getElementById("regEstimatorName").value = prof.estimator_name || "";
    if (document.getElementById("regEstimatorTitle")) document.getElementById("regEstimatorTitle").value = prof.estimator_title || "Senior Estimator";
    if (document.getElementById("regAddress")) document.getElementById("regAddress").value = prof.address || "";
    if (document.getElementById("regPhone")) document.getElementById("regPhone").value = prof.phone || "";
    if (document.getElementById("regEmail")) document.getElementById("regEmail").value = prof.email || "";
    if (document.getElementById("regWebsite")) document.getElementById("regWebsite").value = prof.website || "";
    if (document.getElementById("regTradeSpecialty")) document.getElementById("regTradeSpecialty").value = prof.trade_specialty || "Tile & Stone";
    if (document.getElementById("regLicenseNo")) document.getElementById("regLicenseNo").value = prof.license_no || "";

    const estInput = document.getElementById("projEstimator");
    if (estInput && !estInput.value && prof.estimator_name) {
        estInput.value = prof.estimator_name;
    }
}

function openRegistrationModal(canClose = true) {
    const isRegistered = (userProfile && userProfile.is_registered && userProfile.company_name) || localStorage.getItem("easyTakeOff_pinUnlocked") === "true";
    const effectiveCanClose = canClose && isRegistered;

    const modal = document.getElementById("registrationModal");
    const closeBtn = document.getElementById("regCloseBtn");
    if (!modal) return;

    modal.style.display = "flex";
    if (closeBtn) {
        closeBtn.style.display = effectiveCanClose ? "block" : "none";
    }

    if (!effectiveCanClose) {
        document.body.classList.add("app-locked");
    }

    if (userProfile && userProfile.is_registered) {
        applyUserProfile(userProfile);
        switchGateTab('form');
    } else {
        clearRegistrationForm();
        switchGateTab('pin');
    }
}

function closeRegistrationModal() {
    const isRegistered = userProfile && userProfile.is_registered && userProfile.company_name;
    if (!isRegistered) {
        // Prevent bypassing without registration
        document.body.classList.add("app-locked");
        return;
    }
    const modal = document.getElementById("registrationModal");
    if (modal) modal.style.display = "none";
    document.body.classList.remove("app-locked");
}

async function saveRegistrationProfile(event) {
    if (event) event.preventDefault();

    const company_name = (document.getElementById("regCompanyName")?.value || "").trim();
    const estimator_name = (document.getElementById("regEstimatorName")?.value || "").trim();
    const estimator_title = (document.getElementById("regEstimatorTitle")?.value || "Senior Estimator").trim();
    const address = (document.getElementById("regAddress")?.value || "").trim();
    const phone = (document.getElementById("regPhone")?.value || "").trim();
    const email = (document.getElementById("regEmail")?.value || "").trim();
    const website = (document.getElementById("regWebsite")?.value || "").trim();
    const trade_specialty = document.getElementById("regTradeSpecialty")?.value || "Tile & Stone";
    const license_no = (document.getElementById("regLicenseNo")?.value || "").trim();

    if (!company_name || !estimator_name || !phone || !email) {
        alert("Please complete the required fields (Company Name, Estimator Name, Phone, and Email).");
        return;
    }

    const payload = {
        company_name,
        estimator_name,
        estimator_title,
        address,
        phone,
        email,
        website,
        trade_specialty,
        license_no,
        is_registered: true
    };

    userProfile = payload;
    localStorage.setItem("easyTakeOff_userProfile", JSON.stringify(payload));
    
    // Unlock application
    document.body.classList.remove("app-locked");
    const modal = document.getElementById("registrationModal");
    if (modal) modal.style.display = "none";

    applyUserProfile(payload);

    try {
        await fetch("/api/user/profile", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        showToast(`✅ Profile registered for ${company_name}! Proposals and SOW are now branded.`);
    } catch (e) {
        console.error("Failed to sync profile with server:", e);
        showToast(`✅ Profile saved for ${company_name}!`);
    }

    if (typeof saveProjectDetails === "function") {
        saveProjectDetails();
    }
}

// ============================================================
// GEMINI 3.6 FLASH AI COPILOT & VISION HANDLERS
// ============================================================
let aiChatConversationHistory = [];

function openAICopilotModal() {
    const modal = document.getElementById("aiCopilotModal");
    if (modal) {
        const estName = (userProfile?.estimator_name || document.getElementById("estimatorName")?.value || "").trim();
        const welcomeEl = document.getElementById("aiWelcomeGreeting");
        if (welcomeEl) {
            welcomeEl.textContent = estName ? `Merhaba ${estName}!` : "Hoş Geldiniz!";
        }
        modal.style.display = "flex";
        setTimeout(() => {
            const inp = document.getElementById("aiUserInput");
            if (inp) inp.focus();
        }, 100);
    }
}

function closeAICopilotModal() {
    const modal = document.getElementById("aiCopilotModal");
    if (modal) modal.style.display = "none";
}

function quickAskAI(text) {
    const inp = document.getElementById("aiUserInput");
    if (inp) {
        inp.value = text;
        sendAIChatMessage();
    }
}

async function sendAIChatMessage() {
    const inp = document.getElementById("aiUserInput");
    const history = document.getElementById("aiChatHistory");
    const sendBtn = document.getElementById("btnSendAIChat");
    if (!inp || !history) return;

    const message = inp.value.trim();
    if (!message) return;

    // Append User Message
    const userMsgDiv = document.createElement("div");
    userMsgDiv.className = "ai-msg user";
    userMsgDiv.textContent = message;
    history.appendChild(userMsgDiv);
    inp.value = "";
    history.scrollTop = history.scrollHeight;

    // Append to local history
    aiChatConversationHistory.push({ role: "user", content: message });

    // Append Loading indicator
    const botLoadingDiv = document.createElement("div");
    botLoadingDiv.className = "ai-msg bot";
    botLoadingDiv.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Gemini 3.6 Flash yanıt hazırlıyor...';
    history.appendChild(botLoadingDiv);
    history.scrollTop = history.scrollHeight;

    if (sendBtn) sendBtn.disabled = true;

    try {
        const response = await fetch("/api/ai/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                message: message,
                history: aiChatConversationHistory,
                project: (typeof projectData !== "undefined" && projectData) ? projectData : null
            })
        });
        const data = await response.json();

        if (data.status === "success" && data.reply) {
            aiChatConversationHistory.push({ role: "assistant", content: data.reply });
            if (typeof marked !== "undefined" && marked.parse) {
                botLoadingDiv.innerHTML = marked.parse(data.reply);
            } else {
                const formatted = data.reply
                    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                    .replace(/\n\n/g, "</p><p>")
                    .replace(/\n/g, "<br>");
                botLoadingDiv.innerHTML = `<p>${formatted}</p>`;
            }
        } else {
            botLoadingDiv.innerHTML = `<p style="color: #ef4444;">⚠️ Hata: ${data.message || "Yanıt alınamadı."}</p>`;
        }
    } catch (err) {
        botLoadingDiv.innerHTML = `<p style="color: #ef4444;">⚠️ Bağlantı Hatası: ${err.message}</p>`;
    } finally {
        if (sendBtn) sendBtn.disabled = false;
        history.scrollTop = history.scrollHeight;
    }
}

async function handleAIVisionUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    const statusEl = document.getElementById("uploadStatus");
    const statusText = document.getElementById("uploadStatusText");
    if (statusEl) statusEl.style.display = "block";
    if (statusText) statusText.textContent = "✨ Scanning blueprint with Gemini 3.6 Flash Vision & calculating takeoff...";

    const formData = new FormData();
    formData.append("file", file);
    formData.append("trade", currentTrade || "Tile & Stone");

    try {
        const res = await fetch("/api/ai/analyze_blueprint", {
            method: "POST",
            body: formData
        });
        const data = await res.json();

        if (data.status === "success") {
            showToast(`✨ Gemini Vision Takeoff Completed: ${data.rooms_count} Rooms & ${data.specs_count} Material Specs extracted.`);
            if (typeof loadProject === "function") {
                await loadProject();
            }
            // Open AI Copilot to show summary
            openAICopilotModal();
            const history = document.getElementById("aiChatHistory");
            if (history && data.summary) {
                const summaryDiv = document.createElement("div");
                summaryDiv.className = "ai-msg bot";
                summaryDiv.innerHTML = `<strong>✨ Blueprint Takeoff Summary:</strong><p>${data.summary}</p>`;
                history.appendChild(summaryDiv);
                history.scrollTop = history.scrollHeight;
            }
        } else {
            alert(`AI Analysis Error: ${data.message || "Unknown error"}`);
        }
    } catch (err) {
        alert(`Server / API Error: ${err.message}`);
    } finally {
        if (statusEl) statusEl.style.display = "none";
        event.target.value = "";
    }
}

