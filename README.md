# TetraLog 소스 저장소

이 저장소는 [TetraLog](https://tetralog.onrender.com/) 블로그의 Hugo 소스입니다.

현재 블로그는 `themes/hbtheme`에 들어 있는 전통적인 Hugo 테마를 사용합니다. 외부 Hugo Module은 쓰지 않고, 테마의 프런트엔드 의존성은 pnpm workspace로 설치합니다.

## 개요

- 정적 사이트 생성기: `Hugo`
- 패키지 매니저: `pnpm` (Node.js 기반)
- 테마: [`themes/hbtheme`](themes/hbtheme)
- 특징:
  - `hbstack` / `hugomods`의 Hugo Module 기반 테마를 전통적인 Hugo 테마 구조로 통합
  - Bootstrap, Fuse, highlight.js, 아이콘 등 테마 의존성은 `themes/hbtheme/package.json`에서 관리
  - 루트 `package.json`은 사이트 실행 스크립트와 CLI 엔트리만 유지

## 요구 사항

- Hugo `0.161.1` 이상 권장
- Node.js `20.x` 이상 권장
- pnpm `11.x` 이상 권장

클론 후 프로젝트 루트에서 의존성을 설치합니다. Hugo는 npm 의존성을 자동 설치하지 않습니다.

```bash
pnpm install
```

프로덕션 빌드는 아래 명령을 사용합니다.

```bash
pnpm run build
```

## 자주 쓰는 명령

개발 서버 실행:

```bash
pnpm run dev
```

프로덕션 빌드:

```bash
pnpm run build
```

업데이트 가능한 패키지 확인:

```bash
pnpm run check-update
```

## 테마 관련 문서

`hbtheme` 자체를 이해하거나 다른 사이트에 적용하려면 아래 문서를 참고하면 됩니다.

- 사용자용 안내: [`themes/hbtheme/README.md`](themes/hbtheme/README.md)
- 유지보수용 문서: [`themes/hbtheme/DEVELOPMENT.md`](themes/hbtheme/DEVELOPMENT.md)

## 메모

- 외부 Hugo Module은 없습니다. `hugo mod graph`는 `project hbtheme`만 반환해야 합니다.
- 루트 `config/_default/module.yml`은 필요하지 않습니다. Hugo 기본 mount가 루트 `assets`와 테마 `assets`, `layouts`, `i18n`을 처리합니다.
- `@hbstack/node-packages`는 더 이상 사용하지 않으며, 필요한 테마 패키지는 `themes/hbtheme/package.json`에 직접 선언되어 있습니다.
