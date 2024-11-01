# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `BASE_DIR / "templates"` as a template search path.

### Changed

### Removed

### Fixed
- The `HealthCheckMiddleware` logged an unnecessary statement every time it got a request.

## [0.4.0] - 2024-10-13
### Added
- django_q2 background task support for the sendtestmail management command.
- Environment variables `SECURE_PROXY_SSL_HEADER_NAME` and `SECURE_PROXY_SSL_HEADER_VALUE` to configure the Django
  `SECURE_PROXY_SSL_HEADER` setting.
- Explicit dependency on the packages we already rely on to be installed.
- `worker` extra, which adds `django-q2` and a default configuration targeting the Django ORM.

### Changed
- Changing `ALLOWED_HOSTS` to be singular `ALLOWED_HOST`. No semantics are changed.

## [0.3.0] - 2024-09-26
### Added

### Changed
- Migrating to a default setting initialization that only requires one call in the settings file and no additional
  customization of manage.py / asgi / wsgi.

### Removed

### Fixed

## [0.2.0] - 2024-09-25
### Added
- `py.typed` marker
- Default settings for the static files, storages, SMTP, various security and TLS-related options other Django defaults. 

### Changed
- Moved the `initialize_settings` function. It should be imported via
  `from kition_djangodefaults import initialize_settings`

### Removed

### Fixed

## [0.1.0] - 2024-09-24
Initial release.

[Unreleased]: https://github.com/kition-dev/djangodefaults/compare/0.4.0...HEAD
[0.4.0]: https://github.com/kition-dev/djangodefaults/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/kition-dev/djangodefaults/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/kition-dev/djangodefaults/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/kition-dev/djangodefaults/releases/tag/0.1.0