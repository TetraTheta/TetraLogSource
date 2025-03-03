---
title: "요새 Windows가 왜 이럴까"
slug: disgusting-windows-11
date: 2023-06-18T10:00:03+09:00
series:
#  - 
categories:
  - 잡담
tags:
#  - 
images:
#  - 001.webp
---

나도 안다. 여기에 이런 말을 한다고 해서 뭔가가 바뀌지 않을 거란 것 정도는.

하지만 이렇게라도 털어놓지 않으면 화가 나고 답답해 죽을 것만 같다.

***

최근 들어 Windows에 정이 떨어져 가고 있다. 정확히는 Windows 11에 정이 떨어지고 있다.

Windows 11에서 마음에 들지 않는 것이 한둘이 아니다.

# 기본 앱 강제{id="default-app-enforcing"}

Windows 10까지는 기본 앱을 설정할 때 큰 문제가 없었다.

기껏해야 Windows와 함께 딸려오는 Edge 브라우저의 사용을 권장하거나, 다른 웹 브라우저로 전환할 때 '그냥 Edge 쓰면 안 돼요?'라고 묻는 창을 추가로 띄우는 것 정도였다.

그런데 Windows 11은 사용자가 기본 앱을 바꾸기 힘들게 변했다.

&nbsp;

당신이 여러 확장자에 대한 기본 연결 프로그램을 특정 프로그램으로 설정하고 싶다고 해보자.

Windows 10에서는 그냥 설정 앱을 연 후, 기본 앱 설정을 열어 그 프로그램을 선택한 후, 클릭 몇 번만으로 당신이 원하는 프로그램을 여러 확장자에 대한 기본 연결 프로그램으로 설정할 수 있었다.

하지만 Windows 11에서는 아니다. Windows 11에서는 당신이 원하는 프로그램을 선택한 후, 그 프로그램이 지원하는 확장자에 대한 기본 연결 프로그램을 하나하나 변경해야 한다. 프로그램이 여러 확장자를 지원한다면, 그만큼 필요한 클릭 횟수도 늘어난다.

&nbsp;

물론 대부분의 프로그램은 자체적으로 여러 확장자에 대한 연결을 설정할 수 있다. 하지만 Windows 11에서는 프로그램에서 기본 연결 프로그램을 바꿀 수 없는 확장자가 많이 있다.

당장 Windows 11의 설정을 열고 기본 앱 설정에 들어가 BMP, JPG, PDF, PNG 등의 유명한 확장자를 검색해 보라. 아마 아무런 결과가 나오지 않을 것이다.

특정 확장자의 경우, MS가 제공하는 기본 앱으로의 연결이 강제되어 있으며, 이를 사용자가 변경할 수 없도록 되어 있다. 사용자가 수동으로 그 확장자에 연결된 기본 프로그램을 변경하고자 해도, 검색 결과에 나타나지 않으므로 변경이 불가능하다.

## 해결책: SetUserFTA{id="setuserfta"}

이 문제를 해결하려면 [SetUserFTA](https://setuserfta.com/)라는 외부 프로그램을 써야 한다.
[블로그 글](https://kolbi.cz/blog/2017/10/25/setuserfta-userchoice-hash-defeated-set-file-type-associations-per-user/), [다운로드 링크](https://setuserfta.com/SetUserFTA.zip)

<link-preview url="https://setuserfta.com/" title="SetUserFTA – THE file type association utility" desc="Set file type associations or default browser via command line or script" image="https://setuserfta.com/wp-content/uploads/2024/05/cropped-SetUserFTA-512x512-1-270x270.png"></link-preview>

SetUserFTA는 개별 사용자(User-level)에 대한 기본 연결 프로그램을 변경해 준다. 그러니까 이건 관리자 권한으로 실행하면 안 되는 프로그램이다. 만약 전체 컴퓨터(Machine-level)에 대한 기본 연결 프로그램을 변경하고 싶다면 [DISM을 이용하는 방법](https://learn.microsoft.com/ko-kr/archive/blogs/windowsinternals/windows-10-how-to-configure-file-associations-for-it-pros#how-to-configure-file-association-in-windows-10)밖에 없다.

SetUserFTA는 다음 네 가지 방법으로 사용할 수 있다.

* 특정 확장자/프로토콜의 기본 연결 프로그램 설정
  `SetUserFTA.exe <.확장자/프로토콜> <ProgId> [그룹명]`
* 설정 파일 일괄 적용
  `SetUserFTA.exe <설정 파일>`
* 전체 확장자/프로토콜 연결 확인
  `SetUserFTA.exe get`
  `SetUserFTA.exe get > <텍스트 파일 저장 경로>`
* 특정 확장자/프로토콜 연결 해제
  `SetUserFTA.exe del <.확장자/프로토콜>`

설정 파일은 대충 이런 식으로 확장자와 ProgId를 한 줄에 하나씩 적는 식으로 되어 있다.

```plaintext
.pdf, AcroExch.Document.DC, GRP_Adobe_Reader
.txt, Wordpad.Document.1
.docx, Word.Document.12
```

만약 새 프로그램을 설치할 때마다 연결 프로그램을 묻는 창이 나타나는 게 싫다면, 다음 명령어를 **관리자 권한**으로 실행하면 된다.

```batch
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Explorer" /v "NoNewAppAlert" /t REG_DWORD /d 1 /f
```

아직 프로그램이 설치되지 않았거나 해당 확장자가 윈도에 발견되지 않았을 경우, 관련 레지스트리 키가 생성되지 않는다. 이때에는 SetUserFTA를 사용하기 전에 `HKCU\SOFTWARE\Classes`에 관련 레지스트리 키를 먼저 만들어야 한다.

# 답답한 다운로드 속도{id="very-slow-download-speed"}

Windows의 업데이트 서버는 Azure를 쓰고 있다고 들었는데, 전혀 아닌 것 같다. 너무 느리거든.

128MB짜리 업데이트를 하나 받는데 30분이 지나도 10%를 채 받지 못하거나, MS 스토어에서 앱 업데이트를 받는데 10분이 지나도록 단 한 개의 앱도 다운로드를 시작조차 하지 못하거나 하는 상황이 너무 빈번하게 일어난다.

&nbsp;

가뜩이나 느린 다운로드 속도는 누적 업데이트에서 더욱 빛을 발하게 된다.

누적 업데이트는 그 목적만 보면 참 좋아 보인다. 언제 Windows를 업데이트했는지에 관계없이, 최신 누적 업데이트만 받아 설치하면 Windows가 최신 버전이 된다. 정말 멋지지 않은가?

하지만 여기에는 용량이라는 함정이 숨어있다. Windows에 필요한 프로그램을 이것저것 설치해 보아도 C 드라이브 사용량이 30GB가 넘을까 말까 하는 상황에서, 누적 업데이트 하나의 용량이 무려 128GB나 된다.

바로 이것 때문에 누적 업데이트를 받을 때 그렇게 시간이 오래 걸렸던 것이다. 우리가 여태 Windows에 설치한 업데이트를 다시 받지 않도록, 기존 업데이트 내용과 누적 업데이트의 내용을 하나하나 비교하는 과정 때문에 업데이트 설치가 그토록 느렸던 것이다.

그렇다고 해서 최종적으로 받는 누적 업데이트의 용량이 적은 것도 아니다.

&nbsp;

물론 MS 역시 이를 모르는 건 아니라, MSDN 구독자에 한해 매달 말 모든 누적 업데이트가 미리 통합된 Windows 설치 ISO를 제공한다. 가끔 누적 업데이트가 많이 쌓였다고 생각되면 미디어 생성 도구나 공식 다운로드 사이트에서 제공하는 Windows 설치 ISO도 최신으로 업데이트하고 말이다.

하지만 MSDN 구독료는 절대로 싸지 않고, MS가 공식 사이트에서 배포하는 Windows 설치 ISO를 최신으로 업데이트하는 주기는 매우 길다.

&nbsp;

이것 때문에 [예약된 공간](https://techcommunity.microsoft.com/t5/storage-at-microsoft/windows-10-and-reserved-storage/ba-p/428327)을 다시 활성화해야 하나 고민 중이다. 쓸데없이 7GB나 되는 용량을 차지하는 게 마음에 들지 않아 꺼두는 기능인데, 혹시 이걸 다시 켜면 업데이트 속도가 빨라질까 하는 생각이 들어서이다.

# 사용자는 실험쥐이다{id="user-is-lab-rat"}

Windows 업데이트 관련 소식을 듣다 보면, 잊을만했다 싶을 때 이런 이야기가 튀어나온다.

> KB#######를 설치하면 시스템의 성능이 저하됩니다
{.bq}

> KB#######를 설치하면 \[어떤 프로그램\]을 실행할 수 없습니다
{.bq}

MS는 업데이트를 배포할 때 과연 충분한 테스트를 거치고 배포하는 것인지 의심될 정도이다. 이 정도면 Windows라는 소프트웨어를 비싼 돈을 주고 산 사람들을 대상으로 베타 테스트를 하는 게 아닌가?

Home 에디션은 업데이트를 미룰 수 없으며, Pro 에디션은 업데이트를 최대 5주까지 미룰 수 있다. 하지만 이조차도 MS가 적용이 시급하다고 생각하는 업데이트는 절대 미룰 수 없다.

&nbsp;

바로 이것 때문에 사람들이 기업용 LTSC Windows를 구하는 것인지도 모른다.

LTSC Windows는 의료용 기기나 ATM 등 사용에 있어 오류가 발생하면 안 되는 기기에 쓰일 목적으로 만들어졌기 때문에, LTSC 에디션에 제공되는 업데이트는 안정성이 확실히 보장된 업데이트이다. 업데이트로 인해 문제가 발생할 확률이 극도로 낮은 것이다.

다만 LTSC Windows는 Home 에디션이나 Pro 에디션에 비해 기능 업데이트가 없다시피 하다. 특수한 장비에서 쓰일 목적으로 만들었으니, 새로운 기능을 추가할 이유가 없기 때문이다.

지금 기대할 수 있는 건 Windows 11에 기반한 LTSC인데, 이 녀석은 2024년 하반기에나 나올 예정이라고 한다. 아직도 1년 넘게 남은 것이다.

&nbsp;

따지고 보면 이번에 내 속을 썩인 것도 바로 이 Windows 업데이트였다.

분명 Windows를 처음 설치한 후, `sfc /scannow`와 `dism /online /cleanup-image /restorehealth` 명령어를 실행해 시스템에 아무런 문제가 없음을 확인했지만, 최신 업데이트를 설치한 후 다시 저 두 명령어를 실행해 보니, 시스템에 `Microsoft-OneCore-DirectX-Database-FOD-Package` 패키지가 없으며 이를 복구조차 할 수 없다는 메시지를 받았다.

내가 바로 이 하나의 문제 때문에 사흘 내내 Windows를 설치했다 지웠다를 반복하고 있다. 지금도 이 글을 쓰는 내내 웹 브라우저 뒤에서 Windows 탐색기가 제멋대로 종료되었다 다시 실행되기를 반복하고 있다.

쓰레기 OS 같으니라고.

# 광고, 더 많은 광고{id="more-more-ads"}

방금 말한 내용대로, Windows는 사용자가 돈을 주고 사는 OS이다. Home 에디션은 약 20만 원, Pro 에디션은 약 30만 원이라는 거금을 주고 사야 한다.

그런데 가면 갈수록 Windows 11에 광고가 많아지고 있다.

&nbsp;

Windows를 처음 설치하고 시작 메뉴를 열면 온갖 서드-파티 기본 앱이 넘쳐난다. '디즈니+', '넷플릭스', '캔디 크러시 사가'...

잠시 후, 이 앱들이 제멋대로 다운로드되기 시작한다.

&nbsp;

이러한 서드-파티 앱 외에도 곳곳에서 MS의 광고를 확인할 수 있다.

설정 앱은 끊임없이 'Microsoft 365를 써보세요!', 'Office 365를 써보세요!'라고 광고하며, Windows의 기본 구성 요소들마저 이러한 MS의 서비스와 밀접하게 연동되도록 바뀌고 있다.

묻지도 않았는데 제멋대로 깔려 있는 OneDrive는 말할 것도 없다.

***

옛날에는 Windows 12가 나오면 이 모든 문제가 해결될 거라고 잔뜩 기대했었다. 이전 버전의 Windows에서 새 코드를 쌓아 올리는 기존 방식 대신, 아예 기초부터 새로 설계한 Windows 12가 나오면 이 모든 불편함이 해소될 거라고 말이다.

하지만 최근 MS의 행보를 볼 때, Windows 12가 나오면 이런 문제들이 해결될 것 같다는 생각이 더 이상 들지 않는다.

Windows 12는 여전히 OneDrive가 설치된 채로 설치될 것이고, 설정 앱은 끊임없이 Microsoft 365와 Office 365를 광고할 것이며, 내가 원하지 않는 쓰레기 기본 앱 역시 스토어에서 자동 설치될 것이다.

&nbsp;

그래서 그럴까, 자꾸만 Ubuntu나 Manjaro Linux 같은 다른 OS에 눈이 간다.

하지만 내가 하는 게임 중 원신과 붕괴: 스타레일은 리눅스를 전혀 지원하지 않기 때문에, 반강제로 Windows를 써야 한다.

리눅스로 저 두 게임을 돌리려는 시도가 없는 건 아니지만, 대부분 게임의 안티 치트를 강제로 비활성화한 후 게임을 실행하는 거라서 계정이 영구 정지될 위험이 매우 높다.

&nbsp;

하... Windows가 쾌적하게 바뀌는 게 더 빠를까, 아니면 미호요가 리눅스를 지원하는 게 더 빠를까?
