// 카카오맵 맛집 스크래퍼 (Playwright)
// 사용법:  node kakao.js "파주 한식 맛집" [최대개수]
//
// 로컬 PC 세션에서 실행할 것. 카카오도 서버 IP에서는 지도 호스트가 TLS 연결을
// 리셋하고 평점 API가 세션 키를 요구하므로, 주거용 IP인 로컬 PC에서만 정상 동작한다.
//
// 최초 1회:  npm install  &&  npx playwright install chromium

const { chromium } = require('playwright');

const QUERY = process.argv[2] || '파주 한식 맛집';
const LIMIT = parseInt(process.argv[3] || '10', 10);
const PROXY = process.env.HTTPS_PROXY || null;

function launchArgs() {
  const args = ['--lang=ko-KR', '--disable-blink-features=AutomationControlled'];
  if (PROXY) args.push('--ignore-certificate-errors', '--disable-quic', '--proxy-server=' + PROXY);
  return args;
}

(async () => {
  const browser = await chromium.launch({ headless: true, args: launchArgs() });
  const context = await browser.newContext({
    locale: 'ko-KR',
    ignoreHTTPSErrors: !!PROXY,
    viewport: { width: 1400, height: 1000 },
    userAgent:
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
      '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  });
  const page = await context.newPage();

  // 카카오맵 통합검색 결과 페이지
  const url = 'https://map.kakao.com/?q=' + encodeURIComponent(QUERY);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForSelector('#info\\.search\\.place\\.list > li', { timeout: 40000 });
  await page.waitForTimeout(1500);

  const items = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('#info\\.search\\.place\\.list > li').forEach((li) => {
      const name = (li.querySelector('.head_item .link_name, .tit_name .link_name') || {}).innerText;
      if (!name) return;
      const category = (li.querySelector('.subcategory, .cate_item') || {}).innerText || '';
      const rating = (li.querySelector('.rating .score .num, em.num') || {}).innerText || '';
      const reviewTxt = (li.querySelector('.rating .review, .numberofscore') || {}).innerText || '';
      const review = (reviewTxt.match(/([\d,]+)/) || [])[1] || '';
      const addr = (li.querySelector('.addr p, .addr') || {}).innerText || '';
      out.push({ name: name.trim(), category: category.trim(), rating: rating.trim(), review, address: addr.trim() });
    });
    return out;
  });

  const seen = new Set();
  const rows = items.filter((r) => (seen.has(r.name) ? false : seen.add(r.name))).slice(0, LIMIT);

  console.log(`\n[카카오맵] "${QUERY}" — ${rows.length}곳\n`);
  console.log('상호\t별점\t리뷰수\t분류\t주소');
  rows.forEach((r) =>
    console.log([r.name, r.rating || '-', r.review || '-', r.category, r.address].join('\t'))
  );
  console.log('\nJSON:\n' + JSON.stringify({ query: QUERY, items: rows }, null, 2));

  await browser.close();
})().catch((e) => {
  console.error('에러:', e.message);
  console.error('※ 서버 IP에서는 카카오 지도 호스트가 연결을 리셋한다. 로컬 PC에서 실행할 것.');
  process.exit(1);
});
