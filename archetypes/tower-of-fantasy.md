---
title: "{{ replace .Name "-" " " | replaceRE "^([0-9]+) " "" | title }}"
slug: {{ .Name | urlize | replaceRE "^([0-9]+)-" "" }}
date: {{ .Date }}
series:
#  - 
categories:
  - 타워 오브 판타지
tags:
#  - 
images:
#  - 001.webp
---

Content.
