---
title: "웹 브라우저도 선택지가 점점 사라져간다"
slug: web-browser-comparison
date: 2023-05-28T20:53:37+09:00
series:
#  - 
categories:
  - 잡담
tags:
#  - 
images:
  - web.webp
---

지금은 Chrome이 다 해 먹는 시대가 되었지만, 불과 10년 전만 해도 어떤 웹 브라우저를 쓰느냐가 상당히 중요했었다.

그때 이런저런 웹 브라우저를 사용해 보았고, 지금 와서도 현재 사용 중인 웹 브라우저가 별로 마음에 들지 않으면 곧바로 다른 웹 브라우저를 찾아 설치해 쓰곤 한다.

&nbsp;

그런데 완벽한 웹 브라우저라는 건 존재할 수 없다. 누구나 각자 취향이 다를 것이고, 어떤 웹 브라우저를 써도 불편한 점이 하나 정도는 생긴다.

그래서 아예 날을 잡아, 여태껏 써본 웹 브라우저의 장단점을 정리해 보기로 했다.

당연한 말이겠지만, 아래 적힌 내용은 내 개인적인 사견에 불과하다. 너무 과신하진 말 것.

***

# Chrome

현재 Chrome은 '웹 브라우저의 De Facto Standard'라고 해도 무방하다. 2023년 4월 기준, 전 세계 웹 브라우저 중 72.5%가 Chrome이니 말이다.

하지만 Chrome 뒤에는 세계 최대의 광고 회사, Google이 자리하고 있다.

## Chrome의 장점{id="chrome-pros"}

### 최고의 호환성{id="best-compatibility"}

말해 무엇할까? 어딜 가나 Chrome은 잘 작동할 것이다.

만약 웹 사이트가 오작동한다면, 그건 Chrome의 문제가 아니라 그 웹 사이트의 문제일 확률이 훨씬 더 높다.

## Chrome의 단점{id="chrome-cons"}

### 여러 확장 프로그램의 차단{id="blocked-extension"}

인터넷을 돌아다니다 보면, AdFly처럼 먼저 광고를 일정 시간 보여주고 다음 목적지로 보내는 서비스가 굉장히 많다.

광고를 보고 싶지 않아 하는 건 자연스러운 일이기에, 이러한 서비스를 우회해 곧바로 목적지로 보내주는 Universal Bypass와 같은 확장 프로그램이 등장했다.

하지만 Google은 Universal Bypass를 자사의 확장 프로그램 스토어에서 차단했다. 이후 등장한 후속 프로젝트인 [FastForward](https://fastforward.team/) 역시 차단했고 말이다.

두 프로젝트의 차단 이유는 동일했다. 해당 확장 프로그램이 Paywall(유료 콘텐츠)과 기타 제한 사항을 우회한다는 이유였다. 절대 그런 종류의 확장 프로그램이 아니었음에도 불구하고 말이다.

&nbsp;

Firefox의 확장 프로그램 스토어에서도 차단당한 FastForward이지만, [개발자의 말](https://www.reddit.com/r/Firefox/comments/11zx6px/comment/jdh63t8/?context=3)에 따르면, 그건 순전히 개발자의 잘못이었다고 한다.

후술 할 Manifest v3로의 이전을 준비하느라 바빠 Mozilla에서 보낸 이메일을 제때 확인하지 않았고, 그 탓에 스토어에서 프로젝트가 내려가게 되었다고 한다. Manifest v3로의 이전이 완료되면 다시 스토어에 등록할 예정이라고 한다.

&nbsp;

지금은 FastForward가 다시 [Chrome Web Store](https://chrome.google.com/webstore/detail/fastforward/icallnadddjmdinamnolclfjanhfoafe)에 등재되었지만, 언제 다른 이유를 들어 차단당할지 모르는 상황이다. [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/fastforwardteam/)에도 다시 등록되었다.

### Manifest v3

앞서 말했다시피, Google은 광고 회사이다.

아직도 Google이 검색 엔진 회사라고 믿는 사람은 지금 Google이 가장 많은 수익을 어디서 얻고 있는지 다시 한번 살펴보고 오라.

&nbsp;

그런 Google에게 가장 거슬리는 건 아마 광고 차단 확장 프로그램일 것이다.

하지만 그렇다고 해서 광고 차단 확장 프로그램을 무턱대고 막을 수는 없다. 이미 미국에서 '광고 차단은 이용자의 권리'라고 판결한 사례가 있고, Chrome이 광고 차단 확장 프로그램을 무턱대고 막는다면 사람들은 그저 다른 웹 브라우저로 떠나면 그만이다.

Google은 웹 표준을 선도해 자신에게 유리한 표준을 확립하려 노력하기 때문에, 여기에 있어 가장 중요한 웹 브라우저 점유율을 낮추는 선택을 할 이유가 전혀 없다.

&nbsp;

그래서 Google은 다른 방향으로 광고 차단 확장 프로그램을 방해하기로 했다. 그게 바로 Manifest v3, 줄여서 MV3이다.

겉보기에 MV2에서 MV3로의 이전은 이용자에게 좋은 것으로밖에 들리지 않는다. 하지만 기술적인 측면에서 MV3는 광고 차단 확장 프로그램을 상당히 제한한다.

&nbsp;

실제로 유명 광고 차단 확장 프로그램인 uBlock Origin의 [MV3로의 전환에 대해 다룬 Issue](https://github.com/uBlockOrigin/uBlock-issues/issues/338)를 읽어보면, MV3 적용을 위해선 별도의 확장 프로그램인 uBlock Lite를 만들 수밖에 없다고 한다.

두 확장 프로그램의 개발자인 gorhill이 밝힌 두 확장 프로그램의 차이점을 보면 MV3를 적용한 uBlock Lite가 MV2를 적용한 uBlock Origin보다 기능이 떨어짐이 확연히 보인다.

* Filter lists update only when the extension updates (no fetching up to date lists from servers)  
  필터 목록은 오직 확장 프로그램이 업데이트될 때에만 업데이트됨 (최신 목록을 서버에서 받아올 수 없음)
* Many filters are [dropped at conversion time](https://github.com/gorhill/uBlock/blob/master/dist/mv3/log.txt) due to MV3's limited filter syntax  
  MV3의 제한된 필터 문법 때문에 많은 필터가 MV3로의 이전 과정에서 지원이 중단됨
* No [crafting your own filters](https://github.com/gorhill/uBlock/wiki/Dashboard:-My-filters) (thus no [element picker](https://github.com/gorhill/uBlock/wiki/Element-picker))  
  사용자 필터 생성 불가 (따라서 사용자가 원하는 특정 요소 차단 불가능)
* No [strict-blocked](https://github.com/gorhill/uBlock/wiki/Strict-blocking) pages  
  전체 페이지 차단 불가능
* No [per-site switches](https://github.com/gorhill/uBlock/wiki/Per-site-switches)  
  특정 페이지 전용 스위치 사용 불가능
* No [dynamic filtering](https://github.com/gorhill/uBlock/wiki/Blocking-mode)  
  동적 필터링 사용 불가능
* No [importing external lists](https://github.com/gorhill/uBlock/wiki/Dashboard:-Filter-lists#3rd-party-filter-lists)  
  외부 목록 불러오기 불가능

더 악질적인 건, 이 MV3는 Chrome뿐만 아니라 다른 웹 브라우저의 확장 프로그램에도 적용된다는 점이다. 좋든 싫든, Chrome이 전 세계 웹 브라우저의 절반 이상을 차지하고 있는 이상, 호환성을 위해선 MV3을 도입해야 한다.

물론 다른 웹 브라우저는 Chrome처럼 MV3을 강제하지 않고 MV3과 MV2를 동시에 사용할 수 있도록 할 수 있을 것이다. 하지만 Chrome은 MV3을 강제하기 위해, 예외 없이 2023년 6월부터 모든 MV2 기반 확장 프로그램을 사용할 수 없도록 만들었다.

### 기타 Chrome의 단점{id="misc-chrome-cons"}

Chrome이 간결한 UI를 제공하는 건 좋지만, UI를 편집할 수 없도록 한 것은 단점이다. 북마크 바의 높이가 너무 낮아 높이를 늘리고 싶었지만, Chrome에서는 불가능하다. 이런 점은 Chromium 기반 웹 브라우저가 공유하는 단점으로, Chromium 기반 웹 브라우저가 UI 편집을 제공하지 않는 이상, UI를 일절 편집할 수 없다.

Chrome은 특정 기능의 사용을 강제한다. 읽기 목록이나 QR 코드 생성 기능은 사용자가 끌 수 없다. 물론 Flag를 이용해 임시로 비활성화할 수 있지만, Chrome의 버전이 점차 올라감에 따라 해당 Flag를 더 이상 사용할 수 없게 되면 쓰기 싫은 기능이 UI의 공간을 차지하는 걸 가만히 보고 있을 수밖에 없다.

# Brave

그다음 살펴본 건 Brave 브라우저였다.

Brave 브라우저는 미국의 Brave 社에서 Chrome의 기반이 되는 Chromium의 소스 코드를 가져와 수정해 만든 웹 브라우저이다.

## Brave의 장점{id="brave-pros"}

### 광고 차단{id="adblock"}

난 이미 AdGuard를 쓰고 있기에 Brave의 광고 차단 효과가 그리 눈에 띄지 않지만, 그래도 Brave의 광고 차단 기능은 잘 작동한다.

AdGuard와 Brave를 같이 쓸 경우, AdGuard가 미처 걸러내지 못한 광고를 Brave가 걸러내 준다.

### 빠름{id="fast-brave"}

Brave의 빠른 속도는 광고 차단 기능과 맞물려서 얻는 장점이기도 하다. 웹 브라우저 차원에서 광고 리소스를 요청하지 않기 때문에, 자연스럽게 웹 서핑 속도가 상승한다.

## Brave의 단점{id="brave-cons"}

### Brave Sync{id="brave-sync"}

Brave는 Google이나 MS처럼 계정 기반 동기화를 지원하지 않는다. Brave 브라우저를 동기화하기 위해선 QR 코드를 스캔하거나 동기화 구문을 복사 후 입력해야 한다.

문제는 이 방법이 일반 사용자에겐 굉장히 낯선 방식이기 때문에, 처음 Brave Sync를 설정할 때 몇십 분이나 끙끙대며 내 모바일 기기가 왜 동기화 체인에 등록되지 않는지 고민해야 했다.

### Brave 번역{id="brave-translate"}

Brave는 Chromium의 소스 코드에서 Google 서비스 관련 코드를 전부 자사의 서비스에 연결되도록 바꾼 웹 브라우저이다. 따라서 Chrome이 제공하던 Google 번역 기능 역시 Brave 번역 기능으로 대체되었다.

하지만 번역의 품질이 최악이다. 마치 한때 유행하던 '치익치익 유태인' 번역을 보는 느낌이다. 대체 번역된 문장이 뭘 의미하는지 이해할 수조차 없다.

### 자체 광고 및 BAT{id="ads-and-bat"}

내가 싫어하는 것이 두 가지 있다. 바로 광고와 암호화폐이다. Brave는 둘 다 갖고 있다. 정확히는 그중 광고가 한때 있었다.

&nbsp;

2020년 6월, Brave로 암호화폐 거래소인 바이낸스에 접속하기 위해 사이트 주소를 주소창에 입력하면 자동으로 제휴 코드가 주소 뒤에 추가되는 현상이 발견되었다. `binance.us`를 입력했는데 여기서 `Enter`를 누르면 실제 접속되는 주소는 `binance.us/en?ref=35XXXXXXXX`가 되는 것이다. 물론, 제휴 코드의 주인은 Brave 社였다.

이에 대해 Brave 社의 사장인 브랜든 아이크는 '웹 브라우저에 제휴 코드를 넣는 일은 전혀 문제 될 것이 없다'라고 말했다. 처음 Brave 브라우저의 셀링 포인트는 프라이버시 강화와 광고 차단이었는데 말이다.

{{% collapse heading="그냥 넘겨 들어도 좋은 부분" %}}

결국 여기에 반발해 Brave 브라우저의 소스 코드를 포크해 새로운 웹 브라우저를 만들기로 한 프로젝트가 나타났다. 거기에 대해 브랜든 아이크는 이렇게 말했다.

> 새로운 웹 브라우저를 만드는 건 좋지만, 일단 프로젝트의 이름을 우리 웹 브라우저인 Brave와 유사한 이름인 Braver에서 다른 이름으로 바꿔라.
> 우리가 제공하는 서비스와 서버에 무단으로 올라타지 말고, 자체적인 서비스와 업데이트를 제공해라.

틀린 말은 결코 아니다. 여기에 대해선 나도 브랜든 아이크의 의견에 100% 동의하니까.

&nbsp;

결국 그 프로젝트는 이름을 Braver에서 <a href="https://github.com/BoldBrowser/bold-browser" target="_blank" rel="noopener noreferrer">Bold</a>로 바꿨고, 소스 코드도 Brave 웹 브라우저 대신 Ungoogled Chromium에서 가져오기로 했다. 하지만 그 과정에서 개발 의욕이 바닥난 건지, 프로젝트가 거기서 멈춰버렸다.

오픈 소스가 뭐 그렇지...

{{% /collapse %}}

# Microsoft Edge

그다음 살펴본 Chromium 기반 웹 브라우저는 MS의 Edge였다.

MS Edge 역시 MS가 Chromium의 소스 코드를 가져와 Google과 관련한 코드를 전부 자사의 코드로 바꾸고 추가적으로 수정을 가한 웹 브라우저이다.

## Edge의 장점{id="edge-pros"}

### 빠름{id="fast-edge"}

Google이 대체 Chromium의 소스 코드에 뭔 짓을 한 건지 의심이 들 지경이다.

Brave나 Edge나 Chromium의 소스 코드에서 Google 관련 코드를 들어내고 자사의 코드로 대체한 후, 각자만의 최적화를 더했을 뿐인데 Chrome보다 월등히 빠르다.

Brave, Edge, Chrome을 비교했을 때, Chrome이 제일 느렸다.

### 확장 프로그램{id="extensions"}

Edge는 Chrome의 확장 프로그램을 사용할 수 있을뿐더러, Edge Add-ons에서도 Edge만의 확장 프로그램을 설치할 수 있다. 앞서 말했던 [FastForward](https://microsoftedge.microsoft.com/addons/detail/fastforward/ldcclmkclhomnpcnccgbgleikchbnecl) 역시 Edge Add-ons에 등재되어 있다.

광고가 주 수입원인 Google에 비해, MS는 다른 서비스로도 충분히 돈을 벌 수 있기 때문에 확장 프로그램을 크게 제한하지 않는 것으로 추측된다.

## Edge의 단점{id="edge-cons"}

### 느린 시작{id="slow-startup"}

예전에는 이러지 않았던 것 같은데, Edge를 실행할 때, 웹 브라우저의 창이 나타나지 않고 흰색으로 가득 찬 창만이 나타날 때가 자주 있다.

그대로 Edge를 강제 종료하거나 조금 기다리면 정상적으로 Edge의 창이 나타나지만, 웹 브라우저가 이래서는 안 된다.

PS. 이 문제는 사용자 데이터 폴더[^1]를 완전히 지우니 해결되었다.

[^1]: `%LocalAppData%\Microsoft\Edge\User Data`

# Vivaldi

Vivaldi는 Opera Software 社가 2016년 중국 IT업체 컨소시엄에 인수된 후, Opera Software의 창립자가 새로 세운 Vivaldi Technologies 社에서 만든 Chromium 기반 웹 브라우저이다.

## Vivaldi의 장점{id="vivaldi-pros"}

### UI 편집의 자유{id="flexible-ui-modification"}

브라우저 UI를 Javascript, React, Browserify 등을 이용해 만들었다고 하는데, 그 덕분인지 UI의 편집의 자유도가 굉장히 높다.

Vivaldi의 북마크바는 Chromium처럼 '모든 북마크'를 북마크 바의 오른쪽에 표시하지 않는데, Vivaldi는 '모든 북마크' 폴더를 북마크바의 첫 번째 자리에 둔 후, 다음 CSS를 적용하면 된다.

{{% collapse heading="'모든 북마크' 폴더 CSS 코드" %}}

```css
/* == Chromium Style "Other bookmarks" Bookmark Bar Folder Mod - made by nomadic on the Vivaldi Forums == */
/* Source: https://forum.vivaldi.net/topic/88400 */
/* Moves the first bookmark bar folder to the far right side. Requires the first bookmark bar item to be a folder */
#browser {
  /* You may need to adjust to fit the entire text "Other bookmarks" */
  --overallFolderWidth: 130px;
}
/* Push the first folder to the far right and increase its width */
.bookmark-bar button.folder:first-of-type {
  max-width: var(--overallFolderWidth);
  position: absolute;
  right: 0;
  height: 100%;
  z-index: 1;
}
/* Border in front of folder icon */
.bookmark-bar button.folder:first-of-type::before {
  content: "";
  position: absolute;
  left: -5px;
  top: 20%;
  width: 1px;
  height: 60%;
  background-color: var(--colorFgFadedMost);
}
/* Leave space on the right for the folder */
.bookmark-bar .observer {
  padding-right: var(--overallFolderWidth);
}
```

{{% /collapse %}}

선택한 탭의 파비콘이 강조 표시되는 게 싫다면 다음 CSS를 적용하면 된다.

{{% collapse heading="파비콘 강조 해제 CSS 코드" %}}

```css
.tab.active .favicon {
  filter: none !important;
}
```

{{% /collapse %}}

이 정도의 UI 편집 자유도는 Firefox에서나 볼 수 있을 정도이다.

## Vivaldi의 단점{id="vivaldi-cons"}

### 이상한 곳에서 부족한 기능{id="lack-of-niche-feature"}

의도된 것인지, 단순히 버그인지는 모르겠지만, 당연히 될 것으로 생각했던 것이 되지 않는다.

* HTML 파일을 웹 브라우저에 드래그&드롭했을 때, HTML 파일이 열리지 않음  
  다른 Chromium 기반 웹 브라우저는 물론, 심지어 Firefox에서도 가능했던 일이다.
* Bookmarklet에 적힌 `'` 문자가 `%27`로 대체됨  
  이러면 Bookmarklet이 정상적으로 작동하지 않는다.

### 기타 Vivaldi의 단점{id="misc-vivaldi-cons"}

어째서인지 Vivaldi Sync의 로그인이 자주 풀려 하루에 최소 한 번은 다시 로그인해야 했다.

# SRWare Iron

SRWare Icon은 독일의 SRWare 社가 Chromium 소스 코드를 가져와 만든 웹 브라우저이다.

다만 Brave나 MS Edge처럼 Google과 연관된 코드를 자사의 것으로 교체하지 않고, 오직 개인 정보 보호와 보안에만 집중했다.

만약 Chrome이 내 개인 정보를 지나치게 많이 수집한다고 생각한다면, SRWare Iron이 좋은 대안이 될 수 있을 것이다.

## SRWare Iron의 장점{id="iron-pros"}

### Chromium 그대로의 UI{id="chromium-ui"}

오로지 개인 정보 보호와 보안에만 신경 쓴 웹 브라우저이기 때문에, UI 등에 별다른 수정을 가하지 않았다. 따라서 Chromium의 UI를 그대로 갖고 있다.

### 개인 정보 보호{id="iron-privacy-protection"}

대체 어느 부분이 Chrome과 차이 나는 것인지에 대해, [공식 홈페이지](https://www.srware.net/iron/)에서는 다음 요소들이 제거되었다고 한다.

* 설치 ID  
  Chrome이 처음 설치되고 실행되었을 때 Google에 설치 ID를 보내게 된다.
* 추천  
  설정에 따라 다르지만, 주소창에 입력한 모든 정보가 추천 정보 생성을 위해 Google에 보내진다.
* 대체 오류 페이지  
  설정에 따라 다르지만, 만약 잘못된 주소를 주소창에 입력해 접속했을 시, Google이 제공하는 오류 메시지를 보게 된다.
* 오류 보고  
  설정에 따라 다르지만, 오류가 발생했을 시 자세한 정보가 Google에 전송된다.
* RLZ 추적  
  [RLZ](https://github.com/rogerta/rlz)는 프로모션 이벤트 신호와 익명 사용자 코호트를 그룹화하기 위한 라이브러리인데, 2012년 Chromium 소스 코드에 통합되었다. RLZ는 다양한 정보를 Google에 전송하는데, 예를 들자면 언제 어디서 Chrome이 다운로드되었는가와 같은 정보이다.
* URL 트래커  
  설정에 따라 다르지만, Chrome은 실행 5초 후 백그라운드에서 Google 홈페이지를 몰래 연다.

SRWare Iron이 Chromium에서 제거한 항목들을 보면 웹 브라우저 사용에 있어 없어도 사용에 전혀 지장이 없는 것들로만 가득하다.

&nbsp;

Google은 당신에게 관심이 매우 많다. MS 역시 마찬가지이고.

## SRWare Iron의 단점{id="iron-cons"}

### 자동 업데이트 기능의 부재{id="no-auto-update"}

SRWare Iron에는 자동 업데이트 기능이 일절 존재하지 않는다.

SRWare Iron처럼 개인 정보 보호를 목표로 하는 많은 웹 브라우저들은 최신 버전 확인을 위한 공식 서버 접속마저도 개인 정보를 수집하는 행위라고 여기기 때문에, 자동 업데이트 기능은 이러한 부류의 웹 브라우저에서 찾아보기 힘들다.

공식 포럼에서 공식적으로 [Iron Updater 확장 프로그램](https://www.srware.net/forum/viewtopic.php?f=18&t=11751)을 제공하지만, 이 확장 프로그램은 SRWare Iron을 포터블 버전으로 이용할 때만 사용할 수 있다. 만약 설치 버전에서 해당 확장 프로그램을 이용할 시, SRWare Iron은 최신 버전을 이미 설치했음에도 새 업데이트가 있다고 자꾸 알림을 보낼 것이다.

### 불편한 최신 버전 확인{id="uncomfortable-latest-version-check"}

SRWare Iron의 최신 버전이 얼마인지 알기 위한 방법에는 세 가지가 있다.

* [공식 Twitter](https://twitter.com/srware) 확인
* [공식 포럼](https://www.srware.net/forum/viewforum.php?f=18) 확인
* 직접 설치 파일 버전 확인

자동 업데이트 기능이 없기 때문에, Twitter에 로그인하고 싶지 않은 사람은 공식 포럼을 확인하거나, 직접 설치 파일을 내려받아 속성의 버전 탭을 확인할 수밖에 없다.

### 뒤처지는 업데이트{id="outdated-version"}

SRWare Iron은 최신 Chromium의 버전을 잘 따라가지 않는다.

2023년 8월 31일 기준, 최신 Chrome의 버전이 116.0.5845.141이고 Chromium의 버전이 118.0.5981.0인데 비해 SRWare Iron은 여전히 Chromium 115.0.5850.0 버전에 기반하고 있다.

Chromium은 버전과 빌드가 올라가면서 각종 취약점이나 버그를 고친다는 것을 생각해 보면, 웹 브라우저의 보안이 다소 저하된다는 점이 못내 신경 쓰인다.

### User Agent 변경{id="user-agent-change"}

SRWare Iron은 웹 브라우저의 기본 User Agent를 변경한다.

Chromium의 User Agent:

> Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
{.bq}

SRWare Iron의 User Agent:

> Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 <mark>Iron</mark> Safari/537.36
{.bq}

대부분의 경우, 이는 큰 문제가 되지 않는다.

하지만 몇몇 웹사이트의 경우, 널리 알려진 User Agent가 아닌 사용자가 접속을 시도할 시, 이를 봇 등으로 판단하여 웹사이트의 접속을 차단한다. 고작 Iron 문자열이 하나 추가되었다고 접속이 거부되는 것이다.

Medium의 경우가 바로 그러했는데, Medium의 고객 센터와 상의한 끝에 SRWare Iron이 User Agent에 추가한 'Iron' 문구가 문제를 일으켰다는 결론에 도달했다.

&nbsp;

이를 해결하기 위해서는 SRWare Iron을 설치할 때 같이 설치된 Iron Config & Backup Tool의 UserAgent 탭에서 수동으로 User Agent를 평범한 User Agent로 변경해 주어야 한다.

다만 이는 기본 User Agent를 변경하는 것이 아니라, 사용자가 설정한 User Agent를 사용하도록 설정된 별도의 바로가기를 생성하는 것뿐이기 때문에, 기존에 있던 모든 SRWare Iron 바로가기 역시 수정해 주어야 한다.

# Cent Browser

Cent Browser는 미국의 Cent Studio 社가 Chromium의 소스 코드를 수정해 만든 웹 브라우저이다.

## Cent Browser의 장점{id="cent-browser-pros"}

### 다양한 기본 기능{id="feature-rich"}

다른 웹 브라우저였다면 확장 프로그램을 설치해야 사용할 수 있었을 [많은 기능](https://www.centbrowser.com/features.html)들이 웹 브라우저에 통합되어 있다.

## Cent Browser의 단점{id="cent-browser-cons"}

### 매우 뒤처지는 업데이트{id="very-outdated-version"}

Cent Browser는 SRWare Iron보다 Chromium 버전 업데이트가 느리다.

2023년 8월 31일 기준, 최신 Chrome의 버전이 116.0.5845.141이고 Chromium의 버전이 118.0.5981.0인데 비해 CentBrowser는 아직도 Chromium 102.0.5005.167 버전에 기반하고 있다. SRWare Iron이 Chromium 115.0.5850.0 버전에 기반한 것을 생각하면, 버전 업데이트가 없다시피 한 것이다.

&nbsp;

CentBrowser의 Chromium 버전이 너무 낮기 때문에, Chrome Web Store의 일부 확장 프로그램은 설치가 불가능하고, reCAPTCHA 역시 제대로 로딩이 되지 않는다.

Cent Studio는 reCAPTCHA가 나타나지 않는 문제가 낮은 Chromium 버전 때문이 아니라고 하지만, 비교적 최신 Chromium을 쓰는 다른 웹 브라우저 모두 reCAPTCHA를 정상적으로 표시한다.

&nbsp;

따라서 Cent Browser는 지나치게 느린 Chromium 버전 업데이트 때문에, 사용해서는 안 되는 웹 브라우저이다.

***

# Firefox

만약 Chromium에 기반하지 않은 웹 브라우저를 원한다면 다른 선택지는 Firefox 말고는 없다.

현재 주요 웹 브라우저 엔진과 해당 엔진을 채용한 웹 브라우저의 목록은 다음과 같다.

* Gecko: Mozilla 재단에서 현재 사용 중인 웹 브라우저 엔진  
  Firefox가 이를 사용 중이다.
* Servo: Mozilla 재단에서 개발하다 중단한 후, 다시 개발 중인 웹 브라우저 엔진
* Webkit
  * WebKit2: Apple이 현재 개발 중인 웹 브라우저 엔진  
    Safari 외에는 이를 사용하는 웹 브라우저가 없다.
  * Blink: Google이 현재 개발 중인 웹 브라우저 엔진  
    Chromium 기반 웹 브라우저는 모두 Blink 엔진을 사용한다.
* Presto: Opera에서 사용했던 웹 브라우저 엔진  
  현재 Opera도 Chromium 기반 웹 브라우저가 됨에 따라, 사용하는 웹 브라우저가 없다.

## Firefox의 장점{id="firefox-pros"}

### 높은 자유도{id="maximum-ui-modification"}

고급 사용자용 기능이긴 해도, Firefox 역시 UI를 마음대로 뜯어고칠 수 있다.

Vivaldi처럼, Firefox도 `userChrome.css` 파일을 통해 웹 브라우저의 UI를 마음대로 손볼 수 있다.

`userContent.css` 파일을 이용하면 특정 사이트에서만 적용되는 스타일을 선언할 수도 있다.

### 개인 정보 보호{id="firefox-privacy-protection"}

Google이나 MS는 사용자의 개인정보에 지대한 관심을 두고 있다. 당연히 그들이 개발한 웹 브라우저인 Chrome/Chromium과 MS Edge에는 사용자의 개인정보를 추적하는 기능이 들어있다.

Firefox에는 그러한 개인정보 추적기능이 훨씬 적게 들어가 있으며, 심지어 고급 설정을 통해 그것마저도 전부 끌 수 있다.

## Firefox의 단점{id="firefox-cons"}

### 리다이렉트 오류{id="redirect-malfunction"}

Google 로그인이나 Paypal처럼 리다이렉트를 이용하는 로그인 방식을 사용할 수 없다. Google 로그인의 경우 '오류가 발생했습니다'라는 메시지만 표시할 뿐이었고, Paypal은 아예 사이트가 불러와지지 않았다.

***

이외에도 Naver Whale 등의 다른 웹 브라우저도 사용해 보았지만, 마지막으로 그것들을 사용한 것이 오래되어 따로 여기에 적진 않았다.
