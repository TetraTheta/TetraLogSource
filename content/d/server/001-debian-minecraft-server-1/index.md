---
title: "[Debian] 마인크래프트 서버 설치기 (1) - 데비안 설치"
slug: debian-minecraft-server-1
date: 2026-06-05T16:52:34+09:00
series:
  - "데비안 마인크래프트 서버 설치기"
categories:
  - PIVOX
tags:
#  - 
images:
  - logo.webp
---

어느 날, 갑자기 마인크래프트 서버를 서비스하고 싶어졌다. 그래서 너무 오래되어 쓰지 않는 미니 PC에 마인크래프트 서버를 구동하기로 했다.

# 서버 PC 사양

* CPU: Intel(R) Core(TM) i3-8100 (4) @ 3.60 GHz
  * 4 코어 4 스레드
* RAM: 16 GiB
  * 본래 8 GiB였는데, 내가 별도로 장착되어 있던 것과 동일한 RAM을 하나 더 구매해서 늘린 결과이다.
* HDD: 1 TiB

서버의 사양을 보아하니 마인크래프트 서버만 구동해야 겨우 돌아갈 것 같다.
게다가 SSD가 아닌 HDD를 쓰고 있어 디스크 I/O 속도도 그리 좋게 나오지는 않을 테고.

# 서버 OS 선택

서버 사양이 그리 넉넉하지 않은 관계로, 서버에 설치할 OS는 두 가지 기준을 두고 결정했다.
그래봤자 결국 Debian 계열이냐, Fedora 계열이냐, Arch 계열이냐의 문제지만.

* 안정성: 유지 보수가 비교적 익숙하거나 쉽고, 오랜 기간 업데이트를 하지 않아도 잘 작동할 것
* 가벼움: 잡다한 서비스/패키지 없이 오직 서버 구동에만 초점을 맞출 것

롤링 릴리즈 배포판은 오랜 기간 업데이트를 하지 않은 상태에서 업데이트를 할 시 설정 등이 깨지는 경우가 있다고 하니, 포인트 릴리즈 배포판을 선택해야 한다. 자연스럽게 롤링 릴리즈 배포판 중심인 Arch 계열이 탈락했다.

Fedora 계열은 CentOS 등으로 조금 익숙한 배포판 계열이긴 하지만, '가볍다'라는 평가를 듣는 배포판을 찾지 못했다.

Void Linux도 제법 흥미로웠지만, 전혀 익숙하지 않은 OS이기에 유지 보수가 어려울 것이라 판단하여 후보에서 제외하였다.

결국 남은 건 Debian 계열이었고, 그중 고민 끝에 Debian을 선택했다.
같은 Debian 계열인 데다 오랫동안 써온 Ubuntu Server 대신 Debian을 선택한 이유는 Debian이 Ubuntu Server 최소 설치보다 더 가볍기 때문이었다. 대신 사용하는 패키지의 버전이 Ubuntu Server보다 조금 낮은데, 어차피 마인크래프트 서버만 돌릴 것이라 큰 상관은 없을 것이다.

이 글을 쓰는 시점에서 Debian의 최신 버전은 13.5.0이다.

# 데비안 설정

서버 컴퓨터에 키보드나 모니터를 연결해 작업하는 건 초기 서버 설정 때에나 그렇고, 그 외에는 전부 SSH로 연결해 작업할 계획이다.

Ubuntu Server에서 설치 언어를 영어가 아닌 한국어로 설정했더니 TTY 환경에서 한국어 메시지가 □로 표시되는 경우를 자주 보았기에, Debian을 설치할 때에는 아예 처음부터 설치 언어를 Korean이 아닌 English (United States)로 설정했다.

## 시간대 변경

Ubuntu Server와 다르게, Debian은 설치 언어와 시간대 설정이 함께 묶여 있다.
설치 언어를 English (United States)로 설정했다면 시간대 설정 화면에서 오직 미국 시간대 목록만 표시된다.

따라서 아무 시간대나 선택해 OS 설치를 마친 후, 인위적으로 시간대를 한국 표준시로 변경해야만 했다.

```shell{linenos=false}
$ sudo dpkg-reconfigure tzdata
```

Geographic area는 Asia, Time zone은 Seoul로 설정하면 KST로 시간대 변경이 가능하다.

`timezonectl`이 있다면 다음 명령어로 쉽게 설정할 수 있겠지만, Debian에는 기본적으로 포함되어 있지 않다.

```shell{linenos=false}
$ sudo timedatectl set-timezone Asia/Seoul
```

## SSH 설정

### SSH 서버 설정

SSH 접속에 비밀번호를 사용하는 건 매우 위험한 일이다. 안일하게 기본 설정인 '비밀번호 인증'을 사용했다간 나도 모르는 사이에 내 서버가 야생의 봇에게 점령되어 좀비 PC가 되거나 내 소중한 데이터가 해커의 손에 넘어갈 수 있다.

따라서 SSH 접속에는 무조건 SSH 키를 사용하도록 설정해야 한다.

SSH 서버 설정 수정에는 `/etc/ssh/sshd_config` 파일을 직접 수정하는 방법도 있지만, `sshd_config`에는 다음 줄이 포함되어 있다.

```plaintext{linenostart=11,title="sshd_config"}
# ...
Include /etc/ssh/sshd_config.d/*.conf
# ...
```

`/etc/ssh/sshd_config.d` 아래에 있는 `.conf` 파일을 먼저 불러와 적용하겠다는 의미이다.

그래서 다음 명령어로 별도의 설정 파일을 만들고 수정하기로 했다.

```shell{linenos=false}
$ sudo touch /etc/ssh/sshd_config.d/10-NoPassword.conf
$ sudo nano /etc/ssh/sshd_config.d/10-NoPassword.conf
```

```plaintext{title="10-NoPassword.conf"}
PasswordAuthentication no
```

이렇게 하면 굳이 `sshd_config` 파일을 수정하지 않아도 된다.

### SSH 키 생성

이제 SSH 접속에 사용할 SSH 키를 만들어야 한다. 서버가 아닌 다른 컴퓨터에서 다음 명령어를 입력한다.

```cmd{linenos=false}
> ssh-keygen -t ed25519 -C "your_email@example.com"
```

최근 Windows에는 OpenSSH가 기본적으로 포함되어 있고, Git for Windows를 설치해도 `ssh-keygen`이 같이 설치되기 때문에, `ssh-keygen` 명령어 실행에는 아무런 문제가 없을 거다.

`-C`는 주석을 넣기 위한 스위치라서 `your_email@example.com` 자리에 꼭 본인의 이메일을 넣을 필요는 없다. 다만 본인을 나타내기 가장 쉬운 문자열이 이메일이라서 다들 일종의 관습처럼 이메일을 넣는 것이다.

`ssh-keygen`이 하라는 대로 SSH 키를 만들면 두 개의 파일이 생긴다.

* `<SSH 키 이름>`: 개인 키
* `<SSH 키 이름>.pub`: 공개 키

두 파일을 안전한 곳에 잘 보관하자. Windows 기준, `%UserProfile%\.ssh`에 넣어두는 것이 일반적이다.

### SSH 키 변환

보통 SSH 접속에 PuTTY를 쓰는데, PuTTY는 방금 우리가 생성한 OpenSSH 키 형식을 사용하지 않는다. 따라서 방금 생성한 OpenSSH 개인 키를 PuTTY Private Key 형식(`.ppk`)으로 변환해 저장해야 한다.

#### WinSCP 사용 (Windows CLI)

개인적으로 명령어를 통해 작업하는 것을 선호하는데, Windows용 PuTTYgen은 [의도적으로 명령어 인터페이스를 제공하지 않는다](https://www.chiark.greenend.org.uk/~sgtatham/putty/wishlist/puttygen-batch.html).

하지만 WinSCP 명령어 인터페이스(`winscp.com`)를 이용하면 Windows에서도 OpenSSH 키를 PuTTY 키로 변환할 수 있다.

<link-preview url="https://winscp.net/eng/docs/lang:ko" title="WinSCP 소개 :: WinSCP" desc="WinSCP is a free file manager for Windows supporting FTP, SFTP, S3 and WebDAV." image="https://winscp.net/favicon.ico"></link-preview>

WinSCP를 설치하면 GUI 프로그램인 `winscp.exe`와 CLI 프로그램인 `winscp.com`이 함께 설치되는데, 명령 프롬프트 등에서는 `.exe`보다 `.com`을 먼저 인식한다.

명령 프롬프트 등에서 다음과 같이 입력하면 된다.

```cmd{linenos=false}
> winscp.com /keygen "<SSH 개인 키 경로>" /output="<SSH 개인 키 경로>.ppk"
> REM winscp.com /keygen "%UserProfile%\.ssh\mykey" /output="%UserProfile%\.ssh\mykey.ppk"
```

이렇게 하면 PPK 형식으로 변환된 SSH 키가 저장된다.

#### PuTTYgen 사용 (Windows GUI)

키보드로 명령어를 하나하나 입력하는 것이 싫다면 PuTTYgen을 사용하면 된다.

<link-preview url="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html" title="Download PuTTY: latest release (0.84)" desc="" image="https://www.chiark.greenend.org.uk/~sgtatham/putty/putty.ico"></link-preview>

스크롤을 조금 내리다 보면 '`puttygen.exe` (A RSA and DSA key generation utility'라고 적힌 부분이 있는데, 본인 OS 사양에 맞는 파일을 다운로드하면 된다. 대부분의 경우 '64-bit x86'를 선택하면 된다.

* [64-bit x86](https://the.earth.li/~sgtatham/putty/latest/w64/puttygen.exe): x64
* [64-bit Arm](https://the.earth.li/~sgtatham/putty/latest/wa64/puttygen.exe): Arm64
* [32-bit x86](https://the.earth.li/~sgtatham/putty/latest/w32/puttygen.exe): x86

다운로드 한 파일을 실행하면 아래와 같은 창이 하나 나타난다.

{{< gallery/image src="puttygen-gui" >}}

1. 상단 메뉴의 'Conversions - Import key'를 선택해 `<SSH 키 이름>`(개인 키) 파일을 불러온다.
2. 중간의 'Save private key' 버튼을 누른다.
   - SSH 키를 만들 때 passphrase를 지정하지 않았기에 'Are you sure you want to save this key without a passphrase to protect it?'라는 경고가 뜨는데, '예'를 누른다.
3. 기존 SSH 키를 저장한 경로에 `<SSH 키 이름>.ppk` 파일을 저장한다.

#### PuTTYgen 사용 (Unix CLI)

Linux나 macOS 환경의 경우, `puttygen` 명령어가 포함된 패키지를 설치하면 된다.

- Linux
  - Debian 계열: `sudo apt install putty-tools`
  - Fedora 계열: `sudo yum install putty`
  - Arch 계열: `pacman -S putty`
- macOS (Homebrew): `brew install putty`

패키지를 설치한 다음, 아래 명령어를 이용해 OpenSSH 키를 PPK 형식으로 변환하면 된다.

```shell{linenos=false}
$ puttygen "<SSH 개인 키 경로>" -O private -o "<SSH 개인 키 경로>.ppk"
$ # puttygen "~/.ssh/mykey" -O private -o "~/.ssh/mykey.ppk"
```

### SSH 키 등록

여기까지 잘 따라왔다면 `.ssh` 디렉터리에 다음과 같은 파일 3개가 있을 것이다.

* `<SSH 키 이름>`: OpenSSH 개인 키
* `<SSH 키 이름>.pub`: OpenSSH 공개 키
* `<SSH 키 이름>.ppk`: PuTTY 개인 키

이제 이 SSH 키를 서버에 등록해야 서버에 로그인할 때 SSH 키를 사용할 수 있다.

```shell{linenos=false}
$ sudo touch ~/.ssh/authorized_keys
$ sudo nano ~/.ssh/authorized_keys
```

SSH 키 중 OpenSSH 공개 키 파일(`<SSH 키 이름>.pub`)을 열어보면 대략 다음과 같은 형식의 SSH 키가 적혀 있을 것이다.

```plaintext{title="mykey.pub"}
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOcEDxcz+hKjEFgplgJubB9qItydmlvi+3+LjCf/sJN2 your_email@example.com
```

이 내용을 그대로 복사해 `authorized_keys` 파일에 붙여 넣으면 된다.

```plaintext{title="authorized_keys"}
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOcEDxcz+hKjEFgplgJubB9qItydmlvi+3+LjCf/sJN2 your_email@example.com
```

## 새 사용자 계정 생성

OS 설치 시 생성한 계정은 자동적으로 `sudo` 그룹에 포함되게 된다. 해당 그룹에 있는 사용자는 `sudo` 명령어를 사용할 수 있기 때문에 기본 계정을 그대로 마인크래프트 서버 구동에 사용하는 것은 별로 좋지 않다. Log4Shell같은 일이 또 일어난다면 해커가 내 서버에서 `sudo` 명령어를 사용할 수 있게 되는 거니까.

그래서 마인크래프트 서버 전용 계정을 하나 생성하기로 했다.

```shell{linenos=false}
$ sudo groupadd minecraft
$ sudo useradd -m -g minecraft minecraft
```

1. `minecraft` 그룹을 생성
2. `minecraft` 계정을 홈 디렉터리와 함께 생성하고 `minecraft` 그룹에 추가

이렇게 생성한 계정은 비밀번호가 배정되어 있지 않기 때문에, `sudo su -l minecraft` 명령어를 이용해 접속하는 방법밖에 없다. 물론, 의도한 사항이다.

## 계정 초기 설정

가끔 `.bashrc` 같은 설정이 제대로 설정되지 않는 경우가 있다. 그래서 기본적으로 제공되는 `.bashrc`의 일부 주석을 해제한 버전을 공유한다.

```bash{title=".bashrc"}
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
  *i*) ;;
  *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
#[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
  debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
  xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
  if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
    # We have color support; assume it's compliant with Ecma-48
    # (ISO/IEC-6429). (Lack of such support is extremely rare, and such
    # a case would tend to support setf rather than setaf.)
    color_prompt=yes
  else
    color_prompt=
  fi
fi

if [ "$color_prompt" = yes ]; then
  PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w \$\[\033[00m\] '
else
  PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
  xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1";;
  *)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
  test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
  alias ls='ls --color=auto'
  alias dir='dir --color=auto'
  alias vdir='vdir --color=auto'

  alias grep='grep --color=auto'
  alias fgrep='fgrep --color=auto'
  alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -lha'
alias la='ls -A'
alias l='ls -CF'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.
if [ -f ~/.bash_aliases ]; then
  . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
```

## ufw 설정

별다른 방화벽 설정을 하지 않은 Debian은 모든 연결을 허용하도록 되어 있기 때문에, 방화벽을 설정해 주는 것이 좋다.

먼저 ufw를 설치한다.

```shell{linenos=false}
$ sudo apt install ufw
```

ufw를 설치하려 하면 iptables 패키지도 같이 설치하려 하는데, 이 패키지는 실제 iptables 패키지가 아닌, iptables 호환 레이어를 갖춘 nftables 패키지이다. ufw 역시 nftables를 사용하도록 기본 설정되어 있고.
그러니 오래된 iptables가 같이 깔리는 걸 걱정하지 않고 그냥 ufw를 편하게 설치하면 된다.

이후 다음 명령어를 통해 ufw를 설정한다.

```shell{linenos=false}
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ # SSH(22)는 오직 로컬 대역에서만 허용
$ # IPv4 사설 IP 대역
$ sudo ufw allow from 10.0.0.0/8 to any port 22 proto tcp
$ sudo ufw allow from 172.16.0.0/12 to any port 22 proto tcp
$ sudo ufw allow from 192.168.0.0/16 to any port 22 proto tcp
$ # IPv6 로컬 IP 대역
$ sudo ufw allow from fc00::/7 to any port 22 proto tcp
$ sudo ufw allow from fe80::/10 to any port 22 proto tcp
$ # 마인크래프트(25565) 허용
$ sudo ufw allow 25565/tcp
$ sudo ufw allow 25565/udp
$ # ufw 활성화
$ sudo ufw enable
$ # ufw 현재 상태 확인
$ sudo ufw status verbose
```

이제 서버를 재부팅하면 된다.
ufw 설정이 제대로 되어 있다면 서버 재부팅 후에도 SSH 서버 접속이 가능할 거고, 아니라면 서버에 직접 키보드와 모니터를 연결해서 ufw 설정을 수정해야 한다.

## DNS 설정

어째서인지는 몰라도, Debian 기본 설정을 사용하면 마인크래프트 인증 서버인 `api.minecraftservices.com`에 해당하는 IP 주소를 받아오지 못한다.
이로 인해 마인크래프트 서버가 인증 서버에 접속할 수 없게 되고, 서버에 접속하려는 사람이 마인크래프트를 보유했는지 아닌지를 판단할 수 없게 된다. 그래서 서버는 다음 메시지와 함께 모든 사용자를 거부하게 된다.
> The authentication servers are currently not reachable. Please try again.
{.bq}

이런 건 정말 인터넷에 문제가 있는 게 아니라면 십중팔구 DNS 설정 문제다.

Ubuntu Server라면 `netplan` 같은 명령어를 쓸 수 있겠지만, Debian에는 `netplan`이 없다. 그래서 네트워크 관련 설정 파일인 `/etc/resolv.conf` 파일을 직접 열어보았다.

```plaintext{title="resolv.conf"}
# Generated by dhcpcd from enp2s0.dhcp
# /etc/resolv.conf.head can replace this line
nameserver 192.168.0.1
# /etc/resolv.conf.tail can replace this line
```

DNS 주소가 공유기로 잡혀 있다. 공유기가 DNS 요청을 제대로 서버에 돌려주지 못하는 모양인데, 서버가 사용할 DNS 주소를 다른 것으로 변경하면 해결된다.
하지만 `resolv.conf`에 쓰여 있듯이, `/etc/resolve.conf` 파일은 dhcpcd에 의해 생성된 파일이기 때문에 직접 수정해서는 안되고, dhcpcd의 설정 파일인 `/etc/dhcpcd.conf` 파일을 대신 수정해야 한다.

그전에 현재 사용 중인 네트워크 인터페이스의 이름을 알아내야 한다.

```shell{linenos=false}
$ ip link show | grep "state UP"
2: enp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
```

`enp2s0`가 현재 서버가 사용 중인 네트워크 인터페이스의 이름이다. 경우에 따라서는 `eth0`가 나오기도 한다.

네트워크 인터페이스의 이름을 알아냈으니, `/etc/dhcpcd.conf` 파일을 열어 맨 아래에 다음 내용을 추가했다.

```plaintext{linenostart=45,title="dhcpcd.conf"}
interface enp2s0
static domain_name_servers=8.8.8.8 8.8.4.4
```

## mDNS 설정

공유기의 DHCP 설정으로 서버의 내부 IP를 고정했지만, 좀 더 확실한 접근 방법이 필요하다. 매번 `192.168.0.70`이라고 입력할 수는 없는 노릇 아닌가.
그럴 때 필요한 것이 바로 mDNS(Multicast DNS)이다. 쉽게 말해, 내부망 전체에 '제가 `debian.local`입니다!'라고 소리치도록 설정하는 것이다.

mDNS를 설정하는 방법에는 systemd를 이용하는 것과 Avahi를 이용하는 것, 두 가지가 있는데, systemd를 설정하는 것이 귀찮은 관계로 Avahi를 설치하기로 결정했다.

```shell{linenos=false}
$ sudo apt install avahi-daemon
$ sudo systemctl status avahi-daemon
$ # avahi-daemon 서비스가 실행 중이 아니라면 활성화 후 실행
$ sudo systemctl enable avahi-daemon
$ sudo systemctl start avahi-daemon
```

단순히 패키지를 설치하는 것만으로 자동적으로 ufw 등의 방화벽 설정까지 전부 다 처리해 준다.
