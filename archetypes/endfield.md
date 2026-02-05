---
title: "{{ replace .Name "-" " " | replaceRE "^([0-9]+) " "" | title }}"
slug: {{ .Name | urlize | replaceRE "^([0-9]+)-" "" }}
date: {{ .Date }}
series:
#  - 
categories:
  - '명일방주: 엔드필드'
tags:
#  - 
images:
#  - 001.webp
---

Content.
