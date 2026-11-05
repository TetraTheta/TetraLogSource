---
title: "이제 커스텀 롬은 선택지가 크게 좁혀지겠네"
slug: no-more-aosp-for-korean-galaxy
date: 2026-11-05T15:41:08+09:00
series:
#  - 
categories:
  - 잡담
tags:
#  - 
images:
#  - 001.webp
---

# 고장

여태껏 잘 사용하던 스마트폰이 갑자기 이런 메시지를 내보내기 시작했다.

{{< gallery/image src="critical_error" >}}

일시적 오류라고 생각해서 재부팅을 몇 번이고 해 보았지만, 저 메시지는 도통 사라질 생각을 하지 않았다.

ChatGPT에게 logcat과 sysdump 등의 다양한 자료 등을 제공하며 물어본 결과, 단순한 오류가 아니라 시스템이 정말로 어디선가 손상되어 발생한 오류일 확률이 매우 높다는 대답을 해왔다.
그러고 보면... 최근 한 달 전부터 스마트폰이 재부팅 도중 '삼성 로고'에서 도통 넘어갈 생각을 하지 않아, 강제로 재부팅을 해야 했던 경우가 유독 많았지...

이런 일이 발생할 가능성이 아예 없는 건 아니었다. 지금 쓰고 있는 OS는 삼성이 출시한 마지막 순정 펌웨어를 임의로 뜯어다 Debloat 처리와 각종 트윅을 적용한 것이기 때문이다. 내가 뭔가 중요한 걸 실수로 삭제했을 수도 있고, 그게 버티다 못해 지금 갑자기 터진 것일 수도 있겠지.

그래서 속 시원하게 싹 다 밀고 새 커스텀 롬을 설치하기로 했다. 순정 펌웨어로 다시 돌아가기에는 Knox 카운터 손상으로 인해 쓸 수 없는 기능과 앱이 시스템 영역과 RAM에 상주하는 꼴을 도저히 참을 수 없었으니까.

# 커스텀 롬 후보 찾기

ChatGPT에게 물어보았다. 내 스마트폰에 쓰기 좋은 커스텀 롬이 뭐가 있을까?
ChatGPT는 다음 세 커스텀 롬을 추천해 주었다.

1. [iodéOS](https://iode.tech/iodeos/): 공식 지원 기기에 등재되어 있다고 한다. VoLTE가 중요하다면 이걸 쓰라고 한다.
2. [Project-Matrixx](https://xdaforums.com/t/4657176): 최근 프로젝트 전체가 보관 처리되었다고 한다.
3. [crDroid 12](https://crdroid.net/d2x/12): 커스터마이징의 여지가 가장 넓다고 한다.

하지만 찾아보니, 아니나 다를까, 사실이 아닌 정보도 포함되어 있었다.
iodéOS의 공식 페이지를 찾아가 보니, 내 기기에 대한 다운로드 링크가 아예 제거되어 있었다. 그 옆에는 '공식 인스톨러 미지원', '부트로더 잠금 불가능', 'VoLTE/VoWiFi 미지원'이라는 딱지도 붙어 있었다.
나머지는 그럭저럭 맞는 말이었다. Project-Matrixx는 올해 9월에 프로젝트 전체가 보관 처리되었다고 하고, crDroid는 커스터마이징 영역이 굉장히 넓은 것도 맞으니까.

그래서 crDroid 12(Android 16)을 써보기로 했다.

# 문제 발생

한 시간 정도는 스마트폰에 설치된 앱에서 백업 파일을 생성하는 데 썼고, 나머지 한 시간은 crDroid 설치에 필요한 파일을 다운로드하고 관련 지침을 읽는 데 썼다.
crDroid는 널리 쓰이는 TWRP가 아닌 자체 제작 리커버리를 쓰기 때문에, 'ZIP 파일 하나 플래싱 하면 끝나는' 일반적인 커스텀 롬보다는 설치 과정이 복잡했다.

crDroid 설치가 끝나고 댄디한 Android 16의 모습에 감탄하며 필요한 앱을 설치하고 초기 설정에 들어갔다.
설정을 백업한 앱이 있기는 했지만, 사용하던 앱의 일부분에 불과했기 때문에, 앱을 하나하나 열어 설정을 하는 데에 수 시간이 들었다.

카카오톡을 설정하려는데, 문자메시지가 오지 않는다. crDroid의 XDA 포스트에 적힌 'Known Issue: VoLTE'가 떠올라 급히 집 전화로 내 스마트폰에 전화를 걸어보았지만, 전원이 꺼져 있다는 자동 응답 메시지만이 수화기 너머에서 들려올 뿐이었다.

몇 시간 동안 crDroid를 설치하기 위해 준비하고 실행한 모든 것이 전부 물거품이 된 순간이었다.
crDroid를 설치하면 뭐 하니. 전화랑 문자가 안 되는 깡통 스마트폰이 되어버렸는데!

# 원인 확인

ChatGPT에게 다시 한번 물어보았다.
`*#*#4636#*#*`를 입력해서 나온 화면에서 IMS Service Status를 선택해 확인해 보니, VoLTE가 아예 붙지 않았다고 한다. 찾아보니, 내가 쓰는 스마트폰은 AOSP/LineageOS 기반 OS 전체에서 VoLTE가 제대로 작동하지 않는다고 한다.

[pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch) 같은 사례가 있어, 이걸 사용하면 되지 않을까 생각했지만, ChatGPT가 말하길 픽셀은 단순히 구글이 VoLTE를 잠가놓은 것을 푼 것이지만, AOSP/LineageOS에는 삼성 독점 IMS 바이너리/라이브러리가 없어서 해당 패치를 사용해도 여전히 VoLTE가 작동하지 않을 거라고 한다.

&nbsp;

iodéOS, Project-Matrixx, crDroid 전부 AOSP/LineageOS에 기반한 커스텀 롬이다. 여기에 기반한 모든 커스텀 롬은 VoLTE가 안 되는 상황이기에, 내가 사용할 수 있는 유일한 후보군은 '삼성 정식 펌웨어에 기반한 커스텀 롬'밖에 없는 셈이다.

# 대안 적용

가장 좋은 건 한국향 갤럭시 노트 10+ 5G(`d2xks`) 펌웨어에 기반한 커스텀 롬일 것이다. 하지만 이런 부류의 커스텀 롬은 '후속 기종 펌웨어 포팅 롬'에 비해 매력이 떨어지는 탓에, 관련 프로젝트가 전부 다 죽었다. 당장 내가 순정 펌웨어를 직접 뜯어서 수정한 이유가 바로 그것 때문이기도 했고.

XDA를 뒤진 끝에 내가 찾은 대안은 [EternityROM](https://xdaforums.com/t/4670331)이었다.

- `d2xks`를 정확히 지원함
- 갤럭시 S 22 울트라 펌웨어를 포팅한 커스텀 롬: 삼성 펌웨어 기반이므로, VoLTE가 정상 작동함
- Debloated, Unblocked, Deknoxed: 작동하지 않거나 쓸데없는 것이 줄어들었다
- KernelSU Next 탑재 커널: KernelSU Next Manager만 설치하면 루팅이 된다!

다만, 다음 항목은 작동하지 않는다고 한다.

- 얼굴로 잠금 해제
- 에어커맨드
- 문서 스캔
- 인물 사진 모드(Back Portrait Mode)
- Hi Bixby와 OK Google을 동시 활성화할 때의 마이크

작동하지 않는 기능 중 '얼굴로 잠금 해제'를 제외한 나머지는 나 역시 쓰지 않는 기능이기에, '얼굴로 잠금 해제'만 포기한다면 꽤 괜찮은 선택지가 되는 것이다.

EternityROM은 crDroid보다 한 발짝 더 나아가, 시스템 파티션 구조까지 수정하는 롬이기 때문에, 설치 방법이 많이 복잡하다.

1. 공식 배포처에서 다음 파일을 다운로드한다.
   - `Odin/EternityROM_v3.0_TWRP_OdinPack_N976N.tar`
   - `ROMs/v5.5/EternityROM_v5.5_d2xks.zip`: 외장 SD 카드에 옮겨두기
     v5.0의 배터리 소모량이 더 적다는 이야기가 있지만, 일단 v5.5를 써보기로 했다.
   - `Repartition/Exynos9825_Cleaner_v3.zip`
   - `Repartition/Exynos9825_Repartition_v3.zip`
2. [SamFirm Reborn](https://github.com/ivanmeler/SamFirm_Reborn)으로 최신 순정 펌웨어를 다운로드한다.
   - `N976NKSU2HWH5/N976NOKR2HWH5/N976NKOU2HWH3/N976NKSU2HWH5`
3. Odin으로 순정 펌웨어를 BL, AP, CP, CSC, USERDATA 등 모든 영역에 플래싱 한다.
   이렇게 '초기 상태'로 만들지 않으면 이후 어디가 어떻게 꼬일지 아무도 모른다.
4. 스마트폰 재부팅 후, 다시 Odin으로 `EternityROM_v3.0_TWRP_OdinPack_N976N.tar`를 플래싱 한다.
   해당 파일은 아무 자리에 넣어도 된다.
5. 전원이 꺼진 상태에서 USB-C 케이블을 연결하고 '볼륨 증가 + 전원' 버튼을 TWRP 화면이 나올 때까지 누른다.
   이 TWRP는 공식 TWRP가 아닌, 커스텀 빌드된 TWRP이다.
   화면이 매우 어둡거나 주황색이더라도 놀라지 말고 계속 진행하면 된다. 재부팅하면 다시 돌아오니까.
6. `Exynos9825_Repartition_v3.zip`을 플래싱 한다.
   이때, 자동으로 TWRP로의 재부팅이 일어난다.
7. `Exynos9825_Cleaner_v3.zip`을 플래싱 한다.
   이때, 자동으로 TWRP로의 재부팅이 일어난다.
8. `EternityROM_v5.5_d2xks.zip`을 플래싱 한다.
9. 끝!

`Exynos9825_Repartition_v3.zip`이나 `Exynos9825_Cleaner_v3.zip`은 ADB Sideload를 해도 상관없지만, `EternityROM_v5.5_d2xks.zip`는 반드시 외장 SD 카드에 옮겨두어야 한다. 용량이 너무 커서, 중간에 연결이 끊긴다면 처음부터 다시 해야 한다.

# 후속 조치

## KernelSU Next Manager

설치가 다 끝나고 나니, KernelSU Next Manager가 기본적으로 설치가 되어 있었다.
아무래도 KernelSU Next(KSUN)는 매니저 버전과 빌드 버전이 동일해야 문제가 없는 건지, KernelSU Next의 GitHub Release에서 최신 버전의 매니저를 다운로드해 설치했더니 KSUN이 인식이 안 되었다.
급한 대로 [v1.1.1 HOTFIX](https://github.com/KernelSU-Next/KernelSU-Next/releases/tag/v1.1.1)를 받아 설치했지만, 여전히 빌드 번호가 미묘하게 맞지 않는다.

- KSUN 버전: `12823`
- 매니저 버전: `12851`

[v1.1.0](https://github.com/KernelSU-Next/KernelSU-Next/releases/tag/v1.1.0) 매니저를 설치해야 하는 건가 싶은데... '핫픽스'라고 하니 왠지 저 버전을 쓰면 안 될 것 같아서 일단은 그대로 쓰고 있다.

## Play Integrity

간혹 Play Integrity를 깐깐하게 따지는 앱이 있다.

보통 이런 건 PlayIntegrityFix나 TrickyStore 같은 KSUN 모듈로 해결하는 경우가 많은데, EternityROM은 반대로 이렇게 말한다.

> In order to get DEVICE and STRONG integrity you'll have to remove PIF, TrickyStore, etc. Then clear gms services and play store data. Reboot. If you still get no integrity wait one day.

그런 모듈 설치하지 말고, 그냥 GMS 서비스랑 플레이 스토어 데이터를 날린 후 하루 정도를 기다리라고 한다.

## Bootloop 방지

Google Play System Update의 업데이트된 APEX 모듈이 시스템 모듈과 호환되지 않으면 '무한 부팅(Bootloop)'에 걸린다고 한다.
이건 따로 막을 수도 없어서, KSUN 모듈로 해결을 봐야 한다.

[disable-gpsu-bootloops](https://github.com/dyrok/disable-gpsu-bootloops)를 다운로드해 KSUN 매니저에서 설치했다.
이 모듈은 부팅 과정에서 `apexd`가 실행되기 전 `/data/apex/sessions/*`를 삭제해 업데이트된 APEX 모듈이 사용되는 걸 막고, 부팅 후에는 `com.google.android.modulemetadata` 앱을 비활성화해 Google Play가 APEX 모듈 업데이트를 받는 걸 원천 차단한다.

... 이런 문제는 결국 최신 스마트폰을 사는 것 밖에 해결해주지 못하겠지...

## 얼굴로 잠금 해제 복원

이건 나도 아직 시도해보진 않았다.

Xposed와 Zygisk를 필요로 하는 [KSUN 모듈](https://xdaforums.com/t/4670331/post-90614715)이 있는데, 이걸 설치하면 나타나는 'Face Recognition' 앱을 실행해 설정하면 된다고 한다.

***

# 결론

AOSP/LineageOS에는 삼성 독점 IMS 바이너리/라이브러리가 없어 VoLTE가 작동하지 않기 때문에, AOSP/LineageOS 기반 커스텀 롬은 앞으로 삼성 스마트폰에서 사용하기 어려울 것 같다.
AOSP/LineageOS가 One UI보다 훨씬 가벼워서 좋아했는데, 이젠 무조건 One UI 고정이네...
