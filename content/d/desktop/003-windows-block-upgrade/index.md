---
title: "[Windows] 업그레이드 차단하기"
slug: windows-block-upgrade
date: 2025-05-05T16:36:30+09:00
series:
#  - 
categories:
  - PIVOX
tags:
  - Windows
images:
  - logo.webp
---

작년 10월에 나온 Windows 11 24H2는 출시한 지 반년이 넘었음에도 여전히 온갖 버그와 호환성 문제를 겪고 있습니다.
일반적으로 이러한 문제는 출시 후 3개월 이내에 대부분 수정되기에, 24H2는 버그투성이 버전으로 인식되고 있습니다.

현재 많은 소프트웨어 및 게임 개발사들이 24H2 업그레이드를 하지 말 것을 권유하고 있습니다.
하지만 Microsoft는 Windows 업데이트를 통해 사용자의 의사와 관계없이 강제로 24H2 업그레이드를 수행할 수 있으며, 이는 업데이트를 일시 중지하더라도 막을 수 없습니다.

> [!IMPORTANT] 업데이트 vs 업그레이드
> Windows 업데이트는 OS의 업데이트와 업그레이드를 모두 수행할 수 있습니다.
> &nbsp;
> 업데이트는 보안 패치, 버그 수정 및 성능 향상을 목적으로 하며, 이를 수행하더라도 OS의 버전이 변하지 않습니다.
> 업그레이드는 새로운 기능이나 기술적 개선 사항을 포함한 상위 버전 소프트웨어 설치 및 교체를 목적으로 하며, 이를 수행하면 OS의 버전이 변할 수 있습니다.
> * Windows 11 23H2 → Windows 11 23H2 : 업데이트
> * Windows 11 23H2 → Windows 11 **24H2** : 업그레이드
> * Windows 10 → Windows **11** : 업그레이드

하지만 방법이 아예 없는 것은 아닙니다. Windows에는 OS 업그레이드를 막을 수 있는 기능이 포함되어 있으나, 일반 사용자에게 공개되지 않은 것뿐입니다.

# 현재 사용 중인 OS 버전 확인하기

Windows 업그레이드를 막기 위해선 먼저 현재 사용 중인 OS 버전을 확인해야 합니다.

명령 프롬프트 혹은 Windows PowerShell을 열고 다음과 같이 입력합니다.

```batch
> winver
```

{{< gallery/image src="winver" caption="Windows 11 23H2에서 `winver`을 실행한 결과" >}}

위 창에서 다음과 같은 정보를 확인할 수 있습니다.

* OS: Windows 11
* 버전: 23H2

# 업그레이드 차단

Windows 업그레이드를 차단하는 방법에는 두 가지가 있습니다.

## InControl 사용 (추천)

[InControl](https://www.grc.com/incontrol.htm)을 사용하면 손쉽게 Windows 업그레이드를 차단할 수 있습니다.

<link-preview url="https://www.grc.com/incontrol.htm" title="GRC | InControl" desc="InControl - Disable Windows automatic updates and upgrades" image="https://www.grc.com/apple-touch-icon.png"></link-preview>

{{< gallery/image src="icdl" >}}

사이트 하단의 Download now 버튼을 눌러 InControl을 다운로드합니다.

InControl을 실행하면 다음과 같은 창이 나타납니다.

{{< gallery/image src="ic01" >}}

좌측 하단의 Version / Release에는 현재 사용 중인 Windows의 버전이 자동으로 기입되어 있습니다.
만약 이 칸들이 비어 있다면 아까 `winver`을 통해 확인한 Windows 버전 정보를 기입하면 됩니다.

Take Control 버튼을 누르면 다음과 같은 화면으로 변합니다.

{{< gallery/image src="ic02" >}}

이제 Windows 업데이트는 상위 버전으로의 업그레이드를 수행하지 않습니다.
그대로 Exit 혹은 X 버튼을 눌러 InControl을 종료하면 됩니다.

## 레지스트리 수정

어떠한 이유로 인해 InControl을 사용할 수 없다면 직접 Windows Registry를 수정해 업그레이드를 차단할 수 있습니다.
아래 내용은 InControl이 수행하는 작업과 동일합니다.

**관리자 권한**으로 명령 프롬프트 혹은 Windows PowerShell을 실행한 후, 다음 명령어들을 상황에 맞게 모두 입력합니다.

```batch
REM 상황에 맞게 '23H2'를 '24H2' 등으로 교체할 것
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v "DisableOSUpgrade" /t REG_DWORD /d "1" /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v "ProductVersion" /t REG_SZ /d "Windows 11" /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v "TargetReleaseVersion" /t REG_DWORD /d "1" /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v "TargetReleaseVersionInfo" /t REG_SZ /d "23H2" /f

reg add "HKLM\SOFTWARE\Policies\Microsoft\WindowsStore" /v "DisableOSUpgrade" /t REG_DWORD /d "1" /f

reg add "HKLM\SYSTEM\Setup\UpgradeNotification" /v "UpgradeAvailable" /t REG_DWORD /d "0" /f
```

혹은 다음 내용을 `block_upgrade.reg` 파일로 저장하여 실행해도 됩니다. 위와 마찬가지로, 실행 전 상황에 맞게 내용을 변경해야 합니다.

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate]
"DisableOSUpgrade"=dword:00000001
"ProductVersion"="Windows 11"
"TargetReleaseVersion"=dword:00000001
"TargetReleaseVersionInfo"="23H2"

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsStore]
"DisableOSUpgrade"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\Setup\UpgradeNotification]
"UpgradeAvailable"=dword:00000000
```
