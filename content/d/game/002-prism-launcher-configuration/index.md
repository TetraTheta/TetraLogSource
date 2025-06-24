---
title: "[Prism Launcher] 설정"
slug: prism-launcher-configuration
date: 2025-06-22T23:12:00+09:00
series:
  - Prism Launcher 가이드
categories:
  - PIVOX
tags:
  - Minecraft
  - Prism Launcher
  - 마인크래프트
  - 프리즘 런처
images:
  - logo.webp
---

Prism Launcher는 여러 개의 Minecraft: Java Edition 인스턴스와 Minecraft 계정, 모드 등을 관리할 수 있는 오픈 소스 소프트웨어입니다.
Microsoft가 제공하는 Minecraft Launcher보다 사용이 매우 편리하기에, Minecraft: Java Edition을 플레이하는 사람에게 권장되는 프로그램 중 하나입니다.

이 글에서는 Prism Launcher를 설정하는 방법에 대해 핵심적인 부분만 간략하게 설명합니다.

> [!NOTE] 참고
> 이 튜토리얼은 Prism Launcher 9.4를 기준으로 작성되었습니다.

Prism Launcher 메인 창 상단의 <kbd>설정</kbd> 버튼을 눌러 설정 창을 엽니다.

# 마인크래프트{id="minecraft"}

{{< gallery/image src="minecraft-001" width="50%" >}}

Minecraft의 기본 창 크기는 854 x 480입니다.
게임을 창 모드로 플레이하는 경우, 창 너비와 창 높이를 조절하는 것이 좋습니다.

{{< collapse heading="해상도 예시" >}}

* 기본 비율 (427:240)
  * 1281 x 720
  * 1708 x 960
* 16:9 비율
  * 1280 x 720
  * 1296 x 729
  * 1312 x 738
  * 1392 x 783
  * 1440 x 810

{{< /collapse >}}

# Java{id="java"}

{{< gallery/image src="java-001" width="50%" >}}

## 메모리{id="java-memory"}

Minecraft에 모드를 추가할수록 게임은 더 많은 양의 메모리를 필요로 하게 됩니다.

본인의 게임 및 PC 사용 환경에 따라 최소 메모리 할당량과 최대 메모리 할당량을 설정해 주세요.

| | |
|:-:|:-:|
| | 권장 메모리 할당량 (최소 / 최대) |
| 모드 X | 2048 MiB / 2048 MiB (2 GiB) |
| 모드 O | 4096 MiB / 4096 MiB (4 GiB)<br>6144 MiB / 6144 MiB (6 GiB)<br><b>8192 MiB / 8192 MiB (8 GiB, 권장)</b> |
{_align=middle,_thead=false,style="width:50%;min-width:400px"}

최소 메모리 할당량과 최대 메모리 할당량을 동일하게 설정해야 게임 플레이 중 렉이 덜 걸립니다.

최대 메모리 할당량을 현재 시스템에 설치된 메모리 용량보다 높게 설정할 경우, 오른쪽의 초록색 체크 박스가 붉은색 엑스 박스로 변합니다.

## Java 런타임{id="java-runtime"}

Prism Launcher의 기본값은 위 사진과 같이 설정되어 있습니다.

* Java 경로: (비어있음)
* [ ] Java 호환성 검사 무시
* [ ] Java 설치 마법사 건너뛰기
* [x] Java 버전 자동 감지
* [x] Mojang Java 자동 다운로드

이 상태에서 Prism Launcher는 여러분이 실행한 Minecraft 버전에 맞는 Java 런타임을 자동으로 Mojang 서버에서 다운로드하여 사용할 것입니다.

&nbsp;

만약 여러분이 별도로 설치한 Java 런타임을 사용하고 싶다면 <kbd>자동 감지</kbd> 버튼을 누르세요.

{{< gallery/image src="java-004" width="50%" >}}

현재 시스템에 설치된 Java 런타임의 경로가 표시됩니다.

본인이 사용하고 싶은 Java 런타임을 선택한 후, <kbd>확인</kbd> 버튼을 누르면 됩니다.

### JVM 인수{id="jvm-arguments"}

JVM 인수를 통해 Java 런타임의 작동 방식을 세부적으로 조정하여 게임 플레이를 더욱 원활하게 만들 수 있습니다.

다음은 대부분의 상황에서 유용한 JVM 인수입니다.

```plaintext {data-wrap=true,data-line-nos=false}
--add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20
```

## Java 관리 도구{id="java-management"}

{{< gallery/image src="java-002" width="50%" >}}

Prism Launcher가 다운로드한 Java 런타임을 관리할 수 있습니다.

새 Java 런타임을 다운로드하려면 우측의 <kbd>다운로드</kbd> 버튼을 누르세요.

{{< gallery/image src="java-003" width="50%" >}}

Mojang이 제공하는 Java 런타임 외에도 Eclipse 재단이 제공하는 Adoptium Java 런타임이나 Azul 社에서 제공하는 Zulu Java 런타임을 사용할 수 있습니다.

어느 Java 런타임을 사용해도 좋습니다만, 개인적으로 Mojang이나 Adoptium의 Java 런타임 사용을 추천합니다.
