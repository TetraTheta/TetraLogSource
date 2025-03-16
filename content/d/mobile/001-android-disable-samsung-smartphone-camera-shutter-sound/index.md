---
title: "[Android] 삼성 스마트폰 카메라 촬영음 없애기"
slug: android-disable-samsung-smartphone-camera-shutter-sound
date: 2025-03-16T17:36:50+09:00
series:
#  - 
categories:
  - PIVOX
tags:
#  - 
images:
  - logo.webp
---

스마트 기기에서 카메라 기능을 이용할 때, 촬영음이 나오도록 (사실상) 강제하는 국가는 대한민국과 일본이 유이합니다.

대한민국의 경우, 이를 규정한 것은 법령(법률, 법규명령 등)이 아닙니다. 대한민국의 정보통신 단체표준을 제정하는 *민간 기구*인 '한국정보통신기술협회(TTA)'가 만든, [TTAK.KO-06.0063](https://committee.tta.or.kr/data/standard_view.jsp?rn1=Y&standard_no=TTAK.KO-06.0063&pk_num=TTAK.KO-06.0063%2FR2&nowSu=1&rn=1)에 기반하고 있죠. 여기에 참여한 휴대전화 제조사, 통신사 등이 *자율적으로* 해당 규제를 따르고 있는 겁니다.

즉, 이 표준이 개정되거나 폐지되려면 여기에 참여한 기관과 회사가 적극적으로 나서야 한다는 이야기죠.
그런데 그걸 언제까지 기다려야 하나요?

다행스럽게도, 아이폰과 달리, 삼성 스마트폰은 시스템 변수를 수정해 카메라 촬영음을 끌 수 있습니다.

# 준비물{id="requirements"}

* 삼성 안드로이드 스마트폰
* PC

# 촬영음 비활성화 과정{id="steps"}

## ADB 다운로드{id="download-adb"}

ADB(안드로이드 디버그 브리지)는 안드로이드 디버깅을 위해 사용되는 명령줄 도구입니다. 어떤 방법을 사용하든 ADB가 필요하므로, ADB를 포함한 [SDK 플랫폼 도구를 다운로드](https://developer.android.com/tools/releases/platform-tools)합니다.

아래 링크를 클릭하는 것은 Android SDK 플랫폼 도구 이용약관에 동의함을 의미합니다. 자세한 내용은 위 링크를 참조하세요.

* [Windows 용 SDK 플랫폼 도구](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
* [Mac 용 SDK 플랫폼 도구](https://dl.google.com/android/repository/platform-tools-latest-darwin.zip)
* [Linux 용 SDK 플랫폼 도구](https://dl.google.com/android/repository/platform-tools-latest-linux.zip)

다운로드한 SDK 플랫폼 도구를 적당한 위치에 압축 해제 하세요. 이 글에서는 `C:\ADB` 폴더를 예시로 들겠습니다. `adb.exe`의 경로가 `C:\ADB\adb.exe`가 되도록 압축 파일을 압축 해제하면 됩니다.

## 스마트폰 연결{id="connect-smartphone"}

USB 디버깅을 활성화한 스마트폰을 PC에 연결합니다. 연결 테스트를 위해 명령 프롬프트를 열고 다음과 같이 입력해 보세요.

```plaintext{linenos=false}
C:\ADB>adb shell
```

다음과 같이 ADB 셸이 나타나면 정상적으로 연결된 겁니다.

```plaintext{linenos=false}
C:\ADB>adb shell
* daemon not running; starting now at tcp:5037
* daemon started successfully
codename:/ $
```

ADB 셸을 나가는 방법은 `exit`을 입력하고 <kbd>ENTER</kbd> 키를 누르면 됩니다.

```plaintext{linenos=false}
codename:/ $ exit

C:\ADB>
```

## ADB를 이용한 설정{id="using-adb"}

명령 프롬프트에 다음과 같이 입력하세요.

```plaintext{linenos=false}
C:\ADB>adb shell settings put system csc_pref_camera_forced_shuttersound_key 0 && echo done
```

명령이 제대로 수행되었다면 다음과 같이 `done`이 출력될 것입니다.

```plaintext{linenos=false}
C:\ADB>adb shell settings put system csc_pref_camera_forced_shuttersound_key 0 && echo done
done

C:\ADB>
```

ADB 셸에서의 작업 역시 대동소이합니다.

```plaintext{linenos=false}
C:\ADB>adb shell
codename:/ $ settings put system csc_pref_camera_forced_shuttersound_key 0 && echo done
done
codename:/ $
```

> [!WARNING] 주의 사항
> 소프트웨어 업데이트는 위 변경 사항을 초기화합니다.
> 소프트웨어 업데이트를 완료한 후, 위 명령어를 다시 한번 실행해 주세요.
