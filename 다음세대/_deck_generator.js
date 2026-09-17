const pptxgen = require('pptxgenjs');
const p = new pptxgen();
p.layout = 'LAYOUT_WIDE';           // 13.333 x 7.5
p.author = '중고등부';
p.title  = '아이들의 세계로';

const W = 13.333, H = 7.5;
const INK   = '16243F';   // deep navy (dominant)
const INK2  = '24365C';
const AMBER = 'E39237';
const CORAL = 'C8402E';
const TEAL  = '2E7D71';
const SOFT  = 'EEF1F6';
const MUTED = '64708A';
const WHITE = 'FFFFFF';
const F     = '맑은 고딕';

const sh = () => ({ type:'outer', color:'8895AE', blur:10, offset:2, angle:90, opacity:0.22 });

function darkSlide(){ const s = p.addSlide(); s.background = { color: INK }; return s; }
function lightSlide(){ const s = p.addSlide(); s.background = { color: WHITE }; return s; }

// standard light slide title
function title(s, t, kicker){
  if (kicker) s.addText(kicker, { x:0.75, y:0.42, w:11.8, h:0.32, fontFace:F, fontSize:13, bold:true,
                                  color:AMBER, charSpacing:2, isTextBox:true, margin:0 });
  s.addText(t, { x:0.75, y: kicker?0.78:0.55, w:11.8, h:0.85, fontFace:F, fontSize:33, bold:true,
                 color:INK, isTextBox:true, margin:0, valign:'top' });
}
function src(s, t){
  s.addText(t, { x:0.75, y:6.88, w:11.8, h:0.32, fontFace:F, fontSize:10, color:MUTED, isTextBox:true, margin:0 });
}
// rounded card
function card(s, x, y, w, h, fill){
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, fill:{ color: fill||SOFT }, rectRadius:0.1, line:{ color: fill||SOFT }, shadow: sh() });
}
// big stat block
function stat(s, x, y, w, num, label, numColor, sub){
  s.addText(num, { x, y, w, h:1.0, fontFace:F, fontSize:50, bold:true, color:numColor||INK,
                   align:'center', isTextBox:true, margin:0 });
  s.addText(label, { x, y:y+1.02, w, h:0.75, fontFace:F, fontSize:13, color:INK2, align:'center',
                     isTextBox:true, margin:0, lineSpacingMultiple:1.15 });
  if (sub) s.addText(sub, { x, y:y+1.75, w, h:0.3, fontFace:F, fontSize:10.5, color:MUTED, align:'center', isTextBox:true, margin:0 });
}
function numCircle(s, x, y, n, color){
  s.addShape(p.ShapeType.ellipse, { x, y, w:0.46, h:0.46, fill:{ color: color||INK }, line:{ color: color||INK } });
  s.addText(String(n), { x, y, w:0.46, h:0.46, fontFace:F, fontSize:16, bold:true, color:WHITE,
                         align:'center', valign:'middle', isTextBox:true, margin:0 });
}
function sectionSlide(no, kicker, big, lead){
  const s = darkSlide();
  s.addText(kicker, { x:1.1, y:2.15, w:11, h:0.35, fontFace:F, fontSize:14, bold:true, color:AMBER,
                      charSpacing:3, isTextBox:true, margin:0 });
  s.addShape(p.ShapeType.ellipse, { x:1.1, y:2.72, w:0.62, h:0.62, fill:{ color:AMBER }, line:{ color:AMBER } });
  s.addText(String(no), { x:1.1, y:2.72, w:0.62, h:0.62, fontFace:F, fontSize:22, bold:true, color:INK,
                          align:'center', valign:'middle', isTextBox:true, margin:0 });
  s.addText(big, { x:1.95, y:2.66, w:10.2, h:0.85, fontFace:F, fontSize:38, bold:true, color:WHITE, isTextBox:true, margin:0 });
  s.addText(lead, { x:1.95, y:3.62, w:10.0, h:0.9, fontFace:F, fontSize:15, color:'B9C4DA', isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  return s;
}

const CHART_BASE = {
  showTitle:false, showLegend:false,
  catAxisLabelColor: INK2, catAxisLabelFontFace: F, catAxisLabelFontSize: 13,
  valAxisLabelColor: MUTED, valAxisLabelFontFace: F, valAxisLabelFontSize: 11,
  catGridLine: { style:'none' },
  valGridLine: { color:'DDE3EC', size:1 },
  dataLabelFontFace: F, dataLabelFontSize: 13, dataLabelFontBold: true,
  showValue: true,
};

/* ─────────────────────────── 1. 표지 ─────────────────────────── */
{
  const s = darkSlide();
  s.addShape(p.ShapeType.ellipse, { x:9.5, y:-1.6, w:6.2, h:6.2, fill:{ color:INK2 }, line:{ color:INK2 } });
  s.addShape(p.ShapeType.ellipse, { x:11.4, y:4.6, w:3.2, h:3.2, fill:{ color:'1D2E51' }, line:{ color:'1D2E51' } });
  s.addText('2026 중고등부 교사 회의', { x:1.0, y:1.55, w:9, h:0.35, fontFace:F, fontSize:14, bold:true,
                                        color:AMBER, charSpacing:3, isTextBox:true, margin:0 });
  s.addText('아이들의 세계로', { x:1.0, y:2.05, w:9.5, h:1.3, fontFace:F, fontSize:60, bold:true,
                                color:WHITE, isTextBox:true, margin:0 });
  s.addText('데이터로 읽는 우리 중고등부', { x:1.0, y:3.35, w:9.5, h:0.6, fontFace:F, fontSize:23,
                                           color:'B9C4DA', isTextBox:true, margin:0 });
  s.addShape(p.ShapeType.roundRect, { x:1.0, y:4.35, w:7.7, h:0.95, fill:{ color:'1D2E51' }, rectRadius:0.1, line:{ color:'2C4271' } });
  s.addText('“가르치는 자가 아이들의 세계로 쑥 들어가지 못했다”',
    { x:1.25, y:4.35, w:7.2, h:0.95, fontFace:F, fontSize:15, italic:true, color:'E8EDF6',
      valign:'middle', isTextBox:true, margin:0 });
  s.addText('자료 · 잘잘법 284회 「데이터가 알려주는 우리 아이의 신앙이 자라는 과정」  |  지용근 목회데이터연구소 대표  |  CBS, 2026.9.3',
    { x:1.0, y:5.72, w:11.3, h:0.3, fontFace:F, fontSize:11, color:'8D9AB5', isTextBox:true, margin:0 });
  s.addNotes('오늘 회의는 감(感)이 아니라 데이터로 시작합니다. 20분짜리 영상 하나에 우리 중고등부의 현실이 거의 다 들어 있습니다.');
}

/* ─────────────────────────── 2. 오늘의 약속 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '오늘 이 회의가 끝나면', 'PROMISE · 오늘의 약속');
  const items = [
    ['우리 아이들이 교회를 떠나는 진짜 이유를', '추측이 아니라 숫자로 알게 됩니다'],
    ['교사인 내가 어디에 시간을 써야 하는지', '역할의 비율이 바뀝니다'],
    ['이번 학기에 당장 할 일 여섯 가지를', '이름과 날짜가 붙은 형태로 들고 갑니다'],
  ];
  items.forEach((it, i) => {
    const y = 2.05 + i*1.28;
    card(s, 0.75, y, 11.8, 1.06, SOFT);
    numCircle(s, 1.05, y+0.3, i+1, INK);
    s.addText(it[0], { x:1.72, y:y+0.15, w:10.5, h:0.42, fontFace:F, fontSize:17, bold:true, color:INK, isTextBox:true, margin:0 });
    s.addText(it[1], { x:1.72, y:y+0.58, w:10.5, h:0.38, fontFace:F, fontSize:13.5, color:MUTED, isTextBox:true, margin:0 });
  });
  s.addShape(p.ShapeType.roundRect, { x:0.75, y:5.95, w:11.8, h:0.72, fill:{ color:INK }, rectRadius:0.1, line:{ color:INK } });
  s.addText('오늘의 후렴구 ·  아이는 “예배가 지루해서”라 말하고, 우리는 “공부 때문에”라 말한다',
    { x:1.05, y:5.95, w:11.2, h:0.72, fontFace:F, fontSize:15, bold:true, color:AMBER, valign:'middle', isTextBox:true, margin:0 });
  s.addNotes('이 후렴구는 오늘 회의에서 세 번 반복됩니다. 이것 하나만 기억해도 오늘 회의는 성공입니다.');
}

/* ─────────────────────────── 3. 프롤로그 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '전화를 받는 아이는 누구인가', 'PROLOGUE');
  card(s, 0.75, 2.0, 6.5, 4.2, SOFT);
  s.addText([
    { text:'주일에 결석한 학생에게 주중 전화심방을 합니다.\n', options:{ breakLine:true } },
    { text:'대부분 받지 않습니다. 목사님 전화니까요.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'그런데 받는 아이가 있습니다.\n', options:{ breakLine:true, bold:true, color:INK } },
    { text:'\n', options:{ breakLine:true } },
    { text:'그 아이는 ', options:{} },
    { text:'“부목사님과 엄마가 친한”', options:{ bold:true, color:CORAL } },
    { text:' 아이입니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'이유는 하나 — “엄마한테 혼날까 봐.”', options:{} },
  ], { x:1.05, y:2.3, w:5.9, h:3.6, fontFace:F, fontSize:15.5, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.35 });

  s.addText('여기서 이미 답이 나옵니다', { x:7.7, y:2.1, w:4.85, h:0.4, fontFace:F, fontSize:14, bold:true, color:AMBER, isTextBox:true, margin:0 });
  const pts = [
    ['아이에게 가는 길은 부모를 통한다', '교사가 아이만 붙잡는 방식은 이미 절반짜리다'],
    ['교회를 떠나고 싶은 아이도 못 떠난다', '조사 결과 이유는 “엄마 때문에”'],
    ['그러므로 전화심방의 준비는 통화가 아니다', '그 어머니와 먼저 친해지는 일이다'],
  ];
  pts.forEach((t,i)=>{
    const y = 2.62 + i*1.22;
    s.addShape(p.ShapeType.ellipse, { x:7.7, y:y+0.06, w:0.3, h:0.3, fill:{ color:AMBER }, line:{ color:AMBER } });
    s.addText(t[0], { x:8.15, y:y, w:4.4, h:0.45, fontFace:F, fontSize:14.5, bold:true, color:INK, isTextBox:true, margin:0 });
    s.addText(t[1], { x:8.15, y:y+0.45, w:4.4, h:0.62, fontFace:F, fontSize:12.5, color:MUTED, isTextBox:true, margin:0, lineSpacingMultiple:1.2 });
  });
  src(s, '잘잘법 284회 00:00~03:20');
  s.addNotes('영상의 첫 장면입니다. 이 에피소드가 오늘 데이터 전체의 축소판입니다.');
}

/* ─────────────────────────── 4. 섹션 1 ─────────────────────────── */
sectionSlide(1, 'PART', '지금 우리가 선 자리', '신앙의 무게중심이 강단에서 가정과 미디어로 옮겨 갔습니다.\n지난 10년의 데이터가 그 이동을 정확히 기록하고 있습니다.');

/* ─────────────────────────── 5. 가족종교화 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '가족종교화 시대', '01 · 진단');
  s.addText('부모–자녀 종교 일치도', { x:0.75, y:2.0, w:5.2, h:0.4, fontFace:F, fontSize:15, color:MUTED, isTextBox:true, margin:0 });
  s.addText('80%＋', { x:0.75, y:2.30, w:5.2, h:1.65, fontFace:F, fontSize:86, bold:true, color:INK, isTextBox:true, margin:0 });
  s.addText('부모가 기독교면 자녀도 기독교,\n부모가 아니면 자녀도 아닌 시대',
    { x:0.75, y:4.05, w:5.2, h:0.9, fontFace:F, fontSize:16, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.3 });

  card(s, 6.55, 2.0, 6.0, 4.2, SOFT);
  s.addText('우리 중고등부에 이런 뜻입니다', { x:6.9, y:2.28, w:5.3, h:0.4, fontFace:F, fontSize:15, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText([
    { text:'양친이 모두 비기독교인인 아이는 지금 교회학교에 거의 없습니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'→ 우리가 만나는 아이는 대부분 ', options:{} },
    { text:'“부모의 신앙을 물려받은 아이”', options:{ bold:true, color:INK } },
    { text:'입니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'→ 그래서 아이만 붙잡는 사역은 원인이 아니라 결과를 붙잡는 일이 됩니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'→ 동시에 질문이 남습니다. ', options:{} },
    { text:'믿지 않는 가정의 아이는 어디로 갑니까?', options:{ bold:true, color:CORAL } },
  ], { x:6.9, y:2.78, w:5.3, h:3.2, fontFace:F, fontSize:14, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  src(s, '잘잘법 284회 00:30~01:35  ·  목회데이터연구소 「한국교회의 가족 종교화」');
  s.addNotes('마지막 질문은 영상 댓글에서 실제로 제기된 것입니다. 우리 중고등부의 전도 전략과 직결됩니다.');
}

/* ─────────────────────────── 6. 10년 변화 차트 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '10년 사이, 강단의 영향력은 절반으로 꺾였습니다', '02 · 진단');
  s.addText('“신앙 성장에 가장 도움이 되는 것은 무엇입니까” — 한국 기독교인 응답 10년 추이 (%)',
    { x:0.75, y:1.72, w:11.8, h:0.32, fontFace:F, fontSize:13, color:MUTED, isTextBox:true, margin:0 });
  s.addChart(p.ChartType.bar, [
    { name:'10년 전', labels:['출석교회 예배·설교','가족','미디어(유튜브 등)'], values:[64, 9, 1] },
    { name:'현재',    labels:['출석교회 예배·설교','가족','미디어(유튜브 등)'], values:[28, 20, 19] },
  ], Object.assign({}, CHART_BASE, {
    x:0.75, y:2.15, w:7.5, h:4.0,
    barDir:'col', barGrouping:'clustered', barGapWidthPct:60,
    chartColors:[ 'A9B6CD', INK ],
    dataLabelPosition:'outEnd', dataLabelColor: INK2,
    showLegend:true, legendPos:'t', legendFontFace:F, legendFontSize:12, legendColor:INK2,
    valAxisMaxVal:70,
  }));
  card(s, 8.6, 2.15, 3.95, 4.0, SOFT);
  s.addText('읽는 법', { x:8.9, y:2.42, w:3.4, h:0.35, fontFace:F, fontSize:14, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText([
    { text:'강단이 잃은 36%p를\n', options:{ breakLine:true, bold:true, color:INK } },
    { text:'가족(＋11%p)과 미디어(＋18%p)가 나눠 가졌습니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'미디어 1%→19%는 곧 ', options:{} },
    { text:'“지난 10년 사이 유튜브가 생겼다”', options:{ bold:true, color:INK } },
    { text:'는 뜻입니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'아이들은 이미 영상으로 신앙을 배우고 있습니다. 문제는 그 영상을 우리가 만들지 않았다는 것입니다.', options:{} },
  ], { x:8.9, y:2.85, w:3.4, h:3.1, fontFace:F, fontSize:13, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.28 });
  src(s, '잘잘법 284회 01:37~03:40');
  s.addNotes('우리 중고등부가 쇼츠 한 편이라도 직접 만들어야 하는 이유가 이 그래프에 있습니다.');
}

/* ─────────────────────────── 7. 예배 만족도 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '예배 만족도는 30년 동안 내려왔습니다', '03 · 진단');
  const items = [
    ['30년 전', '90%＋', '출석교회 예배 만족도', 'A9B6CD'],
    ['현재',    '65%',   '출석교회 예배 만족도', CORAL],
  ];
  items.forEach((it,i)=>{
    const x = 0.75 + i*3.1;
    card(s, x, 2.15, 2.85, 2.6, SOFT);
    s.addText(it[0], { x, y:2.42, w:2.85, h:0.35, fontFace:F, fontSize:13, color:MUTED, align:'center', isTextBox:true, margin:0 });
    s.addText(it[1], { x, y:2.8, w:2.85, h:1.0, fontFace:F, fontSize:46, bold:true, color:it[3], align:'center', isTextBox:true, margin:0 });
    s.addText(it[2], { x:x+0.2, y:3.85, w:2.45, h:0.6, fontFace:F, fontSize:12, color:INK2, align:'center', isTextBox:true, margin:0 });
  });
  card(s, 7.15, 2.15, 5.4, 4.15, INK);
  s.addText('그래서 질문은 이것입니다', { x:7.5, y:2.45, w:4.7, h:0.4, fontFace:F, fontSize:14, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText('우리 중고등부 예배는\n지금 90%입니까,\n65%입니까?',
    { x:7.5, y:2.95, w:4.7, h:1.5, fontFace:F, fontSize:26, bold:true, color:WHITE, isTextBox:true, margin:0, lineSpacingMultiple:1.2 });
  s.addText('우리는 이 숫자를 한 번도 재 본 적이 없습니다.\n오늘 회의의 첫 번째 실행 과제가 여기서 나옵니다.',
    { x:7.5, y:4.65, w:4.7, h:1.0, fontFace:F, fontSize:13.5, color:'B9C4DA', isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  s.addText('“예배가 지루하다”는 말은 취향의 문제가 아니라 이탈의 1번 원인입니다.',
    { x:0.75, y:5.05, w:5.95, h:1.2, fontFace:F, fontSize:14.5, bold:true, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  src(s, '잘잘법 284회 02:01~02:25');
}

/* ─────────────────────────── 8. 영향 순위 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '아이의 신앙에 영향을 준 사람 — 아이들의 대답', '04 · 진단');
  s.addText('교회 출석 중고등학생 응답 순위', { x:0.75, y:1.72, w:11.8, h:0.3, fontFace:F, fontSize:13, color:MUTED, isTextBox:true, margin:0 });
  const rank = [
    ['1', '어머니', '압도적 1위', AMBER],
    ['2', '중고등부 목사님 · 전도사님', '교역자의 비중이 매우 크다', INK],
    ['3', '교회 선생님 (교사)', '바로 우리입니다', INK],
    ['4', '교회 친구 · 선후배', '또래의 힘', INK],
    ['5', '아버지', '“아버지는 별로 영향력이 없습니다”', MUTED],
  ];
  rank.forEach((r,i)=>{
    const y = 2.18 + i*0.86;
    card(s, 0.75, y, 7.6, 0.72, i===0 ? 'FDF3E4' : SOFT);
    numCircle(s, 1.0, y+0.13, r[0], r[3]);
    s.addText(r[1], { x:1.62, y:y, w:3.6, h:0.72, fontFace:F, fontSize:16, bold:true, color:INK, valign:'middle', isTextBox:true, margin:0 });
    s.addText(r[2], { x:5.25, y:y, w:2.95, h:0.72, fontFace:F, fontSize:12, color:MUTED, valign:'middle', align:'right', isTextBox:true, margin:0 });
  });
  card(s, 8.7, 2.18, 3.85, 4.06, INK);
  s.addText('교사에게', { x:9.0, y:2.46, w:3.25, h:0.35, fontFace:F, fontSize:14, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText([
    { text:'1·3·4위가 모두 “사람”입니다.\n', options:{ breakLine:true, bold:true, color:WHITE } },
    { text:'\n', options:{ breakLine:true } },
    { text:'프로그램이 아이를 붙잡는 것이 아니라 관계가 붙잡습니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'그리고 1위가 어머니라는 사실은, 교사의 사역 대상에 ', options:{} },
    { text:'부모가 포함된다', options:{ bold:true, color:AMBER } },
    { text:'는 뜻입니다.', options:{} },
  ], { x:9.0, y:2.9, w:3.25, h:3.1, fontFace:F, fontSize:13, color:'C6D0E2', isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  src(s, '잘잘법 284회 03:44~04:12');
}

/* ─────────────────────────── 9. 부모 신앙단계 차트 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '부모의 신앙이 자녀의 주일을 결정합니다', '05 · 진단');
  s.addText('부모 신앙 단계별 자녀의 주일예배 참석 비율 (%)   ·   1단계 = 교회는 다니나 구원의 확신 없음 / 4단계 = 하나님 중심으로 살려는 부모',
    { x:0.75, y:1.72, w:11.8, h:0.32, fontFace:F, fontSize:12.5, color:MUTED, isTextBox:true, margin:0 });
  s.addChart(p.ChartType.bar, [
    { name:'자녀 주일예배 참석률', labels:['부모 신앙 1단계','부모 신앙 4단계'], values:[30, 82] },
  ], Object.assign({}, CHART_BASE, {
    x:0.75, y:2.2, w:7.3, h:3.9,
    barDir:'col', barGapWidthPct:110,
    chartColors:[ CORAL, TEAL ], varyColors:true,
    dataLabelPosition:'outEnd', dataLabelColor: INK2, dataLabelFontSize:18,
    valAxisMaxVal:100,
  }));
  card(s, 8.4, 2.2, 4.15, 3.9, SOFT);
  s.addText('52%p', { x:8.7, y:2.45, w:3.55, h:0.9, fontFace:F, fontSize:46, bold:true, color:TEAL, isTextBox:true, margin:0 });
  s.addText('부모의 신앙 한 단계가 만들어 내는 차이',
    { x:8.7, y:3.35, w:3.55, h:0.55, fontFace:F, fontSize:13.5, bold:true, color:INK, isTextBox:true, margin:0, lineSpacingMultiple:1.2 });
  s.addText('아이의 신앙을 끌어올리려면 부모의 신앙을 끌어올려야 합니다.\n그리고 부모를 세우는 일은 교회의 몫입니다.',
    { x:8.7, y:4.0, w:3.55, h:1.5, fontFace:F, fontSize:13, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  src(s, '잘잘법 284회 04:13~05:05');
}

/* ─────────────────────────── 10. 부모의 현실 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '그런데 부모는 방법을 배운 적이 없습니다', '06 · 진단');
  const st = [
    ['24%', '자녀 신앙교육\n훈련을 받아본 경험', CORAL],
    ['56%', '자녀 신앙교육의\n구체적 방법을 모른다', CORAL],
    ['4%',  '전체 학부모 중\n실제로 가정에서 실천', CORAL],
    ['72%', '교회가 가르쳐 준다면\n받고 싶다', TEAL],
  ];
  st.forEach((t,i)=>{
    const x = 0.75 + i*3.03;
    card(s, x, 2.05, 2.78, 2.45, i===3 ? 'E7F2EF' : SOFT);
    stat(s, x, 2.28, 2.78, t[0], t[1], t[2]);
  });
  card(s, 0.75, 4.78, 11.8, 1.5, INK);
  s.addText([
    { text:'실천율 4%는 절망적인 숫자지만, 의향률 72%는 아직 열려 있는 문입니다.  ', options:{ bold:true, color:WHITE } },
    { text:'문제는 부모의 의지가 아니라, 아무도 가르쳐 주지 않았다는 것입니다.', options:{ color:AMBER, bold:true } },
  ], { x:1.1, y:4.78, w:11.1, h:1.5, fontFace:F, fontSize:16, valign:'middle', isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  src(s, '잘잘법 284회 05:07~06:14');
  s.addNotes('우리 중고등부 학부모를 대상으로 한 “부모 신앙교육 1회”가 지금 가장 비용 대비 효과가 큰 사역일 수 있습니다.');
}

/* ─────────────────────────── 11. 조부모 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '다시 돌아온 조부모의 시대', '07 · 진단');
  const rows = [
    ['서울 30·40대 맞벌이 비율', '약 60%', '전국은 50% 이상'],
    ['영유아를 부모 외에 돌보는 주체', '조부모 약 50%', '전국보육실태조사(2021)'],
    ['손주 양육·교육에 관심 있는 교인', '69%', '65세 이상은 약 80%'],
    ['조부모 신앙교육이 필요하다', '교인 65% / 담임목사 90%', ''],
  ];
  rows.forEach((r,i)=>{
    const y = 2.05 + i*1.05;
    card(s, 0.75, y, 7.35, 0.9, SOFT);
    s.addText(r[0], { x:1.05, y:y, w:3.6, h:0.9, fontFace:F, fontSize:13.5, color:INK2, valign:'middle', isTextBox:true, margin:0 });
    s.addText(r[1], { x:4.7, y:y, w:2.25, h:0.9, fontFace:F, fontSize:18, bold:true, color:INK, valign:'middle', align:'right', isTextBox:true, margin:0 });
    s.addText(r[2], { x:7.0, y:y, w:0.9, h:0.9, fontFace:F, fontSize:9.5, color:MUTED, valign:'middle', align:'right', isTextBox:true, margin:0 });
  });
  card(s, 8.45, 2.05, 4.1, 3.9, 'FDF3E4');
  s.addText('지용근 대표의 고백', { x:8.75, y:2.3, w:3.5, h:0.35, fontFace:F, fontSize:13, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText('“손녀와 5년을 같이 살면서 매일 밤 9시에 기도해 줬습니다. 그런데 기도하는 것 말고는 할 줄 아는 게 없었어요.\n\n교회에서 배운 적이 없으니까요.”',
    { x:8.75, y:2.75, w:3.5, h:3.0, fontFace:F, fontSize:13.5, italic:true, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.32 });
  src(s, '잘잘법 284회 06:16~08:32');
}

/* ─────────────────────────── 12. 가정예배 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '가정예배가 “잔소리 시간”이 되지 않으려면', '08 · 진단');
  card(s, 0.75, 2.05, 3.5, 2.2, 'FBE9E6');
  s.addText('문제', { x:1.05, y:2.28, w:2.9, h:0.35, fontFace:F, fontSize:13, bold:true, color:CORAL, isTextBox:true, margin:0 });
  s.addText('가정예배를 드리는 집 아이들이 가정예배를 싫어합니다.\n이유는 하나 — 그 시간이 잔소리 시간이기 때문입니다.',
    { x:1.05, y:2.7, w:2.9, h:1.4, fontFace:F, fontSize:13.5, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  s.addText('대안 · 교회 소그룹 방식을 가정으로', { x:4.6, y:2.05, w:7.95, h:0.4, fontFace:F, fontSize:15, bold:true, color:AMBER, isTextBox:true, margin:0 });
  const steps = [
    ['부모가 먼저 자기 고민을 말한다', '가르치는 자리에서 내려오는 첫걸음'],
    ['자녀도 자기 고민을 말한다', '수평적 관계에서만 열리는 이야기'],
    ['함께 말씀을 본다', '해석을 강요하지 않고 같이 읽는다'],
    ['같이 기도한다', '아이를 위한 기도가 아니라 함께 드리는 기도'],
  ];
  steps.forEach((t,i)=>{
    const y = 2.55 + i*0.95;
    card(s, 4.6, y, 7.95, 0.8, SOFT);
    numCircle(s, 4.85, y+0.17, i+1, INK);
    s.addText(t[0], { x:5.45, y:y+0.08, w:3.6, h:0.65, fontFace:F, fontSize:14.5, bold:true, color:INK, valign:'middle', isTextBox:true, margin:0 });
    s.addText(t[1], { x:9.15, y:y, w:3.2, h:0.8, fontFace:F, fontSize:11.5, color:MUTED, valign:'middle', align:'right', isTextBox:true, margin:0 });
  });
  s.addText('교사의 역할 : 학부모에게 이 네 단계를 카드 한 장으로 건네는 것', { x:0.75, y:4.55, w:3.5, h:1.6, fontFace:F, fontSize:13, bold:true, color:INK, isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  src(s, '잘잘법 284회 08:34~09:30');
}

/* ─────────────────────────── 13. 섹션 2 ─────────────────────────── */
sectionSlide(2, 'PART', '무엇이 아이를 붙잡는가', '만족과 불만족, 기대와 결단 — 아이들이 직접 말한 답입니다.\n프로그램이 아니라 사람과 경험이 아이를 남게 합니다.');

/* ─────────────────────────── 14. 만족/불만족 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '아이들이 말한 만족 이유와 불만족 이유', '09 · 열쇠');
  const cols = [
    ['만족하는 이유', [['1위','친구'],['2위','목사님 · 전도사님']], TEAL, 'E7F2EF'],
    ['불만족하는 이유', [['1위','예배 (설교)'],['2위','목사님 · 전도사님']], CORAL, 'FBE9E6'],
  ];
  cols.forEach((c,i)=>{
    const x = 0.75 + i*4.1;
    card(s, x, 2.05, 3.85, 2.9, c[3]);
    s.addText(c[0], { x:x+0.3, y:2.3, w:3.25, h:0.4, fontFace:F, fontSize:15, bold:true, color:c[2], isTextBox:true, margin:0 });
    c[1].forEach((r,j)=>{
      s.addText(r[0], { x:x+0.3, y:2.85+j*0.85, w:0.65, h:0.6, fontFace:F, fontSize:13, bold:true, color:MUTED, valign:'middle', isTextBox:true, margin:0 });
      s.addText(r[1], { x:x+0.98, y:2.85+j*0.85, w:2.6, h:0.6, fontFace:F, fontSize:19, bold:true, color:INK, valign:'middle', isTextBox:true, margin:0 });
    });
  });
  card(s, 9.05, 2.05, 3.5, 4.35, INK);
  s.addText('양날의 검', { x:9.35, y:2.32, w:2.9, h:0.35, fontFace:F, fontSize:14, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText([
    { text:'교역자가 만족·불만족 양쪽 2위입니다.\n', options:{ breakLine:true, bold:true, color:WHITE } },
    { text:'\n', options:{ breakLine:true } },
    { text:'여론조사에서 지지·비지지 이유가 똑같이 “경제”로 나오는 것과 같은 구조 — 그만큼 결정적 변수라는 뜻입니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'교회학교는 사역자 한 사람으로 확 부흥하기도, 확 무너지기도 합니다.', options:{ color:AMBER } },
  ], { x:9.35, y:2.78, w:2.9, h:3.4, fontFace:F, fontSize:12.5, color:'C6D0E2', isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  s.addText('“교회학교 안에 신앙적인 친구가 있다면, 그 아이는 절대로 교회를 떠나지 않습니다.”',
    { x:0.75, y:5.2, w:7.95, h:1.1, fontFace:F, fontSize:16, bold:true, italic:true, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  src(s, '잘잘법 284회 09:32~11:40');
}

/* ─────────────────────────── 15. 출석≠신앙 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '출석은 신앙이 아닙니다', '10 · 열쇠');
  s.addChart(p.ChartType.doughnut, [
    { name:'중고등부 학생', labels:['예수를 믿고 있다','믿는지 아닌지 긴가민가하다'], values:[50, 50] },
  ], {
    x:0.75, y:2.0, w:5.3, h:4.2, holeSize:58,
    chartColors:[ TEAL, 'D6DCE6' ],
    showTitle:false, showLegend:true, legendPos:'b', legendFontFace:F, legendFontSize:12, legendColor:INK2,
    showValue:false, showPercent:true, dataLabelFontFace:F, dataLabelFontSize:14, dataLabelFontBold:true, dataLabelColor:'FFFFFF',
  });
  card(s, 6.5, 2.0, 6.05, 4.2, SOFT);
  s.addText('“지금 교회 다니는 아이들 중에 예수 믿는 아이들이 얼마나 될까요?\n절반 정도밖에 안 됩니다.”',
    { x:6.85, y:2.3, w:5.35, h:1.3, fontFace:F, fontSize:18, bold:true, italic:true, color:INK, isTextBox:true, margin:0, lineSpacingMultiple:1.28 });
  s.addText([
    { text:'우리 반 명단에서 ', options:{} },
    { text:'“긴가민가한 절반”', options:{ bold:true, color:CORAL } },
    { text:'은 누구입니까?\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'이름을 댈 수 있다면 사역이 시작되고, 못 댄다면 우리는 아직 출석부만 관리하고 있는 것입니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'※ 오늘 회의 후 과제 : 반별로 이 명단을 작성합니다.', options:{ bold:true, color:INK } },
  ], { x:6.85, y:3.8, w:5.35, h:2.2, fontFace:F, fontSize:14, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  src(s, '잘잘법 284회 10:17~10:40');
}

/* ─────────────────────────── 16. 친구와 찬양 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '아이들이 예배에서 기대하는 두 가지', '11 · 열쇠');
  const two = [
    ['친구', '교회 친구 중 절반은 “이너서클” 안에, 절반은 밖에 있습니다.\n\n전략의 핵심은 밖에 있는 절반을 안으로 들이는 문화와 토양을 만드는 것입니다.', AMBER],
    ['찬양', '찬양을 통해 신앙적으로 결단한 학생이 약 절반입니다.\n\n찬양은 분위기가 아니라 아이들이 실제로 결단하는 접점입니다. 곡 선정에 학생 의견을 넣으십시오.', TEAL],
  ];
  two.forEach((t,i)=>{
    const x = 0.75 + i*4.6;
    card(s, x, 2.05, 4.35, 4.2, SOFT);
    s.addShape(p.ShapeType.ellipse, { x:x+0.35, y:2.4, w:0.75, h:0.75, fill:{ color:t[2] }, line:{ color:t[2] } });
    s.addText(String(i+1), { x:x+0.35, y:2.4, w:0.75, h:0.75, fontFace:F, fontSize:26, bold:true, color:WHITE, align:'center', valign:'middle', isTextBox:true, margin:0 });
    s.addText(t[0], { x:x+1.28, y:2.42, w:2.8, h:0.72, fontFace:F, fontSize:30, bold:true, color:INK, valign:'middle', isTextBox:true, margin:0 });
    s.addText(t[1], { x:x+0.35, y:3.4, w:3.65, h:2.6, fontFace:F, fontSize:13.5, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.32 });
  });
  card(s, 9.95, 2.05, 2.6, 4.2, INK);
  s.addText('그리고\n지금은\n역전되어\n있습니다', { x:10.25, y:2.35, w:2.0, h:1.7, fontFace:F, fontSize:17, bold:true, color:AMBER, isTextBox:true, margin:0, lineSpacingMultiple:1.25 });
  s.addText('과거에는 학교 친구보다 교회 친구가 더 많았습니다.\n\n지금은 자기 삶을 내놓을 수 있는 친구가 교회보다 학교에 훨씬 많습니다.\n\n이 역전을 다시 역전시켜야 합니다.',
    { x:10.25, y:4.05, w:2.0, h:2.0, fontFace:F, fontSize:11.5, color:'C6D0E2', isTextBox:true, margin:0, lineSpacingMultiple:1.28 });
  src(s, '잘잘법 284회 11:40~12:25, 14:10~14:48');
}

/* ─────────────────────────── 17. 수련회 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '신앙 성장을 가장 촉진하는 경험은 수련회였습니다', '12 · 열쇠');
  card(s, 0.75, 2.05, 6.1, 2.35, 'FDF3E4');
  s.addText('1위', { x:1.05, y:2.28, w:1.0, h:0.4, fontFace:F, fontSize:14, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText('여름수련회 · 겨울수련회', { x:1.05, y:2.7, w:5.5, h:0.8, fontFace:F, fontSize:30, bold:true, color:INK, isTextBox:true, margin:0 });
  s.addText('학생들에게 직접 물은 결과입니다. 지용근 대표 자신도 여름수련회에서 예수를 만났습니다.',
    { x:1.05, y:3.55, w:5.5, h:0.7, fontFace:F, fontSize:13, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.25 });
  card(s, 0.75, 4.6, 6.1, 1.65, SOFT);
  s.addText('실행 · 수련회는 여름에 준비하는 행사가 아닙니다', { x:1.05, y:4.82, w:5.5, h:0.35, fontFace:F, fontSize:13.5, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText('연초부터 교사와 부모를 통해 참석을 설득하는 작업을 한 해 사역으로 배치합니다.\n아직 예수님을 모르는 아이일수록 반드시 보내야 합니다.',
    { x:1.05, y:5.22, w:5.5, h:0.85, fontFace:F, fontSize:12.5, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.28 });

  card(s, 7.2, 2.05, 5.35, 4.2, INK);
  s.addText('“한 번만 가자”의 힘', { x:7.55, y:2.32, w:4.65, h:0.4, fontFace:F, fontSize:14, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText([
    { text:'아이가 교회 가는 시간을 아까워했습니다. “그 시간에 학원 가야지.”\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'딱 한 번 강요했습니다. ', options:{} },
    { text:'“수련회 한 번만 가자.”\n', options:{ breakLine:true, bold:true, color:WHITE } },
    { text:'\n', options:{ breakLine:true } },
    { text:'거기서 친구를 사귀었습니다. 그 뒤로 180도 달라져서, 시키지도 않은 송구영신예배까지 스스로 갔습니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'계기는 카톡 한 줄이었습니다.\n', options:{ breakLine:true } },
    { text:'“○○아, 너 오늘 송구영신 올 거야? 와야 돼.”', options:{ bold:true, color:AMBER } },
  ], { x:7.55, y:2.78, w:4.65, h:3.3, fontFace:F, fontSize:13, color:'C6D0E2', isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  src(s, '잘잘법 284회 13:34~14:08, 18:12~19:05');
}

/* ─────────────────────────── 18. 주도성 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '“문학의 밤”은 왜 사라졌을까요', '13 · 열쇠');
  card(s, 0.75, 2.05, 6.1, 2.5, SOFT);
  s.addText('“우리 어릴 때는 문학의 밤을 했습니다. 그때 교사·전도사님은 별로 관여하지 않으셨어요. 우리끼리 콘텐츠를 만들고 포스터를 만들어 동네 벽에 붙였습니다.\n\n그런데 지금 교회학교는 오로지 목사님·전도사님·교사가 다 주도합니다.”',
    { x:1.05, y:2.3, w:5.5, h:2.0, fontFace:F, fontSize:14, italic:true, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.32 });
  s.addText('“학생이 기도·말씀·예배 순서를 직접 담당하는 것에 찬성합니까”',
    { x:7.2, y:2.05, w:5.35, h:0.55, fontFace:F, fontSize:13, color:MUTED, isTextBox:true, margin:0, lineSpacingMultiple:1.2 });
  const votes = [['학생 본인','62%',AMBER],['사역자','89%',TEAL]];
  votes.forEach((v,i)=>{
    const y = 2.68 + i*1.0;
    card(s, 7.2, y, 5.35, 0.85, SOFT);
    s.addText(v[0], { x:7.5, y:y, w:2.6, h:0.85, fontFace:F, fontSize:15, color:INK2, valign:'middle', isTextBox:true, margin:0 });
    s.addText(v[1], { x:10.0, y:y, w:2.25, h:0.85, fontFace:F, fontSize:28, bold:true, color:v[2], align:'right', valign:'middle', isTextBox:true, margin:0 });
  });
  card(s, 7.2, 4.72, 5.35, 1.55, INK);
  s.addText('주도성을 돌려주자', { x:7.5, y:4.95, w:4.75, h:0.4, fontFace:F, fontSize:17, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText('학생도 사역자도 이미 찬성하고 있습니다. 막고 있는 것은 “잘 못할까 봐”라는 우리의 걱정뿐입니다.',
    { x:7.5, y:5.38, w:4.75, h:0.8, fontFace:F, fontSize:12.5, color:'C6D0E2', isTextBox:true, margin:0, lineSpacingMultiple:1.28 });
  s.addText('실행 · 예배 순서 중 최소 하나를 이번 달부터 학생에게 넘깁니다 — 대표기도 / 찬양인도 / 광고 / 간증',
    { x:0.75, y:4.75, w:6.1, h:1.5, fontFace:F, fontSize:14, bold:true, color:INK, isTextBox:true, margin:0, lineSpacingMultiple:1.32 });
  src(s, '잘잘법 284회 12:25~13:32');
}

/* ─────────────────────────── 19. 이탈 예고 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '3명 중 1명 이상이 교회를 떠나겠다고 예고했습니다', '14 · 열쇠');
  s.addText('“앞으로 신앙생활을 어떻게 할 것 같습니까” — 현재 교회 출석 중고등학생 응답 (%)',
    { x:0.75, y:1.72, w:11.8, h:0.3, fontFace:F, fontSize:13, color:MUTED, isTextBox:true, margin:0 });
  s.addChart(p.ChartType.bar, [
    { name:'응답 비율',
      labels:['현재 교회 계속 출석','다른 교회로 이동','교회는 안 나가도\n신앙은 유지','다른 종교로','종교·신앙 모두 버림'],
      values:[49, 13, 22, 3, 11] },
  ], Object.assign({}, CHART_BASE, {
    x:0.75, y:2.2, w:7.9, h:3.95,
    barDir:'col', barGapWidthPct:70,
    chartColors:[ TEAL, 'A9B6CD', CORAL, CORAL, CORAL ], varyColors:true,
    dataLabelPosition:'outEnd', dataLabelColor: INK2,
    valAxisMaxVal:60, catAxisLabelFontSize:11,
  }));
  card(s, 9.0, 2.2, 3.55, 3.95, INK);
  s.addText('37%', { x:9.3, y:2.42, w:2.95, h:1.2, fontFace:F, fontSize:56, bold:true, color:CORAL, isTextBox:true, margin:0 });
  s.addText('교회 이탈 예상 합계', { x:9.3, y:3.62, w:2.95, h:0.4, fontFace:F, fontSize:14, bold:true, color:WHITE, isTextBox:true, margin:0 });
  s.addText('“교회는 안 나가도 신앙은 유지”라는 22%가 가장 큰 덩어리입니다.\n\n이 아이들은 신앙을 버린 것이 아니라 교회를 버린 것입니다.\n\n그렇다면 원인은 신앙이 아니라 교회 쪽에 있습니다.',
    { x:9.3, y:4.08, w:2.95, h:2.0, fontFace:F, fontSize:12, color:'C6D0E2', isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  src(s, '잘잘법 284회 14:48~15:30');
}

/* ─────────────────────────── 20. 섹션 3 ─────────────────────────── */
sectionSlide(3, 'PART', '결정적 간극', '같은 질문을 아이에게, 교사에게, 사역자에게 각각 물었습니다.\n대답이 달랐습니다. 오늘 회의의 핵심은 이 한 장입니다.');

/* ─────────────────────────── 21. ★ 핵심 슬라이드 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '“왜 교회를 떠났습니까” — 세 집단의 다른 대답', '15 · 핵심');
  const g = [
    ['이탈 학생 본인', '예배·설교가\n지루하고 의미가 없다', CORAL, 'FBE9E6', true],
    ['교사', '학업 부담 ·\n심리적 여유 부족', MUTED, SOFT, false],
    ['사역자', '학업 부담 ·\n심리적 여유 부족', MUTED, SOFT, false],
  ];
  g.forEach((c,i)=>{
    const x = 0.75 + i*4.03;
    card(s, x, 2.0, 3.78, 2.85, c[3]);
    s.addText(c[0], { x:x+0.28, y:2.25, w:3.22, h:0.4, fontFace:F, fontSize:14, bold:true, color:c[2], isTextBox:true, margin:0 });
    s.addText('1위로 꼽은 이탈 이유', { x:x+0.28, y:2.62, w:3.22, h:0.3, fontFace:F, fontSize:10.5, color:MUTED, isTextBox:true, margin:0 });
    s.addText(c[1], { x:x+0.28, y:3.0, w:3.22, h:1.6, fontFace:F, fontSize:c[4]?21:19, bold:true, color:c[4]?INK:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.2 });
  });
  card(s, 0.75, 5.1, 11.8, 1.45, INK);
  s.addText([
    { text:'아이는 “예배가 지루해서”라 말하고, 우리는 “공부 때문에”라 말합니다.   ', options:{ color:WHITE, bold:true } },
    { text:'전제가 틀리면 처방도 틀립니다.', options:{ color:AMBER, bold:true } },
  ], { x:1.1, y:5.1, w:11.1, h:1.45, fontFace:F, fontSize:18, valign:'middle', isTextBox:true, margin:0, lineSpacingMultiple:1.25 });
  src(s, '잘잘법 284회 15:30~16:28');
  s.addNotes('후렴구 두 번째 등장. 여기서 잠시 멈추고 교사들에게 물어보십시오 — "우리는 지금까지 무엇 때문이라고 말해 왔습니까?"');
}

/* ─────────────────────────── 22. 결론 인용 ─────────────────────────── */
{
  const s = darkSlide();
  s.addShape(p.ShapeType.ellipse, { x:-2.2, y:4.2, w:5.5, h:5.5, fill:{ color:INK2 }, line:{ color:INK2 } });
  s.addText('지용근 목회데이터연구소 대표의 결론', { x:1.5, y:1.35, w:10.5, h:0.4, fontFace:F, fontSize:14, bold:true, color:AMBER, charSpacing:2, isTextBox:true, margin:0 });
  s.addText('“가르치는 자가\n이 아이들의 세계로\n쑥 들어가지 못했다.”',
    { x:1.5, y:1.95, w:10.5, h:2.7, fontFace:F, fontSize:44, bold:true, color:WHITE, isTextBox:true, margin:0, lineSpacingMultiple:1.18 });
  s.addText('“그래서 앞으로 교회학교, 주일학교 같은 경우는 사역자·교사들이 아이들 세계로 더 들어가야 됩니다.”',
    { x:1.5, y:4.95, w:10.3, h:0.9, fontFace:F, fontSize:17, color:'B9C4DA', isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
  s.addText('잘잘법 284회 16:28~16:42', { x:1.5, y:6.35, w:10.3, h:0.3, fontFace:F, fontSize:11, color:'6F7C99', isTextBox:true, margin:0 });
}

/* ─────────────────────────── 23. 섹션 4 ─────────────────────────── */
sectionSlide(4, 'PART', '그래서 우리는', '교사의 역할이 바뀝니다. 100% 아이가 아니라 50% 아이 + 50% 부모입니다.\n이번 학기에 할 여섯 가지를 정하고 회의를 마칩니다.');

/* ─────────────────────────── 24. 패러다임 전환 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '교사 역할의 재배분', '16 · 전환');
  s.addText('지금까지', { x:0.75, y:2.05, w:5.4, h:0.4, fontFace:F, fontSize:14, bold:true, color:MUTED, isTextBox:true, margin:0 });
  card(s, 0.75, 2.5, 5.4, 1.0, 'D6DCE6');
  s.addText('아이에게 100%', { x:0.75, y:2.5, w:5.4, h:1.0, fontFace:F, fontSize:22, bold:true, color:INK2, align:'center', valign:'middle', isTextBox:true, margin:0 });
  s.addText('앞으로', { x:0.75, y:3.85, w:5.4, h:0.4, fontFace:F, fontSize:14, bold:true, color:AMBER, isTextBox:true, margin:0 });
  card(s, 0.75, 4.3, 2.6, 1.0, INK);
  s.addText('아이 50%', { x:0.75, y:4.3, w:2.6, h:1.0, fontFace:F, fontSize:19, bold:true, color:WHITE, align:'center', valign:'middle', isTextBox:true, margin:0 });
  card(s, 3.55, 4.3, 2.6, 1.0, AMBER);
  s.addText('부모 50%', { x:3.55, y:4.3, w:2.6, h:1.0, fontFace:F, fontSize:19, bold:true, color:INK, align:'center', valign:'middle', isTextBox:true, margin:0 });
  s.addText('교사는 아이와 부모 사이의 매개자가 됩니다', { x:0.75, y:5.45, w:5.4, h:0.9, fontFace:F, fontSize:14, bold:true, color:INK, isTextBox:true, margin:0, lineSpacingMultiple:1.25 });

  card(s, 6.55, 2.05, 6.0, 4.3, SOFT);
  s.addText('매개자로서 교사가 하는 일', { x:6.9, y:2.32, w:5.3, h:0.4, fontFace:F, fontSize:15, bold:true, color:AMBER, isTextBox:true, margin:0 });
  const jobs = [
    '부모에게 아이의 신앙 수준을 알려 준다',
    '부모에게 아이의 교회 안 모습을 전해 준다',
    '부모가 자극받아 스스로 움직이게 만든다',
    '같은 반 학부모끼리 연결해 소그룹이 되게 한다',
    '가정예배 네 단계 카드를 건넨다',
  ];
  jobs.forEach((j,i)=>{
    const y = 2.85 + i*0.66;
    s.addShape(p.ShapeType.ellipse, { x:6.95, y:y+0.09, w:0.26, h:0.26, fill:{ color:INK }, line:{ color:INK } });
    s.addText(j, { x:7.38, y:y, w:4.85, h:0.45, fontFace:F, fontSize:13.5, color:INK2, valign:'middle', isTextBox:true, margin:0 });
  });
  s.addNotes('지용근 대표의 마지막 제안: “부모님이 사역자나 교사들과 정기적으로 대화할 수 있는 시간을 좀 가졌으면 좋겠습니다. 반 선생님과, 그 반 부모들끼리 같이 대화를 하면 교회학교 교육을 현장감 있게 알 수도 있고, 부모님끼리 친해져 소그룹도 하고 삶도 나눌 수 있습니다.”');
  src(s, '잘잘법 284회 16:42~17:35, 19:14~19:55');
}

/* ─────────────────────────── 25. 실행 6가지 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '이번 학기 실행 여섯 가지', '17 · 실행');
  const acts = [
    ['아이들에게 직접 묻는다', '익명 설문 10문항 — “예배에서 가장 지루한 순간은?”'],
    ['소외된 절반을 지명한다', '반별로 이너서클 밖 아이를 실명으로 파악하고 짝을 붙인다'],
    ['주도권을 한 칸 넘긴다', '대표기도 · 찬양인도 · 광고 · 간증 중 최소 하나'],
    ['찬양에 투자한다', '아이들이 결단하는 지점. 곡 선정에 학생 의견 반영'],
    ['교사 시간의 절반을 부모에게', '담당 반 학부모와 학기 1회 이상 통화 또는 만남'],
    ['수련회를 연초부터 준비한다', '신앙 성장 촉진 1위. “한 번만 가자”의 힘'],
  ];
  acts.forEach((a,i)=>{
    const col = i % 2, row = Math.floor(i/2);
    const x = 0.75 + col*6.1, y = 2.05 + row*1.42;
    card(s, x, y, 5.8, 1.22, i<2 ? 'FDF3E4' : SOFT);
    numCircle(s, x+0.28, y+0.38, i+1, i<2 ? AMBER : INK);
    s.addText(a[0], { x:x+0.9, y:y+0.18, w:4.75, h:0.45, fontFace:F, fontSize:15.5, bold:true, color:INK, isTextBox:true, margin:0 });
    s.addText(a[1], { x:x+0.9, y:y+0.63, w:4.75, h:0.48, fontFace:F, fontSize:12, color:MUTED, isTextBox:true, margin:0, lineSpacingMultiple:1.15 });
  });
  s.addText('※ 오늘 회의에서 각 항목의 담당자와 시행 주(週)를 적어 넣습니다.',
    { x:0.75, y:6.45, w:11.8, h:0.35, fontFace:F, fontSize:12.5, bold:true, color:AMBER, isTextBox:true, margin:0 });
}

/* ─────────────────────────── 26. 토의 질문 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '조별 나눔 질문', '18 · 토의');
  const qs = [
    '우리 예배에서 아이들이 지루해하는 구간은 정확히 어디인가? 우리는 물어본 적이 있는가?',
    '우리 반의 “긴가민가한 절반”은 누구인가? 이름을 댈 수 있는가?',
    '지난 학기에 내가 학부모와 실제로 대화한 횟수는 몇 번인가?',
    '학생에게 넘길 수 있는 순서는 무엇이고, 못 넘기는 진짜 이유는 무엇인가?',
    '내가 아이들 앞에서 내 실패담을 마지막으로 말한 게 언제인가?',
  ];
  qs.forEach((q,i)=>{
    const y = 2.1 + i*0.92;
    card(s, 0.75, y, 11.8, 0.78, SOFT);
    s.addText('Q' + (i+1), { x:1.05, y:y, w:0.75, h:0.78, fontFace:F, fontSize:14, bold:true, color:AMBER, valign:'middle', isTextBox:true, margin:0 });
    s.addText(q, { x:1.85, y:y, w:10.4, h:0.78, fontFace:F, fontSize:15, color:INK, valign:'middle', isTextBox:true, margin:0 });
  });
  s.addText('나눔 20분 → 조별 발표 1분씩 → 실행 여섯 가지에 담당자 기입',
    { x:0.75, y:6.75, w:11.8, h:0.35, fontFace:F, fontSize:12.5, color:MUTED, isTextBox:true, margin:0 });
}

/* ─────────────────────────── 27. 부록 A ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '아이들의 세계에 들어간 설교란 무엇인가', '부록 A');
  s.addText('세 가지가 동시에 있어야 합니다. 하나라도 빠지면 강의·상담·잔소리가 됩니다.',
    { x:0.75, y:1.72, w:11.8, h:0.3, fontFace:F, fontSize:13, color:MUTED, isTextBox:true, margin:0 });
  const three = [
    ['본문의 진실', '주해가 살아 있는가', '들어감은 주해를 건너뛰는 면허가 아닙니다. 원어·배경·문맥을 먼저 끝냅니다.', INK],
    ['아이의 실제 질문', '내가 이 아이의 한 주를 아는가', '유행어를 외우는 것은 들어감이 아닙니다. 한 아이의 시험 일정을 아는 것이 들어감입니다.', AMBER],
    ['살 수 있는 형태', '월요일에 들고 갈 것이 있는가', '감동으로 끝내지 않습니다. 작고 구체적이고 오늘 할 수 있는 것 하나를 건넵니다.', TEAL],
  ];
  three.forEach((t,i)=>{
    const x = 0.75 + i*4.03;
    card(s, x, 2.15, 3.78, 3.0, SOFT);
    s.addShape(p.ShapeType.ellipse, { x:x+0.28, y:2.45, w:0.62, h:0.62, fill:{ color:t[3] }, line:{ color:t[3] } });
    s.addText(String(i+1), { x:x+0.28, y:2.45, w:0.62, h:0.62, fontFace:F, fontSize:20, bold:true, color:WHITE, align:'center', valign:'middle', isTextBox:true, margin:0 });
    s.addText(t[0], { x:x+0.28, y:3.2, w:3.22, h:0.45, fontFace:F, fontSize:18, bold:true, color:INK, isTextBox:true, margin:0 });
    s.addText(t[1], { x:x+0.28, y:3.63, w:3.22, h:0.35, fontFace:F, fontSize:12, color:t[3], isTextBox:true, margin:0 });
    s.addText(t[2], { x:x+0.28, y:4.05, w:3.22, h:1.0, fontFace:F, fontSize:12.5, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.28 });
  });
  card(s, 0.75, 5.42, 11.8, 1.1, INK);
  s.addText('“들어간 설교”의 반대말은 어려운 설교가 아니라, 아이의 세계를 모르는 설교입니다.',
    { x:1.1, y:5.42, w:11.1, h:1.1, fontFace:F, fontSize:16.5, bold:true, color:AMBER, valign:'middle', isTextBox:true, margin:0 });
}

/* ─────────────────────────── 28. 부록 B — 성경적 근거 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '왜 “들어가는 것”이 복음의 방식인가', '부록 B · 성경적 근거');
  const bib = [
    ['요 1:14', 'ἐσκήνωσεν', '에스케노센 · σκηνόω', '“우리 가운데 장막을 치셨다.” 어근 σκηνή는 출애굽기의 성막. 방문(visit)이 아니라 거주(dwell)입니다.'],
    ['빌 2:7', 'ἐκένωσεν', '에케노센 · κενόω (케노시스)', '“자기를 비워.” 비우신 것은 신성이 아니라 높은 자리에서 내려다보며 말할 권리였습니다.'],
    ['고전 9:22', 'γέγονα πάντα', '게고나 판타 · 완료형', '“여러 사람에게 여러 모습이 된 것은.” 바울은 복음을 바꾸지 않았습니다. 자기 자신을 바꿨습니다.'],
  ];
  bib.forEach((b,i)=>{
    const y = 2.05 + i*1.3;
    card(s, 0.75, y, 8.3, 1.12, SOFT);
    s.addText(b[0], { x:1.05, y:y+0.1, w:1.5, h:0.4, fontFace:F, fontSize:13, bold:true, color:AMBER, isTextBox:true, margin:0 });
    s.addText(b[1], { x:1.05, y:y+0.5, w:2.4, h:0.5, fontFace:F, fontSize:20, bold:true, color:INK, isTextBox:true, margin:0 });
    s.addText(b[2], { x:3.5, y:y+0.12, w:5.3, h:0.32, fontFace:F, fontSize:11, color:MUTED, isTextBox:true, margin:0 });
    s.addText(b[3], { x:3.5, y:y+0.44, w:5.3, h:0.62, fontFace:F, fontSize:12.5, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.2 });
  });
  card(s, 9.4, 2.05, 3.15, 3.9, INK);
  s.addText('교부와 개혁자', { x:9.7, y:2.3, w:2.55, h:0.35, fontFace:F, fontSize:13, bold:true, color:AMBER, isTextBox:true, margin:0 });
  s.addText([
    { text:'크리소스톰\n', options:{ breakLine:true, bold:true, color:WHITE } },
    { text:'συγκατάβασις (신카타바시스) — 하나님의 “함께 내려오심”. 하나님은 듣는 자의 높이에서 말씀하십니다.\n', options:{ breakLine:true } },
    { text:'\n', options:{ breakLine:true } },
    { text:'칼뱅\n', options:{ breakLine:true, bold:true, color:WHITE } },
    { text:'accommodatio — “하나님은 우리에게 혀 짧은 소리로 옹알이하듯 말씀하신다.”(『기독교 강요』 I.13.1)', options:{} },
  ], { x:9.7, y:2.72, w:2.55, h:3.1, fontFace:F, fontSize:11.5, color:'C6D0E2', isTextBox:true, margin:0, lineSpacingMultiple:1.28 });
  s.addText('예수의 방식 ·  막 10:16 ἐναγκαλισάμενος “품에 안으시고”   |   눅 24:15 συνεπορεύετο “함께 걸으시며” 먼저 질문하심   |   요 4:7 “물을 좀 달라” — 필요를 가진 자로 먼저 서심',
    { x:0.75, y:6.05, w:11.8, h:0.6, fontFace:F, fontSize:12, color:INK2, isTextBox:true, margin:0, lineSpacingMultiple:1.25 });
}

/* ─────────────────────────── 29. 부록 C — 자료 ─────────────────────────── */
{
  const s = lightSlide();
  title(s, '더 공부할 자료', '부록 C');
  card(s, 0.75, 2.05, 5.85, 4.3, SOFT);
  s.addText('책', { x:1.05, y:2.3, w:5.25, h:0.4, fontFace:F, fontSize:15, bold:true, color:AMBER, isTextBox:true, margin:0 });
  const books = [
    ['『십대의 마음을 꿰뚫는 설교』', '덕 필즈 · 더피 로빈스 | 국제제자훈련원\n이 주제의 정본. 로고스·에토스·파토스로 분해'],
    ['『청소년 사역 핵심파일』', '정석원 | 홍성사\n청소년을 “미래”가 아닌 현재의 소청년으로'],
    ['『어쩌다 청소년 사역』', '김성중 | 두란노\n청소년부 운영 실무 노하우'],
    ['『365일 심방하는 목사』', '이세종\n고등부 5년, 출석 70명 → 110~120명의 기록'],
  ];
  books.forEach((b,i)=>{
    const y = 2.78 + i*0.88;
    s.addText(b[0], { x:1.05, y:y, w:5.25, h:0.3, fontFace:F, fontSize:13.5, bold:true, color:INK, isTextBox:true, margin:0 });
    s.addText(b[1], { x:1.05, y:y+0.28, w:5.25, h:0.5, fontFace:F, fontSize:11, color:MUTED, isTextBox:true, margin:0, lineSpacingMultiple:1.18 });
  });

  card(s, 6.95, 2.05, 5.6, 4.3, INK);
  s.addText('영상', { x:7.25, y:2.3, w:5.0, h:0.4, fontFace:F, fontSize:15, bold:true, color:AMBER, isTextBox:true, margin:0 });
  const vids = [
    ['잘잘법 284회 — 오늘의 원자료', 'youtu.be/SgWydfzNVpo'],
    ['잘잘법 242회 — 수련회 못 가는 청소년을 위한 온라인 수련회 (강은도 목사)', 'youtu.be/-SDDRonuP_A'],
    ['잘잘클립 — 수련회 왔는데 목사님이 2시간 기도시켜요', 'youtu.be/DGSwlS9BB-k'],
    ['잘잘법 283회 — 대화법을 배운 적 없는 우리는 (박재연 소장)', 'youtu.be/NB71LgUMqWQ'],
    ['번개탄TV — 다음세대 전문 방송국 (임우현 목사)', 'youtube.com/@next_christiantv'],
  ];
  vids.forEach((v,i)=>{
    const y = 2.72 + i*0.72;
    s.addText(v[0], { x:7.25, y:y, w:5.0, h:0.48, fontFace:F, fontSize:11.5, bold:true, color:WHITE, isTextBox:true, margin:0, lineSpacingMultiple:1.12 });
    s.addText(v[1], { x:7.25, y:y+0.46, w:5.0, h:0.26, fontFace:F, fontSize:10, color:AMBER, isTextBox:true, margin:0 });
  });
  src(s, '상세 정리본 : 다음세대/아이들의_세계에_들어간_설교_자료집.md');
}

/* ─────────────────────────── 30. 클로징 ─────────────────────────── */
{
  const s = darkSlide();
  s.addShape(p.ShapeType.ellipse, { x:10.2, y:3.9, w:5.6, h:5.6, fill:{ color:INK2 }, line:{ color:INK2 } });
  s.addText('요한복음 1:14', { x:1.3, y:1.5, w:10.5, h:0.4, fontFace:F, fontSize:14, bold:true, color:AMBER, charSpacing:2, isTextBox:true, margin:0 });
  s.addText('강단 위에서 내려다보며 외치는 말은 방문이고,\n아이의 자리까지 내려가 함께 앉아 하는 말은 거주입니다.',
    { x:1.3, y:2.15, w:10.6, h:1.9, fontFace:F, fontSize:29, bold:true, color:WHITE, isTextBox:true, margin:0, lineSpacingMultiple:1.28 });
  s.addText('말씀은 우리 가운데 방문하지 않으시고,  장막을 치셨습니다.',
    { x:1.3, y:4.35, w:10.6, h:0.7, fontFace:F, fontSize:22, color:AMBER, isTextBox:true, margin:0 });
  s.addText('그러므로 아이들의 세계로 들어가는 것은 사역의 기술이 아니라, 복음이 우리에게 온 방식 그 자체입니다.',
    { x:1.3, y:5.35, w:10.0, h:0.7, fontFace:F, fontSize:14.5, color:'8D9AB5', isTextBox:true, margin:0, lineSpacingMultiple:1.3 });
}

p.writeFile({ fileName: '중고등부_교사회의_아이들의세계로.pptx' }).then(f => console.log('WROTE', f));
