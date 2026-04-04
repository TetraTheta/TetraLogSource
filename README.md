# TetraLog 소스 저장소

이 저장소는 [TetraLog](https://tetralog.onrender.com/) 블로그의 Hugo 소스입니다.

현재 블로그는 `themes/hbtheme`에 들어 있는 전통적인 Hugo 테마를 사용하며, 일부 아이콘 관련 의존성만 Hugo Module로 유지합니다.

## 개요

- 정적 사이트 생성기: `Hugo`
- 패키지 매니저: `Bun`
- 테마: [`themes/hbtheme`](themes/hbtheme)
- 특징:
  - `hbstack` / `hugomods`의 Hugo Module 기반 테마를 전통적인 Hugo 테마 구조로 통합
  - Bootstrap, Fuse 등 프런트엔드 런타임 의존성은 루트 `package.json`에서 관리

## 요구 사항

- Hugo `0.159.2` 이상 권장
- Bun `1.2.x` 이상 권장

설치 후에는 프로젝트 루트에서 아래 명령을 실행합니다.

```bash
bun install
```

## 자주 쓰는 명령

개발 서버 실행:

```bash
bun run dev
```

프로덕션 빌드:

```bash
bun run build
```

업데이트 가능한 패키지 확인:

```bash
bun run check-update
```

## 테마 관련 문서

`hbtheme` 자체를 이해하거나 다른 사이트에 적용하려면 아래 문서를 참고하면 됩니다.

- 사용자용 안내: [`themes/hbtheme/README.md`](themes/hbtheme/README.md)
- 유지보수용 문서: [`themes/hbtheme/DEVELOPMENT.md`](themes/hbtheme/DEVELOPMENT.md)

## 메모

- 아이콘 vendor는 여전히 Hugo Module import로 유지합니다.
- Bootstrap SCSS/JS와 Fuse는 루트 `node_modules`를 Hugo `mounts`로 노출해 사용합니다.
- `@hbstack/node-packages`는 더 이상 사용하지 않으며, 필요한 패키지는 루트 `package.json`에 직접 선언되어 있습니다.
