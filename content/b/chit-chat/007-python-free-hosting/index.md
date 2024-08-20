---
title: "정녕 Python 무료 호스팅은 없는 걸까"
slug: python-free-hosting
date: 2020-12-23T16:51:38+09:00
series:
#  - 
categories:
  - 잡담
tags:
#  - 
images:
#  - 001.webp
---

> 현재 Heroku는 무료로 사용할 수 없으므로, 무료 호스팅은 실질적으로 없는 셈이 되어버렸다.
{.bq}

***

나는 현재 자그마한 디스코드 봇을 Heroku에 올려두고 사용하는 중이다. 기본적으로 제공되는 월별 1,000시간은 디스코드 봇 하나를 돌리기에는 충분하고도 남을 정도니까.

&nbsp;

그런데 여기에 사용된 라이브러리인 discord.py의 공식 디스코드 사람들은 Heroku를 좋게 보지 않는 듯하다.

`?tag noheroku` 명령어를 입력하면 다음과 같은 메시지가 출력된다.

<blockquote>
- Bots are not what the platform is designed for. Heroku is designed to provide web servers (like Django, Flask, etc). This is why they give you a domain name and open a port on their local emulator.

&nbsp;

\- Heroku's environment is heavily containerized, making it significantly underpowered for a standard use case.

&nbsp;

\- Heroku's environment is volatile. In order to handle the insane amount of users trying to use it for their own applications, Heroku will dispose your environment every time your application dies unless you pay.

&nbsp;

\- Heroku has minimal system dependency control. If any of your Python requirements need C bindings (such as PyNaCl binding to libsodium, or lxml binding to libxml), they are unlikely to function properly, if at all, in a native environment. As such, you often need to resort to adding third-party buildpacks to facilitate otherwise normal CPython extension functionality. (This is the reason why voice doesn't work natively on heroku.)

&nbsp;

\- Heroku only offers a limited amount of time on their free programme for your applications. If you exceed this limit, which you probably will, they'll shut down your application until your free credit resets.
</blockquote>

그리고 `?tag hosting` 명령어를 입력하면 Heroku의 대안 서비스를 소개해 준다.

<blockquote>
Need to run your bot 24/7? Get a cheap VPS.

https://www&#46;scaleway&#46;com/ EU

https://www&#46;linode&#46;com/ US/EU/Asia

https://www&#46;digitalocean&#46;com/ US

https://www&#46;vultr&#46;com/ US

https://www&#46;ovh&#46;co&#46;uk/ EU/Canada

https://www&#46;hetzner&#46;com/ Germany

https://www&#46;time4vps&#46;eu/ Lithuania

&nbsp;

Self-hosting: Any computer.

Free hosting: No. Not even heroku.

Kinda free: GCP, AWS have one year free micros.
</blockquote>

'Free Hosting'에 대해서는 'No. Not even heroku.'라면서 선을 긋는다.

&nbsp;

물론 인터넷을 찾아보면 '디스코드 봇'을 호스팅해 주는 서비스가 몇몇 있긴 하다.

하지만 그 서비스에 대해 검색을 해보면 사용자의 봇 토큰을 몰래 훔쳐 가 악용하거나 서버의 보안이 취약하다는 문제점이 있다며, 절대로 그 서비스를 이용하지 말라는 의견이 자주 보인다.

즉, 못 써먹을 서비스라는 말이다.

&nbsp;

문제는, 내가 추가적인 비용 지급 없이 디스코드 봇을 24시간 돌리고 싶다는 것이고, 몇 가지 문제를 제외하면 Heroku가 제일 나은 방안이라는 것이다.

봇이 보이스 모듈을 쓰지 못하는 건 FFmpeg가 포함된 Buildpack을 추가하면 해결된다.

부족한 무료 제공 시간은 본인의 카드 번호를 추가하면 1,000시간까지 늘릴 수 있다. 한 달이 총 720시간이라는 것을 생각해 보면 차고 넘치는 시간이다.

웹 페이지가 노출되는 문제는 Procfile에서 worker만 설정해 두면 된다. 

누군가가 봇에게 할당된 주소에 접속해도 애당초 웹페이지를 설정하지 않았기 때문에 없는 페이지라는 오류 메시지만 나올 뿐이다.

&nbsp;

글쎄, 난 잘 모르겠다.

결국 discord.py의 공식 디스코드 서버의 사람들이 제시하는 해결책은 돈 없이는 사용할 수 없는 방안이고, 그건 내가 원하는 게 아니니까.

게다가 그들이 말하는, Heroku를 쓰지 말아야 하는 이유조차 나에게 있어 감안할 수 있다는 점에서 그들의 주장도 큰 힘이 없다.

그들의 주장이 discord.py의 공식 주장이 아님임은 말할 것도 없고.

&nbsp;

구글링을 해보아도 Python으로 작성된 프로그램을 큰 걱정 없이 호스팅할 수 있는 사이트는 보이지 않는 것 같다.

별수 있나, 계속 Heroku를 쓸 수밖에.
