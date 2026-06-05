---
title: "[Debian] 마인크래프트 서버 설치기 (2) - 마인크래프트 서버"
slug: debian-minecraft-server-2
date: 2026-06-05T16:55:27+09:00
series:
  - "데비안 마인크래프트 서버 설치기"
categories:
  - PIVOX
tags:
#  - 
images:
  - logo.webp
---

이제 데비안 서버의 기본 설정을 다 마쳤다. 이제 마인크래프트 서버 구동을 위한 설정을 하면 된다.

# 마인크래프트 서버 다운로드 및 설정

서버 컴퓨터의 사양이 그리 좋지 않은 관계로, 모드를 잔뜩 설치한 모드팩 서버는 열기가 힘들다.
정확히 말하면 열 수는 있는데, 조금만 부하가 심해져도 서버가 터질 것 같다.

## Paper 서버 다운로드

그래서 최적화가 잘 된 [Paper 서버](https://papermc.io)에 플러그인을 추가해서 열기로 했다. 추가적인 몬스터나 블록, 아이템은 없겠지만 대신 속도와 안정성을 얻었다.

<link-preview url="https://papermc.io/downloads/paper" title="Paper" desc="Download Paper, our Minecraft server software offering unrivaled performance and stability." image="https://papermc.io/assets/logo/256x.png"></link-preview>

다운로드한 Paper 서버 파일 이름은 `paper-26.1.2.jar`로 변경했다. 그래야 나중에 Paper 서버 빌드를 업데이트할 때 서버 시작 스크립트를 수정하지 않을 수 있으니까.

여기에 개인적으로 선호하는 플러그인을 잔뜩 추가했다.

- [EssentialsX](https://essentialsx.net/downloads)
- [Fast Leaf Decay](https://modrinth.com/plugin/fast-leaf-decay)
- [InvSee++](https://modrinth.com/plugin/invsee++)
- [LuckPerms](https://luckperms.net/)
- [MinePacks](https://www.spigotmc.org/resources/19286/)
- [NoChatReports](https://modrinth.com/plugin/nochatreports-spigot-paper)
- [Vault](https://www.spigotmc.org/resources/34315/)
- [WorldEdit](https://modrinth.com/plugin/worldedit)
- [WorldGuard](https://modrinth.com/plugin/worldguard)

## 마인크래프트 서버 설정

### `server.properties`

1.21.2 버전에 추가된 `pause-when-empty-seconds` 덕분에 '서버에 사람이 없는데 월드 시간만 하릴없이 지나가는 상황'을 막을 수 있다.

```properties{linenos=false,title="server.properties"}
# ...
pause-when-empty-seconds=60
# ...
```

접속 중인 플레이어가 0명인 상황이 60초 이상 지속될 경우, 서버의 시간이 멈춘다.

{{< gallery/image src="za-warudo.gif" c="더 월드! 시간이여 멈춰라!" >}}

## 시작 스크립트

Paper 서버를 Windows에서 테스트한 후 Debian에 복사해 서비스할 생각이기 때문에, Windows용 시작 스크립트와 Linux용 시작 스크립트를 서버 디렉터리 최상단에 작성했다.

[Aikar의 JVM 인수](https://aikar.co/2018/07/02/tuning-the-jvm-g1gc-garbage-collector-flags-for-minecraft/)를 사용하고, RAM을 6GB 할당했다.

- `-Djava.net.preferIPv4Stack=true`: Java가 IPv6를 사용해 마인크래프트 인증 서버에 접속하는 것을 방지

### Windows용

```dos{wrap=true,title="_run.cmd"}
@echo off
cd /d "%~dp0"
java -Xms6144M -Xmx6144M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -Djava.net.preferIPv4Stack=true -jar paper-26.1.2.jar --nogui
pause
```

### Linux용

```bash{wrap=true,title="_run.sh"}
#!/bin/bash
cd "$(dirname "$0")"
/usr/bin/java -Xms6144M -Xmx6144M --add-modules=jdk.incubator.vector -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -Djava.net.preferIPv4Stack=true -jar paper-26.1.2.jar --nogui
```

나중에 Debian 서버에 복사한 후, 실행 가능하도록 권한을 변경해야 한다.

```shell{linenos=false}
$ chmod +x /path/to/_run.sh
```

# 필요 패키지 설치

## Java JRE

마인크래프트 서버 구동에는 Java JRE가 필요하다.

- 1.18 ~ 1.20.4: Java 17
- 1.20.5 ~ 1.21.11: Java 21
- 26.1 ~ 현재: Java 25

Debian이 제공하는 OpenJDK JRE를 설치해도 좋다.

```shell{linenos=false}
$ # 필요한 Java JRE 버전 설치
$ sudo apt install openjdk-17-jre
$ sudo apt install openjdk-21-jre
$ sudo apt install openjdk-25-jre
```

하지만 난 Eclipse Temurin JRE를 설치하고 싶었다. Windows에서 쓰는 JDK가 Eclipse Temurin이었기 때문이다.

먼저 Eclipse Temurin 설치에 필요한 패키지를 설치한다.

```shell{linenos=false}
$ sudo su -
# apt install wget apt-transport-https gpg
```

Eclipse Temurin GPG 키를 apt keyring에 등록한다.

```shell{linenos=false,wrap=true}
# wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | tee /etc/apt/keyrings/adoptium.gpg > /dev/null
```

Eclipse Temurin DEB 저장소를 추가한다.

```shell{linenos=false,wrap=true}
# echo "deb [signed-by=/etc/apt/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | tee /etc/apt/sources.list.d/adoptium.list
```

현재 Debian 13을 쓰고 있기 때문에 `adoptium.list`의 내용을 출력하면 다음과 같은 결과가 나온다.

```shell{linenos=false,wrap=true}
# cat /etc/apt/sources.list.d/adoptium.list
deb [signed-by=/etc/apt/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb trixie main
```

이제 Eclipse Temurin을 설치할 수 있다.

```shell{linenos=false}
# apt update
# # 필요한 Java JRE 버전 설치
# sudo apt install temurin-17-jre
# sudo apt install temurin-21-jre
# sudo apt install temurin-25-jre
```

## tmux

곧 설명하겠지만, 마인크래프트 서버를 tmux 세션에서 실행할 생각이다.

```shell{linenos=false}
$ sudo apt install tmux
```

# systemd 서비스 작성

마인크래프트 서버 관리를 위한 도구는 정말 많다. Pterodactyl이라던가, AMP라던가...
하지만 내 서버의 사양은 그리 좋지 않고, 이런 패널에 드는 리소스조차 아깝다. 따라서 마인크래프트 서버는 systemd 서비스로 구현 및 관리하기로 했다.

```ini{title=minecraft.service}
# /etc/systemd/system/minecraft.service
[Unit]
Description=Minecraft Paper Server (tmux)
After=network.target

[Service]
Type=forking
User=minecraft
Group=minecraft
WorkingDirectory=/home/minecraft/minecraft/paper

Environment="TMUX_TMPDIR=/home/minecraft"

ExecStart=/usr/bin/tmux new -d -s minecraft './_run.sh'

ExecStop=/usr/bin/tmux send-keys -t minecraft "stop" Enter
ExecStop=/usr/bin/bash -c 'while /usr/bin/tmux has-session -t minecraft 2>/dev/null; do sleep 1; done'

KillMode=control-group
TimeoutStopSec=120
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

마인크래프트 서버를 tmux 세션에서 구동하여 필요할 시 서버 콘솔에 직접 접근이 가능하도록 설계했다.

- `User=minecraft` / `Group=minecraft`: 마인크래프트 서버를 root가 아닌 minecraft 사용자가 실행하도록 한다.
- `Environment="TMUX_TMPDIR=/home/minecraft"`: systemd 서비스는 tmux 소켓 기본 생성 경로인 `/tmp/*`에 접근할 수 없으므로, minecraft 사용자의 홈 디렉터리에 생성하도록 설정한다.
- `TimeoutStopSec=120`: 서버가 2분 동안 종료되지 않았다면 강제 종료한다.

systemd 데몬을 다시 불러온 후, minecraft 서비스를 테스트해본다.

```shell{linenos=false}
$ sudo systemctl daemon-reload
$ sudo systemctl enable minecraft
$ sudo systemctl start minecraft
$ sudo systemctl status minecraft
```

이후 서버를 종료할 때에는 `sudo systemctl stop minecraft`를 입력하면 된다.

## `.bashrc` 수정

`minecraft` 계정으로 tmux 세션을 확인하기 위해서는 서비스에서 정의한 환경 변수를 `minecraft` 계정에 동일하게 적용해야 한다.

```shell{linenos=false}
$ # minecraft 계정으로 접속
$ nano ~/.bashrc
```

이후 다음 내용을 맨 아래에 추가한다.

```bash{linenostart=113,title=".bashrc"}
export TMUX_TMPDIR=/home/minecraft
```
