---
title: "[Windows] UAC 확인창 없이 관리자 권한으로 프로그램 실행하기"
slug: skip-uac-prompt
date: 2026-02-15T18:10:44+09:00
series:
#  - 
categories:
  - PIVOX
tags:
  - UAC
  - 사용자 계정 컨트롤
  - 작업 스케줄러
images:
  - logo.webp
---

{{< gallery/image src="uac" >}}

사용자 계정 컨트롤(User Account Control, UAC)은 Windows의 보안에 큰 도움이 되는 기능입니다. UAC가 도입되기 이전의 Windows는 최소한의 필터링도 없이 모든 권한이 열려 있었기 때문입니다.

하지만 이 보안 기능이 때로는 번거로움을 주는 것도 사실입니다. 내가 무엇을 하고 있는지 정확히 알고 있음에도 매번 나타나는 UAC 확인 창은... 솔직히 말해 꽤 귀찮습니다.

그래서 최초 한 번의 실행을 제외하면 UAC 확인 창이 표시되지 않도록 하는 배치 스크립트를 작성했습니다.

## 스크립트 사용 방법

> [!CAUTION] 경고
> 다음 스크립트는 UAC 확인 창을 우회하도록 설계되었습니다. 이는 Windows의 보안 수준을 낮추는 행위입니다.
> 본인이 무엇을 하고 있는지 명확히 이해한 경우에만 아래 스크립트를 사용하시기 바랍니다.

> [!WARNING] 주의 사항
> 다음 사항을 반드시 준수해야 합니다.
> 1. 스크립트 파일 이름에는 공백이 포함되어서는 안 됩니다.
> 2. 스크립트를 실행한 이후에는 파일 이름을 변경하거나 위치를 이동해서는 안 됩니다.
>    반드시 안전한 경로에 스크립트 파일을 저장한 후 실행하세요.
> 3. 해당 스크립트는 실행 인수를 지원하지 않습니다. 절대로 실행 인수를 전달하지 마세요.

> [!NOTE] 확인 사항
> 스크립트를 최초로 실행하는 시각이 오후 11시 59분일 경우, 스크립트가 중복 실행될 수 있습니다.

```bat
@echo off
setlocal ENABLEDELAYEDEXPANSION

REM Check admin privileges
net session >nul 2>&1
if !ErrorLevel! equ 0 (set "IS_ADMIN=true") else (set "IS_ADMIN=false")

if "%1" == "TASKRUN" (
  if "!IS_ADMIN!" == "true" (
    @REM ================ 아래에 실행할 내용 입력 ================
    cd /d "C:\Windows"
    start "First" "C:\Windows\notepad.exe" "C:\Windows\Logs\CBS\CBS.log"
    @REM ================ 위에 실행할 내용 입력 ================
  ) else (
    mshta vbscript:Execute^("msgbox ""This task requires admin privileges"",0,""Error"":close"^)
  )
) else (
  set "TNAME=SkipUAC\%~n0"
  schtasks /query /tn "!TNAME!" >nul 2>&1
  if !ErrorLevel! equ 0 (
    REM Task exists. Run it.
    echo Task detected. Running it...
    schtasks /run /tn "!TNAME!"
  ) else (
    REM Task doesn't exists. Create it.
    echo Task is not detected. Creating new one...
    REM Task creation needs admin privileges
    if not "!IS_ADMIN!" == "true" (goto ELEVATE)
    schtasks /create /f /tn "!TNAME!" /sc ONCE /st "23:59" /tr "\"%~dpnx0\" TASKRUN" /rl HIGHEST
    powershell -Command "& { $task = Get-ScheduledTask -TaskName '%~n0'; foreach ($trigger in $task.Triggers) { $trigger.Enabled = $false; } Set-ScheduledTask -InputObject $task; }"
    if !ErrorLevel! equ 0 (
      REM Run newly created task
      schtasks /run /tn "!TNAME!"
    ) else (
      REM Task creation failed
      mshta vbscript:Execute^("msgbox ""Failed to create task"",0,""Failed"":close"^)
    )
  )
)
goto:eof

:ELEVATE
cd /d %~dp0
mshta "javascript: var shell = new ActiveXObject('shell.application'); shell.ShellExecute('%~nx0', '', '', 'runas', 1);close();"
exit
```

사용 방법은 다음과 같습니다.

1. 위 스크립트를 복사하여 `OpenNotepad.bat`과 같은 이름으로 안전한 경로에 저장합니다.
   * ⚠️ <abbr title="%UserProfile%\Downloads">다운로드</abbr> 폴더는 안전한 경로가 아닙니다.
   * ⚠️ 파일 이름에 공백이 포함되어서는 안 됩니다.
2. 저장한 스크립트 파일을 열고, 다음 두 줄 사이에 실행할 명령어를 입력합니다.
   ```
   @REM ================ 아래에 실행할 내용 입력 ================
   @REM ================ 위에 실행할 내용 입력 ================
   ```
   스크립트 수정 방법은 아래 내용을 참고하세요.
3. 파일을 저장한 뒤 한 번 실행합니다.
   최초 실행 시 UAC 확인 창이 나타나며, 이후부터는 UAC 확인 창이 표시되지 않습니다.
   * ⚠️ 스크립트 파일의 이름을 변경하거나 위치를 이동해서는 안 됩니다.

{{< collapse heading="스크립트 작동 원리" >}}

위 배치 스크립트는 다음과 같은 원리로 동작합니다.

1. 스크립트 실행 시, 첫 번째 실행 인수가 `TASKRUN`인지 확인합니다.
   1. 첫 번째 실행 인수가 `TASKRUN`인 경우, 현재 스크립트가 관리자 권한으로 실행 중인지 확인합니다.
      1. 관리자 권한으로 실행 중이라면, 작업 스케줄러에 등록된 작업을 실행합니다.
   2. 첫 번째 실행 인수가 `TASKRUN`이 아닌 경우, 작업 스케줄러에 `SkipUAC/<스크립트 파일 이름>` 형식의 작업이 존재하는지 확인합니다.
      1. 해당 작업이 이미 존재하면 그 작업을 실행합니다.
      2. 작업이 존재하지 않으면, 작업 스케줄러의 `SkipUAC` 폴더 아래에 스크립트 파일 이름으로 새 작업을 등록합니다.
         이 작업은 스크립트 파일을 관리자 권한으로 실행하도록 설정됩니다.
         작업 등록이 완료되면, 해당 작업을 즉시 실행합니다.

{{< /collapse >}}

## 스크립트 수정 방법

### 다른 프로그램 실행

명령 프롬프트 스크립트의 특성상, 여러 프로그램을 동시에 실행하려면 다음과 같이 수정해야 합니다.

```bat
cd /d "<프로그램 A가 위치한 폴더 경로>"
start "<아무 문자열 1>" "<프로그램 A의 전체 경로>" <프로그램 A의 실행 인수>
cd /d "<프로그램 B가 위치한 폴더 경로>"
start "<아무 문자열 2>" "<프로그램 B의 전체 경로>" <프로그램 B의 실행 인수>
```

단순히 아래와 같이 작성하면, 프로그램 A가 종료된 이후에 프로그램 B가 실행됩니다.

```bat
"<프로그램 A의 전체 경로>" <프로그램 A의 실행 인수>
"<프로그램 B의 전체 경로>" <프로그램 B의 실행 인수>
```
