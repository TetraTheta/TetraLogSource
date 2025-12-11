---
title: "[Windows] Wi-Fi 프로필 내보내기/불러오기"
slug: windows-wifi-profile-import-export
date: 2024-12-25T17:27:52+09:00
series:
#  - 
categories:
  - PIVOX
tags:
  - Windows
images:
  - logo.webp
---

Wi-Fi 프로필 공유는 여러 기기를 쓰는 사람에게 있어 정말 중요한 기능입니다. 프로필 공유 기능이 없었을 때에는 모든 기기에 직접 손으로 Wi-Fi SSID와 비밀번호를 입력해야만 했으니까요.

지금은 대다수의 OS가 QR코드나 계정 연동을 통한 Wi-Fi 프로필 공유를 지원합니다. Apple 기기는 계정 연동을 통해, Android와 Windows는 QR코드를 통해 Wi-Fi 프로필을 공유할 수 있죠.

하지만 다른 OS와 달리, Windows의 경우는 조금 다릅니다. 다른 OS는 모바일 기기에서 쓰이는 걸 주목적으로 하기에, 기기에 QR코드를 스캔할 수 있는 카메라가 기본적으로 달려 있습니다. 하지만 대다수의 Windows 기기는 데스크톱, 즉 카메라가 없는 기기입니다. 이러면 QR코드를 스캔할 수 없어요. 물론 대다수의 데스크톱이 키보드를 필요로 하니, 마우스와 키보드를 이용해 직접 Wi-Fi SSID와 비밀번호를 입력하면 되긴 합니다만... 귀찮죠?

그래서 Windows에는 매번 Wi-Fi SSID와 비밀번호를 입력하기 귀찮은 사람들을 위해 명령어로 Wi-Fi 프로필을 내보내고 불러올 수 있는 기능이 있습니다.

# 프로필 저장 경로 생성

먼저 Wi-Fi 프로필을 저장하거나 불러올 폴더를 만들어야 합니다. 아무 빈 폴더를 써도 무방하나, 이 글에서는 `C:\WiFi` 폴더를 예시로 들겠습니다.

C 드라이브에 직접 `WiFi` 폴더를 만들거나, 명령 프롬프트를 열고 다음과 같이 입력합니다.

```batch
mkdir C:\WiFi
```

앞으로 모든 Wi-Fi 프로필 파일은 이 경로에 저장하고 이 경로에서 불러올 겁니다.

# 프로필 내보내기

만약 특정 Wi-Fi 프로필만 내보내고 싶다면, 현재 저장된 Wi-Fi 프로필을 확인해야 합니다.

```batch
netsh wlan show profiles
```

그러면 다음과 유사한 결과가 출력됩니다.

```plaintext
Wi-Fi 인터페이스의 프로필:

그룹 정책 프로필(읽기 전용)
---------------------------------
    <없음>

사용자 프로필
-------------
    모든 사용자 프로필 : My_WiFi_5G
    모든 사용자 프로필 : My_WiFi
```

현재 Windows 기기에 저장된 Wi-Fi 프로필은 My_WiFi_5G와 My_WiFi 둘입니다.

&nbsp;

이제 Wi-Fi 프로필을 내보낼 시간입니다. 먼저 아까 생성했던 `C:\WiFi` 경로로 이동합니다. 프로필을 내보낼 때 `folder=` 구문을 사용해도 되지만, 직접 해당 폴더로 이동해 작업하는 편이 조금 더 수월합니다.

```batch
cd /D C:\WiFi
```

이제 Wi-Fi 프로필을 내보냅니다. 이 글에서는 `My_WiFi_5G` 프로필만을 내보내겠습니다.

```batch
netsh wlan export profile key=clear name=My_WiFi_5G
```

만약 모든 Wi-Fi 프로필을 내보내고 싶다면 `name=My_WiFi_5G` 부분을 생략하면 됩니다.

```batch
netsh wlan export profile key=clear
```

Wi-Fi 프로필을 정상적으로 내보냈다면 다음과 같은 결과가 출력될 것입니다. 만약 여러 Wi-Fi 프로필을 내보냈다면 비슷한 내용의 결과가 여러 번 출력되겠죠.

```plaintext
인터페이스 프로필 "My_WiFi_5G"이(가) ".\Wi-Fi-My_WiFi_5G.xml" 파일에 성공적으로 저장되었습니다.
```

{{< collapse heading="내보낸 Wi-Fi 프로필 XML의 내용" >}}

내보낸 Wi-Fi 프로필 XML 파일의 내용이 다음과 유사하다면, Wi-Fi 프로필이 제대로 내보내진 것으로 생각할 수 있습니다.

```xml
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
  <name>My_WiFi_5G</name>
  <SSIDConfig>
    <SSID>
      <hex>D156475A3732B9245F314C</hex>
      <name>My_WiFi_5G</name>
    </SSID>
    <nonBroadcast>true</nonBroadcast>
  </SSIDConfig>
  <connectionType>ESS</connectionType>
  <connectionMode>auto</connectionMode>
  <MSM>
    <security>
      <authEncryption>
        <authentication>WPA3SAE</authentication>
        <encryption>AES</encryption>
        <useOneX>false</useOneX>
        <transitionMode xmlns="http://www.microsoft.com/networking/WLAN/profile/v4">true</transitionMode>
      </authEncryption>
      <sharedKey>
        <keyType>passPhrase</keyType>
        <protected>false</protected>
        <keyMaterial>this_is_password_for_my_access_point</keyMaterial>
      </sharedKey>
    </security>
  </MSM>
  <MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
    <enableRandomization>false</enableRandomization>
  </MacRandomization>
</WLANProfile>
```

Wi-Fi 프로필을 내보낼 때 `key=clear` 구문을 사용했기 때문에, Wi-Fi 비밀번호가 평문으로 저장되었습니다.

{{< /collapse >}}

현재 작업 경로가 `C:\WiFi`이므로, My_WiFi_5G Wi-Fi 프로필은 `C:\WiFi\Wi-Fi-My_WiFi_5G.xml`에 저장되었습니다.

이제 Wi-Fi 프로필 파일(들)을 새로운 기기에 옮기면 됩니다. 경로는 이전과 동일하게 `C:\WiFi\*.xml`로 맞춰 주시고요.

# 프로필 불러오기

이전에 저장한 Wi-Fi 프로필을 불러올 차례입니다. 다시 한번 Wi-Fi 프로필이 저장된 경로로 이동합니다.

```batch
cd /D C:\WiFi
```

다음 명령어로 `C:\WiFi` 폴더에 저장된 Wi-Fi 프로필을 불러올 수 있습니다.

```batch
netsh wlan add profile filename="Wi-Fi-My_WiFi_5G.xml"
```

만약 `C:\WiFi`에 있는 모든 Wi-Fi 프로필을 불러오려면 다음과 같이 입력해야 합니다.

```batch
for %f in (*.xml) do netsh wlan add profile filename="%f"
```

배치 파일을 작성할 경우, `%f`를 `%%f`로 고쳐 써야 합니다.

```batch
for %%f in (*.xml) do netsh wlan add profile filename="%%f"
```

Wi-Fi 프로필이 정상적으로 불러와졌다면 다음과 같은 결과가 출력될 것입니다.

```plaintext
Wi-Fi 인터페이스에 My_WiFi_5G 프로필이 추가되었습니다.
```
