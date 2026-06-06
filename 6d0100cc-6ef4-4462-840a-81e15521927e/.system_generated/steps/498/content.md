Title: Live Content

Description: Fetched live

Source: https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPE_P2eYZPrDnITOuiEYmdqWgDiZxsnLpr1rUwX5qg3rAGYS-8G9DaImFqMnLRs0ePu43ey3DX2HxvBNxcoZiGY3jbULZ0Xqypp6TF_002zLDXMJMnrVfusK1HS8Zr_8eEy-QxDzWGJn_m23n1bgilGH-Bv96Q9P5l1LLbgmUdYRRELQ3PPCnP2kCK

---

<!DOCTYPE html>
<html lang="ko">



<head><script>(function(i, s, o, g, r) {
    var a = s.createElement(o);
    var m = s.getElementsByTagName(o)[0];
    a.async = true;
    a.src = g;
    a.onload = function() {
        if (i[r].init) {
            i[r].init('https://js-error-tracer-api.cafe24.com', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJuc21hbGwyMDIyLmNhZmUyNC5jb20iLCJhdWQiOiJqcy1lcnJvci10cmFjZXItYXBpLmNhZmUyNC5jb20iLCJtYWxsX2lkIjoibnNtYWxsMjAyMiIsInNob3Bfbm8iOjEsInBhdGhfcm9sZSI6IlBST0RVQ1RfREVUQUlMIiwibGFuZ3VhZ2VfY29kZSI6ImtvX0tSIiwiY291bnRyeV9jb2RlIjoiS1IiLCJpc195dHMiOmZhbHNlLCJpc19jb250YWluZXIiOnRydWUsIndvcmtzcGFjZSI6InByb2R1Y3Rpb24ifQ._sK0nTuo-Ns1MMXjtjD0C2-cXr7i9X4ZLwncr6qYZb0', {"errors":{"path":"\/api\/v1\/store","collectWindowErrors":true,"preventDuplicateReports":true,"storageKeyPrefix":"EC_JET.PRODUCT_DETAIL","samplingEnabled":true,"samplingRate":0.5},"vitals":{"path":"\/api\/v1\/vitals","samplingEnabled":true,"samplingRate":0.3},"resources":{"path":"\/api\/v1\/resources","samplingEnabled":true,"samplingRate":0.5,"durationThreshold":3000}});
        }
    };
    m.parentNode.insertBefore(a, m);
}(window, document, 'script', '//assets.poxo.com/jet/jet.js', 'EC_JET'));</script>
<script type="text/javascript">window.CAFE24 = window.CAFE24 || {};CAFE24.ROUTE = {"is_mobile":false,"is_need_route":false,"language_code":"ZZ","path":{"origin":"\/product\/\uc778\ub514\uc548\ubc2583g1\/2758\/","result":"\/product\/\uc778\ub514\uc548\ubc2583g1\/2758\/","prefix":""},"shop_no":0,"skin_code":"default","support_language_list":{"ar":"ar_EG","ar-EG":"ar_EG","de":"de_DE","de-DE":"de_DE","en":"en_US","en-IN":"en_IN","en-PH":"en_PH","en-US":"en_US","es":"es_ES","es-ES":"es_ES","hi":"hi_IN","hi-IN":"hi_IN","id":"id_ID","id-ID":"id_ID","it":"it_IT","it-IT":"it_IT","ja":"ja_JP","ja-JP":"ja_JP","ko":"ko_KR","ko-KR":"ko_KR","ms":"ms_MY","ms-MY":"ms_MY","pt":"pt_PT","pt-PT":"pt_PT","ru":"ru_RU","ru-RU":"ru_RU","th":"th_TH","th-TH":"th_TH","tr":"tr_TR","tr-TR":"tr_TR","vi":"vi_VN","vi-VN":"vi_VN","zh":"zh_CN","zh-CN":"zh_CN","zh-HK":"zh_HK","zh-MO":"zh_MO","zh-SG":"zh_SG","zh-TW":"zh_TW"}};</script><script type="text/javascript">if (typeof EC_ROUTE === "undefined") {
    /**
     * 프론트용 라우트 플러그인
     * @type {{bInit: boolean, init: EC_ROUTE.init}}
     * CAFE24.ROUTE 참조
     */
    var EC_ROUTE = {
        EC_DOMAIN_PATH_INFO: 'EC_DOMAIN_PATH_INFO',
        bInit: false,
        aFromList: [],
        aToList: [],
        aCleanFilter: null,
        init: function () {
            if (this.bInit || typeof CAFE24.ROUTE === 'undefined') {
                return;
            }
            this.bInit = true;
            this.aCleanFilter = [
                /^shop[1-9][0-9]*$/,
                /^(m|p)$/,
                new RegExp('^(' + Object.keys(CAFE24.ROUTE.support_language_list).join('|')  + ')$'),
                /^skin-(base|skin[1-9][0-9]*|mobile[0-9]*)$/,
            ];
        },
        isNeedRoute: function ()
        {
            return CAFE24.ROUTE.is_need_route;
        },
        /**
         *
         * @param iShopNo
         * @param bMobile
         * @param sFrontLanguage
         * @param sSkinCode
         * @returns {*|string}
         */
        getUrlDomain: function (iShopNo, bMobile, sFrontLanguage, sSkinCode)
        {
            var oRouteConfig = {};
            if (typeof iShopNo == 'undefined') {
                oRouteConfig.shop_no = CAFE24.SDE_SHOP_NUM;
            } else {
                oRouteConfig.shop_no = iShopNo;
            }
            if (typeof bMobile == 'undefined') {
                oRouteConfig.is_mobile = false;
            } else {
                oRouteConfig.is_mobile = bMobile;
            }
            if (typeof sFrontLanguage == 'undefined') {
                oRouteConfig.language_code = '';
            }else {
                oRouteConfig.language_code = sFrontLanguage; // 내부에서 로직으로 동작할땐 언어_지역 형태의 로케일 형태를 따른다.
            }
            if (typeof sSkinCode == 'undefined') {
                oRouteConfig.skin_code = '';
            }else {
                oRouteConfig.skin_code = sSkinCode;
            }

            var sDomain = '';
            if (oRouteConfig.shop_no != CAFE24.SDE_SHOP_NUM) {
                // 접근된 다른 멀티샵 도메인 정보는 primary domain 를 조회해야함으로 ajax 를 통해 정보를 얻는다.
                sDomain = this._getUrlDomainMultishop(oRouteConfig);
            } else {
                // 샵이 동일할 경우에는 접근된 domain 에 path 정보만 정리하여 반환함.
                sDomain = this._getUrlDomain(oRouteConfig);
            }
            return sDomain;
        },
        _getUrlDomainMultishop: function (oRouteConfig)
        {
            var sDomain = '';
            EC$.ajax({
                type: 'GET',
                url: '/exec/front/Shop/Domain',
                data: {
                    '_shop_no' : oRouteConfig.shop_no,
                    'is_mobile' : oRouteConfig.is_mobile,
                    'language_code' : oRouteConfig.language_code,
                    'skin_code' : oRouteConfig.skin_code,
                },
                async: false,
                dataType: 'json',
                cache: true,
                success: function(oResult) {
                    switch (oResult.code) {
                        case '0000' :
                            sDomain = oResult.data;
                            break;
                        default :
                            break;
                    }
                    return false;
                }
            });
            return sDomain;
        },
        _getUrlDomain: function (oRouteConfig)
        {
            oRouteConfig.domain = this._getCreateHost(oRouteConfig);
            return location.protocol + '//' + oRouteConfig.domain + this._getCreateUri(oRouteConfig);
        },
        _getCreateHost : function (oRouteConfig)
        {
            var sHost = location.host;
            var aHost = sHost.split('.');
            if (this.isBaseDomain(sHost)) {
                if (aHost.length > 3) {
                    aHost[0] = '';
                }
            } else if (oRouteConfig.is_mobile) {
                if (this.isMobileDomain()) {
                    oRouteConfig.is_mobile = false;
                }
            }
            return aHost.filter(Boolean).join('.');
        },
        _getCreateUri: function (oRouteInfo)
        {
            var aUrl = [];
            if (this.isBaseDomain() && oRouteInfo.shop_no > 1) {
                aUrl.push('shop' + oRouteInfo.shop_no);
            }
            if (oRouteInfo.is_mobile) {
                aUrl.push('m');
            }
            if (oRouteInfo.language_code != 'ZZ' && oRouteInfo.language_code != '') {
                var iIndex = Object.values(CAFE24.ROUTE.support_language_list).indexOf(oRouteInfo.language_code);
                if (iIndex !== -1) {
                    aUrl.push(Object.keys(CAFE24.ROUTE.support_language_list)[iIndex]);
                }
            }
            if (this.isBaseDomain() && oRouteInfo.skin_code != 'default' && oRouteInfo.skin_code != '') {
                aUrl.push('skin-' + oRouteInfo.skin_code);
            }
            var sUrl= '/';
            if (aUrl.length > 0) {
                sUrl= '/' + aUrl.join('/');
                sUrl = this.rtrim(sUrl, '/');
            }
            return sUrl;
        },
        /**
         * en, en-US => en_US
         */
        convertValidLanguageCode: function (sUrlLanguageCode)
        {
            if (typeof CAFE24.ROUTE.support_language_list[sUrlLanguageCode] != 'undefined') {
                return CAFE24.ROUTE.support_language_list[sUrlLanguageCode];
            }
            return false;
        },
        isMobileDomain: function (sHost)
        {
            if (typeof sHost == 'undefined') {
                sHost = location.host;
            }
            var aMatched = sHost.match(/^(m|mobile|skin\-mobile|skin\-mobile[0-9]+[\-]{2}shop[0-9]+|skin\-mobile[0-9]+|mobile[\-]{2}shop[0-9]+)\./i);
            return aMatched != null;
        },
        isBaseDomain: function (sHost)
        {
            if (typeof sHost == 'undefined') {
                sHost = location.host;
            }
            return sHost.indexOf(CAFE24.GLOBAL_INFO.getRootDomain()) !== -1;
        },
        removePrefixUrl: function (sUrl)
        {
            if (this.isNeedRoute()) {
                sUrl = sUrl.replace(this.getPrefixUrl('/'), '/'); // 자동으로  prefix 붙은 영역을 제거해준다.
            }
            return sUrl;
        },
        getPrefixUrl: function (sUrl)
        {
            if (this.isNeedRoute() === false) {
                return sUrl;
            }
            if (sUrl.indexOf('/') !== 0) {
                return sUrl;
            }
            if (sUrl.match(/^\/{2,}/) !== null) {
                return sUrl;
            }

            var iCachedPosition = this.aFromList.indexOf(sUrl);
            if (iCachedPosition > -1) {
                return this.aToList[iCachedPosition];
            }

            var bTailSlash = (sCleanUrl !== '/' && sUrl.substr(-1) === '/');
            var sCleanUrl = this.getCleanUrl(sUrl);
            var aPrefixPart = CAFE24.ROUTE.path.prefix.split('/');
            var aUrlPart = sCleanUrl.split('/');
            var bMatched = true;
            var sReturnUrl = sCleanUrl;
            if (aUrlPart.length < aPrefixPart.length) {
                bMatched = false;
            } else {
                for (var i = 0; i < aPrefixPart.length ; i++) {
                    if (aPrefixPart[i] != aUrlPart[i]) {
                        bMatched = false;
                        break;
                    }
                }
            }
            if (bMatched === false) {
                if (sCleanUrl == '/') {
                    sReturnUrl = CAFE24.ROUTE.path.prefix;
                } else {
                    sReturnUrl = CAFE24.ROUTE.path.prefix +  sCleanUrl;
                }
                sReturnUrl = bTailSlash ? sReturnUrl : this.rtrim(sReturnUrl, '/')
                this.aFromList.push(sUrl);
                this.aToList.push(sReturnUrl);
            }
            return sReturnUrl;
        },
        /**
         * document.location.pathname 이 필요할 경우 사용한다.
         * @returns {*}
         */
        getPathName: function()
        {
            if (typeof CAFE24.ROUTE.path.result == 'undefined') {
                return document.location.pathname;
            }
            return CAFE24.ROUTE.path.result;
        },
        rtrim: function (str, chr)
        {
            var rgxtrim = (!chr) ? new RegExp('\\s+$') : new RegExp(chr+'+$');
            return str.replace(rgxtrim, '');
        },
        getShopNo: function ()
        {
            return CAFE24.ROUTE.shop_no;
        },
        getSkinCode: function ()
        {
            return CAFE24.ROUTE.skin_code;
        },
        getLanguageCode: function ()
        {
            return CAFE24.ROUTE.language_code;
        },
        getMobile: function ()
        {
            return CAFE24.ROUTE.is_mobile;
        },
        getIsMobile: function ()
        {
            return CAFE24.ROUTE.is_mobile || CAFE24.ROUTE.skin_code.match(/^mobile[0-9]*$/);
        },
        getCleanUrl: function (sUrl)
        {
            if (sUrl === '/') {
                return sUrl;
            }

            var aUrl = sUrl.split('/');
            aUrl.shift();

            if (aUrl.length < 1) {
                return sUrl;
            }

            // 현재 4 depth 까지 미리보기 기능이 구현되어있음
            var iPos = 0;
            var bFind = false;
            for (var i = 0; i < aUrl.length ; i++) {
                bFind = false;
                for (var iSub = iPos, iSubCount = this.aCleanFilter.length; iSub < iSubCount ; iSub++) {
                    if (aUrl[i].match(this.aCleanFilter[iSub]) !== null) {
                        bFind = true;
                        iPos = iSub + 1;
                        aUrl.splice(i, 1);
                        i--; // aUrl 을 삭제해 주었으니 검색 조건을 -1 제거하여 초기화 한다. 다음 for i++ 로 증감 조회됨.
                        break;
                    }
                }
                if (bFind === false) {
                    break;
                }
            }
            return '/' + aUrl.join('/');
        },
        getIsEasyUrl : function ()
        {
            return !window.location.pathname.match(/^[\w\/\-\.]+(php|html|htm)$/i);
        }
    };
    EC_ROUTE.init();
}
</script>
<meta name="path_role" content="PRODUCT_DETAIL" />
<meta name="author" content="농심몰" />
<meta name="keywords" content="인디안밥(83g*1), 과자,스낵, 농심몰, 🍬스낵 &amp; 젤리" />
<meta name="design_html_path" content="/product/detail.html" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8">

	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=yes"/>
	<!-- PG크로스브라우징필수내용 -->
	<meta http-equiv="Cache-Control" content="no-cache">
	<meta http-equiv="Expires" content="0">
	<meta http-equiv="Pragma" content="no-cache">
	<!-- // PG크로스브라우징필수내용 -->

	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&amp;family=Noto+Sans+KR:wght@100;300;400;500;700;900&amp;display=swap" rel="stylesheet">
		<!-- 해당 CSS는 쇼핑몰 전체 페이지에 영향을 줍니다. 삭제와 수정에 주의해주세요. -->
	
    
    
    
    
    
    
    
    
    
    
    
    
	
	<!--css(/layout/basic/css/aos.css)-->
	
	
	
	

    
	
	
	
    
	
	
    <script src="/layout/basic/js/swiper.min.js"></script>
    <script src="/layout/basic/js/jquery-3.6.0.min.js"></script>
    <!-- <script src="/layout/basic/js/aos.js"></script> -->

    <script src="/layout/basic/js/global2.js"></script>
    <script src="/layout/basic/js/global3.js"></script>
	<script src="/layout/basic/js/global.js"></script>
	
	<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>
	<script src="https://player.vimeo.com/api/player.js"></script>
	<script src="https://www.youtube.com/iframe_api"></script>

    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-PBZFRLS');</script>
     <script>
     if(sessionStorage.USER_MEMBER_ID) {
 	 var ui_1 = sessionStorage.USER_MEMBER_ID+"_data";
 	 var ug_ = JSON.parse(sessionStorage.getItem(ui_1)).gender;
     var ua_ =JSON.parse(sessionStorage.getItem(ui_1)).memberAge;
     var um_ = sessionStorage.USER_MEMBER_GROUP_NAME;
 	 window.dataLayer.push({ 'ug' : ug_, 'ua' : ua_, 'um' : um_ });
     }
	</script>
    <!-- End Google Tag Manager -->
	<script type="text/javascript">
		(function (a, i, u, e, o) {
			a[u] = a[u] || function () {
				(a[u].q = a[u].q || []).push(arguments)};})
		(window, document, "groobee");
		groobee("serviceKey", "1e630fd7e0a04010bf126ea5388958ef");
		groobee("siteType", "custom");
	</script>

	<!-- Meta Pixel Code -->
	<script>
	!function(f,b,e,v,n,t,s)
	{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
	n.callMethod.apply(n,arguments):n.queue.push(arguments)};
	if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
	n.queue=[];t=b.createElement(e);t.async=!0;
	t.src=v;s=b.getElementsByTagName(e)[0];
	s.parentNode.insertBefore(t,s)}(window, document,'script',
	'https://connect.facebook.net/en_US/fbevents.js');
	fbq('init', '523242122475303');
	fbq('track', 'PageView');
	</script>
	<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=523242122475303&amp;ev=PageView&amp;noscript=1"></noscript>
	<script type="text/javascript" charset="UTF-8" src="//t1.daumcdn.net/kas/static/kp.js"></script>
	<!-- End Meta Pixel Code -->
	<meta name="facebook-domain-verification" content="6nagmrawfdwlwixpl5pbhc7igbw9g8"/><script type="text/javascript" src="//wcs.naver.net/wcslog.js"></script>

            <script type="text/javascript">
            if(window.wcs) {
                if(!wcs_add) var wcs_add = {};
    
                // (2) 각 사이트별 식별자 설정
                wcs_add["wa"] = "s_22b61aaaa5d";
    
                // (3) 광고 전환추적을 위한 cookie domain설정
    
                if (window.wcs) {
                    wcs.inflow("m.nongshimmall.com");
                }
    
                // 아래 Script는 개별 event 발생시 로그를 전송하기 위한 구역. 결제 완료 페이지이므로, PV event 와 결제완료 전환 event를 전송함
     
                
    
                // (5) 결제완료 전환 event 전송
    
                var _conv = {} // event 정보 담을 object 생성
    
                _conv.type = "view_product"  // object에 purchase event 세팅
    
                
    
                _conv.items = [       // 전환 event 행동의 내용 및 대상에 대한 정보 기술
                    
                {
                    id: "2758",                                                //string 상품 id (필수)
                    name: "인디안밥(83g*1)"       //string 상품 명 (필수)
                    
                }
            
                ];
    
                
    
                wcs.trans(_conv) // event 정보를 담은 object를 서버에 전송(위 item #1, #2 포함)
            }
            </script>
        
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Product","name":"인디안밥(83g*1)","image":["https://m.nongshimmall.com/web/product/big/202407/a4085415aeb539bf25bf65686fa9344e.jpg"],"description":"","brand":{"@type":"Brand","name":"농심몰"},"offers":{"@type":"Offer","url":"https://m.nongshimmall.com/product/%EC%9D%B8%EB%94%94%EC%95%88%EB%B0%A583g1/2758/","priceCurrency":"KRW","price":1540},"aggregateRating":{"@type":"AggregateRating","ratingValue":4.8,"reviewCount":55}}</script>
<meta name="color-scheme" content="light">
<link rel="canonical" href="https://nongshimmall.com/product/인디안밥83g1/2758/" />
<meta property="og:url" content="https://nongshimmall.com/product/인디안밥83g1/2758/" />
<meta property="og:title" content="인디안밥(83g*1) - 농심몰" />
<meta property="og:site_name" content="농심몰" />
<meta property="og:type" content="product" />
<meta property="og:image" content="https://m.nongshimmall.com/web/product/big/202407/a4085415aeb539bf25bf65686fa9344e.jpg" />
<meta property="product:price:amount" content="1540" />
<meta property="product:price:currency" content="KRW" />
<meta property="product:sale_price:amount" content="1540" />
<meta property="product:sale_price:currency" content="KRW" />
<meta property="product:productId" content="2758" />
<meta property="product:retailer_item_id" content="2758" />
<meta name="google-site-verification" content="QXXSk4NhGOf1WJJf-qMlDSCZh3ds3prTtGIhhskIi9g" />
<meta name="naver-site-verification" content="789d48bf4a5104a44537c3d8b8fd72610eab09e2" />
<link rel="shortcut icon" href="/web/upload/favicon-3e7c7370ac0f975891b01222662c7f65.ico" />
<script type="text/javascript" src="//wcs.naver.net/wcslog.js"></script>
<script type="text/javascript">var CAFE24API = { instance: [], MALL_ID: 'nsmall2022', SHOP_NO: 1, basicAuthKeys: {}, setBasicAuthKey: function (clientId, basicAuthKey) { if (typeof basicAuthKey !== 'string') { return; } if (clientId) { CAFE24API.basicAuthKeys[clientId] = basicAuthKey; } else { CAFE24API.basicAuthKeys['default'] = basicAuthKey; } }, init: function (appInfo) { if (typeof appInfo == 'object') { if (appInfo.hasOwnProperty('client_id')) { var appKey = appInfo.client_id; } } else { var appKey = appInfo; } if (appKey) { if (!this.instance[appKey]) { CAFE24API.clientId = appKey; if (appInfo.hasOwnProperty('version')) { CAFE24API.version = appInfo.version; } else { if (CAFE24API.hasOwnProperty('version')) { delete CAFE24API.version; } } var copyObject = CAFE24API.constructor(); for (var attr in CAFE24API) { if (CAFE24API.hasOwnProperty(attr)) { copyObject[attr] = CAFE24API[attr]; } } this.instance[appKey] = copyObject; } return this.instance[appKey]; } }, initializeXhr: function () { try { return new XMLHttpRequest(); } catch (error) { return new window.ActiveXObject('Microsoft.XMLHTTP'); } }, fullPath: function (url) { return 'https://nsmall2022.cafe24api.com' + url; }, getLoginProvider: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'customer')) { return; } callback(null, { 'login': CAPP_ASYNC_METHODS.AppCommon.getLoginProvider() }); }, getCustomerProvider: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'customer')) { return; } callback(null, { 'login': CAPP_ASYNC_METHODS.AppCommon.getCustomerProvider() }); }, getMemberID: function (callback) { if (!CAPP_ASYNC_METHODS.IS_LOGIN) { callback(null); } else { callback(CAPP_ASYNC_METHODS.AppCommon.getMemberID()); } }, getEncryptedMemberId: function (client_id, callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'customer')) { return; } callback(null, CAPP_ASYNC_METHODS.AppCommon.getEncryptedMemberId(client_id)); }, getMemberInfo: function (callback) { callback({ 'id': CAPP_ASYNC_METHODS.AppCommon.getMemberInfo() }); }, getCustomerIDInfo: function (callback) { if (!CAFE24API.__scopeErr(callback, 'application')) { return; } callback(null, { 'id': CAPP_ASYNC_METHODS.AppCommon.getCustomerIDInfo() }); }, getCustomerInfo: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'customer')) { return; } callback(null, { 'customer': CAPP_ASYNC_METHODS.AppCommon.getCustomerInfo() }); }, getDefaultShippingAddress: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'customer')) { return; } callback(null, { 'shipping_address': CAPP_ASYNC_METHODS.AppCommon.getDefaultShippingAddress() }); }, getMileageInfo: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'customer')) { return; } callback(null, { 'mileage': CAPP_ASYNC_METHODS.AppCommon.getMileageInfo() }); }, getPointInfo: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'customer')) { return; } callback(null, { 'point': CAPP_ASYNC_METHODS.AppCommon.getPointInfo() }); }, getDepositInfo: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'customer')) { return; } callback(null, { 'deposit': CAPP_ASYNC_METHODS.AppCommon.getDepositInfo() }); }, getCreditInfo: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'customer')) { return; } callback(null, { 'credit': CAPP_ASYNC_METHODS.AppCommon.getCreditInfo() }); }, getCartList: function (callback) { if (!CAFE24API.__scopeErr(callback, 'personal')) { return; } CAPP_ASYNC_METHODS.AppCommon.getCartList().then(function (data) { callback(null, { 'carts': data }); }); }, getCartInfo: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'personal')) { return; } callback(null, { 'cart': CAPP_ASYNC_METHODS.AppCommon.getCartInfo() }); }, getCartItemList: function (callback) { if (!CAFE24API.__scopeErr(callback, 'order')) { return; } callback(null, { 'items': CAPP_ASYNC_METHODS.AppCommon.getCartItemList() }); }, getCartCount: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'personal')) { return; } callback(null, CAPP_ASYNC_METHODS.AppCommon.getCartCount()); }, getCouponCount: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'promotion')) { return; } callback(null, CAPP_ASYNC_METHODS.AppCommon.getCouponCount()); }, getWishCount: function (callback) { if (!CAFE24API.__chkValidSessionScope(callback, 'personal')) { return; } callback(null, CAPP_ASYNC_METHODS.AppCommon.getWishCount()); }, getShopInfo: function (callback) { if (!CAFE24API.__scopeErr(callback, 'store')) { return; } callback(null, { 'shop': CAPP_ASYNC_METHODS.AppCommon.getShopInfo() }); }, addCurrentProductToCart: function (mall_id, time, app_key, member_id, hmac, callback) { if (!CAFE24API.__scopeErr(callback, 'order')) { return; } CAPP_ASYNC_METHODS.AppCommon.addCurrentProductToCart(mall_id, time, app_key, member_id, hmac).then(function (data) { callback(null, { 'cart': data }); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error('422'), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }); }, precreateOrder: function (mall_id, time, app_key, member_id, hmac, callback) { if (!CAFE24API.__scopeErr(callback, 'order')) { return; } CAPP_ASYNC_METHODS.AppCommon.precreateOrder(mall_id, time, app_key, member_id, hmac).then(function (data) { callback(null, { 'order': data }); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error('422'), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }); }, calculatePayment: function (mall_id, request_time, app_key, member_id, request_data_json, hmac, callback) { if (!CAFE24API.__scopeErr(callback, 'order')) { return; } CAPP_ASYNC_METHODS.AppCommon.calculatePayment(mall_id, request_time, app_key, member_id, request_data_json, hmac).then(function (data) { callback(null, { 'expected_payment': data }); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error('422'), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }); }, precreateOrderV2: function (mall_id, time, app_key, member_id, request_data_json, hmac, callback) { if (!CAFE24API.__scopeErr(callback, 'order')) { return; } CAPP_ASYNC_METHODS.AppCommon.precreateOrderV2(mall_id, time, app_key, member_id, request_data_json, hmac).then(function (data) { callback(null, { 'order': data }); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error('422'), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }); }, getOrderItemList: function (start_date, end_date, order_status, page, count, order_id, callback) { if (!CAFE24API.__scopeErr(callback, 'order')) { return; } CAPP_ASYNC_METHODS.AppCommon.getOrderItemList(start_date, end_date, order_status, page, count, order_id).then(function (data) { callback(null, { 'items': data }); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error(422), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }); }, getOrderDetailInfo: function (shop_no, order_id, callback) { if (!CAFE24API.__scopeErr(callback, 'order')) { return; } CAPP_ASYNC_METHODS.AppCommon.getOrderDetailInfo(shop_no, order_id).then(function (data) { callback(null, { 'orders': data }); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error(422), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }); }, getClaimableItemList: function (order_id, customer_service_type, callback) { if (!CAFE24API.__scopeErr(callback, 'order')) { return; } CAPP_ASYNC_METHODS.AppCommon.getClaimableItemList(order_id, customer_service_type).then(function (data) { callback(null, { 'items': data }); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error(422), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }); }, emptyCart: function (basket_shipping_type, callback) { if (!CAFE24API.__scopeErr(callback, 'personal')) { return; } CAPP_ASYNC_METHODS.AppCommon.emptyCart(basket_shipping_type).then(function (data) { callback(null, { 'result': data }); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error(422), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }); }, deleteCartItems: function (basket_shipping_type, product_list, callback) { if (!CAFE24API.__scopeErr(callback, 'personal')) { return; } CAPP_ASYNC_METHODS.AppCommon.deleteCartItems(basket_shipping_type, product_list).then(function (data) { callback(null, { 'result': data }); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error(422), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }); }, addCart: function (basket_type, prepaid_shipping_fee, product_list, callback) { if (!CAFE24API.__scopeErr(callback, 'personal')) { return; } CAPP_ASYNC_METHODS.AppCommon.addCart(basket_type, prepaid_shipping_fee, product_list).then(function (data) { callback(null, data); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error(422), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }) }, addBundleProductsCart: function (basket_type, prepaid_shipping_fee, product_list, callback) { if (!CAFE24API.__scopeErr(callback, 'personal')) { return; } CAPP_ASYNC_METHODS.AppCommon.addBundleProductsCart(basket_type, prepaid_shipping_fee, product_list).then(function (data) { callback(null, data); }).catch(function (data) { if (data) { callback(new Error('422'), { 'error': { code: data.code, message: data.message } }); } else { callback(new Error(422), { 'error': { code: 422, message: 'This sdk is not available on the current page' } }); } }) }, get: function (url, callback) { return CAFE24API.complete('GET', url, this, null, callback); }, post: function (url, params, callback) { return CAFE24API.complete('POST', url, this, params, callback); }, put: function (url, params, callback) { return CAFE24API.complete('PUT', url, this, params, callback); }, delete: function (url, callback) { return CAFE24API.complete('DELETE', url, this, null, callback); }, complete: function (method, url, obj, params, callback) { var xhr = CAFE24API.sendXhr(method, url, obj, params, callback); xhr.onreadystatechange = function () { if (xhr.readyState === XMLHttpRequest.DONE) { if (xhr.status >= 200 && xhr.status <= 208) { callback(null, JSON.parse(xhr.responseText)); } else { callback(new Error(xhr.status), JSON.parse(xhr.responseText)); } } }; }, sendXhr: function (method, url, obj, params, callback) { if (method !== 'POST') { var url = obj.fullPath(url); } var xhr = obj.initializeXhr(); var queryVars = {}; if (obj.clientId) queryVars['cafe24_app_key'] = obj.clientId; if (obj.version) queryVars['cafe24_api_version'] = obj.version; var basicAuthKey = CAFE24API.basicAuthKeys[obj.clientId] || CAFE24API.basicAuthKeys['default']; if (basicAuthKey && basicAuthKey.length > 0) { queryVars['authorization'] = 'Basic ' + basicAuthKey; } if (params === null) { var seperator = url.indexOf('?') == -1 ? '?' : '&'; var queryString = []; for (var key in queryVars) { queryString.push(key + '=' + encodeURIComponent(queryVars[key])); } if (queryString.length > 0) { url = url + seperator + queryString.join('&'); } } xhr.open(method, url, true); if (typeof params == 'object' && params !== null) { xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded; charset=utf-8'); for (var key in queryVars) { params[key] = queryVars[key]; } params = 'formData=' + JSON.stringify(params); } xhr.send(params || null); return xhr; }, __sessionErr: function (callback) { callback(new Error(403), { 'error': { code: 403, message: 'Failed to get session. Only available when log in.' } }); }, __scopeErr: function (callback, scope) { if (typeof CAFE24.APPSCRIPT_SDK_DATA != "undefined" && jQuery.inArray(scope, CAFE24.APPSCRIPT_SDK_DATA) > -1) { return true; } callback(new Error(403), { 'error': { code: 403, message: 'You do not have the necessary authority(scope) to use the SDK.' } }); }, __chkValidSessionScope: function (callback, scope) { if (!CAPP_ASYNC_METHODS.IS_LOGIN) { CAFE24API.__sessionErr(callback); return false; } if (!CAFE24API.__scopeErr(callback, scope)) { return false; } return true; } }; </script>
<script type="text/javascript">
window.CAFE24 = window.CAFE24 || {};
CAFE24.MANIFEST_CACHE_REVISION = '2605201482';
CAFE24.getDeprecatedNamespace = function(sDeprecatedNamespace, sSupersededNamespace) {
var sNamespace = sSupersededNamespace 
? sSupersededNamespace 
: sDeprecatedNamespace.replace(/^EC_/, '');
return CAFE24[sNamespace];
}
CAFE24.FRONT_LANGUAGE_CODE = "ko_KR";
CAFE24.MOBILE = true;
CAFE24.MOBILE_DEVICE = false;
CAFE24.MOBILE_USE = true;
var EC_MOBILE = CAFE24.MOBILE;
var EC_MOBILE_DEVICE = CAFE24.MOBILE_DEVICE;
var EC_MOBILE_USE = CAFE24.MOBILE_USE;
CAFE24.SKIN_CODE = "mobile";
CAFE24.FRONT_EXTERNAL_SCRIPT_VARIABLE_DATA = {"common_member_id_crypt":""};
var EC_FRONT_EXTERNAL_SCRIPT_VARIABLE_DATA = CAFE24.getDeprecatedNamespace('EC_FRONT_EXTERNAL_SCRIPT_VARIABLE_DATA');
CAFE24.SDE_SHOP_NUM = 1;CAFE24.SHOP = {getLanguage : function() { return "ko_KR"; },getSkinLanguageCode : function() { return "ko_KR"; },getCurrency : function() { return "KRW"; },getFlagCode : function() { return "KR"; },getTimezone: function() { return "Asia/Seoul" },getDateFormat: function() { return "Y-m-d" },isMultiShop : function() { return false; },isDefaultShop : function() { return true; },isDefaultLanguageShop : function(sLanguageCode) { return SHOP.isDefaultShop() && SHOP.isLanguageShop(sLanguageCode); },isKR : function() { return true; },isUS : function() { return false; },isJP : function() { return false; },isCN : function() { return false; },isTW : function() { return false; },isES : function() { return false; },isPT : function() { return false; },isVN : function() { return false; },isPH : function() { return false; },getCountryAndLangMap : function() { return {
"KR": "ko_KR",
"US": "en_US",
"JP": "ja_JP",
"CN": "zh_CN",
"TW": "zh_TW",
"VN": "vi_VN",
"PH": "en_PH"
}},isLanguageShop : function(sLanguageCode) { return sLanguageCode === "ko_KR"; },getDefaultShopNo : function() { return 1; },getProductVer : function() { return 2; },isSDE : function() { return true; },isMode : function() {return true; },getModeName : function() {return true; },isMobileAdmin : function() {return false; },isNewProMode : function() {return false; },isExperienceMall : function() { return false; },isDcollection : function() {return false; },isYoutubeShops : function() {return false; },getYtShopsShopNo : function() {return 0; },isFrontDesignChangeRequired : function() {return false;},isG2G : function() {return false; },getAdminID : function() {return ''},getMallID : function() {return 'nsmall2022'},getCurrencyFormat : function(sPriceTxt, bIsNumberFormat) { 
sPriceTxt = String(sPriceTxt);
var aCurrencySymbol = ["","\uc6d0",false];
if (typeof CAFE24.SHOP_PRICE !== 'undefined' && isNaN(sPriceTxt.replace(/[,]/gi, '')) === false && bIsNumberFormat === true) {
// bIsNumberFormat 사용하려면 Ui(':libUipackCurrency')->plugin('Currency') 화폐 라이브러리 추가 필요
sPriceTxt = CAFE24.SHOP_PRICE.toShopPrice(sPriceTxt.replace(/[,]/gi, ''), true, CAFE24.SDE_SHOP_NUM);
}
try {
var sPlusMinusSign = (sPriceTxt.toString()).substr(0, 1);
if (sPlusMinusSign === '-' || sPlusMinusSign === '+') {
sPriceTxt = (sPriceTxt.toString()).substr(1);
return sPlusMinusSign + aCurrencySymbol[0] + sPriceTxt + aCurrencySymbol[1];
} else {
return aCurrencySymbol[0] + sPriceTxt + aCurrencySymbol[1];
}
} catch (e) {
return aCurrencySymbol[0] + sPriceTxt + aCurrencySymbol[1];
}
}};CAFE24.CURRENCY_INFO = {getOriginReferenceCurrency : function() {return 'USD'},getCurrencyList : function(sCurrencyCode) { var aCurrencyList = {"JPY":{"currency_symbol":"&yen;","decimal_place":0,"round_method_type":"F"},"VND":{"currency_symbol":"&#8363;","decimal_place":0,"round_method_type":"F"},"PHP":{"currency_symbol":"&#8369;","decimal_place":2,"round_method_type":"R"},"USD":{"currency_symbol":"$","decimal_place":2,"round_method_type":"R"},"CNY":{"currency_symbol":"&yen;","decimal_place":2,"round_method_type":"R"},"TWD":{"currency_symbol":"NT$","decimal_place":0,"round_method_type":"F"},"EUR":{"currency_symbol":"\u20ac","decimal_place":2,"round_method_type":"R"},"BRL":{"currency_symbol":"R$","decimal_place":2,"round_method_type":"R"},"AUD":{"currency_symbol":"A$","decimal_place":2,"round_method_type":"R"},"BHD":{"currency_symbol":".&#1583;.&#1576;","decimal_place":3,"round_method_type":"R"},"BDT":{"currency_symbol":"&#2547;","decimal_place":2,"round_method_type":"R"},"GBP":{"currency_symbol":"&pound;","decimal_place":2,"round_method_type":"R"},"CAD":{"currency_symbol":"C$","decimal_place":2,"round_method_type":"R"},"CZK":{"currency_symbol":"K&#269;","decimal_place":2,"round_method_type":"R"},"DKK":{"currency_symbol":"kr","decimal_place":2,"round_method_type":"R"},"HKD":{"currency_symbol":"HK$","decimal_place":2,"round_method_type":"R"},"HUF":{"currency_symbol":"Ft","decimal_place":2,"round_method_type":"R"},"INR":{"currency_symbol":"&#8377;","decimal_place":2,"round_method_type":"R"},"IDR":{"currency_symbol":"Rp","decimal_place":0,"round_method_type":"F"},"ILS":{"currency_symbol":"&#8362;","decimal_place":2,"round_method_type":"R"},"JOD":{"currency_symbol":" &#1583;&#1610;&#1606;&#1575;&#1585;","decimal_place":3,"round_method_type":"R"},"KWD":{"currency_symbol":"&#1583;&#1610;&#1606;&#1575;&#1585;","decimal_place":3,"round_method_type":"R"},"MYR":{"currency_symbol":"RM","decimal_place":2,"round_method_type":"R"},"MXN":{"currency_symbol":"Mex$","decimal_place":2,"round_method_type":"R"},"NZD":{"currency_symbol":"NZ$","decimal_place":2,"round_method_type":"R"},"NOK":{"currency_symbol":"kr","decimal_place":2,"round_method_type":"R"},"PKR":{"currency_symbol":"&#8360;","decimal_place":2,"round_method_type":"R"},"PLN":{"currency_symbol":"z\u0142","decimal_place":2,"round_method_type":"R"},"RUB":{"currency_symbol":"\u0440\u0443\u0431","decimal_place":2,"round_method_type":"R"},"SAR":{"currency_symbol":"&#65020;","decimal_place":2,"round_method_type":"R"},"SGD":{"currency_symbol":"S$","decimal_place":2,"round_method_type":"R"},"ZAR":{"currency_symbol":"R","decimal_place":2,"round_method_type":"R"},"SEK":{"currency_symbol":"kr","decimal_place":2,"round_method_type":"R"},"CHF":{"currency_symbol":"Fr","decimal_place":2,"round_method_type":"R"},"THB":{"currency_symbol":"&#3647;","decimal_place":2,"round_method_type":"R"},"TRY":{"currency_symbol":"TL","decimal_place":2,"round_method_type":"R"},"AED":{"currency_symbol":"&#1601;&#1604;&#1587;","decimal_place":2,"round_method_type":"R"}}; return aCurrencyList[sCurrencyCode] },isUseReferenceCurrency : function() {return false }};CAFE24.COMMON_UTIL = {convertSslForString : function(sString) { return sString.replace(/http:/gi, '');},convertSslForHtml : function(sHtml) { return sHtml.replace(/((?:src|href)\s*=\s*['"])http:(\/\/(?:[a-z0-9\-_\.]+)\/)/ig, '$1$2');},getProtocol : function() { return 'https'; },moveSsl : function() { if (CAFE24.COMMON_UTIL.getProtocol() === 'http') { var oLocation = jQuery(window.location); var sUrl = 'https://' + oLocation.attr('host') + oLocation.attr('pathname') + oLocation.attr('search'); window.location.replace(sUrl); } },setEcCookie : function(sKey, sValue, iExpire) {var exdate = new Date();exdate.setDate(exdate.getDate() + iExpire);var setValue = escape(sValue) + "; domain=." + CAFE24.GLOBAL_INFO.getBaseDomain() + "; path=/;expires=" + exdate.toUTCString();document.cookie = sKey + "=" + setValue;}};CAFE24.SHOP_LIB_INFO = {getBankInfo : function() { 
var oBankInfo = "";
$.ajax({
type: "GET",
url: "/exec/front/Shop/Bankinfo",
dataType: "json",
async: false,
success: function(oResponse) {
oBankInfo = oResponse;
}
});
return oBankInfo; }};            var EC_SDE_SHOP_NUM = CAFE24.SDE_SHOP_NUM;
var SHOP = CAFE24.getDeprecatedNamespace('SHOP');
var EC_COMMON_UTIL = CAFE24.getDeprecatedNamespace('EC_COMMON_UTIL');
var EC_SHOP_LIB_INFO = CAFE24.getDeprecatedNamespace('EC_SHOP_LIB_INFO');
var EC_CURRENCY_INFO = CAFE24.getDeprecatedNamespace('EC_CURRENCY_INFO');
CAFE24.ROOT_DOMAIN = "cafe24.com";
CAFE24.API_DOMAIN = "cafe24api.com";
CAFE24.GLOBAL_INFO = (function() {
var oData = {"base_domain":"nsmall2022.cafe24.com","root_domain":"cafe24.com","api_domain":"cafe24api.com","is_global":false,"is_global_standard":false,"country_code":"KR","language_code":"ko_KR","admin_language_code":"ko_KR","front_language_code":"ko_KR"};
return {
getBaseDomain: function() {
return oData['base_domain'];
},
getRootDomain: function() {
return oData['root_domain'];
},
getApiDomain: function() {
return oData['api_domain'];
},
isGlobal: function() {
return oData['is_global'];
},
isGlobalStandard: function() {
return oData['is_global_standard'];
},
getCountryCode: function() {
return oData['country_code'];
},
getLanguageCode: function() {
return oData['language_code'];
},
getAdminLanguageCode: function() {
return oData['admin_language_code'];
},
getFrontLanguageCode: function() {
return oData['front_language_code'];
}
};
})();
var EC_ROOT_DOMAIN = CAFE24.ROOT_DOMAIN;
var EC_API_DOMAIN = CAFE24.API_DOMAIN;
var EC_TRANSLATE_LOG_STATUS = CAFE24.TRANSLATE_LOG_STATUS;
var EC_GLOBAL_INFO = CAFE24.getDeprecatedNamespace('EC_GLOBAL_INFO');
CAFE24.AVAILABLE_LANGUAGE = ["ko_KR","zh_CN","en_US","zh_TW","es_ES","pt_PT","vi_VN","ja_JP","en_PH"];
CAFE24.AVAILABLE_LANGUAGE_CODES = {"ko_KR":"KOR","zh_CN":"CHN","en_US":"ENG","zh_TW":"TWN","es_ES":"ESP","pt_PT":"PRT","vi_VN":"VNM","ja_JP":"JPN","en_PH":"PHL"};
var EC_AVAILABLE_LANGUAGE = CAFE24.AVAILABLE_LANGUAGE;
var EC_AVAILABLE_LANGUAGE_CODES = CAFE24.AVAILABLE_LANGUAGE_CODES;
CAFE24.GLOBAL_PRODUCT_LANGUAGE_CODES = {  
sClearanceCategoryCode: '',
sManualLink: '//support.cafe24.com/hc/ko/articles/7739013909529',
sHsCodePopupLink: 'https://www.wcotradetools.org/en/harmonized-system',
aCustomRegex: '"PHL" : "^[0-9]{8}[A-Z]?$"',
sCountryCodeData: 'kor',
sEnglishExampleURlForGlobal: '',
aReverseAddressCountryCode: ["VNM","PHL"],
aSizeGuideCountryAlign: '["US","UK","EU","KR","JP","CN"]',
aIsSupportTran: ["ja_JP","zh_CN","zh_TW","en_US","vi_VN","en_PH","pt_PT","es_ES"]
};
var EC_GLOBAL_PRODUCT_LANGUAGE_CODES = CAFE24.getDeprecatedNamespace('EC_GLOBAL_PRODUCT_LANGUAGE_CODES');
CAFE24.GLOBAL_ORDER_LANGUAGE_CODES = {
aModifyOrderLanguage: {"KR":"ko_KR","JP":"ja_JP","CN":"zh_CN","TW":"zh_TW","VN":"vi_VN","PH":"en_PH"},
aUseIdCardKeyCountry: ["CN","TW"],
aLanguageWithCountryCode: {"zh_CN":["CN","CHN","HK","HNK"],"ja_JP":["JP","JPN"],"zh_TW":["TW","TWN"],"ko_KR":["KR","KOR"],"vi_VN":["VN","VNM"],"en_PH":["PH","PHL"]},
aCheckDisplayRequiredIcon: ["ja_JP","zh_CN","zh_TW","en_US","vi_VN","en_PH"],
aSetReceiverName: {"zh_CN":{"sCountry":"CN","bUseLastName":true},"zh_TW":{"sCountry":"TW","bUseLastName":false},"ja_JP":{"sCountry":"JP","bUseLastName":true}},
aSetDeferPaymethodLanguage: {"ja_JP":"\uc77c\ubcf8","zh_CN":"\uc911\uad6d"},
aUseDeferPaymethod: ["ja_JP","zh_CN"],
aCheckShippingCompanyAndPaymethod: ["ja_JP","zh_CN"],
aSetDeferPaymethodLanguageForShipping: {"ja_JP":"\u65e5\u672c","zh_CN":"\uc911\uad6d"},
aCheckStoreByPaymethod: ["ja_JP","zh_CN"],
aCheckIsEmailRequiredForJs: ["en_US","zh_CN","zh_TW","ja_JP","vi_VN","en_PH"],
aSetIdCardKeyCountryLanguage: {"CN":"\uc911\uad6d\uc758","TW":"\ub300\ub9cc\uc758"},
aReverseGlobalAddress: ["en_PH","vi_VN","PHL","VNM","VN","PH"],
aNoCheckZipCode: ["KOR","JPN"],
aNotPostCodeAPICountryList: ["en_US","es_ES","pt_PT","en_PH"],
aEnableSearchExchangeAddr: ["KR","JP","CN","VN","TW","PH"],
aDuplicatedBaseAddr: ["TW","JP"],
aReverseAddressCountryCode: ["VN","PH"],
aCheckZipCode: ["PHL","en_PH","PH"]
};
var EC_GLOBAL_ORDER_LANGUAGE_CODES = CAFE24.getDeprecatedNamespace('EC_GLOBAL_ORDER_LANGUAGE_CODES');
CAFE24.GLOBAL_MEMBER_LANGUAGE_CODES = {  
sAdminWebEditorLanguageCode: 'ko' ,
oNotAvailDecimalPointLanguages: ["ko_KR","ja_JP","zh_TW","vi_VN"],
oAddressCountryCode: {"KOR":"ko_KR","JPN":"ja_JP","CHN":"zh_CN","TWN":"zh_TW","VNM":"vi_VN","PHL":"en_PH"},
};
var EC_GLOBAL_MEMBER_LANGUAGE_CODES = CAFE24.getDeprecatedNamespace('EC_GLOBAL_MEMBER_LANGUAGE_CODES');
CAFE24.GLOBAL_BOARD_LANGUAGE_CODES = {  
bUseLegacyBoard: true
};
var EC_GLOBAL_BOARD_LANGUAGE_CODES = CAFE24.getDeprecatedNamespace('EC_GLOBAL_BOARD_LANGUAGE_CODES');
CAFE24.GLOBAL_MALL_LANGUAGE_CODES = {
oDesign: {
oDesignAddReplaceInfo: {"group_id":"SKIN.ADD.ADMIN.DESIGNDETAIL","replacement":{"KR":"KOREAN","US":"ENGLISH","JP":"JAPANESE","CN":"SIMPLIFIED.CHINESE","TW":"TRADITIONAL.CHINESE","ES":"SPANISH","PT":"PORTUGUESE","PH":"ENGLISH"}},
oDesignDetailLanguageCountryMap: {"KR":"ko_KR","JP":"ja_JP","CN":"zh_CN","TW":"zh_TW","US":"en_US","ES":"es_ES","PT":"pt_PT","PH":"en_PH"},
oSmartDesignSwitchTipLink: {"edibot":{"img":"\/\/img.echosting.cafe24.com\/smartAdmin\/img\/design\/img_editor_dnd.png","link":"\/\/ecsupport.cafe24.com\/board\/free\/list.html?board_act=list&board_no=12&category_no=9&cate_no=9"},"smart":{"img":"\/\/img.echosting.cafe24.com\/smartAdmin\/img\/design\/ko_KR\/img_editor_smart.png","link":"\/\/sdsupport.cafe24.com"}},
oSmartDesignDecoShopList: ["ko_KR","ja_JP","zh_CN","en_US","zh_TW","es_ES","pt_PT"],
oSmartDesignDecoMultilingual: {"list":{"ko_KR":"KOREAN","en_US":"ENGLISH","ja_JP":"JAPANESE","zh_CN":"SIMPLIFIED.CHINESE","zh_TW":"TRADITIONAL.CHINESE","es_ES":"SPANISH","pt_PT":"PORTUGUESE","vi_VN":"VIETNAMESE"},"group_id":"EDITOR.LAYER.EDITING.DECO"},
aSmartDesignModuleShopList: ["ko_KR","ja_JP","zh_CN","en_US","zh_TW","es_ES","pt_PT"]
},
oStore: {
oMultiShopCurrencyInfo: {"en_US":{"currency":"USD"},"zh_CN":{"currency":"USD","sub_currency":"CNY"},"ja_JP":{"currency":"JPY"},"zh_TW":{"currency":"TWD"},"es_ES":{"currency":"EUR"},"pt_PT":{"currency":"EUR"},"ko_KR":{"currency":"KRW"},"vi_VN":{"currency":"VND"},"en_PH":{"currency":"PHP"}},
oBrowserRedirectLanguage: {"ko":{"primary":"ko_KR","secondary":"en_US"},"en":{"detail":{"en-ph":{"primary":"en_PH","secondary":"en_US"},"en-us":{"primary":"en_US","secondary":"es_ES"},"default":{"primary":"en_US","secondary":"es_ES"}}},"ja":{"primary":"ja_JP","secondary":"en_US"},"zh":{"detail":{"zh-cn":{"primary":"zh_CN","secondary":"en_US"},"zh-tw":{"primary":"zh_TW","secondary":"zh_CN"},"default":{"primary":"en_US","secondary":"ko_KR"}}},"es":{"primary":"es_ES","secondary":"en_US"},"pt":{"primary":"pt_PT","secondary":"en_US"},"vi":{"primary":"vi_VN","secondary":"en_US"},"default":{"primary":"en_US","secondary":"ko_KR"}},
aChangeableLanguages: ["en_US","ja_JP","ko_KR"],
aNoZipCodeLanguage: ["ko_KR","ja_JP"]
},
oMobile: {
sSmartWebAppFaqUrl: "https://support.cafe24.com/hc/ko/articles/8466586607641",
sAmpFaqUrl: "https://ecsupport.cafe24.com/board/free/read.html?no=1864&board_no=5&category_no=13&cate_no=13&category_no=13&category_no=13",
},
oPromotion: {
bQrCodeAvailable: true,
bSnsMarketingAvailable: true
},
oShippingReverseAddressLanguage: ["vi_VN","en_PH"] ,
oGlobalStandardSwitchHelpCodeLink: {"SH.DS":{"link":"\/\/serviceguide.cafe24shop.com\/en_PH\/SH.DS.html"},"PR.DS":{"link":"\/\/serviceguide.cafe24shop.com\/en_PH\/PR.DS.html"},"OR.SM.BO":{"link":"\/\/serviceguide.cafe24shop.com\/en_PH\/OR.SM.BO.html"},"DE.DS":{"link":"\/\/serviceguide.cafe24shop.com\/en_PH\/DE.DS.html"},"MB.DS":{"link":"\/\/serviceguide.cafe24shop.com\/en_PH\/MB.DS.html"},"PM.DS":{"link":"\/\/serviceguide.cafe24shop.com\/en_PH\/PM.DS.html"}},
getAdminMainLocaleLanguage: function(sSkinLocaleCode) {
var oLocaleData = [];
var locale = "";
var shopLangName = "";
if (sSkinLocaleCode == "US") {
locale = "en_US";
shopLangName = "ENGLISH";
} else if (sSkinLocaleCode == "JP") {
locale = "ja_JP";
shopLangName = "JAPANESE";
} else if (sSkinLocaleCode == "CN") {
locale = "zh_CN";
shopLangName = "SIMPLIFIED.CHINESE";
} else if (sSkinLocaleCode == "TW") {
locale = "zh_TW";
shopLangName = "TRADITIONAL.CHINESE";
} else if (sSkinLocaleCode == "ES") {
locale = "es_ES";
shopLangName = "SPANISH";
} else if (sSkinLocaleCode == "PT") {
locale = "pt_PT";
shopLangName = "PORTUGUESE";
} else if (sSkinLocaleCode == "VN") {
locale = "vi_VN";
shopLangName = "VIETNAMESE";
} else if(sSkinLocaleCode == "PH") {
locale = "en_PH";
shopLangName = "ENGLISH.PH";
}
oLocaleData["locale"] = locale;
oLocaleData["shopLangName"] = shopLangName;
return oLocaleData;
}
};
var EC_GLOBAL_MALL_LANGUAGE_CODES = CAFE24.getDeprecatedNamespace('EC_GLOBAL_MALL_LANGUAGE_CODES');
CAFE24.GLOBAL_DATETIME_INFO = {
oConstants: {"STANDARD_DATE_REGEX":"\/([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))\/","IN_ZONE":"inZone","OUT_ZONE":"outZone","IN_FORMAT":"inFormat","OUT_FORMAT":"outFormat","IN_DATE_FORMAT":"inDateFormat","IN_TIME_FORMAT":"inTimeFormat","OUT_DATE_FORMAT":"outDateFormat","OUT_TIME_FORMAT":"outTimeFormat","IN_FORMAT_DATE_ONLY":1,"IN_FORMAT_TIME_ONLY":2,"IN_FORMAT_ALL":3,"OUT_FORMAT_DATE_ONLY":1,"OUT_FORMAT_TIME_ONLY":2,"OUT_FORMAT_ALL":3,"DATE_ONLY":"YYYY-MM-DD","TIME_ONLY":"HH:mm:ss","FULL_TIME":"YYYY-MM-DD HH:mm:ss","ISO_8601":"YYYY-MM-DD[T]HH:mm:ssZ","YEAR_ONLY":"YYYY","MONTH_ONLY":"MM","DAY_ONLY":"DD","WEEK_ONLY":"e","TIME_H_I_ONLY":"HH:mm","TIME_HOUR_ONLY":"HH","TIME_MINUTE_ONLY":"mm","POSTGRE_FULL_TIME":"YYYY-MM-DD HH24:MI:SS","POSTGRE_TIME_ONLY":" HH24:MI:SS","MICRO_SECOND_ONLY":"u","SEOUL":"Asia\/Seoul","TOKYO":"Asia\/Tokyo","SHANGHAI":"Asia\/Shanghai","TAIPEI":"Asia\/Taipei","HANOI":"Asia\/Bangkok","LOS_ANGELES":"America\/Los_Angeles","LISBON":"Europe\/Lisbon","MADRID":"Europe\/Madrid","SINGAPORE":"Asia\/Singapore","UTC":"Etc\/UTC","MAX_DATETIME":"9999-12-31 23:59:59"},
oOptions: {"inZone":"Asia\/Seoul","inFormat":"YYYY-MM-DD HH:mm:ss","inDateFormat":"YYYY-MM-DD","inTimeFormat":"HH:mm:ss","outZone":"Asia\/Seoul","outFormat":"YYYY-MM-DD HH:mm:ss","outDateFormat":"YYYY-MM-DD","outTimeFormat":"HH:mm:ss"},
oPolicies: {"shop":{"outZone":"Asia\/Seoul","outFormat":"YYYY-MM-DD HH:mm:ss","outDateFormat":"YYYY-MM-DD","outTimeFormat":"HH:mm:ss"}},
sOverrideTimezone: '',
sMomentNamespace: 'EC_GLOBAL_MOMENT'
};
CAFE24.FRONT_JS_CONFIG_MANAGE = {"sSmartBannerScriptUrl":"https:\/\/app4you.cafe24.com\/SmartBanner\/tunnel\/scriptTags?vs=1563164396689206","sMallId":"nsmall2022","sDefaultAppDomain":"https:\/\/app4you.cafe24.com","sWebLogOffFlag":"F"};
var EC_FRONT_JS_CONFIG_MANAGE = CAFE24.getDeprecatedNamespace('EC_FRONT_JS_CONFIG_MANAGE');
CAFE24.FRONT_JS_CONFIG_MEMBER = {"sAuthUrl":"https:\/\/ipin-ec.cafe24.com\/certify\/v1\/?action=auth"};
var EC_FRONT_JS_CONFIG_MEMBER = CAFE24.getDeprecatedNamespace('EC_FRONT_JS_CONFIG_MEMBER');
CAFE24.FRONT_JS_CONFIG_SHOP = {"aProductPurchaseInfo_4558":{"bIsSuccess":true,"sMessage":"","bReplaceLoginPage":false,"bIsDisplayPurchaseButton":true},"search_period":[],"calendar_config":{"maxDate":"2028-05-23","locale":"ko"},"sSearchUrl":"\/product\/search.html?keyword=","bIsRecentList":true,"bDirectBuyOrderForm":false,"product_service_type":"standard","bIsExclusivePurchaseOnly":false,"is_cultural_tax":"F","bECUseItemSalePrice":false,"DROPSHIPPING":{"sellable":"T"},"sCouponDownloadPage":"\/coupon\/coupon_productdetail.html","aOptionColorchip":[],"oCategoryInfo":{"":{"category_no":822,"category_name":"\ud83c\udf6c\uc2a4\ub0b5 & \uc824\ub9ac"}},"aProductPurchaseInfo_2758":{"bIsSuccess":true,"sMessage":"","bReplaceLoginPage":false,"bIsDisplayPurchaseButton":true}};
var EC_FRONT_JS_CONFIG_SHOP = CAFE24.getDeprecatedNamespace('EC_FRONT_JS_CONFIG_SHOP');
typeof window.CAFE24 === "undefined" && (window.CAFE24 = {});
CAFE24.BOARD = {"config_4":{"board_no":4,"use_block":"T","use_report":"T"},"captcha_config_review":{"use_captcha_bulletin":"T","use_captcha_comment":"T","use_captcha_member":"F","use_captcha_non_member":"T","use_comment":"T"},"config_6":{"board_no":6,"use_block":"T","use_report":"T"},"captcha_config_qna":{"use_captcha_bulletin":"T","use_captcha_comment":"T","use_captcha_member":"F","use_captcha_non_member":"T","use_comment":"T"},"config_1":{"board_no":1,"use_block":"F","use_report":"F"}};
CAFE24.FRONTEND = {"FW_MANIFEST_CACHE_REVISION":2605201482,"IS_WEB_VIEW":"F"};
CAFE24.ROUTE = {"is_mobile":false,"is_need_route":false,"language_code":"ZZ","path":{"origin":"\/product\/\uc778\ub514\uc548\ubc2583g1\/2758\/","result":"\/product\/\uc778\ub514\uc548\ubc2583g1\/2758\/","prefix":""},"shop_no":0,"skin_code":"default","support_language_list":{"ar":"ar_EG","ar-EG":"ar_EG","de":"de_DE","de-DE":"de_DE","en":"en_US","en-IN":"en_IN","en-PH":"en_PH","en-US":"en_US","es":"es_ES","es-ES":"es_ES","hi":"hi_IN","hi-IN":"hi_IN","id":"id_ID","id-ID":"id_ID","it":"it_IT","it-IT":"it_IT","ja":"ja_JP","ja-JP":"ja_JP","ko":"ko_KR","ko-KR":"ko_KR","ms":"ms_MY","ms-MY":"ms_MY","pt":"pt_PT","pt-PT":"pt_PT","ru":"ru_RU","ru-RU":"ru_RU","th":"th_TH","th-TH":"th_TH","tr":"tr_TR","tr-TR":"tr_TR","vi":"vi_VN","vi-VN":"vi_VN","zh":"zh_CN","zh-CN":"zh_CN","zh-HK":"zh_HK","zh-MO":"zh_MO","zh-SG":"zh_SG","zh-TW":"zh_TW"}};
</script>
<link rel="stylesheet" type="text/css" href="//img.echosting.cafe24.com/editors/froala/css/froala_style_ec.min.css?vs=2605201482" charset="utf-8"/>

<link rel="stylesheet" type="text/css" href="/ind-script/optimizer.php?filename=lZIxDsIwDEX3KCvnMANcACQOAOIATppC1DS2HEeC21NggIKQyPr13v8ezEInwREkFKriA_hSoBfKCp7GkbKdggX_poI3hVLVSNk4ujThVbVtIOE1SIug6FJoEohNijkYhzl_bKXo4BgZ_QD795YtppA7FFjZtV1Cn1A5-mEuIzMczsRzdfc4YGK66vVv3hFK90Vv7ukcn2L7hCUwibY5LpEf_lFen3ID&type=css&k=1d06ada56d1358570bc3bee2585787122dd20a3b&t=1779324292"  /><link rel="stylesheet" type="text/css" href="/ind-script/optimizer_user.php?filename=nZRBTsQwDEX3U7acoxJwAQSbWXMCt_G0Rk4cGmcKtye0IzZohD2ruPF_cePfugTsAhaaUh9lIMZ-LKWFobYwL20dtQ-oQHzXMvfFol8xp_xSi0q8AjF8SdV-gELjdsLEMgA_NtnZXmfPHCNMaIcgBFKSBHwL00GiCD-xnd7bt8vs1IJnwtWu_0jgOZy3S3RlpYxWk0aJ8erF_6j3Dasax0N7wEMlL5FhogSKXm5Gzu5ae_-82FBV7Y37peTTi7QELl5IYXAjIqyUb6jEbp9OwsHvUzimk1ix7S9Ymk0ptPeLlHxj68k55XzyB5_8_yFwAWNtFpZZ8ttMOVOa7ONjhjIrOIDL-rpNwud32D7sbw&type=css&k=b0dab4fbd47e2b2c2daa66d827c94d70a141aaa9&t=1775008043&user=T"  />
<style type="text/css">
#prdDetailContentLazy img[src=""], #prdDetailContentLazy img:not([src]) { visibility: hidden !important; height: 1px !important; }
</style>
<title>인디안밥(83g*1) - 농심몰</title></head>
<body>	<div id="subpage" class="product__detail  ">
		<div class="xans-element- xans-popup xans-popup-multipopup "><!--
				$banner_popup_no =
				※ 노출시킬 팝업의 ID를 숫자로 넣어주세요.
			-->

					
</div>
		
		<div id="wrap">
			<div id="container">
				


<header id="header">
  <div class="header__top header__top--white">
    <div class="header__ad displaynone" rel="js-header__ad">
      <div class="contents">
        <strong>농심의 인기상품을 100원</strong>에 받아가세요!
        <a href="/product/project.html?cate_no=105" class="btnNormal">구경하러가기</a>
      </div>
      <a href="#none" class="btn--close">닫기</a>
    </div>
    <div class="header">
      <h1 id="logo" class="xans-element- xans-layout xans-layout-logotop "><a href="/">농심몰</a>
</h1>
      <h1 class="xans-element- xans-product xans-product-headcategory  "><a href="#">🍬스낵 & 젤리</a>
</h1>
<!-- 상품 -->
      <!-- 게시판 -->
      <a href="/member/login.html?noMemberOrder&amp;returnUrl=/" class="xans-element- xans-layout xans-layout-statelogoff btn--login "><strong><span>로그인</span></strong>
</a>
            <!-- <a class="btn--benefit" href="/lounge/membership.html" module="Layout_stateLogon">멤버십</a> -->
      <a class="btn--aside" href="/layout/basic/gnb.html">카테고리</a>
      <a class="btn--back" href="javascript:history.go(-1)">뒤로가기</a>
      <a class="btn--search" href="#" rel="js-search-toggle">검색</a>
      <a href="/order/basket.html" class="xans-element- xans-layout xans-layout-statelogoff btn--basket ">장바구니 
<span class="count displaynone EC-Layout_Basket-count-display"><span class="EC-Layout-Basket-count"></span></span>
</a>
            <a class="btn--home" href="/">홈</a>
    </div>
    <!--LEADERMINE 2024-06-25 MO 헤더 및 GNB UI/UX  -->
    <div id="gnb-simple">
      <ul class="depth--first depth--first--theme2">
        <li class="point" data-cate-id="">
          <a href="/" tabindex="0" data-category="navigation" data-action="홈" data-label="추천">추천</a>
        </li>
        <li data-cate-id="90">
          <a href="/product/list.html?cate_no=90" tabindex="0" data-category="navigation" data-action="홈" data-label="농꾸">농꾸</a>
        </li>
        <li data-path="/product/special.html">
          <a href="/product/special.html?cate_no=97#cate_99" tabindex="0" data-category="navigation" data-action="홈" data-label="굿즈">굿즈</a>
        </li>
        <li data-path="/product/hotdeal.html" class="xans-element- xans-product xans-product-listmain-11 xans-product-listmain xans-product-11 xans-record-"><a href="/product/hotdeal.html?cate_no=88&amp;sort_method=5" tabindex="0" data-category="navigation" data-action="홈" data-label="핫딜">핫딜</a>
<!-- <ul class="depth--second">
						<li><a href="/product/hotdeal.html?cate_no=88" data-category="navigation" data-action="핫딜" data-label="핫딜">핫딜</a></li>
						<li><a href="javascript:alert('준비중입니다.');" data-category="navigation" data-action="핫딜" data-label="라이브커머스">라이브커머스</a></li>
						<li><a href="/livecommerce.html" data-category="navigation" data-action="핫딜" data-label="라이브커머스">라이브커머스</a></li>
                    </ul>-->
</li>
        <li data-path="/board/gallery/list.html">
          <a href="/board/gallery/list.html?board_no=8" tabindex="0" data-category="navigation" data-action="홈" data-label="이벤트">이벤트</a>
          <!--<ul class="depth--second">-->
          <!-- <li><a href="/product/project.html?cate_no=105">기획전</a></li> -->
          <!-- <li><a href="/product/fao.html?cate_no=101">세계 식량의 날</a></li> -->
          <!-- <li><a href="/product/project.html?cate_no=105" data-category="navigation" data-action="이벤트" data-label="100원 딜">100원 딜</a></li> -->
          <!--<li><a href="/board/gallery/list.html?board_no=17" data-category="navigation" data-action="이벤트" data-label="얼리어먹터">얼리어먹터</a></li>
						<li><a href="/board/gallery/list.html?board_no=8" data-category="navigation" data-action="이벤트" data-label="이벤트">기획전/이벤트</a></li>
						<li><a href="/coupon/coupon_zone.html" data-category="navigation" data-action="이벤트" data-label="쿠폰/상품권">쿠폰/상품권</a></li>
                    </ul>-->
        </li>
        <li data-cate-id="382" class="recommend_nav"><a href="/product/recommend.html?cate_no=382" tabindex="0" data-category="navigation" data-action="홈" data-label="신상템">신상템</a>
        <li data-cate-id="95" class="list_nav"><a href="/product/list.html?cate_no=95" tabindex="0" data-category="navigation" data-action="홈" data-label="정기구독">정기구독</a>
        <!--<ul class="depth--second">
						<li><a href="/product/list.html?cate_no=95" data-category="navigation" data-action="정기구독" data-label="백산수">백산수</a></li>
						<li><a href="/product/list.html?cate_no=96" data-category="navigation" data-action="정기구독" data-label="백산수">일반제품</a></li>
						<li><a href="/lounge/survey.html" data-category="navigation" data-action="정기구독" data-label="고객서베이">고객서베이</a></li>
                    </ul>-->
        
        <!--<li><a href="#" tabindex="0" data-category="navigation" data-action="홈" data-label="라운지">라운지</a>
                    <ul class="depth--second">
						<li><a href="/lounge/membership.html" data-category="navigation" data-action="라운지" data-label="멤버십">멤버십</a></li>
						<li><a href="/lounge/survey.html" data-category="navigation" data-action="라운지" data-label="고객서베이">고객서베이</a></li>
						<li><a href="/board/noodlefoodle/index.html" data-category="navigation" data-action="라운지" data-label="누들푸들">누들푸들</a></li>
						<li><a href="/board/experience/list.html?board_no=101" data-category="navigation" data-action="라운지" data-label="체험단리뷰">체험단 리뷰</a></li>
                    </ul>
                </li>-->
      </ul>
    </div>
    <!--!LEADERMINE 2024-06-25 MO 헤더 및 GNB UI/UX  -->
  </div>
  <!-- LEADERMINE 2025-07-01 MO 바텀 내비게이션바 UI 개선 -->
  <!-- <div class="header__bottom header-default" data-animation="true">
    <a class="header__bottom__dot" rel="js-header__bottom__dot" href="/"></a>
    <div class="header__bottom__box" data-animation-all="true"></div>
    <div class="header__bottom__list">
      <ul class="float_wrap">
        <li class="left_box h_cate_btn"><a href="/layout/basic/gnb.html" class="fold">카테고리</a></li>
        <li class="left_box"><a href="/lounge/coupon.html">쿠폰혜택</a></li>
        <li class="right_box" module="Layout_stateLogoff"><a
            href="/member/login.html?noMemberOrder&returnUrl=/myshop/index.html">마이페이지</a></li>
        <li class="right_box" module="Layout_stateLogon"><a href="/myshop/index.html">마이페이지</a></li>
        <li class="right_box"><a href="/myshop/recent_list.html">최근본상품</a></li>
      </ul>
    </div>
  </div> -->
  <!-- !LEADERMINE 2025-07-01 MO 바텀 내비게이션바 UI 개선 -->
</header>

<div class="header__search header__search--theme2">
  <div class="header__search__in" data-animation="true" data-animation-delay="0.5">
    <form id="searchBarForm" name="" action="/product/search.html" method="get" target="_self" enctype="multipart/form-data" >
<input id="banner_action" name="banner_action" value="" type="hidden"  /><div class="xans-element- xans-layout xans-layout-searchheader "><!--
                $category_page=/product/list.html
            -->
<h2>고객님,<br>무엇을 찾으시나요?</h2>
<fieldset>
        <legend>검색</legend>
        <a href="#" class="btn--close" rel="js-search-toggle"><span>닫기</span></a>
        <div class="header__search__area">
          <input id="keyword" name="keyword" fw-filter="" fw-label="검색어" fw-msg="" class="inputTypeText" placeholder="" onmousedown="SEARCH_BANNER.clickSearchForm(this)" value="" type="text"  />          <input type="hidden" name="order_by" value="favor">
           <a href="#" onclick="customSearchSubmit('searchBarForm'); return false;">검색</a>
          <!-- <a href="#" onclick="SEARCH_BANNER.submitSearchBanner(this); return false;">검색</a> -->
          <div class="autoList" id="">
            <ul class="autoDrop" id=""></ul>
          </div>
        </div>
      </fieldset>
<!-- 최근 검색어 영역 -->
<div class="xans-element- xans-search xans-search-recentkeyword header__search__recent__keyword displaynone"><h3>최근 검색어 <a href="#" onclick="$Recentword.removeAll()" class="all-remove">모두삭제</a>
</h3>
<div class="swiper-container">
          <div class="swiper-wrapper displaynone">
            <div data-index="" class="swiper-slide ">
              <a href=""></a>
              <button type="button" class="btnDelete" onclick=""><img src="/img/icon-remove-keyword.svg" alt=""></button>
            </div>
            <div data-index="" class="swiper-slide ">
              <a href=""></a>
              <button type="button" class="btnDelete" onclick=""><img src="/img/icon-remove-keyword.svg" alt=""></button>
            </div>
          </div>
        </div>
</div>
<div class="xans-element- xans-search xans-search-hotkeyword header__search__best"><h3>인기 검색어</h3>
<ul>
          <li class="xans-record-"><a href="/product/search.html?keyword=누들핏"># 누들핏</a></li>
          <li class="xans-record-"><a href="/product/search.html?keyword=얼리어먹터"># 얼리어먹터</a></li>
<li class="xans-record-"><a href="/product/search.html?keyword=교촌간장치킨맛"># 교촌간장치킨맛</a></li>
<li class="xans-record-"><a href="/product/search.html?keyword=신라면"># 신라면</a></li>
<li class="xans-record-"><a href="/product/search.html?keyword=배홍동"># 배홍동</a></li>
<li class="xans-record-"><a href="/product/search.html?keyword=웰치스"># 웰치스</a></li>
<li class="xans-record-"><a href="/product/search.html?keyword=카프리썬"># 카프리썬</a></li>
<li class="xans-record-"><a href="/product/search.html?keyword=너구리"># 너구리</a></li>
        </ul>
</div>
<p class="button displaynone"><a href="/product/search.html" class="btnLink">상품상세검색</a></p>
</div>
</form>
    <div class="header__search__recent">
      <h3>최근 본 상품</h3>
      <div rel="js-header-recent" class="xans-element- xans-product xans-product-recentlist slideshow xans-record-"><!--
					$count = 10
				-->
<div class="swiper-container">
                  </div>
<div class="swiper-scrollbar"></div>
</div>
      <script>
        new Swiper('[rel="js-header-recent"] .swiper-container', {
          loop: false,
          slidesPerView: 2.4,
          spaceBetween: 10,
          scrollbar: {
            el: '[rel="js-header-recent"] .swiper-scrollbar',
            draggable: true,
            hide: false,
          },
        });
        prd_sale();
      </script>
    </div>
  </div>
</div>

<script>
  $(document).ready(function () {
    gnb();
    inputPH('#keyword', '검색어를 입력해주세요.');
  });

  // 상품정렬 기준 변경(리디렉션 포함)
  function customSearchSubmit(formIdentifier, keyword) {
    let form = document.getElementById(formIdentifier);

    // ID -> class 재시도
    if (!form) {
      form = document.querySelector(`form.${formIdentifier}`);
    }

    if (!form) {
      console.error('폼을 찾을 수 없습니다:', formIdentifier);
      return;
    }

    const keywordInput = form.querySelector('input[name="keyword"]');
    // keyword값을 넘기지 않았을때(검색 버튼 클릭시 대응)
    if (!keyword && keywordInput) {
      keyword = keywordInput.value.trim();
    }

    if (keywordInput) {
      keywordInput.value = keyword;
    } else {
      console.error('keyword input 없음');
      return;
    }

    const orderInput = form.querySelector('input[name="order_by"]');
    if (orderInput) orderInput.value = 'favor';

    const formData = new FormData(form);
    const params = [];

    for (const [key, value] of formData.entries()) {
      params.push(`${encodeURIComponent(key)}=${encodeURIComponent(value)}`);
    }

    const searchURL = form.action + '?' + params.join('&');

    location.href = searchURL;
  }

  document.addEventListener('DOMContentLoaded', function () {
    const url = new URL(location.href);
    const keyword = url.searchParams.get('keyword');
    const orderBy = url.searchParams.get('order_by');

    if (orderBy === 'related' && keyword) {
      // 리디릭션(모바일 대응)
      const emptyEl = document.querySelector('p.empty');
      if (
        emptyEl &&
        emptyEl.textContent.includes('검색 결과가 없습니다') &&
        window.getComputedStyle(emptyEl).display !== 'none'
      ) {
        url.searchParams.set('order_by', 'favor');
        location.replace(url.toString());
      }
    }

    // 최근 검색어
    document.querySelectorAll('.header__search__recent__keyword .swiper-slide a').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        const keyword = el.textContent.trim();
        const input = document.querySelector('#searchBarForm input[name="keyword"]');

        if (input) {
          input.value = keyword;
          customSearchSubmit('searchBarForm');
        }
      });
    });

    // 인기검색어 레이어 선택
    const sortLinks = document.querySelectorAll('.header__search__best ul li a');
    sortLinks.forEach(link => {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        // 파라미터 뽑기
        const url = new URL(this.href, window.location.origin);
        const keyword = url.searchParams.get('keyword') || '';
        customSearchSubmit('searchBarForm', keyword);
      });
    });
  });

</script>
				<section id="contents">
					






<div class="xans-element- xans-product xans-product-detail"><!--
		$coupon_download_page = /coupon/coupon_productdetail.html
    -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/xeicon@2.3.3/xeicon.min.css">
<!--XEICON-->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">
<!--Fontawesome-->
<div id="titleArea">
    <h2>상품상세 정보</h2>
    <span class="xans-element- xans-layout xans-layout-mobileaction "><a href="#none" onclick="history.go(-1);return false;"><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/layout/btn_back.gif" width="33" alt="뒤로가기"></a>
</span>
  </div>
<div class="xans-element- xans-product xans-product-image overview "><div class="topLogo displaynone">
      <span></span>
      <a href="#none" onclick=""><img src="" alt="공급사 바로가기"></a>
    </div>
<div class="prdImgView">
      <p class="prdImg">
        <a href="#none" id="prdDetailImg" data-param="?product_no=2758">
          <img src="//m.nongshimmall.com/web/product/big/202407/a4085415aeb539bf25bf65686fa9344e.jpg" class="bigImage" alt="인디안밥(83g*1)">        </a>
      </p>
          </div>
<div class="color displaynone">
          </div>
<div class="likeButton displaynone">
      <button type="button"><span class="title">좋아요</span><span class="count"></span></button>
    </div>
</div>
<div class="prdInfo ">
    <p class="prdIcon">             </p>
    <div class="name_wrap">
      <h1 class="name">인디안밥(83g*1)</h1>
      <span class="snsBtn "></span>
      <div class="snsLink ">
        <img src="/imgFile/icon/icon_share.png" onclick="clip()" alt="">
        <img src="//img.cafe24.com/images/ec_admin/icon/icon_facebook.gif"  onclick="SnsLinkAction('facebook',2758);" alt="" /> <img src="//img.cafe24.com/images/ec_admin/icon/icon_twitter.gif"  onclick="SnsLinkAction('twitter',2758);" alt="" />        <span class="xans-element- xans-product xans-product-customsns xans-record-"></span>
      </div>
      <div class="sns-share__box " data-animation="true">
        <div class="sns-share__box__cont">
          <strong class="tit">공유하기</strong>
          <ul>
            <li><a href="#none" class="sns-share__box--kakao"><img src="/img/icon_sns_share_kakako.png" alt=""><span>카카오톡</span></a></li>
<!-- displaynone 되어있음! -->
            <li><a href="#" onclick="SnsLinkActionEdit('facebook',2758);"><img src="/img/icon_sns_share_facebook.png" alt=""><span>페이스북</span></a></li>
            <li><a href="#" onclick="SnsLinkActionEdit('twitter',2758);"><img src="/img/icon_sns_share_x.png" alt=""><span>엑스</span></a></li>
            <li><a href="#" onclick="clip()"><img src="/img/icon_sns_share_url.png" alt=""><span>URL 복사</span></a></li>
          </ul>
          <span class="sns-share__close_btn"></span>
        </div>
      </div>
    </div>
    <p class="displaynone desc"></p>
  </div>
<!-- 2024-06-20 상품 가격 할인율 정보 이슬 작성 -->
<div class="lm-priceContainer">
    <div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="상품명">
          <span class="" style="font-size:16px;color:#666666;">인디안밥(83g*1)</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="원산지">
          <span class="" style="font-size:16px;color:#666666;">기타 상세/구매 정보 참조</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="판매가">
          <span class="" style="font-size:16px;color:#666666;font-weight:bold;"><strong id="span_product_price_text">1,540원 </strong><input id="product_price" name="product_price" value="" type="hidden"  /></span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="배송방법">
          <span class="" style="font-size:16px;color:#666666;">택배</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="배송비(실결제금액 기준)">
          <span class="" style="font-size:16px;color:#666666;"><span class="delv_price_B"><input id="delivery_cost_prepaid" name="delivery_cost_prepaid" value="P" type="hidden"  /><strong>3,000원</strong> (30,000원 이상 구매 시 무료)</span></span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="상품코드">
          <span class="" style="font-size:16px;color:#666666;">P0000ECC</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="제품명">
          <span class="" style="font-size:12px;color:#555555;">인디안밥</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="식품의 유형">
          <span class="" style="font-size:12px;color:#555555;">과자</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="생산자 및 소재지">
          <span class="" style="font-size:12px;color:#555555;">㈜농심 / 서울특별시 동작구 여의대방로 112(신대방동)</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="제조연월일">
          <span class="" style="font-size:12px;color:#555555;">매주 입고되는 제품으로 유통기한이 달라 매번 기재하기 어려움. 유통기한 넉넉한 제품이 발송되며 자세한 내용은 문의 부탁드립니다.</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="소비기한 또는 품질유지기한">
          <span class="" style="font-size:12px;color:#555555;">매주 입고되는 제품으로 유통기한이 달라 매번 기재하기 어려움. 유통기한 넉넉한 제품이 발송되며 자세한 내용은 문의 부탁드립니다.</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="포장단위별 용량(중량) 수량">
          <span class="" style="font-size:12px;color:#555555;">상세정보 참고</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="원재료 및 함량">
          <span class="" style="font-size:12px;color:#555555;">상세정보 참고</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="알레르기 유발물질 함유">
          <span class="" style="font-size:12px;color:#555555;">상세정보 참고</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="영양성분">
          <span class="" style="font-size:12px;color:#555555;">상세정보 참고</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="유전자변형식품 유무">
          <span class="" style="font-size:12px;color:#555555;">상세정보 참고</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="소비자 안전을 위한 주의사항">
          <span class="" style="font-size:12px;color:#555555;">상세정보 참고</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="수입식품 여부">
          <span class="" style="font-size:12px;color:#555555;">해당없음</span>        </div>
      </div>
</div>
<div class="xans-element- xans-product xans-product-detaildesign lm-priceWrap xans-record-"><div class="lm-price">
        <div data-title="소비자상담 관련 전화번호">
          <span class="" style="font-size:12px;color:#555555;">1533-0658</span>        </div>
      </div>
</div>
  </div>
<!-- //2024-06-20 상품 가격 할인율 정보 이슬 작성 -->
<div class="lm-membership">
    <!-- <a href="/product/membership.html?product_no=1349">
            <p><i>👑</i> <span>무료배송 + 3,000원</span> 할인 쿠폰 혜택 받기</p>
            <div class="lm-img-container"><img src="/img/ico_arrow_fold.png" alt=""></div>
        </a> -->

    <!-- 로그인 유무에 따른 배너 노출 로직 추가(25/09) -->
        <a href="/member/login.html" target="_blank" class="xans-element- xans-layout xans-layout-statelogoff lm-membership-coupon logoff ">신규가입 시 
<strong>최대 7,000원 할인 쿠폰</strong>
 증정 
<img src="/img/icon_more.png" alt="이미지"></a>
  </div>
<div class="prdDesc ">
    
<script>
	// 쿠폰 포맷팅 및 치환
	document.querySelectorAll(".coupon .discount span").forEach((el) => {
		const text = el.innerText.trim();
		let number = text.replace(/[^0-9]/g, "");
		let unit = "";

		if (text.includes("%")) {
			unit = "%";
		} else if (text.includes("원")) {
			unit = "￦";
		}

		number = Number(number).toLocaleString();

		const parent = el.closest(".discount");
		parent.innerHTML = `${number}<span class="${unit === "%" ? "per" : "won"}">${unit}</span>`;
	});

	// 기간 설정
	document.querySelectorAll(".coupon .period").forEach((el) => {
		const text = el.innerText;

		const converted = text.replace(/(\d{4})-(\d{2})-(\d{2})/g, (_, y, m, d) => {
			return y.slice(2) + ". " + m + ". " + d;
		});

		el.innerText = converted;
	});
</script>
    <div class="xans-element- xans-product xans-product-detaildesign ec-base-table gClearCell"><table border="1">
        <caption>상품 정보</caption>
        <colgroup>
          <col style="width:120px;">
          <col style="width:auto;">
        </colgroup>
        <tbody class="priceArea">
          <tr data-title="상품명" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:16px;color:#666666;">상품명</span></th>
            <td><span class="" style="font-size:16px;color:#666666;">인디안밥(83g*1)</span></td>
          </tr>
          <tr data-title="원산지" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:16px;color:#666666;">원산지</span></th>
            <td><span class="" style="font-size:16px;color:#666666;">기타 상세/구매 정보 참조</span></td>
          </tr>
<tr data-title="판매가" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:16px;color:#666666;font-weight:bold;">판매가</span></th>
            <td><span class="" style="font-size:16px;color:#666666;font-weight:bold;"><strong id="span_product_price_text">1,540원 </strong><input id="product_price" name="product_price" value="" type="hidden"  /></span></td>
          </tr>
<tr data-title="배송방법" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:16px;color:#666666;">배송방법</span></th>
            <td><span class="" style="font-size:16px;color:#666666;">택배</span></td>
          </tr>
<tr data-title="배송비(실결제금액 기준)" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:16px;color:#666666;">배송비<br>(실결제금액 기준)</span></th>
            <td><span class="" style="font-size:16px;color:#666666;"><span class="delv_price_B"><input id="delivery_cost_prepaid" name="delivery_cost_prepaid" value="P" type="hidden"  /><strong>3,000원</strong> (30,000원 이상 구매 시 무료)</span></span></td>
          </tr>
<tr data-title="상품코드" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:16px;color:#666666;">상품코드</span></th>
            <td><span class="" style="font-size:16px;color:#666666;">P0000ECC</span></td>
          </tr>
<tr data-title="제품명" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">제품명</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">인디안밥</span></td>
          </tr>
<tr data-title="식품의 유형" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">식품의 유형</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">과자</span></td>
          </tr>
<tr data-title="생산자 및 소재지" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">생산자 및 소재지</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">㈜농심 / 서울특별시 동작구 여의대방로 112(신대방동)</span></td>
          </tr>
<tr data-title="제조연월일" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">제조연월일</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">매주 입고되는 제품으로 유통기한이 달라 매번 기재하기 어려움. 유통기한 넉넉한 제품이 발송되며 자세한 내용은 문의 부탁드립니다.</span></td>
          </tr>
<tr data-title="소비기한 또는 품질유지기한" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">소비기한 또는 품질유지기한</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">매주 입고되는 제품으로 유통기한이 달라 매번 기재하기 어려움. 유통기한 넉넉한 제품이 발송되며 자세한 내용은 문의 부탁드립니다.</span></td>
          </tr>
<tr data-title="포장단위별 용량(중량) 수량" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">포장단위별 용량<br>(중량) 수량</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
          </tr>
<tr data-title="원재료 및 함량" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">원재료 및 함량</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
          </tr>
<tr data-title="알레르기 유발물질 함유" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">알레르기 유발물질 함유</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
          </tr>
<tr data-title="영양성분" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">영양성분</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
          </tr>
<tr data-title="유전자변형식품 유무" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">유전자변형식품 유무</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
          </tr>
<tr data-title="소비자 안전을 위한 주의사항" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">소비자 안전을 위한 주의사항</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
          </tr>
<tr data-title="수입식품 여부" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">수입식품 여부</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">해당없음</span></td>
          </tr>
<tr data-title="소비자상담 관련 전화번호" class=" xans-record-">
            <th scope="row"><span class="" style="font-size:12px;color:#555555;">소비자상담 관련 전화번호</span></th>
            <td><span class="" style="font-size:12px;color:#555555;">1533-0658</span></td>
          </tr>
        </tbody>
      </table>
</div>

    <div class="ec-base-table gClearCell regularDelivery displaynone">
      <table border="1">
        <colgroup>
          <col style="width:100px;">
          <col style="width:auto;">
        </colgroup>
        <tbody>
          <tr>
            <th scope="row">구매방법</th>
            <td>
              <label><span class="displaynone"></span>정기배송 <span class="badge displaynone"> <i class="icoDown">할인</i></span></label>
              <label class="displaynone">1회구매</label>
            </td>
          </tr>
          <tr class="displaynone" id="">
            <td colspan="2" class="shippingCycle">
              <strong class="title">배송주기</strong>
              <div class="info_box">
                                <div class="info displaynone" id="">
                  <strong class="title">정기배송 할인 <span class="icoSave">save</span></strong>
                  <ul class="xans-element- xans-product xans-product-regulardiscount info"><li class=""> 결제 시 :  <span class="icoDown">할인</span>
</li>
</ul>
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 2024-06-24 상품상세 하단 수량 옵션 이슬 작성 -->
    <div class="ec-base-table typeWrite gClearCell option">
      <table border="1">
        <!--
                $use_per_add_option = yes
                $default_option = yes
                -->
        <caption>상품 옵션</caption>
        <colgroup>
          <col style="width:100px;">
          <col style="width:auto;">
        </colgroup>
        <tbody>
          <!-- HACK: 임시 제품 이름 / 옵션 -->
          <tr class="quantity lm-quantity-clone single_option">
            <th scope="row">수량</th>
            <td>
              <div class="option_box">
                <p class="product"><strong class="lm-name-clone"></strong></p>
                <div class="ec-base-qty">
                  <a href="javascript:;" class="down lm-qty-bt-clone"><img alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                  <span><input type="tel" value="1" class="lm-qty-input-clone"></span>
                  <a href="javascript:;" class="up lm-qty-bt-clone"><img alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                </div>
                <p class="quantity_price"></p>
                <p class="lm-qauntity-saleprice"></p>
              </div>
            </td>
          </tr>
          <!-- //HACK: 임시 옵션 이름 -->
        </tbody>
      </table>
    </div>
    <!-- 2024-06-24 상품상세 하단 수량 옵션 이슬 작성 -->

    <div class="option_wrap">
      <div class="order_fix_wrap">
        <span class="option_close"></span>
        <div class="fix_all">
          <div class="fix_option">
            <div class="ec-base-table typeWrite gClearCell option">
              <table border="1" class="xans-element- xans-product xans-product-option xans-record-"><!--
                                $use_per_add_option = yes
                                $default_option = yes
                                -->
<caption>상품 옵션</caption>
<colgroup>
                  <col style="width:100px;">
                  <col style="width:auto;">
                </colgroup>
<tbody>
                  <tr class="displaynone">
                    <th scope="row">배송</th>
                    <td class="middle">
                      <label><input id="delv_type_A" name="delv_type" value="A" type="radio" checked="checked"  />국내배송</label>
                      <label><input id="delv_type_B" name="delv_type" value="B" type="radio"  />해외배송</label>
                    </td>
                  </tr>
                </tbody>
<tbody>
                                  </tbody>
<tbody>
                  <tr class="displaynone" id="">
                    <td colspan="2" class="selectButton"><button type="button" class="btnStrong" onclick="">옵션 선택</button></td>
                  </tr>
                                    <!-- 다중선택형 -->
                  <tr class="quantity single_option ">
                    <th scope="row">수량</th>
                    <td>
                      <div class="option_box">
                        <p class="product"><strong>인디안밥(83g*1)</strong></p>
                        <div class="ec-base-qty">
                          <a href="javascript:;" class="down QuantityDown lm-single-qty-count-bt"><img id="" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                          <input id="quantity" name="quantity_opt[]" style="" value="1" type="text"  />                          <a href="javascript:;" class="up QuantityUp lm-single-qty-count-bt"><img id="" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                        </div>
                        <p class="quantity_price">1540</p>
                        <div class="lm-qauntity-saleprice"></div>
                      </div>
                    </td>
                  </tr>
                  <!-- 단일선택형 -->
                                  </tbody>
</table>
            </div>

            <div class="sizeGuide displaynone">
              <a href="#none" class="size_guide_info" product_no="2758">사이즈 가이드</a>
            </div>


            

            
            <div id="totalProducts" class="">
              <table border="1" summary="">
                <caption>상품 목록</caption>
                <colgroup>
                  <col style="width:auto;">
                  <col style="width:100px;">
                  <col style="width:35px;">
                </colgroup>
                <thead>
                  <tr>
                    <th scope="col">상품 정보</th>
                    <th scope="col">가격</th>
                    <th scope="col">삭제</th>
                  </tr>
                </thead>
                <!-- 옵션선택 또는 세트상품 선택시 상품이 추가되는 영역입니다. 쇼핑몰 화면에는 아래와 같은 마크업구조로 표시됩니다. 삭제시 기능이 정상동작 하지 않습니다. -->
                <tbody>
                  <!-- 상품 목록 -->
                </tbody>
                <!-- // 옵션선택 또는 세트상품 선택시 상품이 추가되는 영역입니다. 쇼핑몰 화면에는 아래와 같은 마크업구조로 표시됩니다. 삭제시 기능이 정상동작 하지 않습니다. -->
              </table>
            </div>
            <div id="totalPrice" class="totalPrice">
              <div>
                <strong>총 상품금액</strong>
                <strong class="qty-text">(<span class="lm-single-qty-clone">1</span>개)</strong>
              </div>
              <div>
                <span class="total"><strong class="price">0</strong></span>
              </div>
            </div>
            <p class="ec-base-help displaynone EC-price-warning">할인가가 적용된 최종 결제예정금액은 주문 시 확인할 수 있습니다.</p>
          </div>

          <div id="fixedActionButton" class="xans-element- xans-product xans-product-action"><div class="ec-base-button gColumn  ">
              <button type="button" class="btnNormal wish_btn " onclick="gtm_wishlist(); add_wishlist_nologin('/member/login.html');" id="actionWish"></button>
              <button type="button" class="btnNormal basket_btn " onclick="gtm_basket(); product_submit(2, '/exec/front/order/basket/', this)" id="actionCart">장바구니</button>
              <a href="#none" class="btnSubmit " onclick="product_submit(1, '/exec/front/order/basket/', this)"><span id="actionBuy" class="order_btn">바로구매</span><span class="displaynone" id="actionReserve">예약주문</span><span id="" class="order_btn displaynone">정기배송</span></a>
            </div>
<div class="ec-base-button gColumn soldout displaynone ">
              <button type="button" class="btnNormal wish_btn " onclick="add_wishlist_nologin('/member/login.html');" id="actionWishSoldout">관심상품</button>
              <button type="button" class="btnSubmit displaynone">SOLD OUT</button>
            </div>
<script>
              /* 선물하기 app 이슈 */
              var wishListHtml = $('.xans-product-action :not(.displaynone) button:contains("관심상품")').clone().wrapAll('<div />').parent().html();
              console.log(wishListHtml);
            </script>
<!-- 네이버 체크아웃 구매 버튼  -->
<div id="NaverChk_Button" style="display:none;"></div>
<!-- 상품상세페이지에 추가되는 앱 관련 결제버튼's div -->
<div id="appPaymentButtonBox"></div>
</div>
        </div>
      </div>
    </div>
    <div class="xans-element- xans-product xans-product-action order_fix_btn "><div class="ec-base-button gColumn ">
        <button type="button" class="btnNormal wish_btn " onclick="add_wishlist_nologin('/member/login.html');" id="actionWish"></button>
        <button type="button" class="btnNormal basket_btn " id="actionCart">장바구니</button>
        <a href="#none" class="btnSubmit  lm-single-pop-bt"><span id="actionBuy" class="order_btn">바로구매</span><span class="displaynone" id="actionReserve">예약주문</span><span id="" class="order_btn displaynone">정기배송</span></a>
      </div>
</div>

    <div class="dark_bg"></div>

    <div id="orderFixArea" class="xans-element- xans-product xans-product-action ec-base-button gFixed"><div class="ec-base-button gColumn  ">
        <button type="button" class="btnNormal wish_btn " id="actionWishClone">관심상품</button>
        <button type="button" class="btnNormal basket_btn " id="actionCartClone">장바구니</button>

        <a href="#none" class="btnSubmit "><span id="actionBuyCloneFixed" class="order_btn">바로구매</span><span class="displaynone" id="actionReserveCloneFixed">예약주문</span><span id="" class="order_btn displaynone">정기배송</span></a>
      </div>
<div class="ec-base-button gColumn displaynone ">
        <button type="button" class="btnNormal wish_btn " id="actionWishSoldoutClone">관심상품</button>
        <button type="button" class="btnSubmit  displaynone">SOLD OUT</button>
      </div>
</div>
  </div>
<div class="groobee_title">
    <h3>
<strong>함께 하면 좋은 상품</strong>이예요.</h3>
  </div>
<div class="groobee_recommendation" id="RE483bc8af684b4abd8775dc74380317cc"></div>
<!-- <div class='groobee_recommendation' id='REec7e399cc27c45f8be70d3dfdc261e06'></div> -->
</div>

<div class="xans-element- xans-product xans-product-additional"><div id="tabProduct" class="ec-base-tab ">
    <ul>
      <li class="selected"><a href="#prdDetail" target="_self">상세정보</a></li>
      <li><a href="#prdReview" name="use_review">리뷰 (55)</a></li>
      <li><a href="#prdInfo">구매정보</a></li>
      <li class=""><a href="#prdQnA" name="use_qna">문의</a></li>
    </ul>
  </div>
<div id="prdDetail" class="">
    <p class="code"><b>상품코드</b>P0000ECC</p>
    <div class="button" id="prdDetailBtn">
      <a href="/product/zoom.html?product_no=2758" class="btnNormal">원본보기 <span class="ico"></span></a>
    </div>

    <div class="prdDetailContAll">
      <div id="prdDetailContent">
        <div class="cont">
          <div class="detail_delivery displaynone" style="text-align:center;">
<img src="/img/detail_delivery4.jpg">
           </div>
          <div class="eventArea ">
            <h3 class="displaynone"><span>이벤트</span></h3>
            <div class="event"><div id="CommonEvent5"><p><br><img src="/web/upload/NNEditor/20240202/EC8381EC84B8_BN_EBB684EBA6ACEBB0B0EC86A1EC9588EB82B4.jpg" style="display: block; vertical-align: top; margin: 0px auto; text-align: center;" result="success" name="EC8381EC84B8_BN_EBB684EBA6ACEBB0B0EC86A1EC9588EB82B4.jpg" size="800px/296px" filesize="110,33 kB" error=""></p></div></div>
          </div>
          <img ec-data-src="/web/upload/NNEditor/20251205/EC8381EC84B8EC9DB4EBAFB8ECA780_EC9DB8EB9494EC9588EBB0A52883g29_cut_251121.jpg" style="display: block; vertical-align: top; margin: 0px auto; text-align: center;" result="success" name="EC8381EC84B8EC9DB4EBAFB8ECA780_EC9DB8EB9494EC9588EBB0A52883g29_cut_251121.jpg" size="800px/4123px" filesize="637,68 kB" error="" ><img ec-data-src="/web/upload/NNEditor/20251205/EC9881EC9691ECA095EBB3B4_EC9DB8EB9494EC9588EBB0A52883g29.jpg" style="display: block; vertical-align: top; margin: 0px auto; text-align: center;" result="success" name="EC9881EC9691ECA095EBB3B4_EC9DB8EB9494EC9588EBB0A52883g29.jpg" size="800px/571px" filesize="202,37 kB" error="" >          <div style="text-align:center;"><img src="/img/prd-detail__copyright.jpg"></div>
          <div class="detail_delivery" style="text-align:center;"><img src="/img/detail_delivery3.jpg"></div>
        </div>
      </div>
      <div class="more_view">
        <span>상세정보 더보기</span>
      </div>
    </div>
  </div>
<div id="prdInfo" class="">
    <!-- <div class="info_cont color1">
            <h3>상품정보</h3>
            <div class="ec-base-table">
                <table border="1">
                    <caption>상품 상세 정보</caption>
                    <colgroup>
                        <col style="width:105px;">
                        <col style="width:auto;">
                    </colgroup>
                    <tbody>
                        <tr>
                            <th>상품정보</th>
                            <td>라면/비유탕면</td>
                        </tr>
                        <tr>
                            <th>HACCP 인증여부</th>
                            <td>N</td>
                        </tr>
                        <tr>
                            <th>총무게</th>
                            <td>97g</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div> -->
    <div class="info_cont ">
      <h3>결제 안내</h3>
      <div class="contents">
        고액결제의 경우 안전을 위해 카드사에서 확인전화를 드릴 수도 있습니다. 확인과정에서 도난 카드의 사용이나 타인 명의의 주문등      정상적인 주문이 아니라고 판단될 경우 임의로 주문을 보류 또는 취소할 수 있습니다. &nbsp; <br>      <br>실시간 계좌이체의 경우&nbsp; 주문시 입력한 입금자명과 실제입금자의 성명이 반드시 일치하여야 하며, 7일 이내로 입금을 하셔야 하며 입금되지&nbsp;않은 주문은 자동취소 됩니다. <br>      </div>
    </div>
    <div class="info_cont ">
      <h3>배송 안내</h3>
      <div class="ec-base-table">
        <table border="1">
          <caption>상품 상세 정보</caption>
          <colgroup>
            <col style="width:105px;">
            <col style="width:auto;">
          </colgroup>
          <tbody>
            <tr>
              <th>배송 방법</th>
              <td>택배</td>
            </tr>
            <tr>
              <th>배송 지역</th>
              <td>전국지역</td>
            </tr>
            <tr>
              <th>배송 비용</th>
              <td>3,000원</td>
            </tr>
            <tr>
              <th>배송 기간</th>
              <td>2일 ~ 7일</td>
            </tr>
            <tr>
              <th>배송 안내</th>
              <td>산간벽지나 도서지방은 별도의 추가금액을 지불하셔야 하는 경우가 있습니다.<br>주문/결제 시에 계산되는 지역별 추가배송비를 꼭 확인해 주시기 바랍니다.<br>    고객님께서 주문하신 상품은 입금 확인후 배송해 드립니다. 다만, 상품종류에 따라서 상품의 배송이 다소 지연될 수 있습니다.<br></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="info_cont ">
      <h3>교환/반품 안내</h3>
      <div class="contents">
        <strong>교환 및 반품 주소</strong><br>- 충청북도 음성군 대소면 성본산단로 86<strong><br><br>교환 및 반품이 가능한 경우</strong><br>- 상품을 공급 받으신 날로부터 7일이내 단, 포장을 개봉하였거나 포장이 훼손되어 상품 가치가 상실된 경우에는 교환/반품이 불가능합니다.<br>- 공급 받으신 상품 및 용역의 내용이 표시.광고 내용과 다르거나 다르게 이행된 경우에는 공급 받은 날로부터 3월이내, 그 사실을 알게 된 날로부터&nbsp;30일이내<br><br><strong>교환 및 반품이 불가능한 경우</strong><br>- 고객님의 책임 있는 사유로 상품 등이 멸실 또는 훼손된 경우. 단, 상품의 내용을 확인하기 위하여  포장 등을 훼손한 경우는 제외<br>- 포장을 개봉하였거나 포장이 훼손되어 상품 가치가 상실된 경우<br> - 고객님의 사용 또는 일부 소비에 의하여 상품의 가치가 현저히 감소한 경우<br>- 시간의 경과에 의하여 재판매가 곤란할 정도로 상품 등의 가치가 현저히 감소한 경우<br>- 복제가 가능한 상품 등의 포장을 훼손한 경우<br>&nbsp;&nbsp;(자세한 내용은 고객만족센터 1:1 게시판 상담을 이용해 주시기 바랍니다.)<br><br>※ 고객님의 마음이 바뀌어 교환, 반품을 하실 경우 상품반송 비용은 고객님께서 부담하셔야 합니다.<br>      </div>
    </div>
    <div class="info_cont line">
      <h3>상품고시</h3>
      <div class="service_info displaynone">
              </div>
      <div class="xans-element- xans-product xans-product-detaildesign ec-base-table prd_noti"><!--
                    $cache = no
                -->
<table border="1">
          <caption>상품 상세 정보</caption>
          <colgroup>
            <col style="width:105px;">
            <col style="width:auto;">
          </colgroup>
          <tbody>
            <tr data-title="상품명" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:16px;color:#666666;">상품명</span></th>
              <td><span class="" style="font-size:16px;color:#666666;">인디안밥(83g*1)</span></td>
            </tr>
            <tr data-title="원산지" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:16px;color:#666666;">원산지</span></th>
              <td><span class="" style="font-size:16px;color:#666666;">기타 상세/구매 정보 참조</span></td>
            </tr>
<tr data-title="판매가" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:16px;color:#666666;font-weight:bold;">판매가</span></th>
              <td><span class="" style="font-size:16px;color:#666666;font-weight:bold;"><strong id="span_product_price_text">1,540원 </strong><input id="product_price" name="product_price" value="" type="hidden"  /></span></td>
            </tr>
<tr data-title="배송방법" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:16px;color:#666666;">배송방법</span></th>
              <td><span class="" style="font-size:16px;color:#666666;">택배</span></td>
            </tr>
<tr data-title="배송비(실결제금액 기준)" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:16px;color:#666666;">배송비(실결제금액 기준)</span></th>
              <td><span class="" style="font-size:16px;color:#666666;"><span class="delv_price_B"><input id="delivery_cost_prepaid" name="delivery_cost_prepaid" value="P" type="hidden"  /><strong>3,000원</strong> (30,000원 이상 구매 시 무료)</span></span></td>
            </tr>
<tr data-title="상품코드" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:16px;color:#666666;">상품코드</span></th>
              <td><span class="" style="font-size:16px;color:#666666;">P0000ECC</span></td>
            </tr>
<tr data-title="제품명" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">제품명</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">인디안밥</span></td>
            </tr>
<tr data-title="식품의 유형" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">식품의 유형</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">과자</span></td>
            </tr>
<tr data-title="생산자 및 소재지" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">생산자 및 소재지</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">㈜농심 / 서울특별시 동작구 여의대방로 112(신대방동)</span></td>
            </tr>
<tr data-title="제조연월일" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">제조연월일</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">매주 입고되는 제품으로 유통기한이 달라 매번 기재하기 어려움. 유통기한 넉넉한 제품이 발송되며 자세한 내용은 문의 부탁드립니다.</span></td>
            </tr>
<tr data-title="소비기한 또는 품질유지기한" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">소비기한 또는 품질유지기한</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">매주 입고되는 제품으로 유통기한이 달라 매번 기재하기 어려움. 유통기한 넉넉한 제품이 발송되며 자세한 내용은 문의 부탁드립니다.</span></td>
            </tr>
<tr data-title="포장단위별 용량(중량) 수량" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">포장단위별 용량(중량) 수량</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
            </tr>
<tr data-title="원재료 및 함량" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">원재료 및 함량</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
            </tr>
<tr data-title="알레르기 유발물질 함유" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">알레르기 유발물질 함유</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
            </tr>
<tr data-title="영양성분" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">영양성분</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
            </tr>
<tr data-title="유전자변형식품 유무" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">유전자변형식품 유무</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
            </tr>
<tr data-title="소비자 안전을 위한 주의사항" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">소비자 안전을 위한 주의사항</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">상세정보 참고</span></td>
            </tr>
<tr data-title="수입식품 여부" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">수입식품 여부</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">해당없음</span></td>
            </tr>
<tr data-title="소비자상담 관련 전화번호" class=" xans-record-">
              <th scope="row"><span class="" style="font-size:12px;color:#555555;">소비자상담 관련 전화번호</span></th>
              <td><span class="" style="font-size:12px;color:#555555;">1533-0658</span></td>
            </tr>
          </tbody>
        </table>
</div>
    </div>
  </div>
<div id="prdReview" class="">
    <div class="board">
      <h3>상품사용후기</h3>

      <div class="displaynone">
        <div class="ec-base-button gColumn">
          <a href="/board/free/write.html?board_no=4&product_no=2758&cate_no=0&display_group=0" class="btnStrong sizeS">상품후기쓰기</a>
          <a href="/board/free/list.html?board_no=4" class="btnNormal sizeS">모두보기</a>
        </div>

        <a name="use_review"></a>

        <div class="xans-element- xans-product xans-product-review"><!--
                        $count = 5
                    -->
<p class="noAccess displaynone">글읽기 권한이 없습니다.</p>
<div class="minor displaynone">
            <p><span>19세 미만의 미성년자</span>는 출입을 금합니다.</p>
            <a class="btnBasic" href="/intro/board.html">성인인증하기</a>
          </div>
<ul class="board ">
            <li class="xans-record-">
              <p class="descriptions">
                <a href="/product/provider/review_read.xml?no=43963&board_no=4&spread_flag=T">
                  <strong class="summary">   제품이 참좋아요.  맛이 좋아 재구매 입니다.  강추 드려요. <span class="commentCnt"></span>   </strong>
                  <span class="id" title="작성자">장****</span>
                  <span class="date " title="작성일">2026-05-07 14:34:40</span>
                  <span class="">조회 80</span>
                  <span class="">좋아요 0</span>
                  <span class="point "><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star5.png" alt="5점" width="50" height="8"></span>
                </a>
              </p>
            </li>
            <li class="xans-record-">
              <p class="descriptions">
                <a href="/product/provider/review_read.xml?no=43924&board_no=4&spread_flag=T">
                  <strong class="summary">   최고의 가성비 제품 입니다 맛도 좋고 깔끔합니다 <span class="commentCnt"></span> <img src="//img.echosting.cafe24.com/design/skin/admin/ko_KR/ico_hit.gif"  alt="HIT" class="ec-common-rwd-image" />  </strong>
                  <span class="id" title="작성자">김****</span>
                  <span class="date " title="작성일">2026-05-06 09:41:56</span>
                  <span class="">조회 140</span>
                  <span class="">좋아요 0</span>
                  <span class="point "><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star5.png" alt="5점" width="50" height="8"></span>
                </a>
              </p>
            </li>
<li class="xans-record-">
              <p class="descriptions">
                <a href="/product/provider/review_read.xml?no=43699&board_no=4&spread_flag=T">
                  <strong class="summary">   역시 과2ㅏ는 농심 어려서부터 먹어왔던 맛그대로 우유에 말아먹고 추억에 잠겨봅니다 <span class="commentCnt"></span> <img src="//img.echosting.cafe24.com/design/skin/admin/ko_KR/ico_hit.gif"  alt="HIT" class="ec-common-rwd-image" />  </strong>
                  <span class="id" title="작성자">설****</span>
                  <span class="date " title="작성일">2026-04-21 07:28:12</span>
                  <span class="">조회 366</span>
                  <span class="">좋아요 0</span>
                  <span class="point "><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star5.png" alt="5점" width="50" height="8"></span>
                </a>
              </p>
            </li>
<li class="xans-record-">
              <p class="descriptions">
                <a href="/product/provider/review_read.xml?no=43259&board_no=4&spread_flag=T">
                  <strong class="summary">   간식통에 넣어두고 먹으려고 보니 벌써 딸아이가 꿀꺽! 할 수 없이 2개를 더 주문했어요 <span class="commentCnt"></span> <img src="//img.echosting.cafe24.com/design/skin/admin/ko_KR/ico_hit.gif"  alt="HIT" class="ec-common-rwd-image" />  </strong>
                  <span class="id" title="작성자">김****</span>
                  <span class="date " title="작성일">2026-03-19 17:22:49</span>
                  <span class="">조회 620</span>
                  <span class="">좋아요 0</span>
                  <span class="point "><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star5.png" alt="5점" width="50" height="8"></span>
                </a>
              </p>
            </li>
<li class="xans-record-">
              <p class="descriptions">
                <a href="/product/provider/review_read.xml?no=42375&board_no=4&spread_flag=T">
                  <strong class="summary">   그냥 먹어도 맛있는데 우유에 말아먹으면 고소해요 <span class="commentCnt"></span> <img src="//img.echosting.cafe24.com/design/skin/admin/ko_KR/ico_hit.gif"  alt="HIT" class="ec-common-rwd-image" /> <img src="//ecimg.cafe24img.com/pg39b10496077085/nsmall2022/web/upload/icon_202206291041524300.png"  alt="파일첨부" class="ec-common-rwd-image" /> </strong>
                  <span class="id" title="작성자">박****</span>
                  <span class="date " title="작성일">2026-01-14 12:26:11</span>
                  <span class="">조회 1125</span>
                  <span class="">좋아요 0</span>
                  <span class="point "><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star5.png" alt="5점" width="50" height="8"></span>
                </a>
              </p>
            </li>
          </ul>
</div>

        <div class="xans-element- xans-product xans-product-reviewpaging ec-base-paginate typeList"><a href="#none" class="btnPrev">이전 페이지</a>
<ol>
            <li class="xans-record-"><a href="?page_4=1#use_review" class="this">1</a></li>
            <li class="xans-record-"><a href="?page_4=2#use_review" class="other">2</a></li>
            <li class="xans-record-"><a href="?page_4=3#use_review" class="other">3</a></li>
            <li class="xans-record-"><a href="?page_4=4#use_review" class="other">4</a></li>
            <li class="xans-record-"><a href="?page_4=5#use_review" class="other">5</a></li>
          </ol>
<a href="?page_4=2#use_review" class="btnNext">다음 페이지</a>
</div>
      </div>
    </div>
  </div>
<div id="prdQnA" class=" ">
    <!-- 2024-06-20 QnA 리스트 이슬 작성 -->
    <div class="lm-qna">
      <h3>문의가 필요하신가요?</h3>
      <ul>
        <li>
          <a href="/board/faq/list.html?board_no=3">
            <div>
              <p class="lm-title">자주 묻는 질문을 확인하세요.</p>
              <p>
                주문, 배송, 환불, 커스텀(농꾸) 등<br>
                고객님들이 자주 묻는 질문을 모아놨어요.
              </p>
            </div>
            <div class="lm-img-container"><img src="/img/icon-detail-faq.png" alt="자주 묻는 질문"></div>
          </a>
        </li>
        <li>
          <a href="javascript:void(0);">
            <div>
              <p class="lm-title">상담톡으로 빠르게 해결하세요.</p>
              <p>
                빠른 1:1 문의 (주문, 배송, 환불, 상품 등)는<br>
                <span>우측 하단 상담톡</span> 버튼을 눌러주세요.
              </p>
            </div>
            <div class="lm-img-container"><img src="/img/icon-detail-consult.png" alt="자주 묻는 질문"></div>
          </a>
        </li>
        <li>
          <a href="javascript:void(0);">
            <div>
              <p class="lm-title">전화문의 1533-0658</p>
              <p>
                월 ~ 금요일 I 오전 9시 ~ 오후 5시<br>
                (점심시간 오후 12시 ~ 1시, 주말/공휴일 휴무)
              </p>
            </div>
            <div class="lm-img-container"><img src="/img/icon-detail-customer.png" alt="자주 묻는 질문"></div>
          </a>
        </li>
      </ul>
    </div>
    <!-- //2024-06-20 QnA 리스트 이슬 작성 -->

    <div class="board displaynone">
      <h3>상품 Q&amp;A</h3>

      <div class="ec-base-button gColumn">
        <a href="/board/product/write.html?board_no=6&product_no=2758&cate_no=0&display_group=0" class="btnStrong sizeS">상품문의하기</a>
        <a href="/board/product/list.html?board_no=6" class="btnNormal sizeS">모두보기</a>
      </div>

      <a name="use_review"></a>

      <div class="xans-element- xans-product xans-product-qna"><!--
                    $count = 5
                -->
<p class="noAccess displaynone">글읽기 권한이 없습니다.</p>
<div class="minor displaynone">
          <p><span>19세 미만의 미성년자</span>는 출입을 금합니다.</p>
          <a class="btnBasic" href="/intro/board.html">성인인증하기</a>
        </div>
<ul class="board ">
          <li class="xans-record-">
            <p class="descriptions">
              <a href="/board/product/read.html?no=3499&board_no=6&spread_flag=T">
                <strong class="summary">   배송 누락되었어요 <span class="commentCnt"></span>   </strong>
                <span class="id" title="작성자">최****</span>
                <span class="date " title="작성일">2023-01-09 13:49</span>
                <span class="">조회 21</span>
                <span class="">좋아요 0</span>
                <span class="point displaynone"><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star0.png" alt="0점" width="50" height="8"></span>
              </a>
            </p>
          </li>
          <li class="xans-record-">
            <p class="descriptions">
              <a href="/board/product/read.html?no=3520&board_no=6&spread_flag=T">
                <strong class="summary">&nbsp;&nbsp;&nbsp;<img src="//ecimg.cafe24img.com/pg39b10496077085/nsmall2022/web/upload/icon_202206291041587200.png"  alt="답변" class="ec-common-rwd-image" />    배송 누락되었어요 <span class="commentCnt"></span>   </strong>
                <span class="id" title="작성자"></span>
                <span class="date " title="작성일">2023-01-09 14:41</span>
                <span class="">조회 15</span>
                <span class="">좋아요 0</span>
                <span class="point displaynone"><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star0.png" alt="0점" width="50" height="8"></span>
              </a>
            </p>
          </li>
        </ul>
</div>
      <div class="xans-element- xans-product xans-product-qnapaging ec-base-paginate typeList"><a href="#none" class="btnPrev">이전 페이지</a>
<ol>
          <li class="xans-record-"><a href="?page_6=1#use_qna" class="this">1</a></li>
                  </ol>
<a href="#none" class="btnNext">다음 페이지</a>
</div>
    </div>
  </div>
<div class="supplyInfo displaynone ">
    <h3 class="xans-element- xans-product xans-product-headcategory ">판매자 정보
</h3>
    <div class="displaynone">
          </div>
  </div>
</div>


<div class="gtm-area displaynone">
  <div class="xans-element- xans-product xans-product-headcategory "><span class="cate01" data-cate="/category/기획전/822/">기획전</span>
<span class="cate02" data-cate="/category/🍬스낵-젤리/822/">🍬스낵 & 젤리</span>
<span class="cate03" data-cate=""></span>
<span class="cate04" data-cate=""></span>
</div>
  <div class="xans-element- xans-product xans-product-detail "><script>
      //gtm
      dataLayer.push({
        'event': 'view_item',
        'ecommerce': {
          'items': [
            {
              'item_id': 'P0000ECC',
              'item_name': '인디안밥(83g*1)',
              'price': '1540',
              'item_category': $('.gtm-area .cate02').text(),
              'item_category2': $('.gtm-area .cate03').text(),
              'item_brand': '',
              'currency': 'KRW'
            }
          ]
        }
      });

      function gtm_basket() {
        dataLayer.push({
          'event': 'add_to_cart',
          'ecommerce': {
            'items': [
              {
                'item_id': 'P0000ECC',
                'item_name': '인디안밥(83g*1)',
                'price': '1540',
                'item_category': $('.gtm-area .cate02').text(),
                'item_category2': $('.gtm-area .cate03').text(),
                'item_brand': '',
                'quantity': $('#quantity').val(),
                'currency': 'KRW'
              }
            ]
          }
        });
      }

      function gtm_wishlist() {
        dataLayer.push({
          'event': 'add_to_wishlist',
          'ecommerce': {
            'items': [
              {
                'item_id': 'P0000ECC',
                'item_name': '인디안밥(83g*1)',
                'price': '1540',
                'item_category': $('.gtm-area .cate02').text(),
                'item_category2': $('.gtm-area .cate03').text(),
                'item_brand': '',
                'quantity': $('#quantity').val(),
                'currency': 'KRW'
              }
            ]
          }
        });
      }


        // 페이지가 완전히 열린 후 실행 (jQuery 사용)
        $(document).ready(function() {
          
          var $saleElem = $('#span_product_price_sale');
          var $originElem = $('#span_product_price_text');

          // [수정된 함수] "원" 글자 앞에서 자르는 로직 추가!
          var getPrice = function($el) {
              if ($el.length === 0) return 0;
              
              // 1. 전체 텍스트 가져오기 (예: "1,320원20%")
              var rawText = $el.text();
              
              // 2. 할인률 텍스트가 포함되지 않도록 "원"을 기준으로 앞부분만 자르기 (예: "1,320")
              var pricePart = rawText.split('원')[0];

              // 3. 숫자만 남기기
              var num = parseInt(pricePart.replace(/[^0-9]/g, ''));
              return isNaN(num) ? 0 : num;
          };

          // 가격 확정
          var originPrice = getPrice($originElem);
          var salePrice = getPrice($saleElem);
          
          var finalSalePrice = (salePrice > 0) ? salePrice : originPrice;

          // 개발자모드 소스 창 말고 콘솔 창에서 정보 확인
          console.log("실제판매가:", finalSalePrice);
          console.log("원본(origin):", originPrice);
          console.log("할인(sale):", finalSalePrice);

          // Groobee 전송
          groobee('VG', {
              goods: [{
                  name: '인디안밥(83g*1)',              
                  code: '2758',        
                  
                  amt: finalSalePrice,
                  prc: originPrice,          
                  salePrc: finalSalePrice,   
                  
                  img: $('#prdDetailImg img').attr('src'),            
                  status: 'displaynone' == 'displaynone' ? '' : 'SS', 
                  cat: "", 
                  cateNm: $('.gtm-area .cate02').text(), 
                  catL: "", 
                  cateLNm: $('.gtm-area .cate03').text(), 
                  catM: "", 
                  cateMNm: "", 
                  catS: "", 
                  cateSNm: "", 
                  catD: "", 
                  cateDNm: "", 
                  brand: "", 
                  brandNm: "" 
              }]
          });
        });


      // groobee('VG', {
      //   goods: [{
      //     name: '인디안밥(83g*1)',									// 상품명
      //     code: '2758',							// URL에 표시되는 상품코드

      //     // 251120 기존 코드
      //     // amt: '1540.00' ? string_to_num(1540.00) : $('#product_price_mobile').val() ? string_to_num($('#product_price_mobile').val()) : 1540,							// 상품 금액 (할인 판매가 * 수량)
      //     // prc: 1540,								// 판매가 (또는 원가)
      //     // salePrc: '1540.00' ? string_to_num(1540.00) : $('#product_price_mobile').val() ? string_to_num($('#product_price_mobile').val()) : 1540,						// 할인 판매가 (실제 판매가)
           
      //     // 리더마인 251120 shlee $product_sale_price와 $product_price에 따옴표 추가
      //     amt: '1540.00' ? string_to_num('1540.00') : $('#product_price_mobile').val() ? string_to_num($('#product_price_mobile').val()) : '1540',							// 상품 금액 (할인 판매가 * 수량)
          
      //     // 리더마인 251120 shlee $product_price에 따옴표 추가 (핵심 에러 유발 지점)
      //     prc: '1540',								// 판매가 (또는 원가)
          
      //     // 리더마인 251120 shlee $product_sale_price와 $product_price에 따옴표 추가
      //     salePrc: '1540.00' ? string_to_num('1540.00') : $('#product_price_mobile').val() ? string_to_num($('#product_price_mobile').val()) : '1540',						// 할인 판매가 (실제 판매가)
            
      //     img: $('#prdDetailImg img').attr('src'),											// 상품 이미지 전체 URL
      //     status: 'displaynone' == 'displaynone' ? '' : 'SS',											// 품절이거나 상품이 판매상태가 아닐 경우 "SS"
      //     cat: "",											// 상품의 카테고리 코드
      //     cateNm: $('.gtm-area .cate02').text(),				// 상품의 카테고리명
      //     catL: "",											// 상품의 대분류 카테고리 코드
      //     cateLNm: $('.gtm-area .cate03').text(),				// 상품의 대분류 카테고리명
      //     catM: "",											// 상품의 중분류 카테고리 코드
      //     cateMNm: "",										// 상품의 중분류 카테고리명
      //     catS: "",											// 상품의 소분류 카테고리 코드
      //     cateSNm: "",										// 상품의 소분류 카테고리명
      //     catD: "",											// 상품의 세분류 카테고리 코드
      //     cateDNm: "",										// 상품의 세분류 카테고리명
      //     brand: "",											// 상품의 브랜드 코드
      //     brandNm: ""											// 상품의 브랜드명
      //   }]
      // });

 //     $('.xans-product-action .basket').click(function () {
 //		 kakaoPixel('6400742100396522420').addToCart({
 //         	currency: "KRW",
 //        	products:  { id: 'P0000ECC',
 //			name: '인디안밥(83g*1)',
 //			quantity: $('#quantity').val(),
 //	        price: '1540',
 //		    brand: '' }
 //         });
 //      });  ! 25.12.24 픽셀 비활성화 
    </script>
</div>
</div>
<script>
  pdDetail();
  detailScroll();
  shareKakao(location.href, $('title').text(), '', '.sns-share__box--kakao');

  document.addEventListener("DOMContentLoaded", function () {
    // 2024-06-17 판매가, 할인판매가, 할인율 계산
    let originalPriceBox = document.querySelector('div[data-title="판매가"]');
    let salePriceBox = document.querySelector('div[data-title="할인판매가"]');
    if (!salePriceBox) {
      originalPriceBox.classList.add("lm-price");
    } else {
      // 판매가, 할인판매가 데이터 찾기
      let originalPrice = originalPriceBox.querySelector("#span_product_price_text").innerHTML.split("원")[0].replace(",", "");
      let salePrice = salePriceBox.querySelector("#span_product_price_sale").innerHTML.split("원")[0].replace(",", "");
      let newDiscount = document.createElement("span");

      // LEADERMINE 2024-07-23 상품상세 페이지 내 할인률 이중표시 현상
      let cafe24DiscountPercentage = salePriceBox.querySelector("#span_product_price_sale").querySelector("span");
      cafe24DiscountPercentage.classList.add("displaynone");
      // !LEADERMINE 2024-07-23 상품상세 페이지 내 할인률 이중표시 현상

      // 할인율 계산
      const discountPercentage = ((originalPrice - salePrice) / originalPrice) * 100;

      // 소수점 이하의 0 제거
      const resDiscount = discountPercentage.toFixed(0).replace(/\.0$/, '');

      newDiscount.innerHTML = `${resDiscount}%`;
      newDiscount.classList.add("lm-discountPercent");
      originalPriceBox.classList.add("lm-originPrice");
      salePriceBox.prepend(newDiscount);
      salePriceBox.classList.add("lm-price");
    }
    //// 2024-06-17 판매가, 할인판매가, 할인율 계산

    let lmPricePopBt = document.querySelector('.lm-single-pop-bt');

    lmPricePopBt.addEventListener('click', () => {
      let qtyCount = document.querySelector('#quantity').value;
      // 2024-06-17 옵션 팝업 버튼 클릭 시 구매 개수 업데이트 커스텀 이슬 작성
      let addCountEl = document.querySelector('.lm-single-qty-clone');
      addCountEl.innerHTML = qtyCount;
      quantityPriceChange();
      //// 2024-06-17 옵션 팝업 버튼 클릭 시 구매 개수 업데이트 커스텀 이슬 작성
    });

    // 2024-06-17 옵션 팝업 내 개수 조절 버튼 클릭 시 구매 개수 업데이트 커스텀 이슬 작성
    let qtyBt = document.querySelectorAll('.lm-single-qty-count-bt');

    qtyBt.forEach(el => {
      el.addEventListener('click', () => {
        setTimeout(() => {
          let qtyCount = document.querySelector('#quantity').value;
          let addCountEl = document.querySelector('.lm-single-qty-clone');
          addCountEl.innerHTML = qtyCount;
          // 2024-06-24 clone 개수 인풋 value 업데이트 이슬 작성
          cloneQtyInputChange();
        }, 10);
        // 2024-06-17 옵션 팝업 내 버튼 클릭 시 가격 표기 업데이트 이슬 작성
        quantityPriceChange();
      });
    });
    // 2024-06-17 옵션 팝업 내 개수 조절 버튼 클릭 시 구매 개수 업데이트 커스텀 이슬 작성

    // 2024-06-24 상품상세 하단 클론 제품명
    const prdName = document.querySelector('.name_wrap .name').innerText;
    const cloneName = document.querySelector('.lm-name-clone');
    cloneName.innerText = prdName;
    //// 2024-06-24 상품상세 하단 클론 제품명

    // 2024-06-24 상품상세 하단 클론 수량 버튼-팝업 수량 버튼 연결
    let qtyBtdown = document.querySelector('.lm-single-qty-count-bt.down');
    let qtyBtCloneDown = document.querySelector('.lm-qty-bt-clone.down');
    let qtyBtUp = document.querySelector('.lm-single-qty-count-bt.up');
    let qtyBtCloneUp = document.querySelector('.lm-qty-bt-clone.up');

    qtyBtCloneDown.addEventListener('click', () => {
      qtyBtdown.click();
      cloneQtyInputChange();
    });
    qtyBtCloneUp.addEventListener('click', () => {
      qtyBtUp.click();
      cloneQtyInputChange();
    });
    //// 2024-06-24 상품상세 하단 클론 수량 버튼-팝업 수량 버튼 연결

    // 2024-06-24 구매 개수 선택 영역 할인가 표시 이슬 작성
    let qtyInput = document.querySelector('#quantity');
    qtyInput.addEventListener("change", (event) => {
      quantityPriceChange();
    });

    setTimeout(() => {
      quantityPriceChange();
    }, 10);
    function quantityPriceChange() {
      let quantityPrice = document.querySelectorAll('.lm-qauntity-saleprice');
      let salePriceWrap = document.querySelector('[data-title="할인판매가"]');
      let productPrice = document.querySelectorAll('.quantity_price');

      if (salePriceWrap) {
        let salePriceStr = document.querySelector('#span_product_price_sale').innerText.replaceAll(",", "");
        let salePriceNumber = parseFloat(salePriceStr);
        quantityPrice.forEach(el => {
          setTimeout(() => {
            let qtyCount = document.querySelector('#quantity').value;
            let priceStr = (salePriceNumber * qtyCount).toString();
            priceStr = priceStr.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            el.innerHTML = `${priceStr}원`;
          }, 1);
        });
        productPrice.forEach(el => {
          el.style.display = "none";
        });
      } else {
        let originalPriceStr = document.querySelector('#span_product_price_text').innerText.replaceAll(",", "");
        let originalPriceNumber = parseFloat(originalPriceStr);
        productPrice.forEach(el => {
          setTimeout(() => {
            let qtyCount = document.querySelector('#quantity').value;
            let priceStr = (originalPriceNumber * qtyCount).toString();
            priceStr = priceStr.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            el.innerHTML = `${priceStr}원`;
          }, 1);
        });
      }
    }
    //// 2024-06-17 구매 개수 선택 영역 할인가 표시 이슬 작성
  });

  // 2024-06-20 농꾸 버튼 찾아서 위치 수정 이슬 작성
  function cloneQtyInputChange() {
    let qtyOriginalCount = document.querySelector('#quantity').value;
    let qtyInputClone = document.querySelector('.lm-qty-input-clone');
    qtyInputClone.value = qtyOriginalCount;
  }

  // 2024-06-20 농꾸 버튼 찾아서 위치 수정 이슬 작성
  let findBt = function (mutationsList, observer) {
    for (let mutation of mutationsList) {
      if (mutation.type === 'childList') {
        mutation.addedNodes.forEach(node => {
          if (node.nodeType === Node.ELEMENT_NODE && node.getAttribute('onclick')) {
            if (node.getAttribute('onclick').includes("customEditLink.modules.wpEditCall")) {
              const orderFixWrap = document.querySelector('.order_fix_wrap');
              const duplication = orderFixWrap.querySelector('.xans-product-option');
              orderFixWrap.style.position = "static";
              duplication.style.display = "none";
            }
          }
        });
      }
    }
  };
  let observer = new MutationObserver(findBt);
  let targetNode = document.body;
  observer.observe(targetNode, { childList: true, subtree: true });
  //// 2024-06-20 농꾸 버튼 찾아서 위치 수정 이슬 작성
</script>
<script src="https://plusapp-manager.cafe24.com/js/front/recommend-install.js" defer></script>
				</section>
				<!-- <iframe id="dev-area--basket" class="displaynone" src="/dev/basket.html" scrolling="no"></iframe> -->
<!-- <div class="dev-area--basket displaynone">
	<div module="Order_NormNormal"></div>
</div>
<script>
	$(document).ready(function(){
		if(typeof aBasketProductData != 'undefined' && typeof aBasketProductOrderData == 'undefined'){//장바구니 1개 이상 있을 시
			Basket.LMdeleteBasketItem = function(iIdx){
				// 장바구니 분리형세트 상품 판단을 위한 세트번호
				var iSetPrdNo = parseInt(aBasketProductData[iIdx].set_product_no);

				// 분리형세트의 선택주문시 관련세트 구성 전부 체크후 선택주문하기처리
				if (iSetPrdNo > 0) {
					this.setAddSingleSetItemCheckedAction(iSetPrdNo, 'deleteBasket');
					return false;

				}

				//if (confirm(__('선택하신 상품을 삭제하시겠습니까?')) == false) return;

				if (typeof ACEWrap !== 'undefined') {
					ACEWrap.delCheckedBasket();
				}
				var aData = [];
				var iProdNo = aBasketProductData[iIdx].product_no;
				var sOptId = aBasketProductData[iIdx].opt_id;
				var sProductType = aBasketProductData[iIdx].product_type;
				var sIsSetProduct = aBasketProductData[iIdx].is_set_product;
				var iBasketPrdNo = aBasketProductData[iIdx].basket_prd_no;
				var iCustomDataIdx = aBasketProductData[iIdx].custom_data_idx;
				var sDelvType = aBasketProductData[iIdx].delvtype;

				var sKey = iProdNo + ':' + sOptId + ':' + sIsSetProduct + ':' + iBasketPrdNo + ':' + iCustomDataIdx + ':' + sDelvType;

				aData.push(sKey);
				//this._callBasketAjax();
				EC$.post('/exec/front/order/basket/', {
					command: 'select_delete',
					checked_product: aData.join(','),
					delvtype: sBasketDelvType
				}, function(data) {
					location.pathname.indexOf('/order/basket.html') != -1 ? location.reload() : '';
				}, 'json');
			};

			$.each(aBasketProductData, function(ii, ie){//장바구니 상품
				$.each(ie.categories, function(ji, je){//해당되는 카테고리
					if(je == 90){//커스텀 cate_no
						Basket.LMdeleteBasketItem(ii);//상품 삭제
					};
				});
			});
		};
	});
</script> -->
				<footer id="footer" class="xans-element- xans-layout xans-layout-footerpackage "><!--css(/css/module/layout/footerPackage.css)-->
<div class="footer__bbs">
		<strong>공지사항</strong>
		<div rel="js-footer__bbs" class="xans-element- xans-board xans-board-list-1 xans-board-list xans-board-1 slideshow"><!--
				$main_list = yes
			-->
<div class="swiper-container">
				<ul class="swiper-wrapper">
					<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/38595/">미션배지 '너구리 한마리 몰고가세요~' 신규 발급 중단 안내</a></li>
					<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/17905/">개인정보처리방침 변경 (2025.4.8 시행)</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/17878/">농심몰 서비스 점검 안내</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/17777/">농심몰 서비스 점검 안내</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/17676/">개인정보처리방침 변경 (2024.12.18 시행)</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/17650/">개인정보처리방침 변경 (2024.12.04 시행)</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/17576/">개인정보처리방침 변경 (2024.10.23 시행)</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/13916/">개인정보처리방침 변경 (2024.08.02 시행)</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/10978/">농심몰 휴면회원 정책 변경 안내</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/5731/">개인정보처리방침 변경 (2023.2.6 시행)</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/2840/">농심몰 신규 회원 가입 혜택 변경 안내</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/666/">[변경전] 농심몰 신규 회원 가입혜택</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/452/">개인정보처리방침 변경</a></li>
<li class="swiper-slide xans-record-"><a href="/article/공지사항/1/262/">농꾸 제품의 파손 보상 정책</a></li>
				</ul>
			</div>
</div>
		<script>
			var footer__bbs = new Swiper('[rel="js-footer__bbs"] .swiper-container', {
				loop: true,
				direction: 'vertical',
				autoplay: {
					delay: 5000,
					disableOnInteraction: false,
				},
			});
		</script>
	</div>
<div class="xans-element- xans-layout xans-layout-footer"><select onchange="!$(this).val() ? '' : window.open($(this).val())">
			<option value="">FAMILY SITE</option>
			<option value="http://www.nongshim.com/main/index">농심</option>
			<option value="http://nongshimholdings.com/">농심홀딩스</option>
			<option value="http://www.nongshimeng.com/">농심엔지니어링</option>
			<option value="http://www.ildonglakes.co.kr/">농심개발</option>
			<option value="http://www.youlchon.com/">율촌화학</option>
			<option value="http://nds.nongshim.co.kr/">NDS</option>
			<option value="http://www.nongshimfm.com/">농심미분</option>
			<option value="https://home.megamart.com">메가마트</option>
			<option value=" https://www.nongshim.com/management/people/youlchon">율촌재단</option>
			<option value="https://www.nongshimtk.com/main.do">농심태경</option>
			<option value="http://www.hotelnongshim.com/">호텔농심</option>
			<option value="http://www.nongshimusa.com/">농심미국</option>
			<option value="https://www.nongshimchina.com.cn">농심중국</option>
			<option value="http://www.nongshim.co.jp/">농심일본</option>
			<option value="http://www.cocoichibanya.co.kr/main.jsp">코코이찌방야</option>
			<option value="http://library.nongshim.com/">식문화전문도서관</option>
		</select>
<div class="footer__link">
			<a href="http://www.nongshim.com/introduce/overview/index">회사소개</a>
			<a href="/member/mall_agreement.html">이용약관</a>
			<a href="/member/privacy.html"><strong>개인정보처리방침</strong></a>
			<a href="/board/index.html">고객만족센터</a><br>
			<a href="/board/faq/list.html?board_no=3">FAQ</a>
			<a href="https://sso.nongshim.com/nongshim/customer/counseling/receipt" target="_blank">농심 기업,브랜드 협찬/제안</a>
			<!-- <a href="/board/free/write.html?board_no=5">Q&A</a> -->
			<a href="/member/family.html"><strong>임직원인증</strong></a>
		</div>
<div class="xans-element- xans-layout xans-layout-info "><h4>CS CENTER</h4>
<a href="tel:1533-0658" class="footer__cs"><strong>1533-0658</strong></a>
<p>월~금 : 09:00~17:00</p>
<p>점 심 : 12:00 ~13:00</p>
<p>주말 및 공휴일은 휴무입니다.</p>
<p>농심몰 문의 : <a href="mailto:nsmall2022@naver.com">nsmall2022@naver.com</a></p>
</div>
<div class="footer__info ec-base-fold eToggle">
			<div class="title">
				<strong>사업자정보 확인하기</strong>
			</div>
			<div class="contents">
				<dl>
					<dt>법인명(상호)</dt>
					<dd>(주)농심</dd>
				</dl>
				<dl>
					<dt>대표자(성명)</dt>
					<dd><a href="mailto:nsmall2022@naver.com">조용철</a></dd>
				</dl>
				<dl class="">
					<dt>전화</dt>
					<dd><a href="tel:1533-0658">1533-0658</a></dd>
				</dl>
				<dl>
					<dt>주소</dt>
					<dd>서울특별시 동작구 여의대방로 112 (신대방동)<br>농심신대방사옥</dd>
				</dl>
				<dl>
					<dt>사업자등록번호</dt>
					<dd>118-81-03914</dd>
				</dl>
				<dl>
					<dt>통신판매업신고</dt>
					<dd>제 2022-서울동작-0618 호</dd>
				</dl>
				<dl class=" ">
					<dt>개인정보관리책임</dt>
					<dd><a href="mailto:bellfive@nongshim.com">안영진</a></dd>
				</dl>
				<dl>
					<dt>호스팅제공</dt>
					<dd>카페24(주)</dd>
				</dl>
			</div>
		</div>
<div class="escrow">
			<a href="https://iniweb.inicis.com/popup/common/popup_escrow_notice.jsp?mid=ECAnsma4d1" target="_blank"><img src="/img/icon__footer__escrow.png"></a>
			<span>(주)케이지이니시스의 안전 구매 (에스크로) 서비스를 이용하실 수 있습니다.</span>
		</div>
<div class="app">
			<p><b>App</b></p>
			<ul>
				<li class="google"><a href="https://play.google.com/store/apps/details?id=com.cafe24.ec.plusnsmall2022" target="_blank"><img src="/img/icon__footer__app--google.png"></a></li>
				<li class="apple"><a href="https://apps.apple.com/kr/app/%EB%86%8D%EC%8B%AC%EB%AA%B0/id6443553325" target="_blank"><img src="/img/icon__footer__app--apple.png"></a></li>
			</ul>
		</div>
<p class="copyright">Copyright© 농심몰. All Rights Reserved.</p>
</div>
</footer>
<div id="progressPaybar" style="display:none;">
	<div id="progressPaybarBackground" class="layerProgress"></div>
	<div id="progressPaybarView">
		<p class="graph">현재 결제가 진행중입니다.</p>
		<p class="txt">
			본 결제 창은 결제완료 후 자동으로 닫히며, <br>
			결제 진행 중에 본 결제 창을 닫으시면<br>
			주문이 되지 않으니 <br>
			결제 완료 될 때 까지 닫지 마시기 바랍니다.
		</p>
	</div>
</div>

<div class="quick_menu scroll">
	<div class="quick_icon share_btn"><p>공유하기</p></div>
	<div class="quick_icon top_btn"><p>TOP</p></div>
</div>

<style>
	/* 퀵메뉴 변경 */
	/* .quick_menu .quick_icon.share_btn{display:none; background:#fff url('/imgFile/icon/icon_share2.png')no-repeat center center; background-size:16px; box-shadow:3px 3px 20px 10px rgba(0,0,0,0.1); margin-bottom:62px; position:relative;} */
	.quick_menu .quick_icon.share_btn{display:none; background:#fff url('/imgFile/icon/icon_share2.png')no-repeat center center; background-size:16px; box-shadow:3px 3px 20px 10px rgba(0,0,0,0.1); margin-bottom:15px; position:relative;}
	.quick_menu .quick_icon.share_btn p{position:absolute; top:50%; left:-65px; background:var(--main-color1); border-radius:5px; padding:0 7px; line-height:22px; transform:translateY(-50%); font-size:12px;}
	.quick_menu .quick_icon.share_btn p:after{content:''; display:block; width:0; height:0; border:3px solid transparent; border-right:0; border-left:4px solid var(--main-color1); position:absolute; top:50%; right:-4px; transform:translateY(-50%);}
	.pageNum90 .quick_menu .quick_icon.share_btn{display:block;}
	.pageNum90 .quick_menu .quick_icon.recent_btn{display:none;}
</style>

<script>
	//상단이동
	$('.quick_menu .top_btn').click(function(){
		$('html,body').animate({
			scrollTop: $('html,body').offset().top
		});
	});

	$(document).on('click', '.quick_menu .share_btn', function(){
		snsShareGlobal();
	});
</script>


<!-- Pixel Code -->
<script type="text/javascript">
//	kakaoPixel('6400742100396522420').pageView(); 25.12.24 픽셀 비활성화
	$(document).ready(function () {
		$('.xans-product .basket .cart').click(function () {
			console.log($(this).closest('.xans-record-').find('[data-item-title="상품코드"]').data('value'));
		//	kakaoPixel('6400742100396522420').addToCart({
		//		id: $(this).closest('.xans-record-').find('[data-item-title="상품코드"]').data('value')
		//	});
		});
	});

	// 상품 정렬 기준
	document.addEventListener('DOMContentLoaded', function () {
		const form = document.querySelector('form.searchField');
		if (!form) return;

		const inputKeyword = form.querySelector('input.keyword[name="keyword"]');
		const btnSearch = form.querySelector('.btnSubmit');

		// order_by 히든필드
		function ensureOrderByField() {
			let orderInput = form.querySelector('input[name="order_by"]');
			if (!orderInput) {
				orderInput = document.createElement('input');
				orderInput.type = 'hidden';
				orderInput.name = 'order_by';
				form.appendChild(orderInput);
			}
			orderInput.value = 'favor';
		}

		// 검색 버튼 클릭
		if (btnSearch) {
			btnSearch.addEventListener('click', function (e) {
				e.preventDefault();
				ensureOrderByField();
				form.submit();
			});
		}

		// 엔터키 적용
		if (inputKeyword) {
			inputKeyword.addEventListener('keydown', function (e) {
				if (e.key === 'Enter') {
					ensureOrderByField();
				}
			});
		}

		// 인기 키워드
		const popularKeywordLinks = document.querySelectorAll('.searchField .keywordArea ul.list li a');
		popularKeywordLinks.forEach(link => {
			link.addEventListener('click', function (e) {
				e.preventDefault();

				const url = new URL(this.href, window.location.origin);
				const keyword = url.searchParams.get('keyword') || '';
				if (!inputKeyword) return;

				inputKeyword.value = keyword;

				ensureOrderByField();

				customSearchSubmit('searchField', keyword);
			});
		});
	});
</script>
<!-- //Pixel Code -->
<script>
	let sUserAgent = navigator.userAgent.toLowerCase();
	let oPlusAppTest = new RegExp('Cafe24Plus', 'i');
	if (oPlusAppTest.test(sUserAgent) === true) {
		document.querySelector("#footer .app").style.visibility = "hidden";
	}
</script>

<script>
	getURLParam('test') == 'true' ? $('body').addClass('testpage') : '';
</script>

			</div>
			<header id="header">
	<!-- LEADERMINE 2025-07-01 MO 바텀 내비게이션바 UI 개선 -->
	<div class="header__bottom header-default" data-animation="true">
		<div class="header__bottom__box" data-animation-all="true"></div>
		<div class="header__bottom__list">
			<ul class="float_wrap">
				<li class="h_cate_btn"><a href="/layout/basic/gnb.html" class="fold" data-category="navigation" data-action="footer" data-label="category">카테고리</a></li>
				<li class=""><a href="/lounge/coupon.html" data-category="navigation" data-action="footer" data-label="coupon">혜택</a></li>
				<li class=""><a href="/" data-category="navigation" data-action="footer" data-label="logo">홈</a></li>
				<li class="nongshim_tooltip"><a href="/nongshimTV" data-category="navigation" data-action="footer" data-label="recent">ㅋㅋㅋTV</a>
					<div class="lm-tooltip" id="lm-tooltip"></div>
				</li>
				<li class="" class=""><a href="/member/login.html?noMemberOrder&amp;returnUrl=/myshop/index.html" data-category="navigation" data-action="footer" data-label="mypage">마이</a>
</li>
								<!--<li class="right_box x"><a href="/myshop/order/list.html">배송조회</a></li>-->
			</ul>
		</div>
	</div>
	<!-- !LEADERMINE 2025-07-01 MO 바텀 내비게이션바 UI 개선 -->
</header>
<style>
	.header__bottom {
		z-index: 999;
	}

	.right_box.nongshim_tooltip {
		position: relative;
	}

	.lm-tooltip {
		position: absolute;
		top: -25px;
		left: 70%;
		transform: translateX(-50%);
		background-color: #DCF600;
		/* 툴팁 배경 색 (노란색) */
		color: #000;
		/* 텍스트 색 */
		font-size: 12px;
		/* 글씨 크기 */
		font-weight: 500;
		padding: 5px 10px;
		/* 내부 여백 */
		border-radius: 20px;
		/* 둥근 모서리 */
		box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
		/* 그림자 */
		white-space: nowrap;
		/* 줄바꿈 방지 */
		z-index: 1000;
		display: none;
	}

	.lm-tooltip::after {
		content: '';
		position: absolute;
		bottom: -7px;
		/* 말풍선 삼각형의 위치 */
		left: 75px;
		/* 삼각형의 위치 */
		width: 0;
		height: 0;
		border-top: 7px solid #DCF600;
		/* 삼각형의 크기 (높이) */
		border-right: 10px solid transparent;
		/* 삼각형의 크기 (너비) */
	}

	.lm-tooltip.show {
		display: block;
	}
</style>

<script>
	//LEADERMINE - 24.07.08 로그인 페이지 개선
	//member/login.html 에서 .header__bottom display:none
	document.addEventListener('DOMContentLoaded', function () {
		let headerBottom = document.querySelector('.footerGnb .header__bottom');
		if (window.location.pathname === '/member/login.html') {
			if (headerBottom) {
				headerBottom.style.display = 'none';
			} else {
				console.log('오류 발생');
			}
		}
	});
	//!LEADERMINE - 24.07.08 로그인 페이지 개선
</script>
		</div>
		<script>
			//gtm
			if(!!EC_FRONT_EXTERNAL_SCRIPT_VARIABLE_DATA.common_member_id_crypt){
				if(localStorage.getItem('nsmallLogin') !== 'T'){
					dataLayer.push({
						'event': 'login_complete',
						'user_id' : EC_FRONT_EXTERNAL_SCRIPT_VARIABLE_DATA.common_member_id_crypt,
						'login_type': 'email'
					});
					localStorage.setItem('nsmallLogin', 'T');
				}
			}
		</script>
		<script charSet="utf-8" src="//static.groobee.io/dist/g2/groobee.init.min.js"></script>
	</div>
	<script>
		// LEADERMINE 2024-06-25 MO 헤더 및 GNB UI/UX 개선
		// 메인GNB 하위 셀랙탭 페이지에 type-main / 선택된 페이지 gnb.point 클래스를 추가삭제
		// 농꾸, 신상템, 정기구독
		let headerViewCheck = ['90', '95', '96', '409', '382', '385', '386', '387', '407', '409']; 
		let searchParams = new URLSearchParams(window.location.search);
		let lmCateParams = searchParams.get('cate_no');

		let lmCateNav = document.querySelectorAll(`[data-cate-id]`);
		if (lmCateNav.length > 0) {
			lmCateNav.forEach((el, i) => {
				let lmNavId = el.dataset.cateId;
				el.classList.remove(`point`);
				if (lmNavId === lmCateParams) {
					el.classList.add(`point`);
				}
			});
		}
		
		if (headerViewCheck.includes(lmCateParams)) {
			let subPage = document.getElementById('subpage');
			let listNav = document.querySelector('.list_nav');

			if (subPage) {
				subPage.classList.add('type-main');
			}
			if (lmCateParams === '96' && listNav) {
				listNav.classList.add('point');
			}
		}

		// 스페셜, 이벤트
		let currentPage = window.location.pathname;
		let headerViewCheck2 = ['/product/special.html','/board/gallery/list.html', '/product/hotdeal.html'];
		let lmPathNav = document.querySelectorAll('[data-path]');

		if (headerViewCheck2.includes(currentPage)) {
			let subPage2 = document.getElementById('subpage');
			if (subPage2) {
				subPage2.classList.add('type-main');
			}
		}

		if (lmPathNav.length > 0) {
			lmPathNav.forEach((el) => {
				let lmNavId2 = el.dataset.path;
				el.classList.remove('point');
				if (lmNavId2 === currentPage) {
					el.classList.add('point');
				}
			});
		}
		// 신상템
		let nav = document.querySelector('#gnb-simple ul li');
		let headerViewCheck3 = ['/product/recommend.html'];
		let recommendNav = document.querySelector('.recommend_nav');

		if (headerViewCheck3.includes(currentPage)) {
			if (nav) {
				nav.classList.remove('point');
			}
			if (recommendNav && currentPage === '/product/recommend.html') {
				recommendNav.classList.add('point');
			}
		}
		// !LEADERMINE 2024-06-25 MO 헤더 및 GNB UI/UX 개선
	</script>
<div id="multi_option" style="display:none;"></div>
<form id="frm_image_zoom" style="display:none;"></form>
<form id="frm_image_zoom" style="display:none;"></form>
<form id="frm_image_zoom" style="display:none;"></form>
<script type="text/javascript">var sAuthSSLDomain = "https://login2.cafe24ssl.com";</script><script type="text/javascript" src="https://login2.cafe24ssl.com/crypt/AuthSSLManager.js"></script><script type="text/javascript" src="https://login2.cafe24ssl.com/crypt/AuthSSLManager.plugin.js"></script>
<!-- CREMA / CAFE24 API Initialize / cre.ma  -->
<script>
  if (this.CAFE24API) { CAFE24API.init(''); } else {
    window.addEventListener('DOMContentLoaded', (event) => { CAFE24API.init(''); });
  }
</script>
<!-- CREMA / Device Detection / cre.ma -->
<script src="//cdn.jsdelivr.net/npm/mobile-detect@1.4.5/mobile-detect.min.js"></script>
<!-- CREMA / 공통 스크립트 (init.js) / cre.ma -->
<script>
  var md = new MobileDetect(window.navigator.userAgent);
  if (md.mobile()) {
    (function(i,s,o,g,r,a,m){if(s.getElementById(g)){return};a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.id=g;a.async=1;a.src=r;m.parentNode.insertBefore(a,m)})(window,document,'script','crema-jssdk','//widgets.cre.ma/nongshimmall.com/mobile/init.js');
  } else {
    (function(i,s,o,g,r,a,m){if(s.getElementById(g)){return};a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.id=g;a.async=1;a.src=r;m.parentNode.insertBefore(a,m)})(window,document,'script','crema-jssdk','//widgets.cre.ma/nongshimmall.com/init.js');
  }
</script>

<!-- 리뷰톡톡에 연결된 전체리뷰게시판 링크 변경 스크립트 -->
<script>
const deprecated_links = Array.from(document.querySelectorAll('a[href*="/board/smartreview/"]'));
for (let i = 0; i < deprecated_links.length; i++) {
 deprecated_links[i].href = '/board/product/list.html?board_no=4';
}
</script>
<span itemscope="" itemtype="https://schema.org/Organization">
<link itemprop="url" href="https://nongshimmall.com">
<a itemprop="sameAs" href="https://www.instagram.com/nongshim/"></a>
<a itemprop="sameAs" href="https://www.facebook.com/nongshim/"></a>
<a itemprop="sameAs" href="https://www.youtube.com/channel/UCzGara7SUTKXruclCD4eA5g"></a>
<a itemprop="sameAs" href="http://www.nongshim.com"></a>
</span>
<script type="text/javascript" src="/app/Eclog/js/cid.generate.js?vs=355f9de883046011ccac161e1f74b3cf&u=nsmall2022.1"></script>
<script>        (function (i, s, o, g) {
            var a = s.createElement(o), m = s.getElementsByTagName(o)[0];
            var initialized = false;
            var interval = null;

            function safeInit() {
              if (initialized) return;
              if (typeof i.initCaWebAnalytics === 'function') {
                try {
                  i.initCaWebAnalytics({"mid":"nsmall2022","stype":"e","domain":"","shop_no":1,"lang":"ko_KR","mobile_flag":"T","send_endpoint":"https://ca-log.cafe24data.com","path_role":"PRODUCT_DETAIL","category_no":822,"category_name":"🍬스낵 & 젤리"});
                  initialized = true;
                } finally {
                  if (interval) clearInterval(interval);
                  a.onload = a.onreadystatechange = a.onerror = null;
                }
              }
            }

            a.onload = a.onreadystatechange = function () {
              if (!a.readyState || a.readyState === 'loaded' || a.readyState === 'complete') {
                safeInit();
              }
            };

            a.onerror = function () {
              if (interval) { clearInterval(interval); interval = null; }
              a.onload = a.onreadystatechange = a.onerror = null;
            };

            interval = setInterval(safeInit, 200);
            setTimeout(function () {
              if (interval) { clearInterval(interval); interval = null; }
            }, 10000);

            safeInit();

            a.async = 1;
            a.setAttribute('crossorigin', 'anonymous');
            a.src = g;
            m.parentNode.insertBefore(a, m);
        })(window, document, 'script', "//optimizer.poxo.com/ca2/analytics.js?v=20260523");</script>

                <script>
                try {
                    // Account ID 적용
                    if (!wcs_add) var wcs_add = {};
                    wcs_add["wa"] = "s_22b61aaaa5d";
            
                    // 네이버 페이 White list가 있을 경우
                    wcs.checkoutWhitelist = ["nsmall2022.cafe24.com", "www.nsmall2022.cafe24.com", "m.nsmall2022.cafe24.com", "thenongshim.co.kr", "www.thenongshim.co.kr", "m.thenongshim.co.kr", "lifefoodmall.com", "www.lifefoodmall.com", "m.lifefoodmall.com", "nongshimmall.net", "www.nongshimmall.net", "m.nongshimmall.net", "hi-nongshim.net", "www.hi-nongshim.net", "m.hi-nongshim.net", "enongshim.co.kr", "www.enongshim.co.kr", "m.enongshim.co.kr", "mihsgnon.com", "www.mihsgnon.com", "m.mihsgnon.com", "e-nongshim.com", "www.e-nongshim.com", "m.e-nongshim.com", "nongshimmart.com", "www.nongshimmart.com", "m.nongshimmart.com", "nongshimmall.co.kr", "www.nongshimmall.co.kr", "m.nongshimmall.co.kr", "hinongshim.com", "www.hinongshim.com", "m.hinongshim.com", "enongshim.com", "www.enongshim.com", "m.enongshim.com", "hinongshim.co.kr", "www.hinongshim.co.kr", "m.hinongshim.co.kr", "hinongshim.net", "www.hinongshim.net", "m.hinongshim.net", "mihsgnon.co.kr", "www.mihsgnon.co.kr", "m.mihsgnon.co.kr", "hi-nongshim.co.kr", "www.hi-nongshim.co.kr", "m.hi-nongshim.co.kr", "thenongshim.com", "www.thenongshim.com", "m.thenongshim.com", "nongshimmart.co.kr", "www.nongshimmart.co.kr", "m.nongshimmart.co.kr", "hi-nongshim.com", "www.hi-nongshim.com", "m.hi-nongshim.com", "lifefoodmall.co.kr", "www.lifefoodmall.co.kr", "m.lifefoodmall.co.kr", "nongshimshop.com", "www.nongshimshop.com", "m.nongshimshop.com", "e-nongshim.co.kr", "www.e-nongshim.co.kr", "m.e-nongshim.co.kr", "nongshimshop.co.kr", "www.nongshimshop.co.kr", "m.nongshimshop.co.kr", "thenongshim.net", "www.thenongshim.net", "m.thenongshim.net", "mihsgnon.net", "www.mihsgnon.net", "m.mihsgnon.net", "nongshimmall.com", "www.nongshimmall.com", "m.nongshimmall.com"];
                
                    // 레퍼러 
                    wcs.setReferer("https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPE_P2eYZPrDnITOuiEYmdqWgDiZxsnLpr1rUwX5qg3rAGYS-8G9DaImFqMnLRs0ePu43ey3DX2HxvBNxcoZiGY3jbULZ0Xqypp6TF_002zLDXMJMnrVfusK1HS8Zr_8eEy-QxDzWGJn_m23n1bgilGH-Bv96Q9P5l1LLbgmUdYRRELQ3PPCnP2kCK");

                    // 유입 추적 함수 호출
                    wcs.inflow("nongshimmall.com");

                    // 로그수집
                    wcs_do();
                } catch (e) {};
                </script>
            

<!-- External Script Start -->

<!-- crt -->
<!-- CMC script -->
<div id="crt_common_top_script" style="display:none;">
<!-- Criteo 로더 파일 -->
<script type="text/javascript" src="//static.criteo.com/js/ld/ld.js" async="true"></script>
<!-- END Criteo 로더 파일 -->

<!-- Criteo Visit Tag -->
<script type="text/javascript">
if (hasCriteoTag() === false) {
  window.criteo_q = window.criteo_q || [];
  window.criteo_q.push(
    { event: "flushEvents"},
    { event: "setAccount", account: "108876"},
    { event: "setSiteType", type: "m" },
    { event: "viewPage"}
  );
}

function hasCriteoTag() {
  var currentPathRole = getPathRole();

  if (currentPathRole === '') {
    return true;
  }
        
  var tagImplementedPathRoles = ['MAIN','PRODUCT_LIST','PRODUCT_SEARCH','PRODUCT_DETAIL','ORDER_BASKET','ORDER_ORDERRESULT'];
    return tagImplementedPathRoles.includes(currentPathRole);
}

function getPathRole() {
  const metas = document.getElementsByTagName('meta');
  for (let i = 0; i < metas.length; i++) {
    if (metas[i].getAttribute('name') === 'path_role') {
      return metas[i].getAttribute('content');
    }
  }

  return '';
}
</script>
<!-- END Criteo Visit Tag -->

<script type="text/javascript">
var email_sha256 = SHA256('');

function SHA256(s){
    if (s == '') {
      return '';
    }
    var chrsz   = 8;
    var hexcase = 0;
   
    function safe_add (x, y) {
      var lsw = (x & 0xFFFF) + (y & 0xFFFF);
      var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
      return (msw << 16) | (lsw & 0xFFFF);
    }
   
    function S (X, n) { return ( X >>> n ) | (X << (32 - n)); }
    function R (X, n) { return ( X >>> n ); }
    function Ch(x, y, z) { return ((x & y) ^ ((~x) & z)); }
    function Maj(x, y, z) { return ((x & y) ^ (x & z) ^ (y & z)); }
    function Sigma0256(x) { return (S(x, 2) ^ S(x, 13) ^ S(x, 22)); }
    function Sigma1256(x) { return (S(x, 6) ^ S(x, 11) ^ S(x, 25)); }
    function Gamma0256(x) { return (S(x, 7) ^ S(x, 18) ^ R(x, 3)); }
    function Gamma1256(x) { return (S(x, 17) ^ S(x, 19) ^ R(x, 10)); }
   
    function core_sha256 (m, l) {
      
      var K = new Array(0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5, 0x3956C25B, 0x59F111F1, 
        0x923F82A4, 0xAB1C5ED5, 0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3, 
        0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174, 0xE49B69C1, 0xEFBE4786, 
        0xFC19DC6, 0x240CA1CC, 0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA, 
        0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7, 0xC6E00BF3, 0xD5A79147, 
        0x6CA6351, 0x14292967, 0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13, 
        0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85, 0xA2BFE8A1, 0xA81A664B, 
        0xC24B8B70, 0xC76C51A3, 0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070, 
        0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5, 0x391C0CB3, 0x4ED8AA4A, 
        0x5B9CCA4F, 0x682E6FF3, 0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208, 
        0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2);

      var HASH = new Array(0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A, 0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19);

      var W = new Array(64);
      var a, b, c, d, e, f, g, h, i, j;
      var T1, T2;
   
      m[l >> 5] |= 0x80 << (24 - l % 32);
      m[((l + 64 >> 9) << 4) + 15] = l;
   
      for ( var i = 0; i<m.length; i+=16 ) {
        a = HASH[0];
        b = HASH[1];
        c = HASH[2];
        d = HASH[3];
        e = HASH[4];
        f = HASH[5];
        g = HASH[6];
        h = HASH[7];
   
        for ( var j = 0; j<64; j++) {
          if (j < 16) W[j] = m[j + i];
          else W[j] = safe_add(safe_add(safe_add(Gamma1256(W[j - 2]), W[j - 7]), Gamma0256(W[j - 15])), W[j - 16]);
   
          T1 = safe_add(safe_add(safe_add(safe_add(h, Sigma1256(e)), Ch(e, f, g)), K[j]), W[j]);
          T2 = safe_add(Sigma0256(a), Maj(a, b, c));
   
          h = g;
          g = f;
          f = e;
          e = safe_add(d, T1);
          d = c;
          c = b;
          b = a;
          a = safe_add(T1, T2);
        }
   
        HASH[0] = safe_add(a, HASH[0]);
        HASH[1] = safe_add(b, HASH[1]);
        HASH[2] = safe_add(c, HASH[2]);
        HASH[3] = safe_add(d, HASH[3]);
        HASH[4] = safe_add(e, HASH[4]);
        HASH[5] = safe_add(f, HASH[5]);
        HASH[6] = safe_add(g, HASH[6]);
        HASH[7] = safe_add(h, HASH[7]);
      }
      return HASH;
    }
   
    function str2binb (str) {
      var bin = Array();
      var mask = (1 << chrsz) - 1;
      for(var i = 0; i < str.length * chrsz; i += chrsz) {
        bin[i>>5] |= (str.charCodeAt(i / chrsz) & mask) << (24 - i%32);
      }
      return bin;
    }
   
    function Utf8Encode(string) {
      string = string.replace(/\r\n/g,"\n");
      var utftext = "";
   
      for (var n = 0; n < string.length; n++) {
   
        var c = string.charCodeAt(n);
   
        if (c < 128) {
          utftext += String.fromCharCode(c);
        }
        else if((c > 127) && (c < 2048)) {
          utftext += String.fromCharCode((c >> 6) | 192);
          utftext += String.fromCharCode((c & 63) | 128);
        }
        else {
          utftext += String.fromCharCode((c >> 12) | 224);
          utftext += String.fromCharCode(((c >> 6) & 63) | 128);
          utftext += String.fromCharCode((c & 63) | 128);
        }
   
      }
   
      return utftext;
    }
   
    function binb2hex (binarray) {
      var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
      var str = "";
      for(var i = 0; i < binarray.length * 4; i++) {
        str += hex_tab.charAt((binarray[i>>2] >> ((3 - i%4)*8+4)) & 0xF) +
        hex_tab.charAt((binarray[i>>2] >> ((3 - i%4)*8  )) & 0xF);
      }
      return str;
    }
   
    s = Utf8Encode(s);
    return binb2hex(core_sha256(str2binb(s), s.length * chrsz));
   
  }
</script>
</div>
<!-- CMC script -->
<!-- CMC script -->
<div id="crt_product_detail_script" style="display:none;">
<script type="text/javascript">
window.criteo_q = window.criteo_q || [];
window.criteo_q.push( 
	{ event: "flushEvents"},
	{ event: "setAccount", account: "108876"},
        { event: "setEmail", email: email_sha256, hash_method: "sha256" },
        { event: "setZipcode", zipcode: "" },
	{ event: "setSiteType", type: "m" },
	{ event: "viewItem", item: "2758" }
);
</script>
</div>
<!-- CMC script -->

<!-- fbe -->
<!-- CMC3 script -->
<div id="fbe_common_top_script" style="display:none;">
  <script type="text/javascript">
if (typeof facebookChannel === 'undefined' && window === window.top) {
  var facebookChannel = {
    mall_id: CAFE24.SHOP.getMallID(),
    shop_no: CAFE24.SDE_SHOP_NUM,
    shop_id: CAFE24.SHOP.getMallID() + '.' + CAFE24.SDE_SHOP_NUM,
    external_id: null,
    event_id: null,

    setInitActivated: function(is_activated) {
      window.top.fbe_init_activated = !!is_activated;
    },
    getInitActivated: function() {
      return !!window.top.fbe_init_activated;
    },
    setEventActivated: function(event_type, is_activated) {
      if (typeof event_type === 'string' && event_type) {
        let key = 'fbe_' + event_type + '_activated'
        window.top[key] = !!is_activated;
      }
    },
    getEventActivated: function(event_type) {
      if (typeof event_type === 'string' && event_type) {
        let key = 'fbe_' + event_type + '_activated'
        return !!window.top[key];
      }
      return false;
    },
    getCookie: function(name) {
      return (name = (document.cookie + ';').match(name + '=.*;')) && name[0].split(/=|;/)[1];
    },
    getExternalId: function() {
      return facebookChannel.getCookie('fb_external_id');
    },
    getEventId: function() {
      return facebookChannel.getCookie('fb_event_id');
    },
    getInt: function(value) {
      let value_int = parseInt(value);
      value_int = isNaN(value_int) ? 0 : value_int;
      return value_int;
    },
    getFloat: function(value) {
      let value_float = parseFloat(value);
      value_float = isNaN(value_float) ? 0.00 : value_float.toFixed(2);
      return value_float;
    },
    init: function() {
      if (facebookChannel.getInitActivated()) {
        return;
      }
      facebookChannel.setInitActivated(true);

      !function(f,b,e,v,n,t,s)
      {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
        n.callMethod.apply(n,arguments):n.queue.push(arguments)};
        if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
        n.queue=[];t=b.createElement(e);t.async=!0;
        t.src=v;s=b.getElementsByTagName(e)[0];
        s.parentNode.insertBefore(t,s)}(window,document,'script',
        'https://connect.facebook.net/en_US/fbevents.js');

      if ((typeof EC_GLOBAL_INFO !== 'undefined' && EC_GLOBAL_INFO.getCountryCode() === 'US') || (typeof SHOP !== 'undefined' && SHOP.getLanguage() === 'en_US')) {
        fbq('dataProcessingOptions', ['LDU'], 0, 0);
      }

      if (typeof ECLOG !== 'undefined' && !!ECLOG.EXTERNAL_ID) {
        ECLOG.EXTERNAL_ID.chk(facebookChannel.shop_id, function(error, external_id) {
          if (error || !external_id) {
            external_id = facebookChannel.getExternalId();
            console.info('external_id is cookie value.', '(1)');
          }
          fbq('init', '1824102027856970',{external_id: external_id}, {agent: 'plcafe24'});
          fbq('trackSingle', '1824102027856970', 'PageView');
          facebookChannel.external_id = external_id;
          facebookChannel.basketEvent();
        });
      } else {
        let external_id = facebookChannel.getExternalId();
        console.info('external_id is cookie value.', '(2)');

        fbq('init', '1824102027856970',{external_id: external_id}, {agent: 'plcafe24'});
        fbq('trackSingle', '1824102027856970', 'PageView');
        facebookChannel.external_id = external_id;
        facebookChannel.basketEvent();
      }
    },
    pixelEvent: function(event_type, callback, is_cookie_event) {
      if (facebookChannel.getEventActivated(event_type)) {
        return;
      }
      facebookChannel.setEventActivated(event_type, true);
      is_cookie_event = !!is_cookie_event;

      let retry = 0;
      let execute = function() {
        if (!facebookChannel.external_id) {
          if (retry < 100) {
            retry++;
            if (retry >= 5) {
              console.warn('retry #' + retry, event_type);
            }
            setTimeout(execute, 1000);
          } else {
            console.warn('external_id is empty.');
          }
          return;
        }

        if (callback.length === 0) {
          callback();
        }
        else if (!is_cookie_event && typeof ECLOG !== 'undefined' && !!ECLOG.EVENT_ID) {
          ECLOG.EVENT_ID.chk(facebookChannel.shop_id, function(error, event_id) {
            if (error || !event_id) {
              event_id = facebookChannel.getEventId();
              console.info('event_id is cookie value.', '(1)');
            }
            facebookChannel.event_id = event_id;
            if (event_id) {
              callback(event_id);
            } else {
              console.warn('event_id is empty.', '(1)');
            }
          });
        }
        else {
          let event_id = facebookChannel.getEventId();
          console.info('event_id is cookie value.', '(2)');
          facebookChannel.event_id = event_id;
          if (event_id) {
            callback(event_id);
          } else {
            console.warn('event_id is empty.', '(2)');
          }
        }
      };
      execute();
    },
    messengerChatPlugin: function() {
      let event_type = 'messenger';
      let sdk_version = '';
      let locale = '';
      if (!sdk_version) {
        console.warn('sdk_version is empty.');
        return;
      }
      if (!locale) {
        console.warn('locale is empty.');
        return;
      }
      if (facebookChannel.getEventActivated(event_type)) {
        return;
      }
      facebookChannel.setEventActivated(event_type, true);

      window.fbAsyncInit = function() {
        FB.init({
          appId : '216637735743129',
          autoLogAppEvents : true,
          xfbml : true,
          version : sdk_version
        });
      };
      (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = 'https://connect.facebook.net/' + locale + '/sdk/xfbml.customerchat.js';
        fjs.parentNode.insertBefore(js, fjs);
      }(document, 'script', 'facebook-jssdk'));
    },
    basketEvent: function() {
      let event_key = 'AddToCart';
      if (facebookChannel.getEventActivated(event_key + '_listener')) {
        return;
      }
      facebookChannel.setEventActivated(event_key + '_listener', true);

      facebookChannel.pixelEvent(event_key, function(event_id) {
        EC$("body").bind("EC_PRODUCT_ACTION_BASKET", function(e, params) {
          try {
            // 필수 데이터 검증
            let validation_error = null;

            if (!params || typeof params !== 'object') {
              validation_error = 'params가 없거나 유효하지 않음';
            } else if (!params.product_no) {
              validation_error = 'product_no가 없음';
            } else if (!params.contents || params.contents.length === 0) {
              validation_error = 'contents가 비어있음';
            } else if (typeof params.total_price === 'undefined' || params.total_price === null) {
              validation_error = 'total_price가 없음';
            } else {
              // contents 배열의 각 항목 검증
              for (let i = 0; i < params.contents.length; i++) {
                let item = params.contents[i];
                if (!item.variant_code) {
                  validation_error = 'contents[' + i + '].variant_code가 없음';
                  break;
                }
                if (!item.quantity) {
                  validation_error = 'contents[' + i + '].quantity가 없음';
                  break;
                }
                if (typeof item.price === 'undefined' || item.price === null) {
                  validation_error = 'contents[' + i + '].price가 없음';
                  break;
                }
              }
            }

            // 검증 실패 시 로그 전송 후 종료
            if (validation_error) {
              console.warn('AddToCart 이벤트 무시: ' + validation_error);
              window.EC_JET?.message?.({
                mall_id: facebookChannel.mall_id,
                shop_no: facebookChannel.shop_no,
                pixel_id: 1824102027856970,
                external_id: facebookChannel.external_id,
                event_id: event_id,
                validation_error: validation_error,
                params: params
              }, 'MBE_ADDTOCART_VALIDATION_ERROR');
              return;
            }

            let event_data = {
              contents: params.contents.map(function(v) {
                return {
                  id: params.product_no + '.' + v.variant_code,
                  quantity: facebookChannel.getInt(v.quantity),
                  item_price: facebookChannel.getFloat(v.price)
                };
              }),
              content_type: 'product',
              value: facebookChannel.getFloat(params.total_price),
              currency: params.currency
            };

            let event_log_data = Object.assign({
              mall_id: facebookChannel.mall_id,
              shop_no: facebookChannel.shop_no,
              pixel_id: 1824102027856970,
              external_id: facebookChannel.external_id,
              event_id: event_id
            }, event_data);

            window.EC_JET?.message?.(event_log_data, 'MBE_ADDTOCART_EVENT');
            fbq('trackSingle', '1824102027856970', event_key, event_data, {eventID: event_id});
          } catch (e) { console.error(e); }
        });
      });
    }
  };

  window.addEventListener('load', facebookChannel.init, false);
}
</script>
<noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=1824102027856970&ev=PageView&noscript=1"
/></noscript>
</div>
<!-- CMC3 script -->
<!-- CMC3 script -->
<div id="fbe_product_detail_script" style="display:none;">
  <script type="text/javascript">
!function() {
  try {
    let event_key = 'ViewContent';
    let event_data = {
      content_name: '인디안밥(83g*1)',
      content_category: '',
      content_ids: ['2758'],
      content_type: 'product_group',
      value: facebookChannel.getFloat('1540'),
      currency: 'KRW'
    };
    if (typeof facebookChannel !== 'undefined') {
      facebookChannel.pixelEvent(event_key, function (event_id) {
        fbq('trackSingle', '1824102027856970', event_key, event_data, {eventID: event_id});
      });
    }
  } catch (e) { console.error(e); }
}();
</script>
</div>
<!-- CMC3 script -->

<!-- gfa -->
<script type="text/javascript">document.addEventListener("DOMContentLoaded", function() {
                EC_PlusAppBridge.setBridgeFunction()
                });</script><script type="text/javascript">var gfa_cate = "";var gfa_cate1 = "";var gfa_cate2 = "";var gfa_cate3 = "";
        if (gfa_cate1 != "") gfa_cate = gfa_cate1;
        if (gfa_cate2 != "") gfa_cate = gfa_cate2;
        if (gfa_cate3 != "") gfa_cate = gfa_cate3;
        document.addEventListener("DOMContentLoaded", function() {
        var oDataGfaDetail = {
        type: "view_item",
        raw_data: {
        currency: SHOP.getCurrency(),
        items: {
        item_name: "인디안밥(83g*1)",
        item_category: gfa_cate
        },
        value: 1540
        }
        };
        EC_PlusAppBridge.sendBridgeData(oDataGfaDetail);
        });</script>
<!-- kmp -->
<!-- CMC3 script -->
<div id="kmp_common_top_script" style="display:none;">
<script type="text/javascript" charset="UTF-8" src="//t1.daumcdn.net/kas/static/kp.js"></script></script>
<script type="text/javascript">
  kakaoPixel('6400742100396522420').pageView();
  kakaoPixel.setServiceOrigin('20001');
</script>

</div>
<!-- CMC3 script -->
 <!-- CMC3 script -->
<div id="kmp_product_detail_script" style="display:none;">
<script type="text/javascript">
  kakaoPixel('6400742100396522420').viewContent({
    currency: "KRW",
    products: [{id: "2758", name: "인디안밥(83g*1)", price: "1540"}]
  });
</script>
</div>
<!-- CMC3 script -->
 
<!-- ttc -->
<script type="text/javascript">
    !function (w, d, t) {
        w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];
        ttq.methods=[
            "page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"]
            ,
            ttq.setAndDefer=
                function(t,e){
                    t[e]=function(){
                        t.push([e].concat(Array.prototype.slice.call(arguments,0)))
                    }
                };

        for(var i=0;i<ttq.methods.length;i++)
            ttq.setAndDefer(ttq,ttq.methods[i]);

        ttq.instance=function(t){
            for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)
                ttq.setAndDefer(e,ttq.methods[n]);
            return e
        },

            ttq.load=function(e,n){
                var i="https://analytics.tiktok.com/i18n/pixel/events.js";
                ttq._i=ttq._i||{},
                    ttq._i[e]=[],
                    ttq._i[e]._u=i,
                    ttq._t=ttq._t||{},
                    ttq._t[e]=+new Date,
                    ttq._o=ttq._o||{},
                    ttq._o[e]=n||{},
                    ttq._partner=ttq._partner||"Cafe24";
                var o=document.createElement("script");
                o.type="text/javascript",
                    o.async=!0,
                    o.src=i+"?sdkid="+e+"&lib="+t;
                var a=document.getElementsByTagName("script")[0];
                a.parentNode.insertBefore(o,a)
            };

        ttq.load("CV9AL2BC77U76UBU9N9G");
        ttq.page();
    }(window, document, 'ttq');

    if (typeof tiktokChannelPixel === 'undefined') {
        var tiktokChannelPixel = {
            getCookie: function (name) {
                return (name = (document.cookie + ';').match(name + '=.*;')) && name[0].split(/=|;/)[1];
            },
            getEventId: function () {
                const self = tiktokChannelPixel;
                return self.getCookie('fb_event_id');
            },
            getExternalId: function () {
                const self = tiktokChannelPixel;
                return self.getCookie('fb_external_id');
            },
            pixelEvent: function (callback) {
                const self = tiktokChannelPixel;
                if (typeof ECLOG !== 'undefined' && ECLOG.EXTERNAL_ID && ECLOG.EVENT_ID) {
                    ECLOG.EXTERNAL_ID.chk(CAFE24.SHOP.getMallID() + '.' + CAFE24.SDE_SHOP_NUM, function (error, externalId) {
                        if (!error && externalId) {
                            ECLOG.EVENT_ID.chk(CAFE24.SHOP.getMallID() + '.' + CAFE24.SDE_SHOP_NUM, function (error, eventId) {
                                if (!error && eventId) {
                                    callback(eventId, externalId);
                                } else {
                                    const eventId = self.getEventId();
                                    if (eventId) callback(eventId, externalId);
                                }
                            });
                        } else {
                            const eventId = self.getEventId();
                            const externalId = self.getExternalId();
                            if (eventId && externalId) callback(eventId, externalId);
                        }
                    })
                } else {
                    const eventId = self.getEventId();
                    const externalId = self.getExternalId();
                    if (eventId && externalId) callback(eventId,externalId);
                }
            },
            basketEvent: function (eventId, externalId) {
                EC$("body").bind("EC_PRODUCT_ACTION_BASKET", function (e, params) {
                    ttq.identify({
                        external_id: externalId
                    });
                    ttq.instance("CV9AL2BC77U76UBU9N9G").track("AddToCart", {
                        contents: params.contents.map(v => ({
                            content_id: "" + params.product_no,
                            content_name: v.name,
                            content_category: params.category ? Object.values(params.category)[0].category_name : '',
                            price: v.price,
                            quantity: v.quantity
                        })), content_type: "product", currency: params.currency, value: params.total_price
                    }, {event_id: eventId});
                });
            },
            basketEvent2: function () {
                const self = tiktokChannelPixel;
                self.pixelEvent(self.basketEvent)
            }
        }
    }

    if (typeof tiktokChannelPixel !== 'undefined') window.addEventListener('load', tiktokChannelPixel.basketEvent2, false);
</script><script type="text/javascript">
    function ViewEvent(eventId, externalId) {
        ttq.identify({
            external_id: externalId
        });

        ttq.instance("CV9AL2BC77U76UBU9N9G").track('ViewContent', {
            contents: [{
                content_id: "2758",
                content_name: '인디안밥(83g*1)',
                content_category: ""||""||"",
                price: 1540,
                quantity: 1,
            }],
            content_type: 'product',
            value: 1540,
            currency: CAFE24.SHOP.getCurrency()
        }, { event_id: eventId})
    }

    if (typeof tiktokChannelPixel !== 'undefined' && tiktokChannelPixel) tiktokChannelPixel.pixelEvent(ViewEvent)
</script>

<!-- yts -->
<!-- Event snippet for Youtube Shopping Conversion -->
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GT-MJSB7NPN"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GT-MJSB7NPN');
</script>
<!-- External Script End -->

<script type="text/javascript" src="//t1.daumcdn.net/adfit/static/kp.js" charset="utf-8"></script>
<script type="text/javascript" src="//t1.kakaocdn.net/kakao_js_sdk/v1/kakao.min.js" charset="utf-8"></script>
<script type="text/javascript" src="/ind-script/i18n.php?v=2605201482&lang=ko_KR&domain=front&type=" charset="utf-8"></script>

<script src="/ind-script/optimizer.php?filename=vVlbd6M2EH5PeO3vIHt6OX2N8Wabs0mTxtnmeRCDrSAkVZc47K_vAE42NmAj7PbBNob5ZiTxzU3KDZS4VqaIDVrlDcP42cb80-8yerY_5d2nnmtgRfz8j0dTbX5-jn6LLkbJ46tDI0HYzY2IKVVwnIb1RgQMMkIW5TIQAIKDDcHQU6dMMyFt1JJQWwubgUPHS4xLVaJ0MbLb5uKJu9Xj9zk4iEouD6IFT0kWH-l6SNZqw6XLB1Up5mvDV8qUiZLOKCHQDEnfC28vtZ4Zni0HLXrHxdCz3KhmtmdWCZJT8swpfSa4xLMUpBy23AKZKksl98u8giTiSuKINugOaWykHZZa0Dp-FAWt41uVcoHxwwdUO4LOHAekS5V5umXXXI9RnnvJ6kWJSS7zzEXlDoXG4joGiSjxt5anH4ECvldCQTZCtPQOaht3qUXzsr2sAxCtRJVzcYAMGebghaunZkswbtbhQf1osVJ6S_lVA_4KBai4qL_v-SuKLjP3gJPmXX7reZUDgDmmfjlS9k9cxze8wHhm1JqWLAG2wlBs0uH7eFRChF4qCkXj0Q_4wnHtQBSby0R56UYqeMAcDUqGiTf1b3VvOJsY0dMlb0D_fy7JKJRKSzy30_AIlsvlNGyJDrI69I9_Y_S5b33-TtfeuUCBzAUo2Jh-tkE0-4h6T43jh3wnZBGAeItq69JGlFVZQd_gfIjRdnXiz6_OQDOC5n_zd6FEprw7jbJ3zh-v6rqE5YlUzbml_FZxynNHK7wmJQuiuMCWazyIOHsHaUjdDGyBJ3oZV15mG2c8XtlTOYFv7yqCA3lXgTzG_ozL7Aj4PCwq7cL_phiRwS5VBqqGt_QRWzJwrncdahSKbf6d51TWgptm9TiwH19WbAfyG27dJOBlqDP-gC6aqDqpzNhoGAneSFMl5YCLeEYeKpBulipg7BbBsNWI9-Igz6u3RupgPtbCLzl1Ay8tW5V5S3PvNwLawK6yOt3LzHaVkgZN3o2n1rtCofE_GvMK6hdnTq2W-gqeV6fWSj2IO3IhhGJATVehhnqZH9ZGhAtSJTMw8S_Rr9FFnFPrqTkrgqDi04XcGc4ej1k0HlM_oN6tCcRviiaFi-BsRp8nblciOLQ9IEPpdnF9GwOefGjzM2lO1zIfvZr8O37xPMNJhh4VNViXWbagNzBJwQM2RbAdX5AA-dUtFxhWUH5830IRf7ieFuXbHYs2Pc18lQgl8Yq69WzSYDZ1oq_CBhNaTu92VpOgVzTvFn4LkuybI7VM5EvtQ9NqkZ79ocNLTeTm9WhBhOHaPYcwTB2KemY3U2CyLRTdjdL6boioZyxE3KBWJmgsqegpvPYBGGjHVjAUDS-9Wy0WN2Fr-JeEkCFU1C37FEMgTQAvmzDQ2c5sHGMLt0ZaluXQFFeupNTliGFoh2QSU2mnvmI1whrYSrL2O1C6xDLtuvQB0J3J0LAuYw_A2r54Kk73bUuMQg6U9wewSZOHw0c7kKQOoObkdpaH2qoLkr5eawSM9W2LHsCZ3ih8ANSG7gIrqlazSdim2kgmjLfhaShlUGLOp1H0Bqpge18MZKFkoQipqKvnrAFTYFyHctQLx--V9jrUKTzVbSUacqkXHr648_acZEFlmOZySUmWIp4NHXxVt-7vuTOcFlsKJrhPQ6s_eH04Wk2m5Qb_COkR6Hojc-oE2sK2r2U4xAEBvIRUYLB1DW5llMDz3k5zhOmbnjquB6JHB_w2_Z1TquZyhLhdU_Gye7hcy37enINsH2k2BQo9tsxw7UZh6pO8-LIudzSy5gQ4h27a64VuRQitk73nzIYKoLqBoef_Ag&type=js&k=b05326de0e1138cd53dcf3eefc2e0e5d631ca409&t=1779324292" ></script><script src="/ind-script/optimizer_user.php?filename=jZJBbsQgDEX3brdzDqSqN-kJHPAkHmGbYjLTuX1JlFXVUdiAv_Sf9PHHE70lcp41iE2cKdw8ZMJEVVgpCKeU6YGVAAu_3_ziZwTJRBVYrzZinzDNxwmlWlpjg0QNOY_QdCdtIa7eTGAXQD_cxtEJVXvaXbykpMfq0xEvnMT742bBmUbNle5Mj1H3t-L_1oxPW7fHOceNiyZiOlwHeKxc2nh9wu5sCrsawSJe6eNz-1IQrTcQm9URbtnH4zpb07EFWXNjX6x8LVwK69y5Xw&type=js&k=3a4d6abb341598ee04560e0abc6e64463ce99eec&t=1763357877&user=T" ></script>
<script type="text/javascript">
var sIsFrontDesignChangeRequired = 'F';
var sYtshopping = 'F';
var sIsYoutubeShops = 'F';
var sIsValidChRef = 'F';
var sChRef = '';
var sIsDropshipping = 'F';
if (sIsValidChRef === 'T') {
sessionStorage.setItem('ch_ref', sChRef);
}
// ch_ref 존재 여부 체크
CAFE24.hasChRef = function() {
if (sIsValidChRef === 'T' && sessionStorage.getItem('ch_ref')) {
return true;
}
return false;
}
// ch_ref 데이터 조회
CAFE24.getChRefData = function() {
if (sIsValidChRef === 'T') {
return sessionStorage.getItem('ch_ref');
}
}
// 프론트 디자인 변경이 필요한지 여부 반환
CAFE24.checkChannelUI = function() {
// [ECHOSTING-598429] 드롭쉬핑은 항상 전체 UI 노출
if (sIsDropshipping === 'T') {
return false;
}
if ((sIsFrontDesignChangeRequired === 'T' && sessionStorage.getItem('ch_ref')) || sIsYoutubeShops === 'T') {
return true;
} else {
return false;
}
}
// 파라미터에 ch_ref 추가
CAFE24.attachChRef = function(sUrl) {
if (sUrl) {
var sChRef = CAFE24.getChRefData();
if (sChRef) {
var sSeparator = (sUrl.includes('?')) ? '&' : '?';
sUrl += sSeparator + 'ch_ref=' + sChRef;
}
}
return sUrl;
}
var sIsCheckout = 'F';
var sCheckoutToken = '';
if (sIsCheckout === 'T') {
sessionStorage.setItem('checkoutToken', sCheckoutToken);
} else {
sessionStorage.removeItem('checkoutToken');
}
CAFE24.getCheckoutToken = function() {
if (sIsCheckout === 'T') {
return sessionStorage.getItem('checkoutToken');
}
}
CAFE24.attachCheckoutParam = function(sUrl) {
if (sUrl) {
var sCheckoutToken = CAFE24.getCheckoutToken();
if (sCheckoutToken) {
var sSeparator = (sUrl.includes('?')) ? '&' : '?';
sUrl += sSeparator + 'checkoutToken=' + sCheckoutToken;
}
}
return sUrl;
}
CAFE24.MOBILE_WEB = true; var mobileWeb = CAFE24.MOBILE_WEB;
try {
var isUseLoginKeepingSubmit = false;
// isSeqNoKeyExpiretime
function isSeqNoKeyExpiretime(iExpiretime)
{
var sDate = new Date();
var iNow = Math.floor(sDate.getTime() / 1000);
// 유효시간 확인
if (iExpiretime > iNow) {
return false;
}
return true;
}
function isUseLoginKeeping()
{
// 디바이스 확인
if (EC_MOBILE_DEVICE === false) {
return;
}
// 로그인 여부
var isLogin = document.cookie.match(/(?:^| |;)iscache=F/) ? true : false
if (isLogin) {
return;
}
var sLoginKeepingInfo = localStorage.getItem('use_login_keeping_info');
var iSeqnoExpiretime;
var iSeqNoKey;
if (sLoginKeepingInfo == null) {
iSeqnoExpiretime = localStorage.getItem('seq_no_key_expiretime');
iSeqNoKey = localStorage.getItem('seq_no_key');
// 유효시간, key 값 확인
if (iSeqnoExpiretime === null || iSeqNoKey === null) {
return;
}
} else {
var oLoginKeepingInfo = JSON.parse(sLoginKeepingInfo);
iSeqNoKey = oLoginKeepingInfo.seq_no_key;
iSeqnoExpiretime = oLoginKeepingInfo.seq_no_key_expiretime;
if (isNaN(iSeqNoKey) === true || isNaN(iSeqnoExpiretime) === true) {
return;
}
}
if (isSeqNoKeyExpiretime(iSeqnoExpiretime) === false) {
return;
}
useLoginKeepingSubmit();
}
function findGetParamValue(paramKey)
{
var result = null,
tmp = [];
location.search.substr(1).split('&').forEach(function (item) {
tmp = item.split('=');
if (tmp[0] === paramKey) result = decodeURIComponent(tmp[1]);
});
return result;
}
function useLoginKeepingSubmit()
{
var iSeqnoExpiretime;
var iSeqNoKey;
var sUseLoginKeepingIp;
var sLoginKeepingInfo = localStorage.getItem('use_login_keeping_info');
if (sLoginKeepingInfo == null) {
iSeqnoExpiretime = localStorage.getItem('seq_no_key_expiretime');
iSeqNoKey = localStorage.getItem('seq_no_key');
} else {
var oLoginKeepingInfo = JSON.parse(sLoginKeepingInfo);
iSeqNoKey = oLoginKeepingInfo.seq_no_key;
iSeqnoExpiretime = oLoginKeepingInfo.seq_no_key_expiretime;
sUseLoginKeepingIp = oLoginKeepingInfo.use_login_keeping_ip;
}
var oForm = document.createElement('form');
oForm.method = 'post';
oForm.action = '/exec/front/member/LoginKeeping';
document.body.appendChild(oForm);
var oSeqNoObj = document.createElement('input');
oSeqNoObj.name = 'seq_no_key';
oSeqNoObj.type = 'hidden';
oSeqNoObj.value = iSeqNoKey;
oForm.appendChild(oSeqNoObj);
oSeqNoObj = document.createElement('input');
oSeqNoObj.name = 'seq_no_key_expiretime';
oSeqNoObj.type = 'hidden';
oSeqNoObj.value = iSeqnoExpiretime;
oForm.appendChild(oSeqNoObj);
var returnUrl = findGetParamValue('returnUrl');
if (returnUrl == '' || returnUrl == null) {
returnUrl = location.pathname + location.search;
}
oSeqNoObj = document.createElement('input');
oSeqNoObj.name = 'returnUrl';
oSeqNoObj.type = 'hidden';
oSeqNoObj.value = returnUrl;
oForm.appendChild(oSeqNoObj);
if (sUseLoginKeepingIp != undefined) {
oSeqNoObj = document.createElement('input');
oSeqNoObj.name = 'use_login_keeping_ip';
oSeqNoObj.type = 'hidden';
oSeqNoObj.value = sUseLoginKeepingIp;
oForm.appendChild(oSeqNoObj);
}
oForm.submit();
isUseLoginKeepingSubmit = true;
}
isUseLoginKeeping();
} catch(e) {
}
CAFE24.KAKAO_PIXEL_BRIDGE.init("6400742100396522420");
if (typeof CAFE24.SHOP_FRONT_NEW_LIKE_COMMON !== "undefined") {CAFE24.SHOP_FRONT_NEW_LIKE_COMMON.init({"bIsUseLikeProduct":false,"bIsUseLikeCategory":true});}
if (typeof CAFE24.SHOP_FRONT_REVIEW_TALK_REVIEW_COUNT !== "undefined") {CAFE24.SHOP_FRONT_REVIEW_TALK_REVIEW_COUNT.bIsReviewTalk = 'F';}
CAFE24.SHOP_CURRENCY_INFO = {"1":{"aShopCurrencyInfo":{"currency_code":"KRW","currency_no":"410","currency_symbol":"\uffe6","currency_name":"South Korean won","currency_desc":"\uffe6 \uc6d0 (\ud55c\uad6d)","decimal_place":0,"round_method_type":"F"},"aShopSubCurrencyInfo":null,"aBaseCurrencyInfo":{"currency_code":"KRW","currency_no":"410","currency_symbol":"\uffe6","currency_name":"South Korean won","currency_desc":"\uffe6 \uc6d0 (\ud55c\uad6d)","decimal_place":0,"round_method_type":"F"},"fExchangeRate":1,"fExchangeSubRate":null,"aFrontCurrencyFormat":{"head":"","tail":"\uc6d0"},"aFrontSubCurrencyFormat":{"head":"","tail":""}}}; var SHOP_CURRENCY_INFO = CAFE24.SHOP_CURRENCY_INFO;
if (typeof CAFE24.SHOP_FRONT_NEW_OPTION_COMMON !== "undefined") {CAFE24.SHOP_FRONT_NEW_OPTION_COMMON.initObject();}
if (typeof CAFE24.SHOP_FRONT_NEW_OPTION_BIND !== "undefined") {CAFE24.SHOP_FRONT_NEW_OPTION_BIND.initChooseBox();}
if (typeof CAFE24.SHOP_FRONT_NEW_OPTION_DATA !== "undefined") {CAFE24.SHOP_FRONT_NEW_OPTION_DATA.initData();}
var basket_result = '/product/add_basket.html';
var basket_option = '/product/basket_option.html';
var bUseElastic = false;
var sSearchBannerUseFlag = 'F';
$Recentword.init();
var sBlackType = ""
var set_option = {"setproduct_require":"setproduct_require","setproduct_option":"setproduct_option","setproduct_add_option":"setproduct_add_option","addproduct_option":"addproduct_option","addproduct_add_option":"addproduct_add_option","code_setproduct":"setproduct","code_addproduct":"addproduct"};
var aWishlistProductData = [];
var product_min = '1';var order_limit_type = 'O';
var delvtype = 'A';
var mileage_val = '0';var mileage_generate_calc = '0';
var basket_type = 'A0000';var product_name = '인디안밥(83g*1)';var product_max_type = 'F';var has_option = 'F';var mileage_icon = '//img.echosting.cafe24.com/design/skin/admin/ko_KR/ico_product_point.gif';var mileage_icon_alt = '적립금';var price_unit_head = '';var price_unit_tail = '원';var option_push_button = 'F';var product_image_tiny = '202407/9a9dff4954efb071d147021be72bc055.jpg';var is_adult_product = 'F';var is_individual_buy = 'F';var is_soldout_icon = 'F';var link_product_detail = '/product/인디안밥83g1/2758/';var sIsNonmemberLimit = 'F';
var product_max = '-1';
var buy_unit_type = 'O';var buy_unit = '1';
var product_price = '1540';var product_price_content = '';var is_selling_price = 'S';var product_price_mobile = '1540';var mobile_dc_price = '';var isMobileDcStatus = 'F';var product_price_ref = '';var currency_disp_type = 'P';
$.data(document,'SameImage','F');
var _iPrdtPriceOrg = 1400;
var _iPrdtPriceTax = 140;
var qrcode_class = 'EC_Qrcode6a10d949ef165';
var sSocialUrl="/exec/front/Product/Social/";
var sIsMileageDisplay = 'F';
var sMileageUnit = '[:PRICE:]원';
var sIsDisplayNonmemberPrice = "F";
var sNonmemberPrice = '-';
try { sessionStorage.setItem('sStorageDetail', 1779489098); } catch (e) {}
setCategoryCookie({"category_no":822,"category_name":"\ud83c\udf6c\uc2a4\ub0b5 & \uc824\ub9ac"});
var _iPrdtPriceOrg = 1400;
var _iPrdtPriceTax = 140;
var option_type = 'T';var product_code = 'P0000ECC';var item_code = 'P0000ECC000A';var item_count = '1';var stock_number = '2';var single_option_stock_data = '{\"use_stock\":false,\"use_soldout\":\"F\",\"stock_number\":2,\"is_reserve_stat\":\"N\"}';var item_listing_type = 'S';var product_option_price_display = 'T';
var iProductNo = 2758;
var sIsDisplayNonmemberPrice = "F";
var sNonmemberPrice = '';
var _iPrdtPriceOrg = 1400;
var _iPrdtPriceTax = 140;
var iProductNo = 2758;
var sIsDisplayNonmemberPrice = "F";
var sNonmemberPrice = '';
var add_option_name = '';
var iProductNo = '2758';var iCategoryNo = '0';var iDisplayGroup = '0';var option_msg = '필수 옵션을 선택해 주세요.';var sLoginURL = 'login.html';var bPrdOptLayer = '';var sOptionType = 'T';
var aReserveStockMessage = {"show_stock_message":"F","Q":"[\uc7ac\uace0 : [:PRODUCT_STOCK:]\uac1c][\ub2f9\uc77c\ubc1c\uc1a1]","R":"[\uc7ac\uace0 : [:PRODUCT_STOCK:]\uac1c][\uc608\uc57d\uc8fc\ubb38]","N":"","stock_message_replace_name":"[:\uc218\ub7c9:]"};
$(function() { CAFE24.FRONT_NEW_PRODUCT_LAZYLOAD.resetDetailContent();});
$(function() { CAFE24.FRONT_NEW_PRODUCT_LAZYLOAD.resetDetailContent();});
var _iPrdtPriceOrg = 1400;
var _iPrdtPriceTax = 140;
var iProductNo = 2758;
var sIsDisplayNonmemberPrice = "F";
var sNonmemberPrice = '';
var _iPrdtPriceOrg = 1400;
var _iPrdtPriceTax = 140;
var sMileageUnit = '[:PRICE:]원';
var sIsDisplayNonmemberPrice = "F";
var sNonmemberPrice = '-';
try { sessionStorage.setItem('sStorageDetail', 1779489098); } catch (e) {}
setCategoryCookie({"category_no":822,"category_name":"\ud83c\udf6c\uc2a4\ub0b5 & \uc824\ub9ac"});
var bIsUseSpread = false;
var sIsSecret = false;
var iBoardNo = "1";
var aLogData = {"log_server1":"eclog2-225.cafe24.com","log_server2":"elg-db-svcm-227.cafe24.com","mid":"nsmall2022","stype":"e","domain":"","shop_no":1,"lang":"ko_KR","ver":2,"hash":"","ca":"cfa-js.cafe24.com\/cfa.js","etc":"","mobile_flag":"T"};
var sMileageName = 'N포인트';
var sMileageUnit = '[:PRICE:]원';
var sDepositName = '예치금';
var sDepositUnit = '원';
; (function() {
var setPcVersionCookie = function() {
$.ajax({
url: '/exec/front/manage/ajaxcookie',
async: false
});
};
if (typeof window.isPCver === 'function') {
var isPCverOld = window.isPCver;
window.isPCver = function() {
setPcVersionCookie();
isPCverOld();
};
}
}());
CAFE24.APPSCRIPT_ASSIGN_DATA = CAFE24.APPSCRIPT_ASSIGN_DATA || [{'src':'https://calendar-app.cafe24.com/openapi/inject.js?vs=20240827111238.1&client_id=A8RQp67UIt9nBlqvThz2jC'},{'src':'https://free-shipping.wehost24.com/scripttag/free-shipping-location-selector.js?vs=20221004185755.1&client_id=hfAG84KGMa9DZwjrYwg1RB', 'integrity': 'sha384-znzqQbXPKcHchFKODexuA3PijC+N5Fq1R7BRqEzf6WOV1/AwK0LItiusvw9cb4WG'},{'src':'https://live24.app/cafe24/all_inc_pack/41801cc23486d1b65167f44f6c6321da.js?vs=20220614143205.1&client_id=QFf0CgssYa4YTLAyyi7hJC'},{'src':'https://widgets.cre.ma/cafe24/init.js?vs=20221214120129.1&client_id=SdksuzSDEpyhy6OLNQpKXC', 'integrity': 'sha384-WDAJpSw3zUhpJD5ZenKaoJ5rcaUpCGj02Qgj7ZL2wzXbp+GRRDZgJIpeGnZxE4GF'},{'src':'https://cdn.datarize.io/logger/autoembed.min.js?site_id=11401&vs=20250820172918.1&client_id=jClAHyRvAdNkCcIH9Cz1PC'},{'src':'https://eventkiki.com/widget/embed/js/ekiki_cafe24_embed.js?vs=20260119163847.1&client_id=A4MW4TICLZtjYhPhIsp1hC'},{'src':'https://instagram-widget.wehost24.com/scripttag/instagram-widget.js?vs=20230207232748.1&client_id=pOawpY4gJZ0oBnihDmiReG'},{'src':'https://cax.channel.io/cafe24/plugins/87268bfe-cc9a-4135-8433-c5bab8e4ba2e.js?vs=20220718155451.1&client_id=QKWiDNLcK9koJO0swpfnuE'},{'src':'https://cdn.onehae.kr/scripts/v2.7/onehae.min.js?vs=20251210171129.1&client_id=jvweNNwf9UCLuvpBevvToU', 'integrity': 'sha384-1JLOoOq0WoHIScWZZRmMr62CMn1ihFtTJaCM50gevk2a8g1ntBUGFDtQqBm4j7Hc'},{'src':'https://cdn.onehae.kr/scripts/v2.7/product.min.js?vs=20251210171132.1&client_id=jvweNNwf9UCLuvpBevvToU', 'integrity': 'sha384-xImy8VU2YzBbmOeNyYJRoyaj7KCKXXTK2Zv05c9syZ4wcE16QpL+N3F+x/5j1LnD'},{'src':'https://jarvis.wepnp.com/app/cafe24/custom/productDetail_nsmall2022.js?vs=20221004085701.1&client_id=pKrmkevnDyZZ1k0f9cAObI'}];
CAFE24.APPSCRIPT_SDK_DATA = CAFE24.APPSCRIPT_SDK_DATA || ['application','customer','notification','order','product','store','supply','category','shipping','community','promotion','design','collection','privacy','mileage','personal','analytics','salesreport'];
var EC_APPSCRIPT_ASSIGN_DATA = CAFE24.getDeprecatedNamespace('EC_APPSCRIPT_ASSIGN_DATA');
var EC_APPSCRIPT_SDK_DATA = CAFE24.getDeprecatedNamespace('EC_APPSCRIPT_SDK_DATA');
</script></body>
</html>


