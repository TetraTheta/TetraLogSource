---
title: "[macOS] Finder 툴바에 버튼 추가하기"
slug: macos-add-button-to-finder-toolbar
date: 2025-03-18T20:09:51+09:00
series:
#  - 
categories:
  - PIVOX
tags:
#  - 
images:
  - 003.webp
---

줄곧 Windows만 쓰다가 macOS를 쓰게 되니, Finder가 여간 불편한 게 아닙니다. 뭔가 아쉽거나 모자란 점이 많아요.

제일 불편한 점은 역시 우클릭 메뉴에 새 파일을 만들 수 있는 기능이 없다는 것이었습니다.
새 파일을 만들기 위해선 먼저 터미널을 열고, `cd <폴더 경로>`, `touch <새 파일 이름>`을 입력해야만 했습니다.

하지만 Apple은 사용자가 직접 Finder의 기능을 확장할 수 있도록, 잘 만들어진 응용 프로그램과 기능을 제공합니다.
이를 이용하면 Finder 도구 막대에 내가 원하는 기능을 실행하는 버튼을 추가할 수 있습니다.

> [!NOTE] 참고
> 이 가이드는 macOS 15 Sequoia를 기준으로 작성되었습니다.

# Automator를 이용해 응용 프로그램 작성{id="write-app-with-automator"}

제일 먼저 Automator를 실행해야 합니다.
Automator는 Launchpad의 '기타' 폴더 혹은 Spotlight에서 Automator를 검색해 실행할 수 있습니다.

{{< gallery/image src="001|002" caption="'응용 프로그램' 선택 후 'AppleScript' 끌어오기" >}}

Automator를 처음 열면 위와 같은 창이 나오는데, '응용 프로그램'을 선택합니다.

좌측의 보관함에서 'AppleScript 실행'을 우측으로 끌고 오면 위와 같은 화면이 됩니다.

{{< gallery/image src="003|004" caption="AppleScript 작성 후 응용 프로그램 저장" >}}

AppleScript를 작성한 후, 상단의 망치 버튼을 눌러 스크립트에 오류가 있는지 확인할 수 있습니다.
스크립트에 오류가 있다면, 자세한 안내 메시지가 나타납니다.

스크립트 작성을 마쳤다면, <kbd>⌘S</kbd>를 눌러 해당 스크립트를 새 응용 프로그램으로 저장합니다. Automator에서 작성한 파일의 기본 저장 위치는 `~/Library/Services`입니다.

AppleScript 예시는 글 아래에 별도로 소개하겠습니다.

# 응용 프로그램 아이콘 변경하기{id="change-app-icon"}

Automator로 작성한 응용 프로그램은 Automator의 아이콘을 기본 아이콘으로 갖게 됩니다.
Finder의 도구 모음에 응용 프로그램을 등록하면 별도로 설정하지 않는 이상, 아이콘만 보이기 때문에, 이를 적절한 아이콘으로 바꿔주는 것이 좋습니다.

## 다른 응용 프로그램의 아이콘 사용{id="use-other-app-icon"}

제일 먼저, 이미 설치되어 있는 응용 프로그램의 아이콘을 그대로 가져와 사용할 수 있습니다.

사진에서 예시로 든 자작 응용 프로그램은 iTerm2를 실행하는 스크립트이기에, iTerm2 아이콘을 그대로 사용하기로 했습니다.

{{< gallery/image src="005" caption="원하는 응용 프로그램의 '정보 가져오기'" >}}

Finder 좌측 패널의 '응용 프로그램'을 누르면 현재 시스템에 설치된 응용 프로그램의 목록을 확인할 수 있습니다.
본인이 원하는 응용 프로그램을 우클릭한 후, '정보 가져오기'를 누릅니다.

{{< gallery/image src="006|007" >}}

화면 좌상단의 아이콘을 누르면 푸른색으로 하이라이트가 들어옵니다. 이 상태에서 <kbd>⌘C</kbd>를 눌러 아이콘을 복사합니다.

자신이 만든 응용 프로그램의 '정보 가져오기'를 누른 후, 똑같이 좌상단의 아이콘을 누르고, <kbd>⌘V</kbd>를 누르면 방금 복사했던 아이콘을 붙여 넣을 수 있습니다.

## 커스텀 아이콘 사용{id="use-custom-icon"}

본인이 사용할 아이콘 파일을 준비합니다. `.png`, `.jpg`, `.icns` 파일을 사용할 수 있습니다.

마찬가지로 자신이 만든 응용 프로그램의 '정보 가져오기'를 누른 후, 아이콘 파일을 좌상단의 아이콘 자리에 끌어다 놓으면 응용 프로그램의 아이콘을 변경할 수 있습니다.

# Finder 도구 막대에 응용 프로그램 배치{id="put-app-on-finder-toolbar"}

먼저, 새 Finder 창을 열어 `~/Library/Services`로 이동합니다. Finder 상에는 `/사용자/<사용자 이름>/라이브러리/Service`로 보일 겁니다.

<kbd>⌥⌘</kbd> 키를 누른 상태에서 방금 여러분이 작성한 응용 프로그램을 Finder의 도구 막대에 끌어다 놓으면 됩니다.

# Automator 스크립트 예시

## 현재 Finder 경로에 새 iTerm2 창 열기

```applescript
on run {input, parameters}
	-- Check if Finder has focus or not. If not, exit.
	set frontApp to (path to frontmost application as Unicode text)
	if (frontApp does not contain "Finder.app") then
		return
	end if
	
	tell application "Finder"
		set listSize to count of (every window)
		if listSize is equal to 0 then
			-- There is no Finder window opened. Use Home directory as fallback.
			set dir_path to "~"
		else
			try
				-- Get directory path from frontmost Finder window
				set dir_path to quoted form of (POSIX path of (folder of the front window as alias))
			on error errMsg
				-- Special directory (e.g. Network or 'Machine Name') is opened. Use Home directory as fallback.
				set dir_path to "~"
			end try
		end if
	end tell
	
	CDTO(dir_path)
end run

on CDTO(theDir)
	-- You can use "Terminal" instead of "iTerm"
	-- Change working directory of iTerm to given path
	tell application "iTerm"
		set term_window to (create window with default profile)
		set sess to (current session of term_window)
		tell sess to write text "cd " & theDir & ";clear"
	end tell
end CDTO
```

~[출처](https://gist.github.com/pdanford/158d74e2026f393e953ed43ff8168ec1)~

## 현재 Finder 경로에 새 파일 만들기

```applescript
on run {input, parameters}
	-- Check if Finder has focus or not. If not, exit.
	set frontApp to (path to frontmost application as Unicode text)
	if (frontApp does not contain "Finder.app") then
		return
	end if
	
	tell application "Finder"
		set listSize to count of (every window)
		if listSize is equal to 0 then
			-- There is no Finder window opened. Exit.
			return
		else
			try
				-- Get name for new file from dialog.
				set file_name to text returned of (display dialog "새 파일 이름" default answer "" buttons {"취소", "확인"} default button 2 with icon 1)
				-- If name is empty, exit.
				if file_name is equal to "" then
					return
				end if
				make new file at (folder of the front window as alias) with properties {name:file_name}
			on error errMsg
				-- If something went wrong, show error message.
				display dialog (errMsg)
			end try
		end if
	end tell
end run
```
