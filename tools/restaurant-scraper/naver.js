// 네이버 지도 맛집 스크래퍼 (Playwright)
// 사용법:  node naver.js "파주 한식 맛집" [최대개수]
//
// 로컬 PC 세션에서 실행할 것. 네이버는 클라우드/서버 IP를 봇으로 차단(캡차)하므로
// 가정용(주거용) IP인 로컬 PC에서만 정상 동작한다.
//
// 최초 1회:  npm install  &&  npx playwright install chromium

const { chromium } = require('playwright');

const QUERY = process.argv[2] || '파주 한식 맛집';
const LIMIT = parseInt(process.argv[3] || '10', 10);

// 에이전트 프록시 환경(클라우드 세션)에서만 필요. 로컬 PC에는 보통 프록시가 없다.
const PROXY = process.env.HTTPS_PROXY || null;

function launchArgs() {
  const args = ['--lang=ko-KR', '--disable-blink-features=AutomationControlled'];
  if (PROXY) {
    // 클라우드 세션의 재서명 프록시를 통과하기 위한 플래그 (로컬에선 불필요)
    args.push('--ignore-certificate-errors', '--disable-quic', '--proxy-server=' + PROXY);
  }
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

  const url = 'https://map.naver.com/p/search/' + encodeURIComponent(QUERY);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });

  // 검색 결과는 iframe#searchIframe 안에 렌더된다.
  await page.waitForSelector('iframe#searchIframe', { timeout: 40000 });
  const frame = await (await page.$('iframe#searchIframe')).contentFrame();
  await frame.waitForSelector('#_pcmap_list_scroll_container li', { timeout: 40000 });

  // 리스트를 스크롤해 더 많은 항목을 로드
  const scrollBox = await frame.$('#_pcmap_list_scroll_container');
  for (let i = 0; i < 8; i++) {
    if (scrollBox) await scrollBox.evaluate((el) => el.scrollBy(0, el.scrollHeight));
    await page.waitForTimeout(1000);
  }

  const items = await frame.evaluate(() => {
    const out = [];
    document.querySelectorAll('#_pcmap_list_scroll_container > ul > li').forEach((li) => {
      const name = (li.querySelector('span.TYaxT, span.YwYLL, .place_bluelink span') || {}).innerText;
      if (!name) return;
      const category = (li.querySelector('span.KCMnt, span.YzBgS') || {}).innerText || '';
      // 별점: "별점4.53" 형태, 리뷰: "방문자리뷰 1,234", "블로그리뷰 567"
      const spans = Array.from(li.querySelectorAll('span')).map((s) => s.innerText.trim());
      const joined = li.innerText.replace(/\n/g, ' ');
      const rating = (joined.match(/별점\s*([\d.]+)/) || [])[1] || '';
      const visitor = (joined.match(/방문자\s*리뷰?\s*([\d,]+)/) || [])[1] || '';
      const blog = (joined.match(/블로그\s*리뷰?\s*([\d,]+)/) || [])[1] || '';
      out.push({ name: name.trim(), category: category.trim(), rating, visitorReview: visitor, blogReview: blog });
    });
    return out;
  });

  const seen = new Set();
  const rows = items.filter((r) => (seen.has(r.name) ? false : seen.add(r.name))).slice(0, LIMIT);

  console.log(`\n[네이버 지도] "${QUERY}" — ${rows.length}곳\n`);
  console.log('상호\t별점\t방문자리뷰\t블로그리뷰\t분류');
  rows.forEach((r) =>
    console.log([r.name, r.rating || '-', r.visitorReview || '-', r.blogReview || '-', r.category].join('\t'))
  );
  console.log('\nJSON:\n' + JSON.stringify({ query: QUERY, items: rows }, null, 2));

  await browser.close();
})().catch((e) => {
  console.error('에러:', e.message);
  console.error('※ 클라우드/서버 IP에서 실행하면 네이버 봇 차단(캡차)으로 실패한다. 로컬 PC에서 실행할 것.');
  process.exit(1);
});
