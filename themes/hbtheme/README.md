# hbtheme

`hbtheme`는 `hbstack`과 `hugomods` 기반 모듈형 테마를 전통적인 Hugo 테마 구조로 재구성한 테마입니다.

대부분의 레이아웃, SCSS, JS, 파셜, 기본 설정은 테마 내부에 통합되어 있고, 일부 아이콘 vendor만 외부 Hugo Module로 유지합니다.

처음 적용하는 사람은 이 문서부터 읽고, 어떤 모듈이 통합되었는지나 설정 이관 내역까지 확인하려면 [DEVELOPMENT.md](DEVELOPMENT.md)를 참고하면 됩니다.

## 이 테마가 기대하는 것

이 테마는 아래와 같은 환경을 전제로 합니다.

- Hugo 사이트가 `theme: hbtheme`를 사용함
- 사이트 루트에 필요한 프론트엔드 패키지가 설치되어 있음
- 사이트 루트 `config/_default/module.yml`에서 필요한 `mounts`와 외부 Hugo Module을 유지함

즉, `hbtheme`는 전통적인 Hugo 테마이지만, 완전히 독립적인 단일 폴더 테마는 아닙니다.<br>
Bootstrap, Fuse, 아이콘 vendor 같은 일부 외부 의존성은 사이트 루트에서 연결해 주어야 합니다.

## 빠른 적용 방법

1. 테마를 `themes/hbtheme`에 둡니다.
2. `package.json`에 필요한 패키지를 추가합니다.
3. `config/_default/module.yml`에 필요한 `mounts`와 `imports`를 넣습니다.
4. `config/_default/hugo.yml`에 `theme: hbtheme`를 추가합니다.
5. 루트에서 `bun install`을 실행합니다.

## 필요한 `package.json` 의존성

사이트 루트 `package.json`에는 최소한 아래 패키지가 필요합니다.

```json
{
  "dependencies": {
    "@fullhuman/postcss-purgecss": "^8.0.0",
    "@popperjs/core": "^2.11.8",
    "autoprefixer": "^10.4.27",
    "bootstrap": "^5.3.8",
    "fuse.js": "^7.2.0",
    "highlight.js": "^11.11.1",
    "postcss-cli": "^11.0.1",
    "rtlcss": "^4.3.0"
  }
}
```

설치:

```bash
bun install
```

루트 `package.json`에서 사이트 전용 의존성과 테마 전용 의존성을 구분하고 싶다면, `x-dependency-groups.theme` 같은 메타 필드를 함께 두는 방식을 권장합니다.

## 필요한 Hugo 설정

### 1. 테마 활성화

```yml
theme: hbtheme
```

### 2. 필요한 `module.mounts`

아래 mount는 현재 구조에서 필수입니다.

```yml
module:
  mounts:
    - source: assets
      target: assets
    - source: themes/hbtheme/assets
      target: assets
    - source: node_modules/bootstrap/scss
      target: assets/scss/bootstrap
    - source: node_modules/bootstrap/js
      target: assets/js/bootstrap
    - source: node_modules/fuse.js/dist
      target: assets/mods/fuse
    - source: node_modules/highlight.js/styles
      target: assets/scss/highlight.js
```

역할은 다음과 같습니다.

- 사이트 루트 `assets` 유지
- 테마 내부 `assets` 연결
- Bootstrap SCSS/JS를 루트 `node_modules`에서 공급
- Fuse 검색 엔진 파일을 루트 `node_modules`에서 공급

### 3. 필요한 `module.imports`

현재 테마는 아이콘 vendor를 외부 Hugo Module로 유지합니다.

```yml
module:
  imports:
    - path: github.com/hugomods/icons/vendors/bootstrap
    - path: github.com/hugomods/icons/vendors/font-awesome
    - path: github.com/hugomods/icons/vendors/lucide
    - path: github.com/hugomods/icons/vendors/mdi
    - path: github.com/hugomods/icons/vendors/simple-icons
```

### 4. 검색 출력 형식 유지

테마는 `Search` / `SearchIndex` output format 정의를 포함하지만, 사이트에서 `outputs.home`에 `SearchIndex`를 포함해야 검색 인덱스 JSON이 생성됩니다.

```yml
outputs:
  home:
    - HTML
    - RSS
    - SearchIndex
```

## 최소 적용 예시

아래는 다른 사이트에 `hbtheme`를 붙일 때 참고할 수 있는 최소 예시입니다.

```yml
title: Example Site
theme: hbtheme

outputs:
  home:
    - HTML
    - RSS
    - SearchIndex

module:
  mounts:
    - source: assets
      target: assets
    - source: themes/hbtheme/assets
      target: assets
    - source: node_modules/bootstrap/scss
      target: assets/scss/bootstrap
    - source: node_modules/bootstrap/js
      target: assets/js/bootstrap
    - source: node_modules/fuse.js/dist
      target: assets/mods/fuse
    - source: node_modules/highlight.js/styles
      target: assets/scss/highlight.js
  imports:
    - path: github.com/hugomods/icons/vendors/bootstrap
    - path: github.com/hugomods/icons/vendors/font-awesome
    - path: github.com/hugomods/icons/vendors/lucide
    - path: github.com/hugomods/icons/vendors/mdi
    - path: github.com/hugomods/icons/vendors/simple-icons
```

```json
{
  "dependencies": {
    "@fullhuman/postcss-purgecss": "^8.0.0",
    "@popperjs/core": "^2.11.8",
    "autoprefixer": "^10.5.0",
    "bootstrap": "^5.3.8",
    "fuse.js": "^7.3.0",
    "highlight.js": "^11.11.1",
    "postcss-cli": "^11.0.1",
    "rtlcss": "^4.3.0"
  },
  "devDependencies": {
    "@eslint/js": "^10.0.1",
    "@types/html-minifier-terser": "^7.0.2",
    "@types/node": "^25.8.0",
    "eslint": "^10.4.0",
    "eslint-config-prettier": "^10.1.8",
    "prettier": "^3.8.3",
    "typescript-eslint": "^8.59.3"
  },
}
```

## 코드 하이라이팅

`hbtheme`는 코드블럭의 Syntax Highlighting에 [highlight.js](https://highlightjs.org/)를 사용합니다.
코드블럭 언어명은 highlight.js가 인식하는 이름을 그대로 사용해야 하며, 테마는 Hugo/Chroma 언어명을 highlight.js 언어명으로 자동 변환하지 않습니다.

### highlight.js 테마 커스텀

테마는 `assets/mods/code-block-panel/js/highlight-languages.ts`에서 일부 highlight.js 언어 정의를 보강합니다.

- `bash`의 `built_in` 항목에 키워드를 추가합니다. `sh`, `zsh` alias와 `shell`의 bash sub-language에도 같은 규칙이 적용됩니다.
  - `apt`
  - `nano`
  - `systemctl`
- `dos`의 `built_in` 항목에 키워드를 추가합니다. `cmd`의 dos sub-language에도 같은 규칙이 적용됩니다.
  - `ssh-keygen`
- `cmd`는 highlight.js 기본 `dos` alias가 아니라 별도의 `Command Prompt Session` 언어로 재지정합니다. 프롬프트 부분은 `meta.prompt`로 처리하고, 프롬프트 뒤 명령어는 `dos` sub-language에 맡깁니다.

`bash`는 스크립트 코드에, `shell`은 Bash 셸 세션에, `dos`는 배치 파일 코드에, `cmd`는 Windows 명령 프롬프트 세션에 사용합니다.

옵션은 Hugo fenced code block attribute 문법처럼 언어 바로 옆에 지정할 수 있습니다.

````markdown
```dos{linenos=false,linenostart=10,title="example.bat"}
echo hello
```
````

````markdown
```cmd{linenos=false}
C:\Users\AKULA\Desktop>echo test
> test
```
````

지원 옵션은 다음과 같습니다.

| 옵션 | 설명 |
| --- | --- |
| `linenos`, `data-line-nos`, `lineNos` | 줄 번호 표시 여부입니다. `false`면 숨기고, 그 외 truthy 값이면 표시합니다. |
| `wrap`, `data-wrap` | 코드블럭의 기본 줄바꿈을 활성화합니다. |
| `maxlines`, `maxLines`, `data-max-lines` | 접힌 상태의 높이 기준 줄 수입니다. |
| `expand`, `data-expand` | 코드블럭을 처음부터 펼친 상태로 표시합니다. |
| `title` | 코드블럭 제목을 표시합니다. |
| `linenostart`, `data-line-no-start`, `lineNoStart` | 줄 번호 시작 번호입니다. 유효하지 않으면 `1`을 사용합니다. |
| `style` | 해당 코드블럭 래퍼에 직접 적용할 CSS 스타일입니다. |

highlight.js 자체는 줄 번호 기능을 제공하지 않습니다. 줄 번호, 줄 번호 시작 번호, 복사 버튼, 줄바꿈, 접기 UI는 이 테마의 코드블럭 패널이 추가합니다.

`hl_lines`, `anchorLineNos` 같은 Chroma 전용 옵션은 지원하지 않습니다. 사용 가능한 언어명은 highlight.js 공식 문서를 기준으로 확인하세요.

## 추가 참고

- Disqus hook wrapper는 이제 테마 내부에 포함되어 있습니다.
- Bootstrap SCSS와 JS는 테마 내부에 복사해 두지 않고, 루트 `node_modules`를 통해 공급받습니다.
- `@hbstack/node-packages`는 사용하지 않으며, 필요한 패키지는 루트 `package.json`에서 직접 관리합니다.
- Hugo 0.159 기준 deprecated API 대응은 이미 테마 내부에 반영되어 있습니다.

## 유지보수 문서

다음 내용이 필요하면 [DEVELOPMENT.md](DEVELOPMENT.md)를 읽으면 됩니다.

- 어떤 Hugo Module이 직접 통합되었는지
- 어떤 전이 의존성이 함께 흡수되었는지
- 무엇을 외부 모듈로 남겼는지
- 현재 `hugo.toml` 기본값이 어디서 왔는지
- 문제를 추적할 때 어떤 순서로 확인해야 하는지
