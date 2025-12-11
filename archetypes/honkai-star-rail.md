---
title: "{{ replace .Name "-" " " | replaceRE "^([0-9]+) " "" | title }}"
slug: {{ .Name | urlize | replaceRE "^([0-9]+)-" "" }}
date: {{ .Date }}
series:
#  - 
categories:
  - '붕괴: 스타레일'
tags:
#  - 
images:
#  - 001.webp
---

Content.
