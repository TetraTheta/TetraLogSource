---
title: "{{ replace .Name "-" " " | replaceRE "^([0-9]+) " "" | title }}"
slug: {{ .Name | urlize | replaceRE "^([0-9]+)-" "" }}
date: {{ .Date }}
series:
#  - 
categories:
  - 마인크래프트
tags:
#  - 
images:
#  - 001.webp
---

Content.
