---
title: "커스텀의 길은 멀고 험하다"
slug: long-tough-road-of-customization
date: 2020-04-19T20:52:39+09:00
series:
#  - 
categories:
  - 잡담
tags:
#  - 
images:
#  - 001.webp
---

내가 지금 쓰고 있는 스마트폰은 '갤럭시 S8+'이다. 갤럭시 S8+이 출시한 게 17년 3월이니까 나온 지 3년 된 녀석이다.

이미 안드로이드 OS 업그레이드를 오레오, 파이 두 번을 받았기에, 삼성은 더 이상 갤럭시 S8+에 OS 업그레이드를 제공하지 않는다. 이제 남은 건 몇 개월마다 오는 보안 업데이트 정도인데, 이마저도 얼마 남지 않았다.

&nbsp;

그래서 속 시원하게 Knox를 깨버렸다. Knox 카운터를 포기하면 커스텀 롬을 쓸 수 있으니까.

하지만 그때는 몰랐다. 이젠 옛날처럼 하드 하게 커스텀 롬 개발을 하는 사람이 없다는 것을...

***

S8+에는 여러 변종이 있다. 대충 적으면 이렇다.

* G955N: 한국 전용 (엑시노스)
* G955F: 글로벌 싱글심 (엑시노스)
* G955FD: 글로벌 듀얼심 (엑시노스)
* G955U: 미국 내수용 (스냅드래곤)
* G955W: 캐나다 공용 (스냅드래곤)

이외에도 9550이나 955D, 955J도 있는데, 이것들은 중국 혹은 일본 전용 모델이라서 XDA에서 볼 일이 거의 없다. 그 나라 사람들은 XDA가 아니라 자기들 포럼을 따로 차려놓고 거기서 노는 경향이 심하니까.

&nbsp;

일단 국내에는 S8+ 커스텀 롬을 만드는 사람이 없다. 아니, 국내에서 개발하는 커스텀 롬이 남아 있긴 한지부터가 의문이다.

그렇기 때문에 내가 찾아볼 곳은 XDA밖에 없다. 하지만 XDA에서도 S8 개발은 활성화되었어도 S8+은 아닌지, XDA에서의 커스텀 롬 포럼은 'S8 전용'과 'S8/S8+ 크로스 플랫폼' 둘 밖에 없다. 내 스마트폰은 S8+이니, 'S8/S8+ 크로스 플랫폼' 포럼을 뒤져야 한다.

한국 전용 모델인 G955N은 해외에 발매가 되지 않았기 때문에, XDA에 올라온 커스텀 롬의 일부는 G955F/FD만 지원하고 G955N을 지원하지 않기도 한다. 이런 커스텀 롬은 S8+에 올릴 수는 있지만, 전화나 데이터 통신이 불가능하다.

&nbsp;

XDA에서 커스텀 롬을 이것저것 내려받아서 썼는데, 죄다 아쉬운 부분이 있었다. 이게 다 커스텀 롬 개발이 셋 중 하나이기 때문이다.

* S8/S8+ 정식 펌웨어 기반
* S9 등 다른 기기 펌웨어 기반
* Lineage OS 기반

정식 펌웨어 기반 커스텀 롬은 안드로이드 Pie까지만 개발이 가능하고, 다른 기기 펌웨어 기반 커스텀 롬은 S8/S8+을 위해 개발된 앱을 억지로 돌리는 만큼, 불안정하다. Lineage OS 기반은 사용이 불가능한 기능이 있을 수 있다.

&nbsp;

XDA에 올라온 커스텀 롬 중 내가 살펴본 것은 다음과 같다. 애당초 XDA에 올라온 커스텀 롬 중, 최근까지 개발 혹은 업데이트를 한 커스텀 롬이 별로 없다.

<div class="table-responsive">
<table>
  <tr>
    <th style="width: 33.3333%; text-align: center;">커스텀 롬 이름</th>
    <th style="width: 33.3333%; text-align: center;">안드로이드 버전</th>
    <th style="width: 33.3333%; text-align: center;">언급된 지원 기종 (S8+ 한정)</th>
  </tr>
  <tr>
    <td style="width: 33.3333%; text-align: center;">
      <a href="https://xdaforums.com/t/4041977/" target="_blank" rel="noopener">Lineage OS 17.1</a>
    </td>
    <td style="width: 33.3333%; text-align: center;">Android 10 (10.0)</td>
    <td style="width: 33.3333%; text-align: center;">SM-G955F</td>
  </tr>
  <tr>
    <td style="width: 99.9999%; text-align: left;" colspan="3">
      <p>안드로이드 10 AOSP 기반인 커스텀 롬이다.</p>
      <p>삼성이 One UI 차원의 다크 모드를 도입했지만 안드로이드 OS에는 여전히 다크 모드가 존재하지 않기 때문에, 몇몇 앱은 여전히 라이트 모드로 표시된다. 게다가 One UI 때문인지 삼성 펌웨어의 용량은 굉장히 높다.</p>
      <p>삼성 펌웨어를 기반으로 한 커스텀 롬은 대부분 그 용량이 2GB가 훌쩍 넘어간다. 하지만 이건 삼성 펌웨어 기반이 아니라 AOSP 기반이라서 용량이 600MB 정도로 매우 매우 가볍다.</p>
      <p>PS. 나중에 안 건데, 이 커스텀 롬이 지원하는 모델은 G955F밖에 없다. N이던 FD던 지원이 불명확하다는 거다. 이걸 플래싱하고 '왜 통신이 안 돼?'라고 생각했었는데 이것 때문일지도 모르겠다. 이건 내가 바보였다고 할 수밖에.</p>
    </td>
  </tr>
  <tr>
    <td style="width: 33.3333%; text-align: center;">
      <a href="https://xdaforums.com/t/4041973/" target="_blank" rel="noopener">Havoc-OS</a>
    </td>
    <td style="width: 33.3333%; text-align: center;">Android 10 (10.0)</td>
    <td style="width: 33.3333%; text-align: center;">???</td>
  </tr>
  <tr>
    <td style="width: 99.9999%; text-align: left;" colspan="3">
      <p>역시 안드로이드 10 AOSP 기반 커스텀 롬이다.</p>
      <p>이 커스텀 롬은 XDA:DevDB에 등록되어 있지 않다. XDA:DevDB에 등록된 정보를 통해서 해당 커스텀 롬이 어떤 모델을 지원하는지, 마지막 업데이트 일은 언제였는지와 같은 정보를 얻을 수 있기 때문에, DevDB에 등록되지 않은 커스텀 롬은 사용하기가 두렵다.</p>
      <p>설명 페이지에 지원 모델을 자세히 밝히지 않고 뭉뚱그려 'S8+'이라고만 적어두었기에 '써도 괜찮겠지'라고 생각하고 플래싱 했는데, 이 녀석도 통신이 안 되었다.</p>
    </td>
  </tr>
  <tr>
    <td style="width: 33.3333%; text-align: center;">
      <a href="https://xdaforums.com/t/4000491/" target="_blank" rel="noopener">HavocOS 2.X</a>
    </td>
    <td style="width: 33.3333%; text-align: center;">Pie (9.0)</td>
    <td style="width: 33.3333%; text-align: center;">???</td>
  </tr>
  <tr>
    <td style="width: 99.9999%; text-align: left;" colspan="3">
      <p>이 커스텀 롬 역시 XDA:DevDB에 등록되지 않은 Havoc OS 롬이다.</p>
      <p>위와는 다르게 안드로이드 파이 버전의 Havoc OS를 이식한 건데, 지원 기종이 표시되지 않은 것은 여전하다.</p>
      <p>그리고 이 녀석도 통신이 되지 않는다.</p>
    </td>
  </tr>
  <tr>
    <td style="width: 33.3333%; text-align: center;">
      <a href="https://xdaforums.com/t/3891932/" target="_blank" rel="noopener">hadesROM</a>
    </td>
    <td style="width: 33.3333%; text-align: center;">Pie (9.0) + One UI</td>
    <td style="width: 33.3333%; text-align: center;">SM-G955F<br>SM-G955FD<br>SM-G955N</td>
  </tr>
  <tr>
    <td style="width: 99.9999%; text-align: left;" colspan="3">
      <p>맨 처음 써본 커스텀 롬이며, 내가 마지막으로 정착하기로 한 커스텀 롬이기도 하다. 위의 다른 커스텀 롬과 다르게, 노트 8의 삼성 펌웨어를 기반으로 한 커스텀 롬이다.</p>
      <p>다 좋다. 삼성 펌웨어를 기반으로 했기 때문에 '보안 폴더'도 사용할 수 있고 'AOD'도 사용할 수 있다.</p>
      <p>그런데 한 가지 단점이 있다. MMS가 왔을 때 데이터를 켜지 않으면 MMS의 내용을 받지 못한다. MMS를 받기 위해서는 데이터 통신을 켜야 하는데, 국내와 다르게 해외 펌웨어는 MMS 수신을 위해 데이터 통신을 자동으로 켜고 끄지 않는다. APN 설정이 문제인 건가 싶어 시스템 내부에 있는 APN 설정 파일을 들여다보았지만, 별다른 문제를 발견하지 못했다. 'KT IMS'라는 항목이 APN 설정 파일에서 발견되었는데 활성화된 APN 리스트에는 존재하지 않았다. IMS가 MMS 관련한 용어일 텐데...</p>
      <p>아직도 MMS 문제는 정확히 무엇이 원인인지 파악하지 못하고 있다.</p>
    </td>
  </tr>
  <tr>
    <td style="width: 33.3333%; text-align: center;">
      <a href="https://xdaforums.com/t/3907076/" target="_blank" rel="noopener">EclipseSTOCK</a>
    </td>
    <td style="width: 33.3333%; text-align: center;">Pie (9.0) + One UI</td>
    <td style="width: 33.3333%; text-align: center;">SM-G955F<br>SM-G955FD<br>SM-G955N</td>
  </tr>
  <tr>
    <td style="width: 99.9999%; text-align: left;" colspan="3">
      <p>이 커스텀 롬 역시 삼성 펌웨어를 기반으로 한 커스텀 롬이다. hadesROM이 노트 8의 펌웨어를 기반으로 했다면, 이 커스텀 롬은 S8의 펌웨어를 기반으로 만들어졌다. 그래서 그런지, UI의 크기가 조금 크다.</p>
      <p>시간이 충분했다면 이것도 이리저리 뜯어보면서 내 나름의 최적화를 했겠지만, S8+이 아닌 S8 기반인지라 UI 크기부터가 마음에 안 들어서 사용을 그만두었다.</p>
      <p>또한 hadesROM과 달리 '보안 폴더'를 사용할 수 없다. '삼성 패스'는 Knox 카운터가 깨졌으면 절대로 사용 불가능하니까 그렇다 치더라도 '보안 폴더'가 사라진 건 아쉬운 일이다.</p>
    </td>
  </tr>
  <tr>
    <td style="width: 33.3333%; text-align: center;">
      <a href="https://xdaforums.com/t/3753975/" target="_blank" rel="noopener">Alexis ROM</a>
    </td>
    <td style="width: 33.3333%; text-align: center;">Pie (9.0) + One UI </td>
    <td style="width: 33.3333%; text-align: center;">SM-G955F<br>SM-G955FD<br>SM-G955N</td>
  </tr>
  <tr>
    <td style="width: 99.9999%; text-align: left;" colspan="3">
      <p>삼성 펌웨어 기반이지만 XDA:DevDB에 등록되어 있지 않다.</p>
      <p>텔레그램 채널에서 만난 개발자가 '꼬우면 쓰지 말던가'라는 식으로 굉장히 무례하게 날 대해, 곧바로 다른 커스텀 롬으로 옮겨갔다.</p>
    </td>
  </tr>
  <tr>
    <td style="width: 33.3333%; text-align: center;">
      <a href="https://xdaforums.com/t/3891294/" target="_blank" rel="noopener">LightROM</a>
    </td>
    <td style="width: 33.3333%; text-align: center;">Pie (9.0) + One UI </td>
    <td style="width: 33.3333%; text-align: center;">SM-G955F<br>SM-G955FD</td>
  </tr>
  <tr>
    <td style="width: 99.9999%; text-align: left;" colspan="3">
      <p>G955N을 지원한다는 이야기가 없는 데다가 대다수의 배경색이 완전한 검정(<code>#000000</code>)인지라 쓰기 꺼려진다.</p>
    </td>
  </tr>
  <tr>
    <td style="width: 33.3333%; text-align: center;">
      <a href="https://xdaforums.com/t/3996369/" target="_blank" rel="noopener">crDroid</a>
    </td>
    <td style="width: 33.3333%; text-align: center;">Pie(9.0)</td>
    <td style="width: 33.3333%; text-align: center;">???</td>
  </tr>
  <tr>
    <td style="width: 99.9999%; text-align: left;" colspan="3">
      <p>실제로 써보지 않았지만, G955N 지원 언급이 없는 것으로 보아 이 커스텀 롬도 통신이 안될 것이라 생각한다.</p>
      <p>안드로이드 10도 아닌데 보안 폴더도 없고 AOD도 없기 때문에 쓸 이유가 없다 생각해 쓰지 않았다.</p>
    </td>
  </tr>
  <tr>
    <td style="width: 33.3333%; text-align: center;">
      <a href="https://xdaforums.com/t/4083251/" target="_blank" rel="noopener">Evolution X</a>
    </td>
    <td style="width: 33.3333%; text-align: center;">Android 10 (10.0)</td>
    <td style="width: 33.3333%; text-align: center;">???</td>
  </tr>
  <tr>
    <td style="width: 33.3333%; text-align: left;" colspan="3">
      <p>최근에 발견한 커스텀 롬이다. G955N을 지원하는지에 대해서는 명시가 안 되어 있다만, Lineage OS를 시도해 보는 것보다는 이걸 시도해 보는 게 더 낫지 않을까 하는 생각 중이다. 통신만 된다면...!</p>
      <p>&nbsp;</p>
      <p>추가: 해보았는데 통신이 매우 잘 된다. Ambient Display가 AOD를 대체할 수 있을 것이라 기대했는데, Ambient Display가 켜지지 않아서 <a href="https://play.google.com/store/apps/details?id=com.tomer.alwayson" target="_blank" rel="noopener">별도의 앱</a>을 구매해서 AOD를 대체해야 했다. 해당 앱의 배터리 소모량은 좀 많다. 저 앱이 없을 때는 배터리 소모가 그렇게 크지 않다고 생각했는데 저 앱을 쓰니까 배터리 소모량이 확 늘어났다. 그래서 '다시 순정롬으로 가야 하나'하는 한심한 생각까지 드는 중이다.</p>
    </td>
  </tr>
</table>
</div>

어디선가 AOSP 계열의 커스텀 롬은 오딘에서 CP 혹은 BL 부분을 다시 순정 펌웨어의 것으로 플래싱 하면 다시 통신이 작동한다는 이야기를 들은 것 같지만, 직접 시도해 보지는 않았다.

AOSP 계열의 커스텀 롬은 AOD 기능이 없다는 점을 빼면 전반적으로 훌륭하다. 제일 큰 장점은 가볍다는 것이다. 모자란 기능은 서드-파티 앱으로 어느 정도 해결이 가능하니까.

***

커스텀 커널도 있긴 한데, 별로 시도해 보지 않았다.

정확히는 한 번 시도를 해보았지만, 그 커스텀 커널이 내가 설치한 커스텀 롬과 충돌을 일으켜 사용을 중지했다.

* [A2N Kernel](https://xdaforums.com/t/3875640/)  
  G955N을 지원하는 것을 확인했다.  
  하지만 다운로드 항목에 'Android 8.X'와 'Android 9.X' 항목밖에 없어 '그러면 안드로이드 10은 지원하지 않는 건가?'라는 생각이 들게 한다.  
  커널 컨트롤 앱이 존재하지만, 모든 기능을 이용하려면 별도로 추가기능을 구매해야 한다. 마음에 들지 않는다.
* [RZ Kernel](https://xdaforums.com/t/3893139/)  
  커스텀 커널을 쓴다면 이 커널을 쓸 것 같다.  
  G955N을 지원하고, 내려받을 때도 삼성 펌웨어 기반이냐 Lineage OS 기반이냐에 따라 나눠서 내려받도록 안내하고 있다.  
  지원하는 안드로이드 버전도 8부터 10까지이니, 지원 범위도 여유롭다.

***

'안드로이드 키친'이라는 종류의 프로그램이 있다. Lineage OS 혹은 삼성 펌웨어를 개조할 수 있도록 도와주는 프로그램이다.

'안드로이드 키친'이 처음 나왔을 때에는 모든 것이 무료였다. 하지만 지금 볼 수 있는 안드로이드 키친은 전부 유료 버전이 따로 있다. 무료 버전은 가장 기본적인 기능만 풀어둔 채, '모든 기능을 쓰고 싶다면 돈을 내세요'라고 말한다.

이런 식의 변화에 대해 무조건 반대하는 것은 아니다. 개발자도 사람이니 먹고살아야 하지 않겠는가. 다만 기능을 제한할 게 아니라 차라리 사용 시간을 제한했으면 더 좋았을 것 같다고 생각한다.

&nbsp;

이런 프로그램의 '구매'는 엄연히 말해, 구매가 아니다. 페이팔 등을 통해 제작자에게 직접 '기부' 한 후, 그 보상으로 라이선스 키를 받는 방식이기 때문이다. 따라서 '14일 내 환불'은 물론이요, 프로그램에 문제가 생겨도 환불은 절대로 불가능하다. 개발자가 돈만 먹고 튈 수도 있고.

구글 플레이 스토어나 애플 앱스토어에 올라온 Freemium 앱들은 사용자와 개발자 사이에 슈퍼 갑인 구글과 애플이 껴있기 때문에, 이들이 제시한 약관에 의해 사용자는 환불할 권리를 보장받는다. 하지만 이런 식의 '기부'를 통한 구매는 개발자가 '환불이요? 싫은데요? 어쩌라고요?'라고 해도 할 수 있는 일이 별로 없다.

미리 무료 버전으로 충분히 시험해 보면 되지 않느냐고 할 수 있겠지만, 무료 버전의 업데이트는 방치한 채, 유료 버전만 업데이트하는 경우도 많다.

차라리 가격이라도 싸다면 그냥 돈을 버린 셈 칠 수 있을 것이다. 하지만 제일 싼 라이선스가 20달러나 하더라. 세상에, 20달러라고? 게임 하나 사는 데에도 손을 부들부들 떨어야 하는 내게 20달러는 굉장히 큰돈이다.

이래서 난 프로그램의 유료화가 싫다.

&nbsp;

내가 살펴본 안드로이드 키친은 다음과 같다. 안드로이드 키친 개발도 옛날 같지 않다...

* [Classy Kitchen](https://xdaforums.com/t/3862584/)  
  지금까지 살펴본 안드로이드 키친 중 이게 그나마 제일 사용하기 편한 것 같다.  
  물론 돈을 내지 못하면 쓰지 못하는 기능이 있지만, 꼭 필요한 기능이 아니기 때문에 괜찮다.  
  다만 De-Knox와 De-Bloat 기능에서 삭제되는 앱이 너무 적다. 이건 그만큼 해외 펌웨어에는 쓸데없는 앱이 별로 들어가 있지 않다는 것으로 해석해도 좋겠지.
* [S.U.R](https://xdaforums.com/t/4048291/)  
  이건 안드로이드 키친이라기보다는 펌웨어 언팩 및 리팩 도구라고 해야 한다.
* [SuperR's Kitchen](https://xdaforums.com/f/6337/)  
  기능은 굉장히 좋아 보인다. 하지만 업데이트와 관련해서는 눈살이 찌푸려진다.  
  원래는 리눅스 전용의 완전 무료 도구였지만, 해당 도구의 업데이트를 완전 중단하고, 윈도나 맥에서도 사용할 수 있는 버전을 만든 후, 반드시 '구매'를 해야만 다운로드할 수 있도록 만들어 두었다. 한참 전에 업데이트가 끊겨 제대로 사용할 수 없는 도구를 체험판이랍시고 내놓으니 '내가 이 지랄까지 하며 커롬질을 해야 하나'라는 생각까지 들더라.  
  하지만 20달러라는 금액을 자신 있게 제시할 만큼 기능이 다양하고 강력하긴 하다. 기능 면에 있어서는 다른 모든 키친을 압도하는 것으로 보인다.

***

Knox 카운터가 깨지면 삼성 펌웨어에 제공되는 많은 기본 앱의 기능을 사용할 수 없게 된다. '보안 폴더', '삼성 헬스', '삼성 페이', '삼성 패스' 등이 그 예이다.

하지만 그 기능의 사용에 있어 Knox 카운터의 무결성이 필요한 것이 아닌 앱이 있다. 보안 폴더의 경우, 그 근간은 안드로이드에서 기본적으로 제공하는 기능이기 때문에 Knox 카운터를 확인하는 부분만 개조하면 Knox 카운터가 깨져도 사용할 수 있다.

이를 대신해주는 프로그램이 [Smali Patcher](https://xdaforums.com/t/3680053/)이다.

그런데 이걸 썼더니 카메라가 제대로 작동하지 않거나, 보안 폴더가 잠기지 않고 보안 폴더의 암호도 수정할 수 없는 등의 문제가 발생했다.

난 이게 문제의 원인일 것이라 전혀 생각하지 못하고 몇 번이고 오딘을 통해 커스텀 롬을 플래싱 했다. 게다가 Magisk 모듈이라 모듈을 비활성화하면 다시 수정 전 시스템 파일로 돌아갈 줄 알았는데, 모듈을 비활성화해도 시스템 파일이 수정된 채 그대로 남아있었다.

앞으로 이 프로그램은 절대로 쓰지 않기로 했다.

***

시간만 여유롭다면 내가 직접 G955N 펌웨어를 개조해 커스텀 롬을 만들어 배포할 텐데, 그러려면 일단 SamFirm으로 최신 보안 패치가 적용된 펌웨어를 받는 방법을 알아야 한다.

SamFirm으로 최신 펌웨어를 받으면 보안 패치가 1월 버전이지만, 정식 펌웨어를 정상적으로 설치했을 경우에는 보안 패치가 4월 버전이다.

***

지금은 hadesROM에 순정 펌웨어의 KT OMC와 Accessibility를 추가해 쓰고 있다. 여전히 MMS 문제는 해결하지 못했지만, 다른 커스텀 롬을 찾기에는 너무 지쳤다.

4월 보안 패치가 적용된 펌웨어를 구했기 때문에 시간만 남아돈다면 이걸 기반으로 내가 직접 커스텀 롬을 만들 수도 있을 것이다.

PS. 나중에 또다시 4월 보안 패치가 적용된 펌웨어를 내려받을 때 이걸 사용할 것.

> G955NKSU4DTD1 / G955NOKR4DTD1 / G955NKOU4DTC2
{.block-quote}
