<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📚 Timetable Manager · Teacher dashboard</title>
    <!-- Font Awesome (icons) & Google Font -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:opsz@14..32&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }
        body {
            background: #f4f7fc;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem 1rem;
        }
        .app-card {
            max-width: 1300px;
            width: 100%;
            background: white;
            border-radius: 40px;
            box-shadow: 0 30px 60px rgba(0,20,40,0.12);
            padding: 2.5rem 2rem;
            transition: 0.2s;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            border-bottom: 2px solid #eef2f7;
            padding-bottom: 1.2rem;
            margin-bottom: 2rem;
        }
        .header h1 {
            font-weight: 600;
            font-size: 2rem;
            color: #0b1c33;
            letter-spacing: -0.3px;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .header h1 i {
            color: #2a6df4;
            font-size: 2.2rem;
        }
        .badge-connection {
            background: #e3f0ff;
            color: #1a5bc7;
            padding: 0.5rem 1.4rem;
            border-radius: 60px;
            font-weight: 500;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 10px;
            border: 1px solid #c3dbff;
        }
        .badge-connection i {
            font-size: 1.2rem;
        }
        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 18px;
            margin: 2rem 0 2.5rem 0;
        }
        .menu-btn {
            background: #f8faff;
            border: 1px solid #e6edf8;
            border-radius: 30px;
            padding: 1.2rem 0.8rem;
            font-weight: 600;
            font-size: 1.1rem;
            color: #1f2a44;
            transition: 0.15s;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        }
        .menu-btn i {
            font-size: 1.5rem;
            color: #2a6df4;
            width: 1.8rem;
        }
        .menu-btn:hover {
            background: #e8f0fe;
            border-color: #b6cef0;
            transform: scale(1.02);
            box-shadow: 0 8px 14px rgba(42,109,244,0.08);
        }
        .menu-btn.exit-btn {
            background: #fff2f0;
            border-color: #ffcec9;
            color: #b33a2e;
        }
        .menu-btn.exit-btn i {
            color: #c94a3c;
        }
        .menu-btn.exit-btn:hover {
            background: #ffe2de;
        }
        .panel {
            background: #fafcff;
            border-radius: 32px;
            padding: 2rem 1.8rem;
            border: 1px solid #eef4fa;
            margin-top: 1.5rem;
            box-shadow: inset 0 2px 6px rgba(0,0,0,0.01);
        }
        .panel-title {
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 600;
            font-size: 1.4rem;
            color: #0b1c33;
            margin-bottom: 1.6rem;
        }
        .panel-title i {
            color: #2a6df4;
        }
        .teacher-table-wrap {
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.95rem;
        }
        th {
            text-align: left;
            padding: 14px 8px;
            background: #eef5fe;
            color: #1a3a6b;
            font-weight: 600;
        }
        td {
            padding: 12px 8px;
            border-bottom: 1px solid #e3eaf3;
        }
        .badge-subject {
            background: #dde9fd;
            color: #1f4e9e;
            padding: 4px 12px;
            border-radius: 40px;
            font-size: 0.8rem;
            font-weight: 500;
        }
        .input-group {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 14px 20px;
            background: #f2f8ff;
            padding: 1.2rem 1.5rem;
            border-radius: 60px;
            margin: 20px 0 12px 0;
        }
        .input-group label {
            font-weight: 500;
            color: #1e3b66;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .input-group input, .input-group select {
            border: 1px solid #d2dff0;
            border-radius: 40px;
            padding: 10px 18px;
            font-size: 0.95rem;
            background: white;
            min-width: 160px;
            outline: none;
            transition: 0.1s;
        }
        .input-group input:focus, .input-group select:focus {
            border-color: #2a6df4;
            box-shadow: 0 0 0 3px rgba(42,109,244,0.15);
        }
        .action-btn {
            background: #2a6df4;
            border: none;
            color: white;
            font-weight: 600;
            padding: 10px 28px;
            border-radius: 60px;
            font-size: 0.95rem;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            transition: 0.15s;
            border: 1px solid #1f5ad4;
        }
        .action-btn i {
            font-size: 1rem;
        }
        .action-btn:hover {
            background: #1b5bd0;
            transform: scale(1.01);
        }
        .action-btn-outline {
            background: transparent;
            border: 1px solid #b8cef0;
            color: #1f3d6b;
        }
        .action-btn-outline:hover {
            background: #e9f1fd;
        }
        .flex-row {
            display: flex;
            flex-wrap: wrap;
            gap: 18px 30px;
            align-items: center;
        }
        .day-timetable {
            background: #ffffff;
            border-radius: 24px;
            padding: 1.5rem;
            border: 1px solid #e5edf7;
            margin-top: 1.2rem;
        }
        .period-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 14px;
            margin: 16px 0;
        }
        .period-item {
            background: #f2f9ff;
            border-radius: 20px;
            padding: 12px 8px;
            text-align: center;
            font-weight: 500;
            border: 1px solid #dbe6f5;
        }
        .period-item span {
            display: block;
            font-weight: 400;
            color: #445e7e;
            font-size: 0.8rem;
        }
        .mt-3 { margin-top: 1.2rem; }
        .text-muted { color: #5d7599; }
        .flex-between { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; }
        .emoji-big { font-size: 1.6rem; vertical-align: middle; }
        @media (max-width: 640px) {
            .app-card { padding: 1.5rem 0.8rem; }
            .header h1 { font-size: 1.6rem; }
            .menu-grid { grid-template-columns: 1fr 1fr; }
        }
    </style>
</head>
<body>
<div class="app-card" id="app">

    <!-- HEADER -->
    <div class="header">
        <h1><i class="fas fa-chalkboard-teacher"></i> Timetable Manager</h1>
        <div class="badge-connection">
            <i class="fas fa-plug"></i> MySQL <span style="font-weight:700;color:#0f3e8a;">●</span> connected
        </div>
    </div>

    <!-- MENU (MAIN FUNCTIONS) -->
    <div class="menu-grid">
        <div class="menu-btn" @click="activePanel='create'"><i class="fas fa-plus-circle"></i> Add Teacher</div>
        <div class="menu-btn" @click="activePanel='display'"><i class="fas fa-list-ul"></i> Teacher Info</div>
        <div class="menu-btn" @click="activePanel='search'"><i class="fas fa-calendar-alt"></i> Timetable</div>
        <div class="menu-btn" @click="activePanel='delete'"><i class="fas fa-trash-alt"></i> Delete</div>
        <div class="menu-btn" @click="activePanel='update'"><i class="fas fa-pen"></i> Assign / Update</div>
        <div class="menu-btn exit-btn" @click="exitApp()"><i class="fas fa-sign-out-alt"></i> Exit</div>
    </div>

    <!-- ========== DYNAMIC PANELS ========== -->
    <div class="panel" v-show="activePanel==='create'">
        <div class="panel-title"><i class="fas fa-user-plus"></i> Enter teacher details</div>
        <div class="input-group">
            <label><i class="fas fa-id-badge"></i> Code</label>
            <input type="number" v-model="newTeacher.code" placeholder="101">
            <label><i class="fas fa-user"></i> Name</label>
            <input v-model="newTeacher.name" placeholder="Dr. Sharma">
            <label><i class="fas fa-book"></i> Subject</label>
            <input v-model="newTeacher.subject" placeholder="Mathematics">
        </div>
        <div style="display:flex; gap:12px; flex-wrap:wrap; margin:8px 0 12px 0;">
            <button class="action-btn" @click="createTeacher()"><i class="fas fa-save"></i> Create & fill timetable</button>
            <span class="text-muted" style="align-self:center; font-size:0.9rem;"><i class="fas fa-info-circle"></i> You'll be prompted for each day (7 periods)</span>
        </div>
        <!-- quick preview of periods (mock) -->
        <div v-if="showPeriodPrompt" class="day-timetable" style="background:#f5faff;">
            <div class="flex-between"><strong><i class="fas fa-clock"></i> Enter periods for each day</strong> <span class="badge-subject">step 2/2</span></div>
            <div v-for="(day,idx) in days" :key="idx" style="margin-top:16px; border-top:1px dashed #d0def0; padding-top:12px;">
                <strong style="display:block; margin-bottom:6px;">{{ day.name }}</strong>
                <div class="period-grid">
                    <div v-for="p in 7" :key="p" class="period-item">
                        <span>Period {{ p }}</span>
                        <input v-model="dayPeriods[day.key][p-1]" placeholder="e.g. Math" style="width:100%; border:1px solid #d2dff0; border-radius:30px; padding:6px 8px; margin-top:6px; background:white;">
                    </div>
                </div>
            </div>
            <button class="action-btn" style="margin-top:20px;" @click="submitFullTeacher()"><i class="fas fa-check-circle"></i> Save all periods</button>
        </div>
        <div v-if="createMessage" style="margin-top:18px; background:#e4f3e0; padding:12px 24px; border-radius:60px; color:#1c6b3a;"><i class="fas fa-check-circle"></i> {{ createMessage }}</div>
    </div>

    <!-- DISPLAY TEACHER INFO -->
    <div class="panel" v-show="activePanel==='display'">
        <div class="panel-title"><i class="fas fa-users"></i> Teacher directory</div>
        <div class="teacher-table-wrap">
            <table>
                <thead><tr><th>Code</th><th>Name</th><th>Subject</th><th style="text-align:right;">Action</th></tr></thead>
                <tbody>
                    <tr v-for="t in teachers" :key="t.code">
                        <td><strong>{{ t.code }}</strong></td>
                        <td>{{ t.name }}</td>
                        <td><span class="badge-subject">{{ t.subject }}</span></td>
                        <td style="text-align:right;"><i class="fas fa-chevron-right" style="color:#7b98c7;"></i></td>
                    </tr>
                    <tr v-if="teachers.length===0"><td colspan="4" style="text-align:center; color:#889bbd;">No teachers added yet</td></tr>
                </tbody>
            </table>
        </div>
        <div style="margin-top:1.2rem;"><i class="fas fa-database text-muted"></i> <span class="text-muted">{{ teachers.length }} records</span></div>
    </div>

    <!-- SEARCH / TIMETABLE -->
    <div class="panel" v-show="activePanel==='search'">
        <div class="panel-title"><i class="fas fa-search"></i> View timetable</div>
        <div class="flex-row">
            <div class="input-group" style="border-radius:60px; background:#eff6fe; padding:0.8rem 1.8rem;">
                <label><i class="fas fa-id-card"></i> Teacher code</label>
                <input type="number" v-model="searchCode" placeholder="101">
                <button class="action-btn" @click="fetchTimetable()"><i class="fas fa-eye"></i> Show</button>
            </div>
            <span class="text-muted" style="font-size:0.9rem;"><i class="fas fa-arrow-right"></i> See whole week or specific day</span>
        </div>
        <div v-if="timetableData" class="day-timetable">
            <div class="flex-between">
                <span><i class="fas fa-user-graduate"></i> <strong>{{ timetableData.name }}</strong> ({{ timetableData.subject }})</span>
                <span class="badge-subject">Code: {{ timetableData.code }}</span>
            </div>
            <div style="display:flex; gap:10px; flex-wrap:wrap; margin:12px 0;">
                <button class="action-btn action-btn-outline" @click="viewDay('monday')">Monday</button>
                <button class="action-btn action-btn-outline" @click="viewDay('tuesday')">Tuesday</button>
                <button class="action-btn action-btn-outline" @click="viewDay('wednesday')">Wednesday</button>
                <button class="action-btn action-btn-outline" @click="viewDay('thursday')">Thursday</button>
                <button class="action-btn action-btn-outline" @click="viewDay('friday')">Friday</button>
                <button class="action-btn action-btn-outline" @click="viewDay('saturday')">Saturday</button>
                <button class="action-btn" @click="viewDay('all')"><i class="fas fa-calendar-week"></i> Whole week</button>
            </div>
            <div v-if="selectedDayView" style="margin-top:10px;">
                <div v-if="selectedDayView==='all'" class="period-grid" style="grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr;">
                    <div v-for="(p,idx) in timetableData.monday" :key="'mon'+idx" class="period-item"><span>Mon P{{idx+1}}</span>{{ p || '—' }}</div>
                    <div v-for="(p,idx) in timetableData.tuesday" :key="'tue'+idx" class="period-item"><span>Tue P{{idx+1}}</span>{{ p || '—' }}</div>
                    <div v-for="(p,idx) in timetableData.wednesday" :key="'wed'+idx" class="period-item"><span>Wed P{{idx+1}}</span>{{ p || '—' }}</div>
                    <div v-for="(p,idx) in timetableData.thursday" :key="'thu'+idx" class="period-item"><span>Thu P{{idx+1}}</span>{{ p || '—' }}</div>
                    <div v-for="(p,idx) in timetableData.friday" :key="'fri'+idx" class="period-item"><span>Fri P{{idx+1}}</span>{{ p || '—' }}</div>
                    <div v-for="(p,idx) in timetableData.saturday" :key="'sat'+idx" class="period-item"><span>Sat P{{idx+1}}</span>{{ p || '—' }}</div>
                </div>
                <div v-else class="period-grid">
                    <div v-for="(p,idx) in dayViewPeriods" :key="idx" class="period-item"><span>P{{idx+1}}</span>{{ p || '—' }}</div>
                </div>
            </div>
        </div>
        <div v-if="timetableError" style="color:#b33a2e; background:#ffeae7; padding:12px 24px; border-radius:60px; margin-top:1rem;">{{ timetableError }}</div>
    </div>

    <!-- DELETE -->
    <div class="panel" v-show="activePanel==='delete'">
        <div class="panel-title"><i class="fas fa-trash"></i> Delete teacher</div>
        <div class="flex-row">
            <div class="input-group" style="border-radius:60px;">
                <label><i class="fas fa-id-badge"></i> Teacher code</label>
                <input type="number" v-model="deleteCode" placeholder="101">
                <button class="action-btn" style="background:#c94a3c;" @click="deleteTeacher()"><i class="fas fa-trash-alt"></i> Delete permanently</button>
            </div>
        </div>
        <div v-if="deleteMessage" style="margin-top:16px; background:#fff1ef; padding:10px 24px; border-radius:60px; color:#9e3b2e;">{{ deleteMessage }}</div>
    </div>

    <!-- UPDATE / ASSIGN -->
    <div class="panel" v-show="activePanel==='update'">
        <div class="panel-title"><i class="fas fa-pen-fancy"></i> Assign class / update period</div>
        <div class="flex-row" style="margin-bottom:12px;">
            <div class="input-group" style="border-radius:60px;">
                <label><i class="fas fa-id-card"></i> Teacher code</label>
                <input type="number" v-model="updateCode" placeholder="101">
                <button class="action-btn" @click="loadUpdateData()"><i class="fas fa-edit"></i> Load timetable</button>
            </div>
        </div>
        <div v-if="updateTimetable" class="day-timetable">
            <div><strong>{{ updateTimetable.name }}</strong> ({{ updateTimetable.subject }}) <span class="badge-subject">code {{ updateTimetable.code }}</span></div>
            <div style="display:flex; flex-wrap:wrap; gap:12px; margin:12px 0;">
                <button v-for="(day,key) in dayNames" :key="key" class="action-btn action-btn-outline" @click="selectUpdateDay(key)">{{ day }}</button>
            </div>
            <div v-if="selectedUpdateDay" style="margin-top:12px; background:#f5f9ff; padding:1rem; border-radius:30px;">
                <strong>{{ selectedUpdateDayName }}</strong>
                <div class="period-grid">
                    <div v-for="(p,idx) in updatePeriods" :key="idx" class="period-item">
                        <span>P{{ idx+1 }}</span>
                        <input v-model="updatePeriods[idx]" placeholder="class" style="width:100%; border-radius:30px; border:1px solid #d2dff0; padding:6px; margin-top:4px;">
                    </div>
                </div>
                <button class="action-btn" style="margin-top:16px;" @click="saveUpdatePeriods()"><i class="fas fa-save"></i> Update periods</button>
            </div>
            <div v-if="updateMsg" style="margin-top:12px; background:#e4f3e0; padding:8px 20px; border-radius:60px;">{{ updateMsg }}</div>
        </div>
    </div>

    <!-- footer -->
    <div style="margin-top:2.5rem; border-top:1px solid #eef2f7; padding-top:1.5rem; display:flex; justify-content:space-between; flex-wrap:wrap; color:#6a7f9e; font-size:0.9rem;">
        <span><i class="fas fa-code"></i> Timetable v1.0 · demo UI</span>
        <span><i class="fas fa-clock"></i> {{ new Date().toLocaleDateString('en-IN', { weekday:'short', year:'numeric', month:'short', day:'numeric' }) }}</span>
    </div>
</div>

<!-- Vue & logic -->
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    (function(){
        new Vue({
            el: '#app',
            data: {
                activePanel: 'display',
                teachers: [
                    { code: 101, name: 'Dr. Anita Sharma', subject: 'Mathematics' },
                    { code: 202, name: 'Mr. Ravi Kumar', subject: 'Physics' },
                    { code: 303, name: 'Ms. Neha Singh', subject: 'Computer Science' }
                ],
                // create
                newTeacher: { code: '', name: '', subject: '' },
                showPeriodPrompt: false,
                days: [
                    { key: 'monday', name: 'Monday' },
                    { key: 'tuesday', name: 'Tuesday' },
                    { key: 'wednesday', name: 'Wednesday' },
                    { key: 'thursday', name: 'Thursday' },
                    { key: 'friday', name: 'Friday' },
                    { key: 'saturday', name: 'Saturday' }
                ],
                dayPeriods: {
                    monday: ['','','','','','',''],
                    tuesday: ['','','','','','',''],
                    wednesday: ['','','','','','',''],
                    thursday: ['','','','','','',''],
                    friday: ['','','','','','',''],
                    saturday: ['','','','','','','']
                },
                createMessage: '',
                // display
                // search
                searchCode: '',
                timetableData: null,
                timetableError: '',
                selectedDayView: null,
                dayViewPeriods: [],
                // delete
                deleteCode: '',
                deleteMessage: '',
                // update
                updateCode: '',
                updateTimetable: null,
                updatePeriods: ['','','','','','',''],
                selectedUpdateDay: null,
                selectedUpdateDayName: '',
                updateMsg: '',
                dayNames: { monday:'Monday', tuesday:'Tuesday', wednesday:'Wednesday', thursday:'Thursday', friday:'Friday', saturday:'Saturday' }
            },
            methods: {
                // CREATE teacher + periods (simulate)
                createTeacher() {
                    if (!this.newTeacher.code || !this.newTeacher.name || !this.newTeacher.subject) {
                        this.createMessage = '⚠️ Please fill all fields (code, name, subject)';
                        return;
                    }
                    // check duplicate
                    if (this.teachers.find(t => t.code == this.newTeacher.code)) {
                        this.createMessage = '⚠️ Teacher code already exists.';
                        return;
                    }
                    this.showPeriodPrompt = true;
                    this.createMessage = '📝 Now fill periods for each day and click "Save all periods"';
                },
                submitFullTeacher() {
                    // validate all periods filled? optional
                    const newT = {
                        code: Number(this.newTeacher.code),
                        name: this.newTeacher.name,
                        subject: this.newTeacher.subject,
                        monday: [...this.dayPeriods.monday],
                        tuesday: [...this.dayPeriods.tuesday],
                        wednesday: [...this.dayPeriods.wednesday],
                        thursday: [...this.dayPeriods.thursday],
                        friday: [...this.dayPeriods.friday],
                        saturday: [...this.dayPeriods.saturday]
                    };
                    this.teachers.push({ code: newT.code, name: newT.name, subject: newT.subject });
                    // store full timetable (for demo we keep in a map)
                    if (!window._timetableMap) window._timetableMap = {};
                    window._timetableMap[newT.code] = newT;
                    this.createMessage = `✅ Teacher ${newT.name} (${newT.code}) added with timetable.`;
                    this.showPeriodPrompt = false;
                    this.newTeacher = { code: '', name: '', subject: '' };
                    // reset periods
                    this.days.forEach(d => { this.dayPeriods[d.key] = ['','','','','','','']; });
                },
                // DISPLAY is just binding
                // SEARCH
                fetchTimetable() {
                    const code = Number(this.searchCode);
                    this.timetableError = '';
                    this.timetableData = null;
                    this.selectedDayView = null;
                    // check teacher exists
                    const teacher = this.teachers.find(t => t.code === code);
                    if (!teacher) {
                        this.timetableError = '❌ Teacher not found.';
                        return;
                    }
                    // get timetable from map or create default
                    let tt = window._timetableMap ? window._timetableMap[code] : null;
                    if (!tt) {
                        // build default empty
                        tt = {
                            code: code,
                            name: teacher.name,
                            subject: teacher.subject,
                            monday: ['','','','','','',''],
                            tuesday: ['','','','','','',''],
                            wednesday: ['','','','','','',''],
                            thursday: ['','','','','','',''],
                            friday: ['','','','','','',''],
                            saturday: ['','','','','','','']
                        };
                        if (!window._timetableMap) window._timetableMap = {};
                        window._timetableMap[code] = tt;
                    }
                    this.timetableData = tt;
                    this.selectedDayView = null;
                },
                viewDay(dayKey) {
                    if (!this.timetableData) return;
                    if (dayKey === 'all') {
                        this.selectedDayView = 'all';
                        return;
                    }
                    this.selectedDayView = dayKey;
                    const periods = this.timetableData[dayKey] || ['','','','','','',''];
                    this.dayViewPeriods = periods;
                },
                // DELETE
                deleteTeacher() {
                    const code = Number(this.deleteCode);
                    const idx = this.teachers.findIndex(t => t.code === code);
                    if (idx === -1) {
                        this.deleteMessage = '❌ Teacher not found.';
                        return;
                    }
                    this.teachers.splice(idx, 1);
                    if (window._timetableMap) delete window._timetableMap[code];
                    this.deleteMessage = `🗑️ Teacher code ${code} removed.`;
                    this.deleteCode = '';
                },
                // UPDATE
                loadUpdateData() {
                    const code = Number(this.updateCode);
                    const teacher = this.teachers.find(t => t.code === code);
                    if (!teacher) {
                        this.updateMsg = '❌ Teacher not found.';
                        this.updateTimetable = null;
                        return;
                    }
                    let tt = window._timetableMap ? window._timetableMap[code] : null;
                    if (!tt) {
                        tt = {
                            code: code,
                            name: teacher.name,
                            subject: teacher.subject,
                            monday: ['','','','','','',''],
                            tuesday: ['','','','','','',''],
                            wednesday: ['','','','','','',''],
                            thursday: ['','','','','','',''],
                            friday: ['','','','','','',''],
                            saturday: ['','','','','','','']
                        };
                        if (!window._timetableMap) window._timetableMap = {};
                        window._timetableMap[code] = tt;
                    }
                    this.updateTimetable = tt;
                    this.selectedUpdateDay = null;
                    this.updateMsg = `📋 Loaded ${tt.name}`;
                },
                selectUpdateDay(dayKey) {
                    this.selectedUpdateDay = dayKey;
                    this.selectedUpdateDayName = this.dayNames[dayKey] || dayKey;
                    const periods = this.updateTimetable[dayKey] || ['','','','','','',''];
                    this.updatePeriods = [...periods];
                },
                saveUpdatePeriods() {
                    if (!this.selectedUpdateDay || !this.updateTimetable) return;
                    this.updateTimetable[this.selectedUpdateDay] = [...this.updatePeriods];
                    // update map
                    if (window._timetableMap) {
                        window._timetableMap[this.updateTimetable.code] = this.updateTimetable;
                    }
                    this.updateMsg = `✅ ${this.selectedUpdateDayName} updated.`;
                },
                exitApp() {
                    if (confirm('Exit Timetable Manager?')) {
                        this.activePanel = 'display';
                        this.createMessage = '';
                        this.deleteMessage = '';
                        this.timetableData = null;
                        this.updateTimetable = null;
                    }
                }
            },
            mounted() {
                // prefill timetable map for demo
                if (!window._timetableMap) window._timetableMap = {};
                this.teachers.forEach(t => {
                    if (!window._timetableMap[t.code]) {
                        window._timetableMap[t.code] = {
                            code: t.code,
                            name: t.name,
                            subject: t.subject,
                            monday: ['Math','Physics','Chem','','','',''],
                            tuesday: ['Physics','Chem','Math','','','',''],
                            wednesday: ['Chem','Math','Physics','','','',''],
                            thursday: ['Math','Physics','','','','',''],
                            friday: ['Physics','Math','Chem','','','',''],
                            saturday: ['','','','','','','']
                        };
                    }
                });
            }
        });
    })();
</script>
</body>
</html>
