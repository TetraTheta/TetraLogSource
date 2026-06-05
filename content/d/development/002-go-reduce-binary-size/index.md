---
title: "[Go] 바이너리 파일 크기 줄이기"
slug: go-reduce-binary-size
date: 2026-06-02T12:00:00+09:00
series:
#  - 
categories:
  - PIVOX
tags:
  - golang
images:
  - go.webp
---

<details>
<summary>정보 출처</summary>

* [xaionaro/documentation](https://github.com/xaionaro/documentation/blob/master/golang/reduce-binary-size.md)

</details>

***

# 원본 소스 코드

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello world!")
}
```

```plaintext{linenos=false}
$ go version
go version go1.13 linux/amd64
$ export CGO_ENABLED=0
$ go build; stat -c %s helloworld
2012745
```

바이너리 파일 크기: `2012745`

# 간단한 방법

`-ldflags`에 대한 자세한 설명은 프로젝트 루트에서 `go build -ldflags -help`를 실행하여 확인할 수 있습니다.
`-gcflags`에 대한 자세한 설명은 프로젝트 루트에서 `go build -gcflags -help`를 실행하여 확인할 수 있습니다.

* `go build -a`: force rebuilding of packages that are already up-to-date.

## 디버그 정보 제거

`-ldflags="-w -s"` 플래그를 추가합니다.

* `-w`: disable DWARF generation
* `-s`: disable symbol table

```plaintext{linenos=false}
$ go build -a -ldflags="-w -s"; stat -c %s helloworld
1437696
```

바이너리 파일 크기: `1437696` (원본 대비 약 71%)

## Function Inlining 비활성화

`-gcflags=all=-l` 플래그를 추가합니다.
예제 코드에서는 별 효과가 없지만, 대형 프로젝트에서는 최대 10% 정도의 용량 절감을 기대할 수 있습니다.

* `-l`: disable inlining

```plaintext{linenos=false}
$ go build -a -ldflags="-w -s" -gcflags=all=-l; stat -c %s helloworld
1437696
```

바이너리 파일 크기: `1437696` (원본 대비 약 71%)

## Bound Check 비활성화

`-gcflags=all=-B` 플래그를 추가합니다.

* `-B`: disable bounds checking

```plaintext{linenos=false}
$ go build -a -gcflags=all="-l -B" -ldflags="-w -s"; stat -c %s helloworld
1404928
```

바이너리 파일 크기: `1404928` (원본 대비 약 70%)

## 기타 `gcflags` 사용

`-gcflags=all=-C` 플래그를 추가합니다.

* `-C`: disable printing of columns in error messages

```plaintext{linenos=false}
$ go build -a -gcflags=all="-l -B -C" -ldflags="-w -s"
```

## UPX 압축

[UPX](https://github.com/upx/upx)를 이용해 바이너리 파일을 압축할 수 있습니다.
하지만 다음과 같은 단점이 있습니다.

* 프로그램의 초기화 시간 증가
  프로그램의 압축이 해제된 후 RAM에 적재되기에, 프로그램이 실행되는 데 걸리는 시간이 증가합니다.
* RAM 사용량 증가
  선택적으로 적재할 수 있는 부분까지 모두 일괄적으로 RAM에 적재하여, 사용하는 RAM의 양이 증가합니다.
* 이미 압축된 바이너리 파일의 경우, 압축 효율 거의 없음

```plaintext{linenos=false}
Compression tuning options:
  --lzma              try LZMA [slower but tighter than NRV]
  --brute             try all available compression methods & filters [slow]
  --ultra-brute       try even more compression variants [very slow]
```

```plaintext{linenos=false}
$ upx --ultra-brute helloworld
```

## 32비트로 컴파일

64비트 바이너리가 아닌 32비트 바이너로 컴파일하여 바이너리 파일의 크기를 줄일 수 있습니다.
하지만 32비트 주소 공간, 정수, 시스템 콜 사용 등으로 인해 64비트 바이너리에 비해 성능 저하가 발생할 수 있습니다.

```plaintext{linenos=false}
$ GOARCH=386 go build -a -gcflags=all="-l -B -C" -ldflags="-w -s"
```

## `reflect.Call` 미사용

DCE(Dead Code Elimination)은 `reflect.Call`과 같은 리플렉션이 사용될 시 제대로 작동하지 않습니다.
리플렉션을 사용하지 않으면 훨씬 더 작은 크기의 바이너리 파일을 얻을 수 있습니다.

# 위험한 방법

다음은 프로그램의 정상 작동을 방해하거나 오류를 일으킬 가능성이 있는 방법입니다.
본인이 무엇을 하고 있는 지 알고 있는 게 아니라면 절대로 따라하지 마세요.

## Write Barrier 비활성화

> [!CAUTION] 경고
> [관련 Issue](https://github.com/golang/go/issues/36597)에 따르면 Write Barrier를 비활성화할 시 GC가 제대로 작동하지 않는다고 합니다.
>
> GC 오작동으로 인해 프로그램 실행 시 `GOGC=off` 환경 변수를 추가해야 합니다.

`-gcflags=all=-wb=false` 플래그를 추가합니다.

* `-wb`: enable write barrier (default true)

```plaintext{linenos=false}
$ go build -a -gcflags=all="-l -B -wb=false" -ldflags="-w -s"; stat -c %s helloworld
1380352
```

바이너리 파일 크기: `1380352` (원본 대비 약 69%)
