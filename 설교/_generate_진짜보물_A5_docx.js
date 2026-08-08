// 진짜 보물, 예수 그리스도 (마 6:19-24) — A5 / 본문 12pt
// 순복음 sermon-formatter 하우스 스타일을 A5·12pt로 조정

const {
  Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle, ShadingType
} = require('docx');
const fs = require('fs');

const F = "맑은 고딕";
const BLUE = "1F497D";
const BODY = 24;   // 12pt

function makeTitle(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 100 },
    children: [new TextRun({ text, font: F, size: 34, bold: true })]
  });
}

function makeSubtitle(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text, font: F, size: 24, bold: true })]
  });
}

function makeInfo(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 160 },
    children: [new TextRun({ text, font: F, size: 18, color: "777777" })]
  });
}

// 본문 성경 전문 박스 (여러 줄)
function makeScriptureBlock(lines) {
  const kids = [];
  lines.forEach((l, i) => {
    if (i > 0) kids.push(new TextRun({ break: 1 }));
    kids.push(new TextRun({ text: l, font: F, size: 21, color: "333333" }));
  });
  return new Paragraph({
    spacing: { before: 100, after: 160, line: 300 },
    indent: { left: 200, right: 200 },
    border: {
      top:    { style: BorderStyle.SINGLE, size: 4,  color: "888888" },
      bottom: { style: BorderStyle.SINGLE, size: 4,  color: "888888" },
      left:   { style: BorderStyle.SINGLE, size: 12, color: BLUE },
    },
    children: kids
  });
}

function makeHeading(text) {
  return new Paragraph({
    spacing: { before: 280, after: 100 },
    keepNext: true,
    children: [new TextRun({ text, font: F, size: 26, bold: true, color: BLUE })]
  });
}

function makeVerseLabel(text) {
  return new Paragraph({
    spacing: { before: 160, after: 0 },
    keepNext: true,
    children: [new TextRun({ text, font: F, size: 23, bold: true })]
  });
}

function makeVerseText(text) {
  return new Paragraph({
    spacing: { before: 50, after: 60, line: 300 },
    indent: { left: 300 },
    children: [new TextRun({ text, font: F, size: 23, italics: true, color: BLUE })]
  });
}

function makeBody(text) {
  return new Paragraph({
    spacing: { before: 70, after: 70, line: 312 },
    indent: { firstLine: 240 },
    children: [new TextRun({ text, font: F, size: BODY })]
  });
}

// 청중에게 던지는 질문 / 강조 문장 — 가운데 굵게
function makeQuestion(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 140, after: 140 },
    children: [new TextRun({ text, font: F, size: BODY, bold: true })]
  });
}

// 후렴구(핵심 한 문장) — 음영 박스, 가운데
function makeRefrain(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 160, after: 160 },
    indent: { left: 100, right: 100 },
    shading: { type: ShadingType.CLEAR, fill: "EAF1F8" },
    border: {
      top:    { style: BorderStyle.SINGLE, size: 6, color: BLUE },
      bottom: { style: BorderStyle.SINGLE, size: 6, color: BLUE },
      left:   { style: BorderStyle.SINGLE, size: 6, color: BLUE },
      right:  { style: BorderStyle.SINGLE, size: 6, color: BLUE },
    },
    children: [new TextRun({ text, font: F, size: BODY, bold: true, color: BLUE })]
  });
}

// 중고등부 보충란 — 음영 박스, 좌측 주황선
function makeKidsBox(text) {
  return new Paragraph({
    spacing: { before: 160, after: 160, line: 300 },
    indent: { left: 200, right: 100 },
    shading: { type: ShadingType.CLEAR, fill: "FFF6E5" },
    border: {
      top:    { style: BorderStyle.SINGLE, size: 4,  color: "E8B96A" },
      bottom: { style: BorderStyle.SINGLE, size: 4,  color: "E8B96A" },
      left:   { style: BorderStyle.SINGLE, size: 14, color: "D98E20" },
      right:  { style: BorderStyle.SINGLE, size: 4,  color: "E8B96A" },
    },
    children: [
      new TextRun({ text: "중고등부를 위한 한마디", font: F, size: 21, bold: true, color: "9C5B0A" }),
      new TextRun({ break: 1 }),
      new TextRun({ text, font: F, size: 22, color: "4A3208" })
    ]
  });
}

function makeDivider() {
  return new Paragraph({
    spacing: { before: 140, after: 140 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: "CCCCCC" } },
    children: [new TextRun("")]
  });
}

function makeEmpty() {
  return new Paragraph({ spacing: { before: 30, after: 30 }, children: [new TextRun("")] });
}

// 설교 노트 (마지막 페이지)
function makeNoteTitle(text) {
  return new Paragraph({
    spacing: { before: 240, after: 80 },
    children: [new TextRun({ text, font: F, size: 22, bold: true, color: "666666" })]
  });
}
function makeNote(text) {
  return new Paragraph({
    spacing: { before: 40, after: 40, line: 280 },
    children: [new TextRun({ text, font: F, size: 18, color: "666666" })]
  });
}

const REFRAIN = "땅에 쌓으면 내가 그 보물의 것이 되고, 하늘에 쌓으면 그 보물이 내 것이 됩니다.";

const doc = new Document({
  styles: { default: { document: { run: { font: F, size: BODY } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 8391, height: 11906 },              // A5 (148 x 210mm)
        margin: { top: 1020, right: 907, bottom: 1020, left: 907 }
      }
    },
    children: [

      makeTitle("진짜 보물, 예수 그리스도"),
      makeSubtitle("마태복음 6장 19절 ~ 24절"),
      makeInfo("전 세대 통합 (장년 · 중고등부)  /  약 30분"),

      makeScriptureBlock([
        "19 너희를 위하여 보물을 땅에 쌓아 두지 말라 거기는 좀과 동록이 해하며 도둑이 구멍을 뚫고 도둑질하느니라",
        "20 오직 너희를 위하여 보물을 하늘에 쌓아 두라 거기는 좀이나 동록이 해하지 못하며 도둑이 구멍을 뚫지도 못하고 도둑질도 못하느니라",
        "21 네 보물 있는 그 곳에는 네 마음도 있느니라",
        "22 눈은 몸의 등불이니 그러므로 네 눈이 성하면 온 몸이 밝을 것이요",
        "23 눈이 나쁘면 온 몸이 어두울 것이니 그러므로 네게 있는 빛이 어두우면 그 어둠이 얼마나 더하겠느냐",
        "24 한 사람이 두 주인을 섬기지 못할 것이니 혹 이를 미워하고 저를 사랑하거나 혹 이를 중히 여기고 저를 경히 여김이라 너희가 하나님과 재물을 겸하여 섬기지 못하느니라"
      ]),
      makeDivider(),

      // ───────── 서론 ─────────
      makeHeading("서론 ─ 잃으면 가장 무너지는 것 (4분)"),

      makeBody("조금 불편한 질문으로 시작하겠습니다."),
      makeQuestion("“내가 지금 가진 것 중에, 잃어버리면"),
      makeQuestion("내 인생 전체가 무너질 것 같은 것은 무엇입니까?”"),
      makeBody("돈일 수도 있습니다. 건강일 수도 있고, 자녀일 수도 있고, 지금 앉아 있는 그 자리일 수도 있습니다. 학생이라면 성적일 수도, 친한 친구일 수도 있습니다. 방금 떠오른 그것을 성경은 “보물”이라고 부릅니다. 오늘 말씀은 바로 그것에 관한 이야기입니다."),
      makeBody("시작하기 전에 오해 하나를 풀겠습니다. 오늘 말씀은 “가진 것을 다 버려라”가 아닙니다. 19절과 20절을 나란히 놓고 보십시오. 예수님은 19절에서 “너희를 위하여” 땅에 쌓지 말라 하시고, 20절에서도 똑같이 “너희를 위하여” 하늘에 쌓으라 하십니다."),
      makeBody("“너희를 위하여”가 양쪽에 다 있습니다. 예수님은 “너한테 좋은 걸 바라지 마라”고 하지 않으셨습니다. “너한테 진짜 좋은 게 어디 있는지 보라”고 하신 겁니다."),
      makeBody("그렇다고 “욕심은 괜찮으니 대상만 바꿔라”는 뜻은 절대 아닙니다. 성경은 욕심에 대해 아주 단호합니다."),

      makeVerseLabel("골로새서 3장 5절입니다."),
      makeVerseText("그러므로 땅에 있는 지체를 죽이라 곧 음란과 부정과 사욕과 악한 정욕과 탐심이니 탐심은 우상 숭배니라"),

      makeBody("“탐심”은 더 갖고 싶어 못 견디는 마음입니다. 성경은 그것을 죽이라고 합니다. 그냥 참으라가 아니라 죽이라입니다. 그리고 오늘 본문과 짝을 이루는 누가복음은 아예 이 말씀으로 시작합니다."),

      makeVerseLabel("누가복음 12장 15절입니다."),
      makeVerseText("그들에게 이르시되 삼가 모든 탐심을 물리치라 사람의 생명이 소유의 넉넉한 데 있지 아니하니라 하시고"),

      makeBody("그러니 오늘 우리는 두 가지를 함께 들어야 합니다. 움켜쥔 손을 펴라는 명령과, 더 좋은 것을 보라는 초대입니다. 이 둘은 언제나 같이 갑니다."),
      makeBody("오늘 이 말씀에서 여러분이 가져가실 것은 이겁니다. 예수님이 물으시는 세 가지 ─ 나는 무엇을 쌓고 있나, 무엇을 보고 있나, 누구의 것인가 ─ 그리고 이번 주에 바로 해볼 실천 하나입니다. 오늘의 한 문장을 미리 드립니다."),

      makeRefrain(REFRAIN),
      makeDivider(),

      // ───────── 1대지 ─────────
      makeHeading("첫째 ─ 무엇을 쌓고 있습니까 (19~21절, 6분)"),

      makeBody("“쌓아 두지 말라.”"),
      makeBody("성경이 처음 쓰인 말로 보면, 여기 “보물”과 “쌓다”가 뿌리가 같은 낱말입니다. 그대로 옮기면 “보물을 보물로 쌓지 말라”가 됩니다. 같은 말을 일부러 두 번 겹쳐 쓴 것인데, 힘주어 말할 때 쓰는 방식입니다."),
      makeBody("그리고 이 명령은 한 번 하는 행동이 아니라 계속하는 행동을 가리키는 모양으로 되어 있습니다. 그러니까 “이번 달 적금 붓지 마라”, “집 한 채 마련하지 마라”가 아닙니다. “모으는 것 자체를 네 인생의 목표로 삼지 마라”는 뜻입니다."),
      makeBody("그러면 왜 그러면 안 됩니까? 예수님은 “그건 나쁜 짓이야”라고 하지 않으십니다. “그건 안 지켜져”라고 하십니다. 세 가지를 드십니다."),
      makeBody("좀 ─ 옷을 갉아먹는 작은 벌레입니다. 그때는 좋은 옷이 큰 재산이었습니다. 지금으로 치면 통장 같은 것이었죠. 그런데 그 옷을 벌레가 조용히 갉아먹습니다."),
      makeBody("동록 ─ 쇠에 스는 녹입니다. 원래 낱말은 “갉아먹는 것”이라는 뜻이라서, 쇠에 녹이 스는 것으로도, 쌓아 둔 곡식을 쥐와 벌레가 먹어 치우는 것으로도 볼 수 있습니다."),
      makeBody("도둑이 구멍을 뚫고 ─ 여기 “뚫다”는 말은 “파고 들어간다”는 뜻입니다. 그때 보통 집은 흙벽돌로 지었습니다. 그래서 도둑은 문을 부수지 않고 벽을 파서 들어왔습니다. 사람들은 귀한 것을 집 안 땅에 묻어 두었는데, 벽 하나 뚫리면 평생 모은 게 하룻밤에 사라졌습니다."),
      makeBody("여기서 꼭 보셔야 할 게 있습니다. 셋 다 내가 막을 수 없습니다. 좀은 내가 자는 동안 옷장 안에서 일합니다. 녹은 아무도 손대지 않아도 저절로 슬어 갑니다. 도둑은 내가 대비할수록 더 교묘해집니다."),
      makeBody("그래서 땅에 쌓는 인생에는 반드시 따라오는 게 하나 있습니다. 불안입니다. 이건 제 짐작이 아닙니다. 예수님이 이 말씀 바로 뒤에 하시는 말씀이 이겁니다."),

      makeVerseLabel("마태복음 6장 25절입니다."),
      makeVerseText("그러므로 내가 너희에게 이르노니 목숨을 위하여 무엇을 먹을까 무엇을 마실까 몸을 위하여 무엇을 입을까 염려하지 말라 목숨이 음식보다 중하지 아니하며 몸이 의복보다 중하지 아니하냐"),

      makeBody("보물 이야기 다음이 곧바로 걱정 이야기입니다. 왜냐하면 땅에 쌓는 것과 걱정하는 것은 한 몸이기 때문입니다. 많이 쌓을수록 지킬 게 많아지고, 지킬 게 많을수록 잠이 얕아집니다."),
      makeBody("그리고 21절, 오늘 말씀의 심장이 나옵니다."),

      makeVerseLabel("본문말씀 21절입니다."),
      makeVerseText("네 보물 있는 그 곳에는 네 마음도 있느니라"),

      makeBody("순서를 놓치지 마십시오. 마음이 먼저가 아닙니다. 보물이 먼저고, 마음이 그 뒤를 따라갑니다. 우리는 늘 “마음부터 고쳐먹어야지” 합니다. 그런데 마음은 결심만으로 잘 안 움직입니다. 예수님이 알려 주신 길은 다릅니다. 내 것을 어디에 두느냐를 바꾸면, 마음이 그리로 따라옵니다."),
      makeBody("이건 우리가 이미 아는 일입니다. 돈을 넣은 곳은 하루에도 몇 번씩 확인하게 됩니다. 기도해 준 사람은 자꾸 생각납니다. 시간을 쏟은 일에는 정이 붙습니다."),
      makeBody("그래서 아주 정직한 확인 방법이 하나 생깁니다. 내 마음이 어디 있는지 알고 싶으면, 지난 한 달 내 시간과 돈이 어디로 갔는지 보면 됩니다. 입은 거짓말을 하지만, 통장과 시간표는 거짓말을 못 합니다."),

      makeKidsBox("“저는 하나님을 제일 사랑해요”라고 말하는 건 쉬워요. 그런데 지난 일주일에 내가 제일 오래 붙잡고 있던 게 뭐였는지 떠올려 보세요. 휴대폰? 게임? 성적? 그게 지금 내 마음이 사는 주소예요. 혼내려는 게 아니에요. 네가 지금 어디 서 있는지 너 스스로 한번 보라는 거예요."),
      makeDivider(),

      // ───────── 2대지 ─────────
      makeHeading("둘째 ─ 무엇을 보고 있습니까 (22~23절, 5분)"),

      makeBody("갑자기 눈 이야기가 나옵니다. 뜬금없어 보이지만, 보물 이야기 한가운데 있습니다. 이유가 있습니다."),
      makeBody("“눈이 성하다”는 말은 원래 “하나다, 나뉘지 않았다”는 뜻입니다. 그리고 이 낱말의 짝이 되는 말은 성경에서 종종 “너그럽게 베푼다”는 뜻으로 쓰입니다."),
      makeBody("반대로 “눈이 나쁘다”는 “악하다”는 말인데, 그 시대 사람들에게 “악한 눈”은 인색한 사람, 움켜쥐고 안 내놓는 사람을 가리키는 익숙한 표현이었습니다. 성경에 그대로 나옵니다."),

      makeVerseLabel("잠언 28장 22절입니다."),
      makeVerseText("악한 눈이 있는 자는 재물을 얻기에만 급하고 빈궁이 자기에게로 임할 줄은 알지 못하느니라"),

      makeVerseLabel("잠언 22장 9절입니다."),
      makeVerseText("선한 눈을 가진 자는 복을 받으리니 이는 양식을 가난한 자에게 줌이니라"),

      makeBody("보이십니까? 성경에서 눈은 손과 연결됩니다. 눈이 한 곳을 보고 손이 펴져 있으면 온 삶이 밝습니다. 눈이 돈에 붙어 손이 오그라들면 온 삶이 어두워집니다."),
      makeBody("그리고 23절 마지막 문장이 오늘 본문에서 제일 무섭습니다."),

      makeVerseLabel("본문말씀 23절 하반절입니다."),
      makeVerseText("그러므로 네게 있는 빛이 어두우면 그 어둠이 얼마나 더하겠느냐"),

      makeBody("등불이 꺼졌다는 말이 아닙니다. 등불인 줄 알았던 것이 사실은 어둠이었다는 말입니다. 이게 왜 무섭습니까. 등불이 꺼진 사람은 어두운 줄이라도 압니다. 그런데 어둠을 등불로 착각한 사람은 자기가 잘 가고 있다고 믿으면서 열심히 걸어갑니다. 열심일수록 더 깊이 들어갑니다."),
      makeBody("가족을 위한다며 평생 일했는데 정작 가족을 잃어버린 사람이 있습니다. 자녀를 위한다며 몰아붙였는데 자녀 마음을 잃어버린 사람이 있습니다. 방향이 틀리면 성실함이 오히려 더 멀리 데려갑니다."),

      makeKidsBox("밤길에 손전등을 켰는데 그게 사실 반대쪽을 비추고 있었다면, 열심히 걸을수록 어떻게 될까요? 더 멀어지죠. 예수님은 “네가 등불이라고 믿는 그거, 진짜 등불 맞니?” 하고 물으세요. 성적이 내 인생의 등불이면, 성적 떨어지는 날 내 인생 전체가 캄캄해집니다. 한 번 무너질 때 나까지 무너지게 만드는 건, 등불이 아니라 함정이에요."),
      makeDivider(),

      // ───────── 3대지 ─────────
      makeHeading("셋째 ─ 누구의 것입니까 (24절, 5분)"),

      makeBody("여기 “섬기다”로 옮긴 말은, 그냥 일해 준다는 뜻이 아닙니다. 종으로서 그 사람에게 속해 있다는 뜻입니다. 이걸 알면 24절이 다르게 들립니다."),
      makeBody("요즘은 일을 두 개 할 수 있습니다. 낮에 한 곳, 저녁에 한 곳. 그래서 우리는 생각합니다. “하나님도 섬기고 돈도 좀 챙기고, 적당히 같이 하면 되지 않나?”"),
      makeBody("그런데 예수님이 쓰신 말은 직원이 아니라 종입니다. 직원은 시간을 파는 사람이지만, 종은 자기 자신이 주인의 것인 사람입니다. 그래서 마음을 반으로 나눌 수가 없습니다. 예수님이 “어렵다”고 하지 않으시고 “못 한다”고 하신 이유입니다."),
      makeBody("그리고 여기 “재물”로 번역된 말이 “맘몬”입니다. 예수님이 이 말을 굳이 번역하지 않고 그대로 쓰신 데 주목하십시오. 마치 사람 이름처럼, 사람을 부리는 가짜 주인처럼 쓰셨습니다. 돈을 물건이 아니라 주인 자리에 앉혀 놓고 말씀하신 겁니다."),
      makeBody("오해하지 마십시오. 돈이 나쁜 게 아닙니다. 성경은 아주 정확하게 말합니다."),

      makeVerseLabel("디모데전서 6장 10절입니다."),
      makeVerseText("돈을 사랑함이 일만 악의 뿌리가 되나니 이것을 탐내는 자들은 미혹을 받아 믿음에서 떠나 많은 근심으로써 자기를 찔렀도다"),

      makeBody("“돈이 악의 뿌리”가 아니라 “돈을 사랑함이” 악의 뿌리입니다. 돈은 아주 좋은 도구이고, 아주 나쁜 주인입니다. 도구일 때는 사람을 살리고, 주인이 되면 사람을 부립니다. 예수님이 물으시는 것은 “네 통장에 얼마 있냐”가 아니라 “너는 누구 것이냐”입니다."),

      makeKidsBox("여러분에게 맘몬은 꼭 돈이 아닐 수 있어요. 내 기분을 좌우하고, 내 하루를 정하고, 그게 없으면 못 견디는 것 ─ 그게 지금 내 주인이에요. 성적일 수도, 인기일 수도, 게임일 수도 있죠. “내가 그걸 갖고 있는 걸까, 그게 나를 갖고 있는 걸까?” 오늘 이 질문 하나만 가져가세요."),
      makeDivider(),

      // ───────── 4대지 ─────────
      makeHeading("넷째 ─ 그러면 진짜 보물은 누구입니까 (6분)"),

      makeBody("여기까지 들으면 이런 생각이 드실 겁니다. “맞는 말인데, 그래서 뭘 어쩌라는 겁니까?”"),
      makeBody("예수님은 하늘 창고에 뭐가 들었는지 여기서 말씀하지 않으십니다. 그런데 마태복음 13장에서 두 개의 짧은 이야기로 답하십니다."),

      makeVerseLabel("마태복음 13장 44절입니다."),
      makeVerseText("천국은 마치 밭에 감추인 보화와 같으니 사람이 이를 발견한 후 숨겨 두고 기뻐하며 돌아가서 자기의 소유를 다 팔아 그 밭을 샀느니라"),

      makeVerseLabel("마태복음 13장 45절~46절입니다."),
      makeVerseText("또 천국은 마치 좋은 진주를 구하는 장사와 같으니 극히 값진 진주 하나를 발견하매 가서 자기의 소유를 다 팔아 그 진주를 샀느니라"),

      makeBody("44절에 있는 한 낱말을 보십시오. “기뻐하며”입니다. 그 사람은 아까워하며 억지로 판 게 아닙니다. 눈물 흘리며 판 게 아닙니다. 더 좋은 걸 봤기 때문에 나머지가 시시해진 겁니다."),
      makeBody("우리가 땅의 것을 못 놓는 이유는 의지가 약해서가 아닙니다. 아직 더 좋은 걸 못 봤기 때문입니다. 바울이 딱 그 고백을 합니다."),

      makeVerseLabel("빌립보서 3장 8절입니다."),
      makeVerseText("또한 모든 것을 해로 여김은 내 주 그리스도 예수를 아는 지식이 가장 고상하기 때문이라 내가 그를 위하여 모든 것을 잃어버리고 배설물로 여김은 그리스도를 얻고"),

      makeBody("바울은 다 버린 사람이 아니라 더 큰 걸 얻은 사람입니다. 손해 본 얼굴이 아니라 남는 장사를 한 얼굴입니다."),
      makeBody("그런데 진짜 놓치면 안 되는 게 있습니다. 오늘 이 말씀이 예수님 자신의 이야기라는 것입니다."),

      makeVerseLabel("고린도후서 8장 9절입니다."),
      makeVerseText("우리 주 예수 그리스도의 은혜를 너희가 알거니와 부요하신 이로서 너희를 위하여 가난하게 되심은 그의 가난함으로 말미암아 너희를 부요하게 하려 하심이라"),

      makeBody("하늘의 모든 걸 가지신 분이 자기 창고를 다 비우고 오셨습니다. 사시는 동안 집 한 채 없으셨습니다."),

      makeVerseLabel("마태복음 8장 20절입니다."),
      makeVerseText("예수께서 이르시되 여우도 굴이 있고 공중의 새도 거처가 있으되 오직 인자는 머리 둘 곳이 없다 하시더라"),

      makeBody("그리고 십자가에서는 마지막 남은 옷 한 벌까지 잃으셨습니다."),

      makeVerseLabel("요한복음 19장 24절입니다."),
      makeVerseText("군인들이 서로 말하되 이것을 찢지 말고 누가 얻나 제비 뽑자 하니 이는 성경에 그들이 내 옷을 나누고 내 옷을 제비 뽑나이다 한 것을 응하게 하려 함이러라 군인들은 이런 일을 하고"),

      makeBody("세상에서 가장 완벽하게 다 잃으신 분입니다. 왜 그러셨습니까? 성경은 하나님이 자기 백성을 어떻게 부르시는지 이렇게 말합니다."),

      makeVerseLabel("말라기 3장 17절입니다."),
      makeVerseText("만군의 여호와가 이르노라 나는 나의 특별한 소유를 삼는 날에 그들을 내 것으로 삼고 또 사람이 자기를 섬기는 아들을 아낌 같이 내가 그들을 아끼리니"),

      makeBody("하나님이 우리를 자기 보물이라고 부르십니다. 그러니 21절 ─ 보물 있는 곳에 마음이 있다 ─ 이 원리가 우리에게 오기 전에, 하나님께 먼저 있었던 셈입니다. 그분의 보물이 이 땅에 있었기 때문에, 그분의 마음이 이 땅으로 오셨습니다."),
      makeBody("여기서 딱 하나 분명히 해야 할 게 있습니다. 우리가 잘나서, 값이 나가서 보물이 된 게 아닙니다."),

      makeVerseLabel("신명기 7장 7절입니다."),
      makeVerseText("여호와께서 너희를 기뻐하시고 너희를 택하심은 너희가 다른 민족보다 수효가 많기 때문이 아니니라 너희는 오히려 모든 민족 중에 가장 적으니라"),

      makeBody("이유는 딱 하나, 그분이 그냥 사랑하셨기 때문입니다. 값이 있어서 보물이 된 게 아니라, 그분이 보물로 여기셔서 값이 생긴 것입니다."),
      makeBody("이것이 우리가 손을 펼 수 있는 유일한 힘입니다. 이를 악물고 내려놓는 게 아니라, 이미 나를 위해 전부를 내려놓으신 분을 봤기 때문에 손이 펴지는 겁니다."),

      makeKidsBox("정말 갖고 싶은 걸 발견하면 다른 건 안 아깝잖아요. 참는 게 아니라 그냥 눈에 안 들어오는 거죠. 예수님을 진짜로 만난 사람도 똑같아요. “꿈을 포기해, 좋아하는 거 버려”가 아니에요. 그것보다 더 큰 게 생겨서, 그것들이 더 이상 나를 흔들지 못하게 되는 것이에요."),
      makeDivider(),

      // ───────── 적용 ─────────
      makeHeading("적용 ─ 오해하지 말 것, 실천할 것 (3분)"),

      makeBody("첫째, 오늘 말씀이 아닌 것 세 가지입니다."),
      makeBody("하나, “저축하지 마라”가 아닙니다. 성실히 일해 가족을 책임지는 건 성경이 분명히 명하는 선한 일입니다."),

      makeVerseLabel("디모데전서 5장 8절입니다."),
      makeVerseText("누구든지 자기 친족 특히 자기 가족을 돌보지 아니하면 믿음을 배반한 자요 불신자보다 더 악한 자니라"),

      makeBody("둘, “가난해야 거룩하다”가 아닙니다. 가난이 곧 경건이고 부유함이 곧 죄라는 뜻이 아닙니다. 예수님이 물으시는 건 액수가 아니라 주인입니다. 지금 형편이 어려우신 분께 오늘 말씀은 책망이 아니라 위로입니다. 좀도 녹도 도둑도 손댈 수 없는 창고가 이미 여러분 것입니다."),
      makeBody("셋 ─ 이게 제일 중요합니다 ─ “착한 일 많이 하면 천국에 적금이 쌓인다”가 아닙니다. 오늘 “쌓으라”는 말을 여러 번 들으셨으니 이 말씀을 꼭 함께 붙들어야 합니다."),

      makeVerseLabel("에베소서 2장 8절~9절입니다."),
      makeVerseText("너희는 그 은혜에 의하여 믿음으로 말미암아 구원을 받았으니 이것은 너희에게서 난 것이 아니요 하나님의 선물이라 행위에서 난 것이 아니니 이는 누구든지 자랑하지 못하게 함이라"),

      makeBody("구원은 선물입니다. 우리가 쌓아서 사는 게 아닙니다. 하늘에 쌓는다는 건 천국 값을 치르는 게 아니라, 이미 그분의 것이 된 사람이 그분 뜻대로 사는 것입니다. 순서가 반대로 되면 오늘 말씀이 짐이 됩니다."),
      makeBody("학생들도 같습니다. 열심히 공부하는 건 잘못이 아닙니다. 다만 그게 무너질 때 내 존재 전체가 무너진다면, 그건 이미 보물이 아니라 주인이 된 것입니다."),

      makeBody("둘째, 오늘 말씀인 것 ─ 이번 한 주 세 가지입니다."),
      makeBody("하나, 확인하기. 지난 한 달 카드 명세서(학생은 용돈 쓴 내역과 휴대폰 사용 시간)를 딱 5분만 봅니다. 거기 내 마음 주소가 적혀 있습니다. 자책하지 말고 확인만 합니다."),
      makeBody("둘, 손 펴기. 이번 주 한 번, 돌려받을 수 없는 곳에 씁니다. 예수님이 직접 이렇게 하라고 하셨습니다."),

      makeVerseLabel("누가복음 14장 13절~14절입니다."),
      makeVerseText("잔치를 베풀거든 차라리 가난한 자들과 몸 불편한 자들과 저는 자들과 맹인들을 청하라 그리하면 그들이 갚을 것이 없으므로 네게 복이 되리니 이는 의인들의 부활 시에 네가 갚음을 받겠음이라"),

      makeBody("액수는 상관없습니다. 학생은 용돈의 작은 일부나 친구를 위한 30분이면 충분합니다. 그리고 가능하면 아무도 모르게 하십시오. 오늘 본문 바로 앞에서 예수님이 그렇게 하라고 하셨습니다."),

      makeVerseLabel("마태복음 6장 3절~4절입니다."),
      makeVerseText("너는 구제할 때에 오른손이 하는 것을 왼손이 모르게 하여 네 구제함을 은밀하게 하라 은밀한 중에 보시는 너의 아버지께서 갚으시리라"),

      makeBody("셋, 첫 자리 내드리기. 하루의 첫 5분을 하나님께 먼저 드립니다. 하루의 첫 자리를 누구에게 주느냐가, 그날의 주인이 누구인지를 정합니다."),
      makeDivider(),

      // ───────── 결론 ─────────
      makeHeading("결론 ─ 두 개의 창고 (1분)"),

      makeBody("오늘 예수님은 세 가지를 물으셨습니다. 무엇을 쌓고 있느냐. 무엇을 보고 있느냐. 누구의 것이냐."),
      makeBody("우리 앞에 창고가 둘 있습니다. 하나는 내가 밤새 지켜야 하는 창고입니다. 좀이 갉아먹고, 녹이 슬고, 도둑이 벽을 뚫습니다. 쌓을수록 그것이 나를 붙잡습니다. 다른 하나는 나를 지켜 주는 창고입니다. 아무도 손댈 수 없고, 그 창고의 이름은 예수 그리스도이십니다."),

      makeRefrain(REFRAIN),

      makeBody("예수님이 이 말씀을 이렇게 맺으십니다."),

      makeVerseLabel("마태복음 6장 33절입니다."),
      makeVerseText("그런즉 너희는 먼저 그의 나라와 그의 의를 구하라 그리하면 이 모든 것을 너희에게 더하시리라"),

      makeBody("“먼저”입니다. 다 버리라가 아니라, 순서를 바꾸라는 것입니다. 오늘 이 자리에서 움켜쥔 손을 펴고 고백하십시오. “주님, 제 1호 보물은 예수님이십니다.” 우리 보물은 금고 안에 있지 않고 십자가 위에 계십니다. 그 보물은 좀도 녹도 도둑도 영원히 건드리지 못합니다."),

      makeQuestion("기도하겠습니다."),
      makeDivider(),

      // ───────── 설교 노트 ─────────
      makeNoteTitle("설교 노트 (강단용 참고 — 인쇄 시 제외 가능)"),
      makeNote("• 시간 배분(30분): 서론 4 / 첫째 6 / 둘째 5 / 셋째 5 / 넷째 6 / 적용 3 / 결론 1"),
      makeNote("• 시간이 모자라면 잠언 22장 9절, 마태복음 8장 20절, 요한복음 19장 24절은 낭독 대신 언급만 하고 넘어갈 것."),
      makeNote("• 후렴구(파란 박스)는 서론과 결론 두 곳에 있음. 가능하면 주보나 화면에도 같은 문장을 노출할 것."),
      makeNote("• 문맥 다리: 앞(6:1-4 은밀한 구제)이 “하늘에 어떻게 쌓나”의 답, 뒤(6:25 염려 / 6:33 먼저 그의 나라)가 “왜 땅에 쌓으면 불안한가”의 답."),
      makeNote("• 주의 1 ─ 행위구원 오해: “쌓으라”를 반복하는 설교이므로 적용부의 에베소서 2장 8~9절을 빼지 말 것."),
      makeNote("• 주의 2 ─ 순서: “우리가 하나님의 보물”은 말라기 3장 17절로 근거를 대되, 신명기 7장 7절로 “값이 있어서가 아니라 그분이 보물로 여기셔서”라고 반드시 뒤집을 것."),
      makeNote("• 주의 3 ─ 19절 원어: 같은 뿌리 낱말을 겹쳐 쓴 것은 ‘강조’, ‘계속되는 행동’은 별개로 명령형의 형태에서 옴. 한 근거로 뭉뚱그리지 말 것."),
      makeNote("• 주의 4 ─ 하지 말 것: “은행이 없던 시대”(마 25:27이 은행을 언급), “맘몬은 아멘과 같은 어근”(미확정 어원), “노예는 법적으로 반반 소유가 불가”(로마법에 공동 소유 노예 있음)."),
      makeNote("• 인쇄: A5, 본문 12pt. 원본 원고는 저장소 설교/마태복음6장19-24_진짜보물_예수그리스도_2안.md"),
    ]
  }]
});

Packer.toBuffer(doc).then(buf => {
  const out = "/home/user/home/설교/진짜보물_예수그리스도_마6장19-24절_A5.docx";
  fs.writeFileSync(out, buf);
  console.log("생성 완료:", out, (buf.length/1024).toFixed(1) + "KB");
});
